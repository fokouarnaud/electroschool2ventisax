"""Garde-fou du contenu versionné : tout texte destiné aux apprenants existe en français ET en anglais."""
import json

import pytest
from django.conf import settings
from django.core.management import call_command

from assessments.models import Question
from courses.models import Module, Section

CONTENT = settings.BASE_DIR / "content" / "electro"
LANGS = ("fr", "en")

# Justification (DoD, critère 2) : le contenu électronique est rédigé à l'étape « Contenu » du plan, après le backend.
# Dès que le manifeste existe, ces garde-fous s'exécutent sans condition.
pytestmark = pytest.mark.skipif(
    not (CONTENT / "formation.json").exists(),
    reason="content/electro/formation.json pas encore rédigé (étape Contenu)",
)


def manifest():
    return json.loads((CONTENT / "formation.json").read_text(encoding="utf-8"))


def assert_bilingual(data, field, where):
    values = data.get(field) or {}
    for lang in LANGS:
        assert (values.get(lang) or "").strip(), f"{where} : {field}.{lang} manquant"


def iter_modules():
    for partie in manifest()["parties"]:
        for module in partie["modules"]:
            yield partie, module


def test_formation_parts_and_modules_are_bilingual():
    data = manifest()
    assert_bilingual(data, "title", "formation")
    for partie, module in iter_modules():
        assert_bilingual(partie, "title", partie["slug"])
        assert_bilingual(module, "title", module["dir"])


def test_every_section_has_a_french_and_an_english_text_file():
    for _, module in iter_modules():
        for section in module["sections"]:
            assert_bilingual(section, "title", f"{module['dir']}/{section['file']}")
            for lang in LANGS:
                path = CONTENT / module["dir"] / f"{section['file']}.{lang}.md"
                assert path.exists() and path.read_text(encoding="utf-8").strip(), f"{path} manquant ou vide"


def test_every_question_choice_and_explanation_is_bilingual():
    ids = set()
    for _, module in iter_modules():
        path = CONTENT / module["dir"] / "questions.json"
        if not path.exists():
            continue
        for q in json.loads(path.read_text(encoding="utf-8")):
            assert q["id"] not in ids, f"identifiant en double : {q['id']}"
            ids.add(q["id"])
            assert_bilingual(q, "prompt", q["id"])
            assert_bilingual(q, "explanation", q["id"])
            for i, choice in enumerate(q["choices"]):
                assert_bilingual(choice, "text", f"{q['id']} choix {i}")
    assert ids, "aucune question"


@pytest.mark.django_db
def test_versioned_content_imports_with_english_everywhere():
    call_command("import_content", str(CONTENT / "formation.json"), verbosity=0)
    assert Module.objects.exists()
    assert not Module.objects.filter(title_en="").exists()
    assert not Section.objects.filter(body_md_en="").exists()
    assert not Question.objects.filter(prompt_en="").exists()
    assert not Question.objects.filter(explanation_en="").exists()


def test_every_markdown_file_is_referenced_by_the_manifest():
    referenced = set()
    for _, module in iter_modules():
        for section in module["sections"]:
            for lang in LANGS:
                referenced.add((CONTENT / module["dir"] / f"{section['file']}.{lang}.md").resolve())
    on_disk = {p.resolve() for p in CONTENT.rglob("*.md")}
    assert sorted(str(p) for p in on_disk - referenced) == []


def questions_by_module():
    for _, module in iter_modules():
        path = CONTENT / module["dir"] / "questions.json"
        yield module, (json.loads(path.read_text(encoding="utf-8")) if path.exists() else [])


def test_every_question_cites_an_existing_section_of_its_module():
    for module, questions in questions_by_module():
        files = {s["file"] for s in module["sections"]}
        for q in questions:
            assert q.get("section") in files, f"{q['id']} : section {q.get('section')!r} inconnue dans {module['dir']}"


