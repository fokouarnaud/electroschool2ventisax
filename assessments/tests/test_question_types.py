"""US-16 à US-18, US-20 : questions numériques, d'appariement et sur schéma, de la publication à la note ; temps passé."""
from decimal import Decimal

import pytest
from django.core.exceptions import ValidationError

from assessments.models import Assessment, Question
from assessments.services import save_answer, start_attempt, submit_attempt

SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 50"><rect width="100" height="50"/></svg>'


def reviewed(module, qtype, **fields):
    return Question.objects.create(
        module=module, qtype=qtype, prompt_fr="Q ?", prompt_en="Q?", reviewed_fr=True, reviewed_en=True, **fields
    )


@pytest.fixture
def numeric_q(module):
    q = reviewed(module, "numeric", numeric_value=Decimal("4700"), unit="Ω")
    q.publish()
    return q


@pytest.fixture
def matching_q(module):
    q = reviewed(module, "matching")
    for i, (left, right) in enumerate([("R", "Résistance"), ("C", "Condensateur"), ("L", "Bobine"), ("D", "Diode")]):
        q.pairs.create(left_fr=left, left_en=left, right_fr=right, right_en=right, order=i)
    q.publish()
    return q


@pytest.fixture
def hotspot_q(module):
    q = reviewed(module, "hotspot", hotspot_svg=SVG)
    q.choices.create(text_fr="Base", text_en="Base", is_correct=True, shape={"x": 0, "y": 0, "w": 20, "h": 20}, order=0)
    q.choices.create(text_fr="Émetteur", text_en="Emitter", shape={"x": 50, "y": 0, "w": 20, "h": 20}, order=1)
    q.publish()
    return q


def quiz_attempt(learner, module):
    return start_attempt(learner, Assessment.quiz_for(module))


# --- Publication ------------------------------------------------------------------------------------------------------


@pytest.mark.django_db
def test_numeric_question_needs_an_expected_value(module):
    with pytest.raises(ValidationError):
        reviewed(module, "numeric", unit="V").publish()


@pytest.mark.django_db
def test_numeric_question_has_no_choices(module):
    q = reviewed(module, "numeric", numeric_value=Decimal("12"), unit="V")
    q.choices.create(text_fr="12 V", text_en="12 V", is_correct=True)

    with pytest.raises(ValidationError):
        q.publish()


@pytest.mark.django_db
def test_numeric_question_defaults_to_a_two_percent_tolerance(numeric_q):
    assert numeric_q.tolerance_pct == 2


@pytest.mark.django_db
def test_matching_question_needs_at_least_two_pairs(module):
    q = reviewed(module, "matching")
    q.pairs.create(left_fr="R", left_en="R", right_fr="Résistance", right_en="Resistor", order=0)

    with pytest.raises(ValidationError):
        q.publish()


@pytest.mark.django_db
def test_hotspot_question_needs_a_schematic(module):
    q = reviewed(module, "hotspot")
    q.choices.create(text_fr="Base", text_en="Base", is_correct=True, shape={"x": 0, "y": 0, "w": 9, "h": 9})

    with pytest.raises(ValidationError):
        q.publish()



@pytest.mark.django_db
def test_hotspot_schematic_with_script_is_refused(module):
    q = reviewed(module, "hotspot", hotspot_svg=SVG.replace("<rect", "<rect onload=\"alert(1)\""))
    q.choices.create(text_fr="Base", text_en="Base", is_correct=True, shape={"x": 0, "y": 0, "w": 9, "h": 9})

    with pytest.raises(ValidationError):
        q.publish()

@pytest.mark.django_db
def test_hotspot_question_has_exactly_one_right_zone(module):
    q = reviewed(module, "hotspot", hotspot_svg=SVG)
    for i in range(2):
        q.choices.create(text_fr=f"Z{i}", text_en=f"Z{i}", is_correct=True, shape={"x": i * 30, "y": 0, "w": 9, "h": 9})

    with pytest.raises(ValidationError):
        q.publish()


@pytest.mark.django_db
def test_every_hotspot_zone_needs_a_shape(module):
    q = reviewed(module, "hotspot", hotspot_svg=SVG)
    q.choices.create(text_fr="Base", text_en="Base", is_correct=True, shape={"x": 0, "y": 0, "w": 9, "h": 9})
    q.choices.create(text_fr="Sans zone", text_en="No zone")

    with pytest.raises(ValidationError):
        q.publish()


