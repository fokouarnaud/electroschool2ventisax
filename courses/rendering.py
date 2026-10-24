"""Markdown → HTML nettoyé (bleach) pour le contenu des sections."""
import re

import bleach
import markdown

ALLOWED_TAGS = {
    "p", "br", "strong", "em", "ul", "ol", "li", "h2", "h3", "h4", "blockquote", "code", "pre",
    "table", "thead", "tbody", "tr", "th", "td", "a", "img", "hr",
}
ALLOWED_ATTRIBUTES = {"a": ["href", "title"], "img": ["src", "alt", "title"]}
# Calculateurs du cours (US-13) : un paragraphe « [[calc:<nom>]] » seul devient un emplacement inerte,
# rempli par static/acad/js/calculators.js. Remplacé APRÈS bleach : seuls ces noms fixes peuvent sortir.
# Ceux de la formation `moteurs` (US-68) sont remplis par static/acad/js/calculators-moteurs.js, chargé en plus.
MOTOR_CALCULATORS = ("motor_current", "speed", "torque", "stardelta")
CALCULATORS = ("ohm", "divider", "resistor", "bias", "reactance", "cutoff", "resonance", "gain", "transformer", "ripple",
               *MOTOR_CALCULATORS)
CALC_MARKER = re.compile(r"<p>\[\[calc:(%s)\]\]</p>" % "|".join(CALCULATORS))
# Schémas du cours : ajustés à la largeur et liés à leur fichier pleine taille (agrandissement sur téléphone).
# Seuls les SVG servis par le site (/static/content/) sont concernés, après nettoyage par bleach.
DIAGRAM = re.compile(r'(<img alt="[^"]*" src="(/static/content/[\w/.-]+\.svg)">)')


def render_markdown(text):
    html = markdown.markdown(text or "", extensions=["tables"])
    clean = bleach.clean(html, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES, protocols={"http", "https"}, strip=True)
    clean = DIAGRAM.sub(r'<a class="figure-zoom" href="\2">\1</a>', clean)
    return CALC_MARKER.sub(r'<div class="calc" data-calc="\1"></div>', clean)
