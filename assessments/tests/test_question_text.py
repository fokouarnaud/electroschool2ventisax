"""US-109 (formation `esp32`, C6) : énoncé, choix et explication d'une question en Markdown restreint."""
import html
import json
import re
from pathlib import Path

import pytest
from django.conf import settings

from courses.rendering import render_question_text

BLOCK_PROMPT = "Qu'affiche le terminal après une seconde ?\n\n```cpp\nSerial.println(97);\n```"


def test_inline_code_in_a_question_stays_inline():
    assert render_question_text("Que fait `digitalWrite(2, HIGH)` ?") == "Que fait <code>digitalWrite(2, HIGH)</code> ?"


def test_a_plain_question_renders_as_its_own_text():
    assert render_question_text("Combien vaut R ?") == "Combien vaut R ?"


def test_a_code_block_in_a_question_becomes_a_pre_block():
    rendered = render_question_text(BLOCK_PROMPT)

    assert "<p>Qu'affiche le terminal après une seconde ?</p>" in rendered
    assert "<pre><code>Serial.println(97);\n</code></pre>" in rendered


@pytest.mark.parametrize("source, forbidden", [
    ("[la doc](https://example.com)", "<a"),
    ("![x](/static/x.svg)", "<img"),
    ("## Titre", "<h2"),
    ("| a |\n|---|\n| 1 |", "<table"),
    ("<script>alert(1)</script>", "<script"),
])
def test_a_question_keeps_only_paragraphs_code_and_emphasis(source, forbidden):
    assert forbidden not in render_question_text(source)


def test_code_in_a_question_is_escaped():
    assert render_question_text("`a < b`") == "<code>a &lt; b</code>"


def _visible_text(markup):
    return " ".join(html.unescape(re.sub(r"<[^>]+>", " ", markup)).split())


def _texts(question):
    yield question["prompt"]
    yield question.get("explanation") or {}
    for choice in question.get("choices", []):
        yield choice["text"]


@pytest.mark.parametrize("slug", ["electro", "moteurs"])
def test_existing_questions_render_to_the_same_visible_text(slug):
    """Garde-fou : passer au Markdown ne change aucun énoncé, choix ni explication d'`electro` ou de `moteurs`."""
    files = sorted((settings.BASE_DIR / "content" / slug).glob("p*/m*/questions.json"))
    assert files
    changed = []
    for path in files:
        for question in json.loads(Path(path).read_text(encoding="utf-8")):
            for text in _texts(question):
                for lang, value in text.items():
                    if _visible_text(render_question_text(value)) != " ".join(value.split()):
                        changed.append((question["id"], lang, value))
    assert changed == []


@pytest.mark.django_db
def test_the_quiz_page_shows_the_prompt_code_outside_the_legend(client, enrolled, module, question_factory):
    from assessments.models import Assessment
    from assessments.services import start_attempt

    question = question_factory(module)
    question.prompt_fr = BLOCK_PROMPT
    question.save()
    attempt = start_attempt(enrolled, Assessment.quiz_for(module))
    client.force_login(enrolled)

    page = client.get(f"/fr/tentatives/{attempt.public_id}/").content.decode()

    legend = re.search(r"<legend[^>]*>(.*?)</legend>", page, re.S).group(1)
    assert "<pre>" not in legend
    assert "<pre><code>Serial.println(97);\n</code></pre>" in page


# --- US-121 et US-129 (formation `esp32`) : le code des choix et des appariements se lit partout ---------------------


@pytest.fixture
def code_matching(module):
    from assessments.models import Question

    question = Question.objects.create(module=module, qtype="matching", prompt_fr="Associez chaque niveau à son écriture.",
                                       prompt_en="Match.", reviewed_fr=True, reviewed_en=True)
    question.pairs.create(left_fr="Arduino", right_fr="`digitalWrite(LED_PIN, HIGH)`", order=1)
    question.pairs.create(left_fr="ESP-IDF", right_fr="`gpio_set_level(pin, 1)`", order=2)
    question.publish()
    return question


def answer_matching_correctly(attempt, question):
    from assessments.services import save_answer

    pairs = {str(p.public_id): str(p.public_id) for p in question.pairs.all()}
    save_answer(attempt, question.public_id, [], pairs=pairs)


@pytest.mark.django_db
def test_the_corrected_matching_shows_code_as_code(client, enrolled, module, code_matching):
    from assessments.models import Assessment
    from assessments.services import start_attempt, submit_attempt

    attempt = start_attempt(enrolled, Assessment.quiz_for(module))
    answer_matching_correctly(attempt, code_matching)
    submit_attempt(attempt)
    client.force_login(enrolled)

    page = client.get(f"/fr/tentatives/{attempt.public_id}/resultat/").content.decode()

    assert "<code>digitalWrite(LED_PIN, HIGH)</code>" in page
    assert "`digitalWrite" not in page


@pytest.mark.django_db
def test_matching_options_show_code_without_backticks(client, enrolled, module, code_matching):
    from assessments.models import Assessment
    from assessments.services import start_attempt

    attempt = start_attempt(enrolled, Assessment.quiz_for(module))
    client.force_login(enrolled)

    page = client.get(f"/fr/tentatives/{attempt.public_id}/").content.decode()

    assert ">digitalWrite(LED_PIN, HIGH)</option>" in page
    assert "`" not in page.split("<main", 1)[1]


@pytest.mark.django_db
def test_the_trainer_reads_a_code_answer_as_code(client, enrolled, promotion, module, question_factory):
    from accounts.models import User
    from assessments.models import Assessment
    from assessments.services import save_answer, start_attempt, submit_attempt

    question = question_factory(module)
    right = question.choices.filter(is_correct=True).first()
    right.text_fr = "`97`"
    right.save()
    attempt = start_attempt(enrolled, Assessment.quiz_for(module))
    save_answer(attempt, question.public_id, [right.public_id])
    submit_attempt(attempt)
    trainer = User.objects.create_user(username="formateur", password="x-Secret-123", role=User.Role.TRAINER)
    promotion.trainers.add(trainer)
    client.force_login(trainer)

    page = client.get(f"/fr/formateur/tentatives/{attempt.public_id}/").content.decode()

    assert "<code>97</code>" in page
    assert "`97`" not in page