# --- Réponses et notes ------------------------------------------------------------------------------------------------


@pytest.mark.django_db
def test_numeric_answer_is_scored_with_the_tolerance(learner, module, numeric_q):
    attempt = quiz_attempt(learner, module)

    save_answer(attempt, numeric_q.public_id, [], text="4,75 kΩ")
    submit_attempt(attempt)

    attempt.refresh_from_db()
    assert attempt.score_pct == 100
    assert attempt.attempt_questions.get().answer_text == "4,75 kΩ"


@pytest.mark.django_db
def test_wrong_numeric_answer_scores_zero(learner, module, numeric_q):
    attempt = quiz_attempt(learner, module)

    save_answer(attempt, numeric_q.public_id, [], text="47 Ω")
    submit_attempt(attempt)

    attempt.refresh_from_db()
    assert attempt.score_pct == 0


@pytest.mark.django_db
def test_matching_answer_earns_the_share_of_right_pairs(learner, module, matching_q):
    r, c, l, d = (str(p.public_id) for p in matching_q.pairs.all())
    attempt = quiz_attempt(learner, module)

    save_answer(attempt, matching_q.public_id, [], pairs={r: r, c: l, l: c, d: d})
    submit_attempt(attempt)

    attempt.refresh_from_db()
    assert attempt.score_pct == 50


@pytest.mark.django_db
def test_matching_answer_drops_unknown_identifiers(learner, module, matching_q):
    r = str(matching_q.pairs.first().public_id)
    attempt = quiz_attempt(learner, module)

    save_answer(attempt, matching_q.public_id, [], pairs={r: r, "00000000-0000-0000-0000-000000000000": r})

    assert attempt.attempt_questions.get().answer_json == {r: r}


@pytest.mark.django_db
def test_matching_right_column_order_is_frozen_per_attempt(learner, module, matching_q):
    attempt = quiz_attempt(learner, module)

    aq = attempt.attempt_questions.get()
    assert sorted(p.pk for p in aq.ordered_pairs()) == sorted(matching_q.pairs.values_list("pk", flat=True))


@pytest.mark.django_db
def test_hotspot_answer_is_the_clicked_zone(learner, module, hotspot_q):
    base = hotspot_q.choices.get(is_correct=True)
    attempt = quiz_attempt(learner, module)

    save_answer(attempt, hotspot_q.public_id, [base.public_id])
    submit_attempt(attempt)

    attempt.refresh_from_db()
    assert attempt.score_pct == 100


@pytest.mark.django_db
def test_feedback_gives_the_expected_numeric_value(learner, module, numeric_q):
    attempt = quiz_attempt(learner, module)
    save_answer(attempt, numeric_q.public_id, [], text="1 kΩ")

    [item] = attempt.feedback()

    assert (item["score"], item["answer_text"], item["expected_value"]) == (0, "1 kΩ", "4,7 kΩ")


# --- Temps passé (US-20, US-28) ---------------------------------------------------------------------------------------


@pytest.mark.django_db
def test_time_spent_on_a_question_adds_up_across_saves(learner, module, numeric_q):
    attempt = quiz_attempt(learner, module)

    save_answer(attempt, numeric_q.public_id, [], text="1k", time_spent_s=40)
    save_answer(attempt, numeric_q.public_id, [], text="4.7k", time_spent_s=25)

    assert attempt.attempt_questions.get().time_spent_s == 65


@pytest.mark.django_db
def test_reported_time_is_clamped_to_a_plausible_range(learner, module, numeric_q):
    attempt = quiz_attempt(learner, module)

    save_answer(attempt, numeric_q.public_id, [], text="1k", time_spent_s=-30)
    save_answer(attempt, numeric_q.public_id, [], text="1k", time_spent_s=999999)

    assert attempt.attempt_questions.get().time_spent_s == 3600


# --- Correction lisible (US-15 à US-17) -------------------------------------------------------------------------------