def test_every_content_section_is_covered_by_at_least_one_question():
    for module, questions in questions_by_module():
        cited = {q.get("section") for q in questions}
        missing = [s["file"] for s in module["sections"] if s["kind"] == "content" and s["file"] not in cited]
        assert missing == [], f"{module['dir']} : sections sans question {missing}"


def test_every_module_has_enough_quiz_and_exam_questions():
    for module, questions in questions_by_module():
        quiz = sum(q["usage"] == "quiz" for q in questions)
        exam = sum(q["usage"] == "exam" for q in questions)
        assert quiz >= 4 and exam >= 4, f"{module['dir']} : {quiz} quiz, {exam} examen"


def test_review_flags_are_explicit_for_both_languages():
    """Relecture approuvée par le formateur le 2026-10-17 ; toute nouvelle question entre avec false/false."""
    for _, questions in questions_by_module():
        for q in questions:
            assert set(q["reviewed"]) == {"fr", "en"}, q["id"]
            assert all(isinstance(v, bool) for v in q["reviewed"].values()), q["id"]


@pytest.mark.django_db
def test_import_never_publishes_and_only_reviewed_questions_can_be():
    """E12 : le contenu rédigé par Claude arrive en brouillon ; seul ce qu'un formateur a relu se publie."""
    call_command("import_content", str(CONTENT / "formation.json"), verbosity=0)
    assert not Question.objects.published().exists()  # l'import ne publie jamais tout seul
    reviewed = Question.objects.filter(reviewed_fr=True, reviewed_en=True)
    for question in reviewed:
        question.publish()
    assert Question.objects.published().count() == reviewed.count()


@pytest.mark.django_db
def test_every_question_is_publishable_once_reviewed():
    call_command("import_content", str(CONTENT / "formation.json"), verbosity=0)
    refused = []
    for question in Question.objects.all():
        question.reviewed_fr = question.reviewed_en = True  # simulate the trainer's review
        try:
            question.validate_for_publication()
        except Exception as exc:  # noqa: BLE001
            refused.append(f"{question.external_id}: {exc}")
    assert refused == []
    assert Question.objects.count() == sum(len(qs) for _, qs in questions_by_module())


# --- Volumes et schémas décidés au grill (AGENTS.md, E3 et E12) -------------------------------------------------------

STATIC = settings.BASE_DIR / "static"
IMAGE = __import__("re").compile(r"!\[([^\]]*)\]\((/static/[^)\s]+)\)")


def test_part_one_has_the_four_modules_of_chapters_one_to_four():
    partie = next(p for p in manifest()["parties"] if p["slug"] == "p1")
    assert [m["dir"] for m in partie["modules"]] == ["p1/m1", "p1/m2", "p1/m3", "p1/m4"]
    assert manifest()["open"] is True


def test_every_module_has_six_to_eight_sections_with_one_mini_project():
    for _, module in iter_modules():
        kinds = [s["kind"] for s in module["sections"]]
        assert 6 <= len(kinds) <= 8, f"{module['dir']} : {len(kinds)} sections"
        assert kinds.count("practical") == 1, f"{module['dir']} : un mini-projet attendu"


def test_question_volumes_and_types_per_module():
    for module, questions in questions_by_module():
        quiz = [q for q in questions if q["usage"] == "quiz"]
        exam = [q for q in questions if q["usage"] == "exam"]
        assert len(quiz) >= 15 and len(exam) >= 12, f"{module['dir']} : {len(quiz)} quiz, {len(exam)} examen"
        assert sum(q["type"] == "numeric" for q in quiz) >= 4, f"{module['dir']} : moins de 4 numériques"
        assert sum(q["type"] in ("matching", "hotspot") for q in quiz) >= 2, f"{module['dir']} : moins de 2 interactives"


def test_matching_pairs_are_bilingual():
    for _, questions in questions_by_module():
        for q in questions:
            for i, pair in enumerate(q.get("pairs", [])):
                assert_bilingual(pair, "left", f"{q['id']} paire {i}")
                assert_bilingual(pair, "right", f"{q['id']} paire {i}")


