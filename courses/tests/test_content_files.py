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
    [partie] = manifest()["parties"]
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
