"""Garde-fou du contenu versionné, formation par formation (US-64) : tout texte destiné aux apprenants existe en français
ET en anglais, dans les volumes décidés au grill ; puis les règles propres à chaque formation."""
import json
import re

import pytest
from django.conf import settings
from django.core.management import call_command

from assessments.models import Question
from courses.models import Module, Section
from courses.tests.content_rules import (
    numeric_shortfalls,
    practical_problems,
    scan_folder,
)

LANGS = ("fr", "en")
STATIC = settings.BASE_DIR / "static"
IMAGE = re.compile(r"!\[([^\]]*)\]\((/static/[^)\s]+)\)")


def content_dir(slug):
    return settings.BASE_DIR / "content" / slug


# Règles propres à chaque formation (US-64). `numeric` : minimum de numériques au quiz, par dossier de module ;
# `interactive` : types interactifs exigés au quiz de chaque module.
ELECTRO_DIRS = ["p1/m1", "p1/m2", "p1/m3", "p1/m4", "p2/m5", "p2/m6", "p2/m7", "p3/m8", "p3/m9", "p3/m10", "p3/m11"]
MOTEURS_DIRS = ["p1/m1", "p1/m2", "p1/m3", "p2/m4", "p2/m5", "p2/m6", "p3/m7", "p3/m8", "p3/m9", "p4/m10", "p4/m11", "p4/m12"]
RULES = {
    "electro": {
        "id_prefix": "e-",
        "numeric": {folder: 4 for folder in ELECTRO_DIRS},
        "interactive": "matching ou hotspot (au moins 2)",
    },
    "moteurs": {
        "id_prefix": "m-",
        # M4 : 4 numériques dans les modules de calcul, 2 dans les modules qualitatifs (M1, M2, M4, M8, M12).
        "numeric": {folder: 2 if folder in ("p1/m1", "p1/m2", "p2/m4", "p3/m8", "p4/m12") else 4 for folder in MOTEURS_DIRS},
        "interactive": "1 matching et 1 hotspot",
    },
}


def formation_param(slug):
    """Justification (DoD, critère 2) : le contenu de `moteurs` est rédigé partie par partie (M14, livraisons 2 à 5).
    Dès que son manifeste existe, ces garde-fous s'exécutent sans condition."""
    missing = not (content_dir(slug) / "formation.json").exists()
    return pytest.param(slug, marks=pytest.mark.skipif(missing, reason=f"content/{slug}/formation.json pas encore rédigé"))


FORMATIONS = [formation_param(slug) for slug in RULES]
by_formation = pytest.mark.parametrize("slug", FORMATIONS)


def manifest(slug="electro"):
    return json.loads((content_dir(slug) / "formation.json").read_text(encoding="utf-8"))


def assert_bilingual(data, field, where):
    values = data.get(field) or {}
    for lang in LANGS:
        assert (values.get(lang) or "").strip(), f"{where} : {field}.{lang} manquant"


def iter_modules(slug="electro"):
    for partie in manifest(slug)["parties"]:
        for module in partie["modules"]:
            yield partie, module


def questions_by_module(slug="electro"):
    for _, module in iter_modules(slug):
        path = content_dir(slug) / module["dir"] / "questions.json"
        yield module, (json.loads(path.read_text(encoding="utf-8")) if path.exists() else [])


def section_text(slug, module, section, lang):
    return (content_dir(slug) / module["dir"] / f"{section['file']}.{lang}.md").read_text(encoding="utf-8")


def import_formation(slug):
    call_command("import_content", str(content_dir(slug) / "formation.json"), verbosity=0)


# --- Contrôles génériques, pour chaque formation rédigée -------------------------------------------------------------


@by_formation
def test_formation_parts_and_modules_are_bilingual(slug):
    data = manifest(slug)
    assert_bilingual(data, "title", "formation")
    for partie, module in iter_modules(slug):
        assert_bilingual(partie, "title", partie["slug"])
        assert_bilingual(module, "title", module["dir"])


@by_formation
def test_every_section_has_a_french_and_an_english_text_file(slug):
    for _, module in iter_modules(slug):
        for section in module["sections"]:
            assert_bilingual(section, "title", f"{module['dir']}/{section['file']}")
            for lang in LANGS:
                path = content_dir(slug) / module["dir"] / f"{section['file']}.{lang}.md"
                assert path.exists() and path.read_text(encoding="utf-8").strip(), f"{path} manquant ou vide"


