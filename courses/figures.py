"""Figures interactives explicatives (grill F1 à F15) : liste fermée des figures du cours."""
import re
from pathlib import Path
from typing import NamedTuple

from django.conf import settings
from django.template.loader import render_to_string

from assessments.templatetags.acad_svg import inert_svg


class Figure(NamedTuple):
    """Une figure : dessin et script générés par tools/figures/<nom>/build.mjs (jamais retouchés à la main), carte HTML."""
    drawing: str  # gabarit, sous templates/
    card: str  # gabarit, sous templates/
    script: str  # fichier statique, sous static/


REGISTRY = {
    "rc_lowpass": Figure(drawing="figures/rc_lowpass.svg", card="figures/rc_lowpass.html", script="acad/js/figures/rc_lowpass.js"),
    "rc_highpass": Figure(drawing="figures/rc_highpass.svg", card="figures/rc_highpass.html", script="acad/js/figures/rc_highpass.js"),
    "rc_cutoff": Figure(drawing="figures/rc_cutoff.svg", card="figures/rc_cutoff.html", script="acad/js/figures/rc_cutoff.js"),
    "rc_phase": Figure(drawing="figures/rc_phase.svg", card="figures/rc_phase.html", script="acad/js/figures/rc_phase.js"),
    "rl_lowpass": Figure(drawing="figures/rl_lowpass.svg", card="figures/rl_lowpass.html", script="acad/js/figures/rl_lowpass.js"),
    "lc_resonance": Figure(drawing="figures/lc_resonance.svg", card="figures/lc_resonance.html", script="acad/js/figures/lc_resonance.js"),
    "rlc_response": Figure(drawing="figures/rlc_response.svg", card="figures/rlc_response.html", script="acad/js/figures/rlc_response.js"),
}
FIGURES = tuple(REGISTRY)
SLOT = re.compile(r'<div class="fig" data-fig="(%s)"></div>' % "|".join(FIGURES))


def drawing(name):
    return (Path(settings.BASE_DIR) / "templates" / REGISTRY[name].drawing).read_text(encoding="utf-8")


def expand(body_html):
    """Remplace chaque emplacement par la carte de sa figure (US-88) ; renvoie le HTML et les figures présentes."""
    found = []

    def card(match):
        name = match.group(1)
        found.append(name)
        # Le dessin est contrôlé à chaque affichage : modifié et devenu actif, il n'est pas intégré.
        return render_to_string(REGISTRY[name].card, {"svg": inert_svg(drawing(name))})

    return SLOT.sub(card, body_html), list(dict.fromkeys(found))
