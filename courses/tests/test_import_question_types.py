"""US-37 : l'import versionné gère les questions numériques, d'appariement et sur schéma, et l'ouverture au catalogue."""
import json
from decimal import Decimal

import pytest
from django.core.management import call_command

from assessments.models import Question
from courses.models import Formation

SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 50"><rect width="100" height="50"/></svg>'
BILINGUAL = {"fr": "Q ?", "en": "Q?"}
REVIEWED = {"fr": True, "en": True}

QUESTIONS = [
    {"id": "e-p1-m1-num", "type": "numeric", "prompt": BILINGUAL, "reviewed": REVIEWED,
     "numeric": {"value": "0.0047", "unit": "A", "tolerance_pct": 5}},
    {"id": "e-p1-m1-match", "type": "matching", "prompt": BILINGUAL, "reviewed": REVIEWED,
     "pairs": [
         {"left": {"fr": "R", "en": "R"}, "right": {"fr": "Résistance", "en": "Resistor"}},
         {"left": {"fr": "C", "en": "C"}, "right": {"fr": "Condensateur", "en": "Capacitor"}},
     ]},
    {"id": "e-p1-m1-hot", "type": "hotspot", "prompt": BILINGUAL, "reviewed": REVIEWED, "svg": "schemas/npn.svg",
     "choices": [
         {"text": {"fr": "Base", "en": "Base"}, "correct": True, "shape": {"x": 0, "y": 0, "w": 20, "h": 20}},
         {"text": {"fr": "Émetteur", "en": "Emitter"}, "shape": {"x": 50, "y": 0, "w": 20, "h": 20}},
     ]},
]


@pytest.fixture
def content_dir(tmp_path):
    module_dir = tmp_path / "p1" / "m1"
    (module_dir / "schemas").mkdir(parents=True)
    (module_dir / "schemas" / "npn.svg").write_text(SVG, encoding="utf-8")
    (module_dir / "questions.json").write_text(json.dumps(QUESTIONS), encoding="utf-8")
    manifest = {
        "slug": "electro", "open": True,
        "title": {"fr": "Électronique", "en": "Electronics"},
        "parties": [{"slug": "p1", "order": 1, "title": {"fr": "DC", "en": "DC"},
                     "modules": [{"order": 1, "dir": "p1/m1", "title": {"fr": "M1", "en": "M1"}, "sections": []}]}],
    }
    (tmp_path / "formation.json").write_text(json.dumps(manifest), encoding="utf-8")
    return tmp_path


def run_import(content_dir):
    call_command("import_content", str(content_dir / "formation.json"), verbosity=0)


@pytest.mark.django_db
def test_manifest_opens_the_formation_to_the_catalogue(content_dir):
    run_import(content_dir)

    assert Formation.objects.get(slug="electro").is_open


@pytest.mark.django_db
def test_numeric_question_is_imported_with_value_unit_and_tolerance(content_dir):
    run_import(content_dir)

    q = Question.objects.get(external_id="e-p1-m1-num")
    assert (q.qtype, q.numeric_value, q.unit, q.tolerance_pct) == ("numeric", Decimal("0.0047"), "A", 5)


@pytest.mark.django_db
def test_matching_question_is_imported_with_bilingual_pairs(content_dir):
    run_import(content_dir)

    q = Question.objects.get(external_id="e-p1-m1-match")
    assert [(p.left_fr, p.right_en) for p in q.pairs.all()] == [("R", "Resistor"), ("C", "Capacitor")]


@pytest.mark.django_db
def test_hotspot_question_reads_its_svg_file_and_zones(content_dir):
    run_import(content_dir)

    q = Question.objects.get(external_id="e-p1-m1-hot")
    assert q.hotspot_svg == SVG
    assert [c.shape["x"] for c in q.choices.all()] == [0, 50]


@pytest.mark.django_db
def test_imported_question_types_are_publishable(content_dir):
    run_import(content_dir)

    for q in Question.objects.all():
        q.publish()


