"""US-118 à US-129 (formation `esp32`) : règles backend vérifiées sur des données de la forme d'`esp32`, avant le contenu
réel (livraisons 2 à 4), dont les garde-fous sont dans test_content_files.py et esp32_rules.py."""
import io
import json
import re
from decimal import Decimal
from fractions import Fraction

import pytest
from django.core.management import call_command

from accounts.models import Promotion, User
from assessments.models import Assessment, Question
from assessments.scoring import score_numeric
from assessments.services import save_answer, start_attempt, submit_attempt
from catalog.models import Enrollment
from certificates.models import Certificate
from certificates.tests.test_achievements import complete_module, take_exam
from courses.models import Formation, Module, Partie, Section

PARTS = (
    ("p1", "Premiers pas et entrées-sorties", ("L'ESP32 et sa carte", "Sorties numériques", "Entrées numériques")),
    ("p2", "Temps, mesures et terminal", ("Temporisations et interruptions", "Le terminal série", "Analogique et tactile")),
    ("p3", "Bus, mémoire et connectivité", ("Bus I2C et SPI", "Mémoire et énergie", "Wi-Fi et serveur web")),
)
BLINK_FR = "```cpp\n// Broche de la LED\nconst uint8_t LED_PIN = 2;\n```"
BLINK_EN = "```cpp\n// LED pin\nconst uint8_t LED_PIN = 2;\n```"
READING_PROMPT = "Qu'affiche le terminal ?\n\n```cpp\nSerial.println('a' + 0);\n```"


@pytest.fixture
def esp32(db):
    formation = Formation.objects.create(title_fr="Microcontrôleurs : l'ESP32", slug="esp32", order=3, is_open=True, icon="code")
    for order, (slug, title, modules) in enumerate(PARTS, start=1):
        partie = Partie.objects.create(formation=formation, title_fr=title, order=order, slug=slug)
        for rank, module_title in enumerate(modules, start=1):
            Module.objects.create(partie=partie, title_fr=module_title, order=rank, duration_hours=10 if module_title.startswith("Wi-Fi") else 8)
    return formation


@pytest.fixture
def p1(esp32):
    return esp32.parties.get(slug="p1")


@pytest.fixture
def esp32_learner(esp32):
    user = User.objects.create_user(username="fotso", password="x-Secret-123", first_name="Line", last_name="Fotso")
    Enrollment.objects.create(user=user, formation=esp32, source=Enrollment.Source.CATALOG)
    return user


def module_named(formation, title):
    return Module.objects.get(partie__formation=formation, title_fr=title)


def published(module, qtype="single", **fields):
    question = Question.objects.create(module=module, qtype=qtype, prompt_fr=fields.pop("prompt_fr", "Q ?"), prompt_en="Q?",
                                       reviewed_fr=True, reviewed_en=True, **fields)
    return question


# --- US-118 : trois parties, neuf modules numérotés M1 à M9, aucun verrou ------------------------------------------


def test_modules_are_numbered_m1_to_m9_across_the_three_parts(esp32):
    from progress.services import module_number

    numbers = [module_number(m) for m in Module.objects.filter(partie__formation=esp32).order_by("partie__order", "order")]

    assert numbers == list(range(1, 10))


def test_a_part_three_section_opens_without_part_one_nor_electro(client, esp32, esp32_learner):
    section = Section.objects.create(module=module_named(esp32, "Wi-Fi et serveur web"), title_fr="Station", order=1)
    client.force_login(esp32_learner)

    assert client.get(f"/fr/sections/{section.public_id}/").status_code == 200


# --- US-119 : un programme se lit dans la section, commentaires dans la langue de la page --------------------------


def test_a_section_shows_its_program_with_comments_in_the_page_language(client, esp32, esp32_learner):
    section = Section.objects.create(module=module_named(esp32, "Sorties numériques"), title_fr="Blink", title_en="Blink",
                                     order=1, body_md_fr=BLINK_FR, body_md_en=BLINK_EN)
    client.force_login(esp32_learner)

    fr = client.get(f"/fr/sections/{section.public_id}/").content.decode()
    en = client.get(f"/en/sections/{section.public_id}/").content.decode()

    assert "<pre><code>// Broche de la LED\nconst uint8_t LED_PIN = 2;\n</code></pre>" in fr
    assert "<pre><code>// LED pin\nconst uint8_t LED_PIN = 2;\n</code></pre>" in en


