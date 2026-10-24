"""Schémas de la formation « Moteurs électriques et commande » (`moteurs`), tous originaux, symboles CEI (IEC 60617).

Usage : python -m tools.schemas moteurs
Écrit les schémas des sections dans static/content/moteurs/m<N>/ et ceux des questions sur schéma dans
content/moteurs/p<P>/m<N>/schemas/ (p1 pour les modules 1 à 3, p2 pour 4 à 6, p3 pour 7 à 9, p4 pour 10 à 12).
"""
from .common import ROOT

SLUG = "moteurs"

# Libellés anglais des schémas ; les virgules décimales restantes deviennent des points (tr).
EN = {}

SECTION_DIAGRAMS = {}
QUESTION_DIAGRAMS = {}

PARTS = {"p1": range(1, 4), "p2": range(4, 7), "p3": range(7, 10), "p4": range(10, 13)}


def question_dir(module):
    """Dossier des schémas des questions sur schéma : content/moteurs/<partie>/m<N>/schemas."""
    part = next((slug for slug, modules in PARTS.items() if module in modules), None)
    if part is None:
        raise ValueError(f"module {module} hors des parties 1 à 4")
    return ROOT / "content" / SLUG / part / f"m{module}" / "schemas"