@by_formation
def test_every_question_choice_and_explanation_is_bilingual(slug):
    ids = set()
    for _, questions in questions_by_module(slug):
        for q in questions:
            assert q["id"] not in ids, f"identifiant en double : {q['id']}"
            ids.add(q["id"])
            assert_bilingual(q, "prompt", q["id"])
            assert_bilingual(q, "explanation", q["id"])
            for i, choice in enumerate(q["choices"]):
                assert_bilingual(choice, "text", f"{q['id']} choix {i}")
    assert ids, "aucune question"


@by_formation
def test_question_ids_carry_the_prefix_of_their_formation(slug):
    """M12 : `external_id` est unique dans toute la base ; le préfixe de la formation évite tout conflit."""
    prefix = RULES[slug]["id_prefix"]
    wrong = [q["id"] for _, questions in questions_by_module(slug) for q in questions if not q["id"].startswith(prefix)]
    assert wrong == []


@by_formation
@pytest.mark.django_db
def test_versioned_content_imports_with_english_everywhere(slug):
    import_formation(slug)
    modules = Module.objects.filter(partie__formation__slug=slug)
    assert modules.exists()
    assert not modules.filter(title_en="").exists()
    assert not Section.objects.filter(module__in=modules, body_md_en="").exists()
    assert not Question.objects.filter(module__in=modules, prompt_en="").exists()
    assert not Question.objects.filter(module__in=modules, explanation_en="").exists()


@by_formation
def test_every_markdown_file_is_referenced_by_the_manifest(slug):
    referenced = set()
    for _, module in iter_modules(slug):
        for section in module["sections"]:
            for lang in LANGS:
                referenced.add((content_dir(slug) / module["dir"] / f"{section['file']}.{lang}.md").resolve())
    on_disk = {p.resolve() for p in content_dir(slug).rglob("*.md")}
    assert sorted(str(p) for p in on_disk - referenced) == []


@by_formation
def test_every_question_cites_an_existing_section_of_its_module(slug):
    for module, questions in questions_by_module(slug):
        files = {s["file"] for s in module["sections"]}
        for q in questions:
            assert q.get("section") in files, f"{q['id']} : section {q.get('section')!r} inconnue dans {module['dir']}"


@by_formation
def test_every_content_section_is_covered_by_at_least_one_question(slug):
    for module, questions in questions_by_module(slug):
        cited = {q.get("section") for q in questions}
        missing = [s["file"] for s in module["sections"] if s["kind"] == "content" and s["file"] not in cited]
        assert missing == [], f"{module['dir']} : sections sans question {missing}"


@by_formation
def test_review_flags_are_explicit_for_both_languages(slug):
    """Toute nouvelle question entre avec des drapeaux de relecture explicites, FR et EN."""
    for _, questions in questions_by_module(slug):
        for q in questions:
            assert set(q["reviewed"]) == {"fr", "en"}, q["id"]
            assert all(isinstance(v, bool) for v in q["reviewed"].values()), q["id"]


@by_formation
@pytest.mark.django_db
def test_import_never_publishes_and_only_reviewed_questions_can_be(slug):
    """E12 : le contenu rédigé par Claude arrive en brouillon ; seul ce qui a été relu se publie."""
    import_formation(slug)
    assert not Question.objects.published().exists()  # l'import ne publie jamais tout seul
    reviewed = Question.objects.filter(reviewed_fr=True, reviewed_en=True)
    for question in reviewed:
        question.publish()
    assert Question.objects.published().count() == reviewed.count()


@by_formation
@pytest.mark.django_db
def test_every_question_is_publishable_once_reviewed(slug):
    import_formation(slug)
    refused = []
    for question in Question.objects.all():
        question.reviewed_fr = question.reviewed_en = True  # simule la relecture du formateur
        try:
            question.validate_for_publication()
        except Exception as exc:  # noqa: BLE001
            refused.append(f"{question.external_id}: {exc}")
    assert refused == []
    assert Question.objects.count() == sum(len(qs) for _, qs in questions_by_module(slug))


@by_formation
def test_every_module_has_six_to_eight_sections_with_one_mini_project(slug):
    for _, module in iter_modules(slug):
        kinds = [s["kind"] for s in module["sections"]]
        assert 6 <= len(kinds) <= 8, f"{module['dir']} : {len(kinds)} sections"
        assert kinds.count("practical") == 1, f"{module['dir']} : un mini-projet attendu"