def test_hotspot_diagrams_exist_next_to_the_questions():
    for module, questions in questions_by_module():
        for q in questions:
            if q["type"] == "hotspot":
                assert (CONTENT / module["dir"] / q["svg"]).exists(), q["id"]


def test_every_content_section_shows_at_least_two_existing_diagrams_in_both_languages():
    for _, module in iter_modules():
        for section in module["sections"]:
            if section["kind"] != "content":
                continue
            for lang in LANGS:
                text = (CONTENT / module["dir"] / f"{section['file']}.{lang}.md").read_text(encoding="utf-8")
                images = IMAGE.findall(text)
                where = f"{module['dir']}/{section['file']}.{lang}"
                assert len(images) >= 2, f"{where} : {len(images)} schéma(s)"
                for alt, src in images:
                    assert alt.strip(), f"{where} : texte alternatif manquant pour {src}"
                    assert (STATIC / src.removeprefix("/static/")).exists(), f"{where} : {src} introuvable"


def test_no_long_dash_in_learner_facing_text():
    """Guide de style : ni tiret cadratin ni demi-cadratin dans les textes destinés aux apprenants."""
    for path in list(CONTENT.rglob("*.md")) + list(CONTENT.rglob("*.json")):
        text = path.read_text(encoding="utf-8")
        assert chr(0x2014) not in text and chr(0x2013) not in text, path  # tirets cadratin et demi-cadratin


def test_every_content_diagram_is_well_formed_and_inert():
    from xml.etree import ElementTree

    from config.uploads import ACTIVE_SVG

    svgs = list((STATIC / "content" / "electro").rglob("*.svg")) + list(CONTENT.rglob("*.svg"))
    assert svgs, "aucun schéma"
    for path in svgs:
        raw = path.read_bytes()
        assert ElementTree.fromstring(raw).tag.endswith("svg"), path
        assert not ACTIVE_SVG.search(raw), f"{path} : contenu actif"


def test_english_pages_show_english_diagrams():
    """Les schémas portent du texte : la version anglaise du cours pointe vers static/content/electro/en/."""
    from xml.etree import ElementTree

    for _, module in iter_modules():
        for section in module["sections"]:
            for lang in LANGS:
                path = CONTENT / module["dir"] / f"{section['file']}.{lang}.md"
                for _alt, src in IMAGE.findall(path.read_text(encoding="utf-8")):
                    assert src.startswith("/static/content/electro/en/") == (lang == "en"), f"{path} : {src}"
                    if lang == "en":
                        svg = ElementTree.fromstring((STATIC / src.removeprefix("/static/")).read_bytes())
                        texts = " ".join(t.text or "" for t in svg.iter() if t.tag.endswith("text"))
                        assert not __import__("re").search(r"\d,\d", texts), f"{src} : virgule décimale"


# --- Partie 2 « Courant alternatif et filtres » (AGENTS.md, E25 à E29) -------------------------------------------------


def part(slug):
    return next(p for p in manifest()["parties"] if p["slug"] == slug)


def test_part_two_has_the_three_modules_of_chapters_five_to_seven():
    p2 = part("p2")
    assert [m["dir"] for m in p2["modules"]] == ["p2/m5", "p2/m6", "p2/m7"]
    assert_bilingual(p2, "description", "p2")
    assert "Partie 1" in p2["description"]["fr"] and "Part 1" in p2["description"]["en"]


PRACTICAL_HEADINGS = {
    "fr": ("## Variante oscilloscope", "## Variante multimètre seul", "## Sécurité"),
    "en": ("## Oscilloscope variant", "## Multimeter-only variant", "## Safety"),
}