# --- US-121 : question de lecture de code, posée en QCM -------------------------------------------------------------


def test_a_code_reading_question_is_scored_and_corrected_with_its_program(client, esp32, esp32_learner):
    module = module_named(esp32, "Le terminal série")
    question = published(module, prompt_fr=READING_PROMPT)
    right = question.choices.create(text_fr="`97`", is_correct=True, order=1)
    question.choices.create(text_fr="`a`", is_correct=False, order=2)
    question.publish()
    attempt = start_attempt(esp32_learner, Assessment.quiz_for(module))
    save_answer(attempt, question.public_id, [right.public_id])
    submit_attempt(attempt)
    client.force_login(esp32_learner)

    page = client.get(f"/fr/tentatives/{attempt.public_id}/resultat/").content.decode()

    attempt.refresh_from_db()
    assert attempt.score_pct == 100
    assert "<pre><code>Serial.println('a' + 0);\n</code></pre>" in page
    assert "<code>97</code>" in page


# --- US-122 : réponse entière sans unité, en décimal ----------------------------------------------------------------


@pytest.mark.parametrize("answer, score", [
    ("2048", 1),          # valeur ADC de 1,65 V
    ("2048 V", 0),        # une unité saisie rend la réponse fausse
    ("0x800", 0),         # aucune saisie hexadécimale (C8)
    ("0b100000000000", 0),
    ("2047", 1),          # dans la tolérance de 2 %
])
def test_an_adc_value_is_answered_as_a_decimal_integer_without_unit(answer, score):
    assert score_numeric(Decimal("2048"), "", Decimal("2"), answer) == Fraction(score)


def test_an_ascii_code_needs_the_exact_integer():
    assert score_numeric(Decimal("97"), "", Decimal("0"), "97") == 1
    assert score_numeric(Decimal("97"), "", Decimal("0"), "98") == 0


def test_a_duty_cycle_is_answered_in_percent():
    assert score_numeric(Decimal("50"), "%", Decimal("2"), "50 %") == 1
    assert score_numeric(Decimal("50"), "%", Decimal("2"), "0,5") == 0


# --- US-123 : question sur schéma, tout ou rien ---------------------------------------------------------------------


@pytest.mark.parametrize("zone, score", [("flash", 100), ("sure", 0)])
def test_clicking_the_flash_pin_on_the_devkit_is_all_or_nothing(esp32, esp32_learner, zone, score):
    module = module_named(esp32, "L'ESP32 et sa carte")
    question = published(module, qtype="hotspot", hotspot_svg='<svg xmlns="http://www.w3.org/2000/svg"></svg>')
    zones = {name: question.choices.create(text_fr=name, is_correct=name == "flash", order=n,
                                           shape={"x": 10 * n, "y": 0, "w": 5, "h": 5})
             for n, name in enumerate(("flash", "sure"), start=1)}
    question.publish()
    attempt = start_attempt(esp32_learner, Assessment.quiz_for(module))

    save_answer(attempt, question.public_id, [zones[zone].public_id])
    submit_attempt(attempt)

    attempt.refresh_from_db()
    assert attempt.score_pct == score


# --- US-124 : le mini-projet s'ouvre sur la consigne de sécurité --------------------------------------------------


def test_the_mini_project_page_shows_the_safety_rule_before_both_variants(client, esp32, esp32_learner):
    body = ("## Sécurité\nAu plus 12 V CC, jamais 5 V sur une broche, masse commune.\n\n"
            "## Variante kit complet\nOscilloscope.\n\n## Variante multimètre seul\nTerminal série.")
    section = Section.objects.create(module=module_named(esp32, "Sorties numériques"), title_fr="Mini-projet", order=8,
                                     kind=Section.Kind.PRACTICAL, body_md_fr=body)
    client.force_login(esp32_learner)

    page = client.get(f"/fr/sections/{section.public_id}/").content.decode()

    assert 0 < page.index("12 V CC") < page.index("Variante kit complet") < page.index("Variante multimètre seul")