@by_formation
def test_question_volumes_and_types_per_module(slug):
    """E12 et M4 : 15 de quiz, 12 d'examen, minimum de numériques propre au module, questions interactives."""
    by_dir = dict((m["dir"], qs) for m, qs in questions_by_module(slug))
    for folder, questions in by_dir.items():
        quiz = [q for q in questions if q["usage"] == "quiz"]
        exam = [q for q in questions if q["usage"] == "exam"]
        assert len(quiz) >= 15 and len(exam) >= 12, f"{folder} : {len(quiz)} quiz, {len(exam)} examen"
        if slug == "electro":
            assert sum(q["type"] in ("matching", "hotspot") for q in quiz) >= 2, f"{folder} : moins de 2 interactives"
        else:
            assert {"matching", "hotspot"} <= {q["type"] for q in quiz}, f"{folder} : appariement et zone cliquable attendus"
    assert numeric_shortfalls(by_dir, {f: n for f, n in RULES[slug]["numeric"].items() if f in by_dir}) == []


@by_formation
def test_matching_pairs_are_bilingual(slug):
    for _, questions in questions_by_module(slug):
        for q in questions:
            for i, pair in enumerate(q.get("pairs", [])):
                assert_bilingual(pair, "left", f"{q['id']} paire {i}")
                assert_bilingual(pair, "right", f"{q['id']} paire {i}")


@by_formation
def test_hotspot_diagrams_exist_next_to_the_questions(slug):
    for module, questions in questions_by_module(slug):
        for q in questions:
            if q["type"] == "hotspot":
                assert (content_dir(slug) / module["dir"] / q["svg"]).exists(), q["id"]


@by_formation
def test_every_content_section_shows_at_least_two_existing_diagrams_in_both_languages(slug):
    for _, module in iter_modules(slug):
        for section in module["sections"]:
            if section["kind"] != "content":
                continue
            for lang in LANGS:
                images = IMAGE.findall(section_text(slug, module, section, lang))
                where = f"{module['dir']}/{section['file']}.{lang}"
                assert len(images) >= 2, f"{where} : {len(images)} schéma(s)"
                for alt, src in images:
                    assert alt.strip(), f"{where} : texte alternatif manquant pour {src}"
                    assert (STATIC / src.removeprefix("/static/")).exists(), f"{where} : {src} introuvable"


@by_formation
def test_no_long_dash_in_learner_facing_text(slug):
    """Guide de style : ni tiret cadratin ni demi-cadratin dans les textes destinés aux apprenants."""
    for path in list(content_dir(slug).rglob("*.md")) + list(content_dir(slug).rglob("*.json")):
        text = path.read_text(encoding="utf-8")
        assert chr(0x2014) not in text and chr(0x2013) not in text, path  # tirets cadratin et demi-cadratin


@by_formation
def test_every_content_diagram_is_well_formed_and_inert(slug):
    from xml.etree import ElementTree

    from config.uploads import ACTIVE_SVG

    svgs = list((STATIC / "content" / slug).rglob("*.svg")) + list(content_dir(slug).rglob("*.svg"))
    assert svgs, "aucun schéma"
    for path in svgs:
        raw = path.read_bytes()
        assert ElementTree.fromstring(raw).tag.endswith("svg"), path
        assert not ACTIVE_SVG.search(raw), f"{path} : contenu actif"


@by_formation
def test_english_pages_show_english_diagrams_of_their_own_formation(slug):
    """Les schémas portent du texte : la version anglaise pointe vers static/content/<slug>/en/, la française vers
    static/content/<slug>/ ; aucune formation n'emprunte les schémas d'une autre."""
    from xml.etree import ElementTree

    for _, module in iter_modules(slug):
        for section in module["sections"]:
            for lang in LANGS:
                for _alt, src in IMAGE.findall(section_text(slug, module, section, lang)):
                    where = f"{module['dir']}/{section['file']}.{lang} : {src}"
                    assert src.startswith(f"/static/content/{slug}/"), where
                    assert src.startswith(f"/static/content/{slug}/en/") == (lang == "en"), where
                    if lang == "en":
                        svg = ElementTree.fromstring((STATIC / src.removeprefix("/static/")).read_bytes())
                        texts = " ".join(t.text or "" for t in svg.iter() if t.tag.endswith("text"))
                        assert not re.search(r"\d,\d", texts), f"{src} : virgule décimale"


# --- Formation `electro`, Partie 1 (AGENTS.md, E3 et E12) ------------------------------------------------------------


def test_part_one_has_the_four_modules_of_chapters_one_to_four():
    partie = next(p for p in manifest()["parties"] if p["slug"] == "p1")
    assert [m["dir"] for m in partie["modules"]] == ["p1/m1", "p1/m2", "p1/m3", "p1/m4"]
    assert manifest()["open"] is True


# --- Partie 2 « Courant alternatif et filtres » (AGENTS.md, E25 à E29) -------------------------------------------------