def test_part_two_mini_projects_offer_both_measurement_variants_and_a_safety_rule():
    """US-43 : oscilloscope et GBF, ou multimètre seul avec transformateur 230 V vers 9 ou 12 V AC ; sécurité en tête."""
    for module in part("p2")["modules"]:
        [practical] = [s for s in module["sections"] if s["kind"] == "practical"]
        for lang, headings in PRACTICAL_HEADINGS.items():
            text = (CONTENT / module["dir"] / f"{practical['file']}.{lang}.md").read_text(encoding="utf-8")
            positions = [text.find(h) for h in headings]
            assert -1 not in positions, f"{module['dir']}.{lang} : titres attendus {headings}"
            assert positions[2] < positions[0], f"{module['dir']}.{lang} : la sécurité vient avant les variantes"
            assert "230 V" in text, f"{module['dir']}.{lang} : transformateur 230 V non mentionné"


def test_part_two_sections_use_the_three_new_calculators():
    """US-42 : réactance (M5), fréquence de coupure (M6), résonance (M7), en français et en anglais."""
    for module, kind in zip(part("p2")["modules"], ("reactance", "cutoff", "resonance")):
        for lang in LANGS:
            texts = [(CONTENT / module["dir"] / f"{s['file']}.{lang}.md").read_text(encoding="utf-8") for s in module["sections"]]
            assert any(f"[[calc:{kind}]]" in t for t in texts), f"{module['dir']}.{lang} : [[calc:{kind}]] absent"


def test_part_two_asks_for_phase_shifts_in_degrees():
    """US-41 : au moins deux déphasages notés en degrés dans le module des filtres."""
    _, questions = next((m, qs) for m, qs in questions_by_module() if m["dir"] == "p2/m6")
    assert sum(q["type"] == "numeric" and q["numeric"]["unit"] == "°" for q in questions) >= 2


def test_part_two_questions_are_reviewed_in_both_languages():
    """E29 : relecture de la Partie 2 validée d'emblée ; ses questions sont publiées au déploiement."""
    for module, questions in questions_by_module():
        if module["dir"].startswith("p2/"):
            assert questions and all(q["reviewed"] == {"fr": True, "en": True} for q in questions), module["dir"]


# --- Partie 3 « Amplification, oscillateurs et alimentations » (AGENTS.md, E30 à E44) ---------------------------------

P3_MODULES = ["p3/m8", "p3/m9", "p3/m10", "p3/m11"]



def test_part_three_has_the_four_modules_of_chapters_eight_to_eleven():
    """US-48 : M8 à M11 dans la formation electro, description conseillant de suivre d'abord les Parties 1 et 2."""
    p3 = part("p3")
    assert p3["order"] == 3
    assert [m["dir"] for m in p3["modules"]] == P3_MODULES
    assert_bilingual(p3, "description", "p3")
    assert "Parties 1 et 2" in p3["description"]["fr"] and "Parts 1 and 2" in p3["description"]["en"]


def test_formation_description_covers_the_three_parts():
    """US-57 : la fiche du catalogue annonce les amplificateurs, oscillateurs et alimentations."""
    description = manifest()["description"]
    assert "amplificateurs" in description["fr"] and "alimentations" in description["fr"]
    assert "amplifiers" in description["en"] and "power supplies" in description["en"]


def test_part_three_section_counts_follow_the_plan():
    """E34 et E35 : M8 8 sections, M9 7, M10 6, M11 7 (mini-projet compris)."""
    assert [len(m["sections"]) for m in part("p3")["modules"]] == [8, 7, 6, 7]


def test_part_three_mini_projects_offer_both_measurement_variants_and_put_safety_first():
    """US-52 et E36 : deux variantes de mesure ; sécurité du secteur en tête ; jamais de travail côté 230 V."""
    for module in part("p3")["modules"]:
        [practical] = [s for s in module["sections"] if s["kind"] == "practical"]
        for lang, headings in PRACTICAL_HEADINGS.items():
            text = (CONTENT / module["dir"] / f"{practical['file']}.{lang}.md").read_text(encoding="utf-8")
            positions = [text.find(h) for h in headings]
            assert -1 not in positions, f"{module['dir']}.{lang} : titres attendus {headings}"
            assert positions[2] < positions[0], f"{module['dir']}.{lang} : la sécurité vient avant les variantes"
            if module["dir"] in ("p3/m10", "p3/m11"):
                assert "230 V" in text, f"{module['dir']}.{lang} : consigne du secteur 230 V absente"