@pytest.mark.django_db
def test_import_is_idempotent_for_pairs(content_dir):
    run_import(content_dir)
    run_import(content_dir)

    assert Question.objects.get(external_id="e-p1-m1-match").pairs.count() == 2


@pytest.mark.django_db
def test_changing_an_expected_value_sends_the_question_back_to_draft(content_dir):
    run_import(content_dir)
    q = Question.objects.get(external_id="e-p1-m1-num")
    q.publish()
    changed = [dict(QUESTIONS[0], numeric={"value": "0.0050", "unit": "A", "tolerance_pct": 5})] + QUESTIONS[1:]
    (content_dir / "p1" / "m1" / "questions.json").write_text(json.dumps(changed), encoding="utf-8")

    run_import(content_dir)

    q.refresh_from_db()
    assert q.status == Question.Status.DRAFT


@pytest.mark.django_db
def test_svg_path_cannot_escape_the_module_folder(content_dir):
    escaped = [dict(QUESTIONS[2], svg="../../../formation.json")]
    (content_dir / "p1" / "m1" / "questions.json").write_text(json.dumps(escaped), encoding="utf-8")

    with pytest.raises(ValueError):
        run_import(content_dir)


@pytest.fixture
def part_two_dir(tmp_path):
    """Manifeste à deux parties ; la Partie 2 contient une question de déphasage en degrés (dossier p2/m5)."""
    angle = {"id": "e-p2-m5-phase", "type": "numeric", "usage": "quiz", "prompt": BILINGUAL, "reviewed": REVIEWED,
             "numeric": {"value": "45", "unit": "°"}}
    draft = {**angle, "id": "e-p2-m5-draft", "reviewed": {"fr": True, "en": False}}
    for folder in ("p1/m1", "p2/m5"):
        (tmp_path / folder).mkdir(parents=True)
    (tmp_path / "p2" / "m5" / "questions.json").write_text(json.dumps([angle, draft], ensure_ascii=False), encoding="utf-8")
    manifest = {
        "slug": "electro", "open": True, "title": {"fr": "Électronique", "en": "Electronics"},
        "parties": [
            {"slug": "p1", "order": 1, "title": {"fr": "DC", "en": "DC"},
             "modules": [{"order": 1, "dir": "p1/m1", "title": {"fr": "M1", "en": "M1"}, "sections": []}]},
            {"slug": "p2", "order": 2, "title": {"fr": "AC", "en": "AC"},
             "modules": [{"order": 1, "dir": "p2/m5", "title": {"fr": "M5", "en": "M5"}, "sections": []}]},
        ],
    }
    (tmp_path / "formation.json").write_text(json.dumps(manifest), encoding="utf-8")
    return tmp_path


@pytest.mark.django_db
def test_part_two_import_is_idempotent_and_publishes_only_reviewed_questions(part_two_dir, learner):
    """US-45, US-46 et US-41 : import répété, publication des seules questions relues, réponse en degrés notée."""
    from assessments.models import Assessment
    from assessments.services import save_answer, start_attempt, submit_attempt
    from courses.models import Module

    run_import(part_two_dir)
    call_command("publish_reviewed", stdout=__import__("io").StringIO())
    run_import(part_two_dir)

    m5 = Module.objects.get(partie__slug="p2", order=1)
    assert Module.objects.filter(partie__slug="p2").count() == 1
    phase = Question.objects.get(external_id="e-p2-m5-phase")
    assert (phase.module, phase.unit, phase.numeric_value) == (m5, "°", Decimal("45"))
    assert phase.status == Question.Status.PUBLISHED  # inchangé : reste publiée après le second import
    assert Question.objects.get(external_id="e-p2-m5-draft").status == Question.Status.DRAFT

    attempt = start_attempt(learner, Assessment.quiz_for(m5))
    save_answer(attempt, phase.public_id, [], text="45,5 °")
    assert submit_attempt(attempt).score_pct == 100