def part(slug, formation="electro"):
    return next(p for p in manifest(formation)["parties"] if p["slug"] == slug)


def test_part_two_has_the_three_modules_of_chapters_five_to_seven():
    p2 = part("p2")
    assert [m["dir"] for m in p2["modules"]] == ["p2/m5", "p2/m6", "p2/m7"]
    assert_bilingual(p2, "description", "p2")
    assert "Partie 1" in p2["description"]["fr"] and "Part 1" in p2["description"]["en"]


def test_part_two_mini_projects_offer_both_measurement_variants_and_a_safety_rule():
    """US-43 : oscilloscope et GBF, ou multimètre seul avec transformateur 230 V vers 9 ou 12 V AC ; sécurité en tête."""
    for module in part("p2")["modules"]:
        [practical] = [s for s in module["sections"] if s["kind"] == "practical"]
        for lang in LANGS:
            assert practical_problems(section_text("electro", module, practical, lang), lang, "230 V") == [], module["dir"]


def test_part_two_sections_use_the_three_new_calculators():
    """US-42 : réactance (M5), fréquence de coupure (M6), résonance (M7), en français et en anglais."""
    for module, kind in zip(part("p2")["modules"], ("reactance", "cutoff", "resonance")):
        for lang in LANGS:
            texts = [section_text("electro", module, s, lang) for s in module["sections"]]
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
        voltage = "230 V" if module["dir"] in ("p3/m10", "p3/m11") else ""
        for lang in LANGS:
            assert practical_problems(section_text("electro", module, practical, lang), lang, voltage) == [], module["dir"]


def test_part_three_sections_use_their_calculators():
    """US-50 et E38 : gain (M8), résonance (M9), transformateur (M10), ondulation (M11), en français et en anglais."""
    for module, kind in zip(part("p3")["modules"], ("gain", "resonance", "transformer", "ripple")):
        for lang in LANGS:
            texts = [section_text("electro", module, s, lang) for s in module["sections"]]
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

    import_formation("electro")
    import_formation("electro")

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

    import_formation("electro")
    call_command("publish_reviewed", stdout=io.StringIO())

    published = Question.objects.published().filter(module__partie__slug="p3")
    assert published.count() == 108
    assert published.filter(usage="exam").count() == 48


# --- Formation `moteurs` (grill M1 à M21), vérifiée partie par partie dès que son manifeste existe --------------------

MOTEURS = formation_param("moteurs").marks  # même justification que FORMATIONS
MOTEURS_SECTIONS = {"p1/m1": 7, "p1/m2": 8, "p1/m3": 7, "p2/m4": 7, "p2/m5": 7, "p2/m6": 8,
                    "p3/m7": 7, "p3/m8": 7, "p3/m9": 8, "p4/m10": 7, "p4/m11": 7, "p4/m12": 8}


@MOTEURS[0]
def test_moteurs_modules_follow_the_plan_of_m3_m17_and_m18():
    """M3, M17, M18 : modules rangés dans leur partie, nombre de sections de chaque module livré."""
    counts = {m["dir"]: len(m["sections"]) for _, m in iter_modules("moteurs")}
    assert counts == {folder: MOTEURS_SECTIONS[folder] for folder in counts}
    assert list(counts) == [f for f in MOTEURS_DIRS if f in counts]


@MOTEURS[0]
def test_moteurs_mini_projects_put_safety_first_at_24_volts_with_both_variants():
    """M5, M20 : très basse tension (24 V au plus), sécurité en tête, variantes oscilloscope et multimètre seul."""
    for _, module in iter_modules("moteurs"):
        [practical] = [s for s in module["sections"] if s["kind"] == "practical"]
        for lang in LANGS:
            assert practical_problems(section_text("moteurs", module, practical, lang), lang, "24 V") == [], module["dir"]


@MOTEURS[0]
def test_moteurs_has_one_hotspot_question_per_module():
    """M19 : une question sur schéma par module."""
    counts = {m["dir"]: sum(q["type"] == "hotspot" for q in qs) for m, qs in questions_by_module("moteurs")}
    assert all(n >= 1 for n in counts.values()), counts


@MOTEURS[0]
def test_moteurs_content_uses_iec_mains_and_plc_addresses_and_links_only_to_its_own_sections():
    """M2, M7, M11 et US-78 : ni 60 Hz, 460 V ou 120 V, ni adresse Rockwell (I:1/0), ni lien vers une section d'`electro`
    (un rappel renvoie à la fiche du catalogue)."""
    assert scan_folder(content_dir("moteurs")) == []