@pytest.mark.parametrize("value, unit, lang, shown", [
    ("0.002553", "A", "fr", "2,553 mA"),
    ("0.002553", "A", "en", "2.553 mA"),
    ("4700", "Ω", "fr", "4,7 kΩ"),
    ("12", "V", "fr", "12 V"),
    ("0.0000001", "F", "fr", "100 nF"),
    ("1500000", "Hz", "en", "1.5 MHz"),
    ("-0.6", "V", "fr", "-600 mV"),
    ("0", "V", "fr", "0 V"),
])
@pytest.mark.django_db
def test_expected_value_is_shown_with_an_si_prefix(module, value, unit, lang, shown):
    from django.utils import translation

    q = reviewed(module, "numeric", numeric_value=Decimal(value), unit=unit)
    with translation.override(lang):
        assert q.expected_value_display() == shown


@pytest.mark.parametrize("value, lang, shown", [
    ("63.4", "fr", "63,4°"),
    ("63.4", "en", "63.4°"),
    ("0.5", "fr", "0,5°"),       # jamais « 500 m° »
    ("-45", "fr", "-45°"),
    ("1200", "en", "1200°"),     # jamais « 1,2 k° »
])
@pytest.mark.django_db
def test_expected_angle_is_shown_in_degrees_without_si_prefix(module, value, lang, shown):
    """US-41 : un déphasage attendu s'affiche en degrés, sans préfixe ni espace."""
    from django.utils import translation

    q = reviewed(module, "numeric", numeric_value=Decimal(value), unit="°")
    with translation.override(lang):
        assert q.expected_value_display() == shown


@pytest.mark.django_db
def test_matching_feedback_lists_the_learners_pairs_with_their_verdict(learner, module, matching_q):
    r, c, l, d = (str(p.public_id) for p in matching_q.pairs.all())
    attempt = quiz_attempt(learner, module)
    save_answer(attempt, matching_q.public_id, [], pairs={r: r, c: l})

    [item] = attempt.feedback()

    assert [(row["left"], row["given"], row["expected"], row["ok"]) for row in item["pair_rows"]] == [
        ("R", "Résistance", "Résistance", True),
        ("C", "Bobine", "Condensateur", False),
        ("L", "", "Bobine", False),
        ("D", "", "Diode", False),
    ]


@pytest.mark.parametrize("value, lang, shown", [
    ("0.05", "fr", "0,05"),      # rapport de transformation : jamais « 50 m »
    ("0.05", "en", "0.05"),
    ("-10", "fr", "-10"),
    ("1500", "fr", "1500"),      # jamais « 1,5 k »
    ("200", "en", "200"),
])
@pytest.mark.django_db
def test_expected_ratio_is_shown_without_si_prefix(module, value, lang, shown):
    """US-49 : un gain ou un rapport attendu (sans unité) s'affiche tel quel, sans préfixe SI."""
    from django.utils import translation

    q = reviewed(module, "numeric", numeric_value=Decimal(value), unit="")
    with translation.override(lang):
        assert q.expected_value_display() == shown


@pytest.mark.parametrize("value, unit, lang, shown", [
    ("1450", "tr/min", "fr", "1450 tr/min"),
    ("1450", "tr/min", "en", "1450 rpm"),
    ("1500", "tr/min", "fr", "1500 tr/min"),   # jamais « 1,5 ktr/min »
    ("4", "%", "fr", "4 %"),
    ("4", "%", "en", "4%"),
    ("2.5", "%", "fr", "2,5 %"),
    ("0.5", "%", "fr", "0,5 %"),               # jamais « 500 m% »
    ("155", "°C", "fr", "155 °C"),
    ("1500", "°C", "en", "1500 °C"),           # jamais « 1,5 k°C »
    ("2500", "N·m", "fr", "2,5 kN·m"),
    ("25", "N·m", "en", "25 N·m"),
    ("11000", "VA", "fr", "11 kVA"),
    ("4000", "var", "fr", "4 kvar"),
    ("0.5", "s", "fr", "500 ms"),
    ("0.008", "m", "fr", "8 mm"),
])
@pytest.mark.django_db
def test_expected_value_in_electrical_engineering_units(module, value, unit, lang, shown):
    """US-67 : tr/min, % et °C sans préfixe SI ; « tr/min » devient « rpm » en anglais ; N·m, VA, var, s et m préfixés."""
    from django.utils import translation

    q = reviewed(module, "numeric", numeric_value=Decimal(value), unit=unit)
    with translation.override(lang):
        assert q.expected_value_display() == shown