def test_part_three_sections_use_their_calculators():
    """US-50 et E38 : gain (M8), résonance (M9), transformateur (M10), ondulation (M11), en français et en anglais."""
    for module, kind in zip(part("p3")["modules"], ("gain", "resonance", "transformer", "ripple")):
        for lang in LANGS:
            texts = [(CONTENT / module["dir"] / f"{s['file']}.{lang}.md").read_text(encoding="utf-8") for s in module["sections"]]
            assert any(f"[[calc:{kind}]]" in t for t in texts), f"{module['dir']}.{lang} : [[calc:{kind}]] absent"


def test_part_three_has_one_hotspot_question_per_module():
    """US-51 et E43 : une question sur schéma par module de la Partie 3."""
    counts = {m["dir"]: sum(q["type"] == "hotspot" for q in qs) for m, qs in questions_by_module() if m["dir"] in P3_MODULES}
    assert list(counts) == P3_MODULES
    assert all(n >= 1 for n in counts.values()), counts


def test_part_three_gain_prompts_say_whether_the_sign_counts():
    """US-49 et E41 : tout énoncé de gain sans unité précise « en valeur absolue » ou « avec son signe »."""
    markers = {"fr": ("valeur absolue", "avec son signe"), "en": ("absolute value", "with its sign")}
    gains = 0
    for module, questions in questions_by_module():
        if module["dir"] not in P3_MODULES:
            continue
        for q in questions:
            if q["type"] == "numeric" and q["numeric"]["unit"] == "" and "gain" in q["prompt"]["fr"].lower():
                gains += 1
                for lang, words in markers.items():
                    assert any(w in q["prompt"][lang] for w in words), f"{q['id']}.{lang} : signe du gain non précisé"
    assert gains >= 2, "au moins deux questions de gain dans la Partie 3"


def test_part_three_questions_are_reviewed_in_both_languages():
    """E39 : relecture de la Partie 3 validée d'emblée ; ses 108 questions sont publiées au déploiement (US-55)."""
    total = 0
    for module, questions in questions_by_module():
        if module["dir"] in P3_MODULES:
            assert questions and all(q["reviewed"] == {"fr": True, "en": True} for q in questions), module["dir"]
            total += len(questions)
    assert total == 108


@pytest.mark.django_db
def test_importing_the_content_builds_part_three_and_its_exam():
    """US-53 et US-54 : M8 à M11 importés dans l'ordre ; examen de la Partie 3 à 70 %, 3 tentatives, 60 min."""
    from assessments.models import Assessment
    from courses.models import Partie

    call_command("import_content", str(CONTENT / "formation.json"), verbosity=0)
    call_command("import_content", str(CONTENT / "formation.json"), verbosity=0)

    p3 = Partie.objects.get(formation__slug="electro", slug="p3")
    assert list(p3.modules.order_by("order").values_list("title_fr", flat=True)) == [
        "Les amplificateurs à transistor", "Les oscillateurs", "Le transformateur", "Les alimentations"]
    assert Section.objects.filter(module__partie=p3).count() == 28
    exam = Assessment.exam_for(p3)
    assert (exam.pass_threshold, exam.max_attempts, exam.duration_minutes) == (70, 3, 60)


@pytest.mark.django_db
def test_publish_reviewed_publishes_the_108_questions_of_part_three():
    """US-55 : après import, publish_reviewed publie les 108 questions relues de la Partie 3, 48 d'examen."""
    import io

    call_command("import_content", str(CONTENT / "formation.json"), verbosity=0)
    call_command("publish_reviewed", stdout=io.StringIO())

    published = Question.objects.published().filter(module__partie__slug="p3")
    assert published.count() == 108
    assert published.filter(usage="exam").count() == 48