# --- US-126 : examen de partie de 30 questions, certificat distinct, aucun certificat de formation ------------------


@pytest.fixture
def p1_with_questions(p1, question_factory):
    for module in p1.modules.all():
        Section.objects.create(module=module, title_fr=f"Section de {module.title}", order=1)
        question_factory(module)
        for _ in range(12):
            question_factory(module, usage="exam")
    return p1


def test_the_part_exam_opens_after_its_three_modules_and_draws_ten_per_module(esp32_learner, p1_with_questions):
    from progress.services import exam_unlocked

    m1, m2, m3 = p1_with_questions.modules.order_by("order")
    complete_module(esp32_learner, m1)
    complete_module(esp32_learner, m2)
    assert not exam_unlocked(esp32_learner, p1_with_questions)
    complete_module(esp32_learner, m3)
    exam = Assessment.exam_for(p1_with_questions)

    attempt = start_attempt(esp32_learner, exam)

    assert (exam.pass_threshold, exam.max_attempts, exam.duration_minutes) == (70, 3, 60)
    assert attempt.attempt_questions.count() == 30


def test_passing_esp32_part_one_issues_its_own_verifiable_certificate_and_no_formation_one(client, esp32_learner,
                                                                                          p1_with_questions):
    for module in p1_with_questions.modules.all():
        complete_module(esp32_learner, module)

    take_exam(esp32_learner, p1_with_questions, right=True)

    [certificate] = Certificate.objects.filter(user=esp32_learner)
    assert certificate.partie == p1_with_questions
    assert "Premiers pas et entrées-sorties" in client.get(f"/fr/verify/{certificate.public_id}/").content.decode()


# --- US-127 : formation fermée pendant la fumée de production ---------------------------------------------------


def test_a_closed_esp32_is_hidden_and_refuses_free_enrollment_but_admits_an_enrolled_test_account(client, esp32,
                                                                                                    esp32_learner):
    esp32.is_open = False
    esp32.save()
    section = Section.objects.create(module=module_named(esp32, "L'ESP32 et sa carte"), title_fr="Carte", order=1)
    visitor = User.objects.create_user(username="visiteur", password="x-Secret-123")

    assert "Microcontrôleurs" not in client.get("/fr/catalogue/").content.decode()
    client.force_login(visitor)
    client.post(f"/fr/catalogue/{esp32.public_id}/inscription/")
    assert not Enrollment.objects.filter(user=visitor, formation=esp32).exists()
    client.force_login(esp32_learner)
    assert client.get(f"/fr/sections/{section.public_id}/").status_code == 200


# --- US-128 : les 81 questions relues d'une partie sont publiées au déploiement -----------------------------------


def question_data(qid, usage, reviewed=True):
    return {
        "id": qid, "type": "single", "usage": usage, "section": "01-intro",
        "prompt": {"fr": READING_PROMPT, "en": "What does the terminal show?\n\n```cpp\nSerial.println('a' + 0);\n```"},
        "explanation": {"fr": "Le code ASCII de « a ».", "en": "The ASCII code of 'a'."},
        "reviewed": {"fr": reviewed, "en": reviewed},
        "choices": [{"text": {"fr": "`97`", "en": "`97`"}, "correct": True}, {"text": {"fr": "`a`", "en": "`a`"}, "correct": False}],
    }


@pytest.fixture
def esp32_p1_dir(tmp_path):
    modules = []
    for n, title in enumerate(PARTS[0][2], start=1):
        folder = tmp_path / "p1" / f"m{n}"
        folder.mkdir(parents=True)
        (folder / "01-intro.fr.md").write_text(BLINK_FR, encoding="utf-8")
        (folder / "01-intro.en.md").write_text(BLINK_EN, encoding="utf-8")
        questions = [question_data(f"s-p1-m{n}-q{i:02d}", "quiz" if i <= 15 else "exam") for i in range(1, 28)]
        (folder / "questions.json").write_text(json.dumps(questions), encoding="utf-8")
        modules.append({"order": n, "dir": f"p1/m{n}", "duration_hours": 6 if n == 1 else 8, "title": {"fr": title, "en": title},
                        "sections": [{"order": 1, "file": "01-intro", "title": {"fr": "Intro", "en": "Intro"}}]})
    manifest = {"slug": "esp32", "icon": "code", "open": False,
                "title": {"fr": "Microcontrôleurs : l'ESP32", "en": "Microcontrollers: the ESP32"},
                "parties": [{"slug": "p1", "order": 1, "title": {"fr": PARTS[0][1], "en": "First steps, inputs and outputs"},
                             "modules": modules}]}
    (tmp_path / "formation.json").write_text(json.dumps(manifest), encoding="utf-8")
    return tmp_path


