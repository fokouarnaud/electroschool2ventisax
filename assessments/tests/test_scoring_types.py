"""Notation des types ajoutés (AGENTS.md, E13) : numérique avec tolérance, appariement, zone cliquable."""
from decimal import Decimal
from fractions import Fraction

import pytest

from assessments.scoring import parse_quantity, score_answer, score_matching, score_numeric


@pytest.mark.parametrize("text, expected", [
    ("4700", (Decimal("4700"), "")),
    ("4,7k", (Decimal("4700"), "")),
    ("4.7 kΩ", (Decimal("4700"), "Ω")),
    ("2.2µA", (Decimal("0.0000022"), "A")),
    ("2.2μA", (Decimal("0.0000022"), "A")),   # mu grec
    ("2.2 uA", (Decimal("0.0000022"), "A")),
    ("10 mA", (Decimal("0.010"), "A")),
    ("1.5 MHz", (Decimal("1500000"), "Hz")),
    ("50 Hz", (Decimal("50"), "Hz")),
    ("-0,6 V", (Decimal("-0.6"), "V")),
    ("100 nF", (Decimal("0.0000001"), "F")),
    ("3 pF", (Decimal("0.000000000003"), "F")),
    ("1e3", (Decimal("1000"), "")),
    ("  12 V  ", (Decimal("12"), "V")),
    ("470 ohms", (Decimal("470"), "Ω")),
])
def test_parse_quantity_reads_si_prefixes_and_units(text, expected):
    value, unit = parse_quantity(text)
    assert (value, unit) == (expected[0], expected[1])
    assert value == expected[0]


@pytest.mark.parametrize("text", ["", "abc", "4.7.1k", "k", "12 V V"])
def test_parse_quantity_rejects_garbage(text):
    assert parse_quantity(text) is None


@pytest.mark.parametrize("answer, score", [
    ("4.7k", 1),
    ("4,79 kΩ", 1),      # écart 1,9 %
    ("4794", 1),         # écart 2,0 % exactement : accepté
    ("4795", 0),         # écart 2,02 %
    ("4.8k", 0),         # écart 2,1 %
    ("4.7 kV", 0),       # unité saisie différente
    ("", 0),
    ("quatre", 0),
])
def test_numeric_answer_is_right_within_the_relative_tolerance(answer, score):
    assert score_numeric(Decimal("4700"), "Ω", Decimal("2"), answer) == Fraction(score)


def test_numeric_answer_to_a_zero_expected_value_must_be_zero():
    assert score_numeric(Decimal("0"), "V", Decimal("2"), "0 V") == 1
    assert score_numeric(Decimal("0"), "V", Decimal("2"), "0.001 V") == 0


def test_numeric_tolerance_applies_to_negative_values():
    assert score_numeric(Decimal("-0.6"), "V", Decimal("5"), "-0,62 V") == 1
    assert score_numeric(Decimal("-0.6"), "V", Decimal("5"), "0,6 V") == 0


def test_matching_scores_the_share_of_right_pairs():
    expected = {"r": "resistance", "c": "capacitance", "l": "inductance", "d": "diode"}

    assert score_matching(expected, {"r": "resistance", "c": "inductance", "l": "capacitance", "d": "diode"}) == Fraction(1, 2)
    assert score_matching(expected, dict(expected)) == 1
    assert score_matching(expected, {}) == 0


def test_matching_ignores_pairs_that_do_not_exist():
    assert score_matching({"r": "resistance"}, {"r": "resistance", "x": "resistance"}) == 1


def test_hotspot_is_all_or_nothing_on_the_clicked_zone():
    assert score_answer("hotspot", [7], [7]) == 1
    assert score_answer("hotspot", [7], [8]) == 0


def test_ohm_sign_and_greek_omega_are_the_same_unit():
    assert parse_quantity("4.7 k\u2126") == (Decimal("4700"), "\u03a9")
    assert score_numeric(Decimal("4700"), "\u2126", Decimal("2"), "4.7 k\u03a9") == 1


@pytest.mark.parametrize("text, expected", [
    ("45°", (Decimal("45"), "°")),
    ("45 °", (Decimal("45"), "°")),
    ("-63,4°", (Decimal("-63.4"), "°")),
    ("90.0 °", (Decimal("90.0"), "°")),
])
def test_parse_quantity_reads_degrees(text, expected):
    """US-41 : un déphasage se saisit en degrés, avec ou sans espace, virgule ou point."""
    assert parse_quantity(text) == expected


@pytest.mark.parametrize("text", ["°", "4 k°", "45 m°", "45°°"])
def test_parse_quantity_refuses_si_prefixes_on_degrees(text):
    assert parse_quantity(text) is None


@pytest.mark.parametrize("answer, score", [
    ("45°", 1),
    ("45,9 °", 1),     # écart 2,0 %
    ("46°", 0),        # écart 2,2 %
    ("45", 1),         # unité facultative
    ("45 rad", 0),     # autre unité
    ("45 V", 0),
])
def test_score_numeric_in_degrees(answer, score):
    assert score_numeric(Decimal("45"), "°", Decimal("2"), answer) == Fraction(score)


# --- US-49 : gains et rapports sans unité (Partie 3, E41) -------------------------------------------------------------


@pytest.mark.parametrize("answer, score", [
    ("10", 1),
    ("10,1", 1),       # écart 1 %
    ("-10", 0),        # « en valeur absolue » : le signe opposé est faux
    ("10 V", 0),       # une unité saisie rend la réponse fausse
    ("dix", 0),
])
def test_score_numeric_for_a_gain_in_absolute_value(answer, score):
    assert score_numeric(Decimal("10"), "", Decimal("2"), answer) == Fraction(score)


@pytest.mark.parametrize("answer, score", [
    ("-10", 1),
    ("−10", 1),   # signe moins typographique, celui des énoncés
    ("- 10", 0),
    ("10", 0),         # « avec son signe » : la valeur absolue seule est fausse
])
def test_score_numeric_for_a_signed_gain(answer, score):
    assert score_numeric(Decimal("-10"), "", Decimal("2"), answer) == Fraction(score)


def test_parse_quantity_reads_the_typographic_minus_sign():
    assert parse_quantity("−4,7") == (Decimal("-4.7"), "")
    assert parse_quantity("−0,6 V") == (Decimal("-0.6"), "V")
