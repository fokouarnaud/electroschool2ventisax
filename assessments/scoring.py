"""Règles de notation (AGENTS.md, Q8 et E13). Scores exacts en Fraction, de 0 à 1."""
import re
import unicodedata
from decimal import Decimal, InvalidOperation
from fractions import Fraction

SI_PREFIXES = {
    "p": Decimal("1e-12"), "n": Decimal("1e-9"), "u": Decimal("1e-6"), "µ": Decimal("1e-6"), "μ": Decimal("1e-6"),
    "m": Decimal("1e-3"), "k": Decimal("1e3"), "M": Decimal("1e6"), "G": Decimal("1e9"),
}
DEGREE = "°"  # déphasage (US-41) : jamais de préfixe SI
RPM, PERCENT, CELSIUS, NEWTON_METRE, METRE = "tr/min", "%", "°C", "N·m", "m"
# Vitesse, pourcentage et température (US-66) ne prennent pas plus de préfixe que les degrés.
UNPREFIXED = {DEGREE, RPM, PERCENT, CELSIUS}
# Saisie normalisée en NFKC : le signe ohm U+2126 devient oméga U+03A9, le micro U+00B5 devient mu U+03BC.
UNIT_ALIASES = {
    "ohm": "Ω", "ohms": "Ω", "Ohm": "Ω", "Ohms": "Ω",
    "rpm": RPM, "tr.min-1": RPM, "N.m": NEWTON_METRE, "Nm": NEWTON_METRE,
}
# Unités lues telles quelles, avant tout préfixe : « 8 m » vaut 8 mètres, pas 8 milli.
WHOLE_UNITS = UNPREFIXED | {NEWTON_METRE, METRE} | set(UNIT_ALIASES)
QUANTITY = re.compile(r"^([+-]?\d+(?:[.,]\d+)?(?:[eE][+-]?\d+)?)\s*(\S*)$")
LETTER_UNIT = re.compile(r"[A-Za-zΩΩ]+")


def _unit(text):
    """Unité saisie, ramenée à sa forme stockée ; None si ce n'est pas une unité."""
    unit = UNIT_ALIASES.get(text, text)
    return unit if unit in WHOLE_UNITS or LETTER_UNIT.fullmatch(unit) else None


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
    # Le signe moins typographique U+2212 des énoncés (gain signé, US-49) vaut le trait d'union.
    match = QUANTITY.match(unicodedata.normalize("NFKC", text or "").strip().replace("−", "-"))
    if not match:
        return None
    number, rest = match.groups()
    prefix, unit = "", ""
    if rest in WHOLE_UNITS:
        unit = UNIT_ALIASES.get(rest, rest)
    elif rest and rest[0] in SI_PREFIXES:
        prefix, unit = rest[0], _unit(rest[1:]) if rest[1:] else ""
        if unit is None or unit in UNPREFIXED:
            return None
    elif rest:
        unit = _unit(rest)
        if unit is None:
            return None
    try:
        value = Decimal(number.replace(",", "."))
    except InvalidOperation:
        return None
    if prefix:
        value *= SI_PREFIXES[prefix]
    return value, unit


DISPLAY_PREFIXES = {-12: "p", -9: "n", -6: "µ", -3: "m", 0: "", 3: "k", 6: "M", 9: "G"}


def format_quantity(value, unit):
    """Decimal("0.002553"), "A" -> « 2,553 mA » (préfixe d'ingénieur, séparateur décimal de la langue active)."""
    from django.utils.formats import get_format

    from django.utils.translation import pgettext

    # Les degrés (déphasage, US-41) ne prennent ni préfixe SI ni espace : « 63,4° ».
    # Un gain ou un rapport sans unité (US-49) non plus : « 0,05 », jamais « 50 m ».
    # Ni la vitesse, le pourcentage ou la température (US-67) : « 1500 tr/min », jamais « 1,5 ktr/min ».
    exponent = 0 if value == 0 or unit in UNPREFIXED | {""} else max(-12, min(9, (value.adjusted() // 3) * 3))
    scaled = (value.scaleb(-exponent)).normalize()
    number = format(scaled, "f").replace(".", get_format("DECIMAL_SEPARATOR"))
    if unit == DEGREE:
        return f"{number}{DEGREE}"
    if unit == RPM:
        return f"{number} {pgettext('unité de vitesse de rotation', 'tr/min')}"
    if unit == PERCENT:
        # Une espace avant « % » en français, aucune en anglais.
        return pgettext("pourcentage", "%(number)s %%") % {"number": number}
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