@pytest.mark.django_db
def test_publish_reviewed_publishes_the_81_reviewed_questions_of_an_esp32_part(esp32_p1_dir):
    call_command("import_content", str(esp32_p1_dir / "formation.json"), verbosity=0)
    out = io.StringIO()

    call_command("publish_reviewed", stdout=out)

    published_questions = Question.objects.published().filter(module__partie__formation__slug="esp32")
    assert published_questions.count() == 81
    assert "esp32 : 81 question(s) publiée(s)." in out.getvalue().splitlines()
    assert not Formation.objects.get(slug="esp32").is_open


@pytest.mark.django_db
def test_an_unreviewed_esp32_question_stays_a_draft(esp32_p1_dir):
    path = esp32_p1_dir / "p1" / "m1" / "questions.json"
    questions = json.loads(path.read_text(encoding="utf-8"))
    questions[0]["reviewed"] = {"fr": True, "en": False}
    path.write_text(json.dumps(questions), encoding="utf-8")
    call_command("import_content", str(esp32_p1_dir / "formation.json"), verbosity=0)

    call_command("publish_reviewed", stdout=io.StringIO())

    assert Question.objects.get(external_id="s-p1-m1-q01").status == "draft"
    assert Question.objects.published().count() == 80


# --- US-129 : l'espace formateur couvre les 9 modules et les 3 examens, sans code propre à `esp32` ---------------


@pytest.fixture
def esp32_trainer(esp32, esp32_learner):
    trainer = User.objects.create_user(username="tchana", password="x-Secret-123", role=User.Role.TRAINER)
    promotion = Promotion.objects.create(name="Embarqué 2026", formation=esp32)
    promotion.trainers.add(trainer)
    Enrollment.objects.filter(user=esp32_learner).update(promotion=promotion)
    return trainer


def test_trainer_table_lists_the_nine_modules_and_three_part_exams(client, esp32_trainer):
    client.force_login(esp32_trainer)

    response = client.get("/fr/formateur/")

    [table] = response.context["tables"]
    assert [m.title for m in table["modules"]] == [title for _, _, modules in PARTS for title in modules]
    html = response.content.decode()
    assert all(f">Examen P{n}</th>" in html for n in (1, 2, 3)) and ">Examen P4</th>" not in html
    assert "M9 : Wi-Fi et serveur web" in html


def test_csv_export_has_a_column_per_esp32_module_and_part_exam(client, esp32_trainer, esp32_learner):
    client.force_login(esp32_trainer)

    header, *rows = client.get("/fr/formateur/export.csv").content.decode("utf-8-sig").splitlines()

    assert header.count(";") == 2 + 9 + 2 * 3
    assert any(esp32_learner.username in row for row in rows)


def test_the_trainer_reads_a_code_reading_answer_in_the_attempt_detail(client, esp32_trainer, esp32_learner, esp32):
    module = module_named(esp32, "Le terminal série")
    question = published(module, prompt_fr=READING_PROMPT)
    right = question.choices.create(text_fr="`97`", is_correct=True, order=1)
    question.publish()
    attempt = start_attempt(esp32_learner, Assessment.quiz_for(module))
    save_answer(attempt, question.public_id, [right.public_id])
    submit_attempt(attempt)
    client.force_login(esp32_trainer)

    page = client.get(f"/fr/formateur/tentatives/{attempt.public_id}/").content.decode()

    assert re.search(r"<pre><code>Serial\.println\('a' \+ 0\);\n</code></pre>", page)
