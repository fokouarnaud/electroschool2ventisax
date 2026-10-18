"""Règles de notation (AGENTS.md, Q8 et E13). Scores exacts en Fraction, de 0 à 1."""
import re
import unicodedata
from decimal import Decimal, InvalidOperation
from fractions import Fraction

SI_PREFIXES = {
    "p": Decimal("1e-12"), "n": Decimal("1e-9"), "u": Decimal("1e-6"), "µ": Decimal("1e-6"), "μ": Decimal("1e-6"),
    "m": Decimal("1e-3"), "k": Decimal("1e3"), "M": Decimal("1e6"), "G": Decimal("1e9"),
}
# Saisie normalisée en NFKC : le signe ohm U+2126 devient oméga U+03A9, le micro U+00B5 devient mu U+03BC.
UNIT_ALIASES = {"ohm": "Ω", "ohms": "Ω", "Ohm": "Ω", "Ohms": "Ω"}
QUANTITY = re.compile(r"^([+-]?\d+(?:[.,]\d+)?(?:[eE][+-]?\d+)?)\s*([pnuµμmkMG]?)\s*([A-Za-zΩΩ]*)$")


def score_answer(qtype, correct_ids, selected_ids):
    correct_ids, selected_ids = set(correct_ids), set(selected_ids)
    if qtype == "multiple":
        if not correct_ids:
            return Fraction(0)
        good = len(selected_ids & correct_ids)
        bad = len(selected_ids - correct_ids)
        return max(Fraction(0), Fraction(good - bad, len(correct_ids)))
    return Fraction(1) if selected_ids == correct_ids else Fraction(0)


def parse_quantity(text):
    """« 4,7 kΩ » -> (Decimal("4700"), "Ω") ; None si la saisie n'est pas une grandeur."""
    match = QUANTITY.match(unicodedata.normalize("NFKC", text or "").strip())
    if not match:
        return None
    number, prefix, unit = match.groups()
    try:
        value = Decimal(number.replace(",", "."))
    except InvalidOperation:
        return None
    if prefix:
        value *= SI_PREFIXES[prefix]
    return value, UNIT_ALIASES.get(unit, unit)


DISPLAY_PREFIXES = {-12: "p", -9: "n", -6: "µ", -3: "m", 0: "", 3: "k", 6: "M", 9: "G"}


def format_quantity(value, unit):
    """Decimal("0.002553"), "A" -> « 2,553 mA » (préfixe d'ingénieur, séparateur décimal de la langue active)."""
    from django.utils.formats import get_format

    exponent = 0 if value == 0 else max(-12, min(9, (value.adjusted() // 3) * 3))
    scaled = (value.scaleb(-exponent)).normalize()
    number = format(scaled, "f").replace(".", get_format("DECIMAL_SEPARATOR"))
    return f"{number} {DISPLAY_PREFIXES[exponent]}{unit}".strip()


def score_numeric(expected, unit, tolerance_pct, answer):
    """Juste si |saisie − attendu| ≤ |attendu| × tolérance / 100 ; une unité saisie doit être l'unité attendue."""
    parsed = parse_quantity(answer)
    if parsed is None:
        return Fraction(0)
    value, given_unit = parsed
    unit = unicodedata.normalize("NFKC", unit)
    if given_unit and given_unit != UNIT_ALIASES.get(unit, unit):
        return Fraction(0)
    return Fraction(1) if abs(value - expected) <= abs(expected) * tolerance_pct / 100 else Fraction(0)


def score_matching(expected_pairs, given_pairs):
    """Part des paires justes : {gauche: droite} attendu contre {gauche: droite} donné."""
    if not expected_pairs:
        return Fraction(0)
    right = sum(1 for left, target in expected_pairs.items() if given_pairs.get(left) == target)
    return Fraction(right, len(expected_pairs))
