"""Markdown → HTML nettoyé (bleach) pour le contenu des sections."""
import re

import bleach
import markdown

from .figures import FIGURES

ALLOWED_TAGS = {
    "p", "br", "strong", "em", "ul", "ol", "li", "h2", "h3", "h4", "blockquote", "code", "pre",
    "table", "thead", "tbody", "tr", "th", "td", "a", "img", "hr",
}
ALLOWED_ATTRIBUTES = {"a": ["href", "title"], "img": ["src", "alt", "title"]}
# Calculateurs du cours (US-13) : un paragraphe « [[calc:<nom>]] » seul devient un emplacement inerte,
# rempli par static/acad/js/calculators.js. Remplacé APRÈS bleach : seuls ces noms fixes peuvent sortir.
# Ceux de la formation `moteurs` (US-68) sont remplis par static/acad/js/calculators-moteurs.js, chargé en plus.
MOTOR_CALCULATORS = ("motor_current", "speed", "torque", "stardelta")
# Ceux de la formation `esp32` (US-111) sont remplis par static/acad/js/calculators-esp32.js, chargé en plus.
ESP32_CALCULATORS = ("led", "adc", "pwm", "uart")
CALCULATORS = ("ohm", "divider", "resistor", "bias", "reactance", "cutoff", "resonance", "gain", "transformer", "ripple",
               *MOTOR_CALCULATORS, *ESP32_CALCULATORS)
CALC_MARKER = re.compile(r"<p>\[\[calc:(%s)\]\]</p>" % "|".join(CALCULATORS))
# Figures interactives (US-88) : même principe ; l'emplacement est remplacé par la carte de la figure dans la vue.
FIG_MARKER = re.compile(r"<p>\[\[fig:(%s)\]\]</p>" % "|".join(FIGURES))
# Schémas du cours : ajustés à la largeur et liés à leur fichier pleine taille (agrandissement sur téléphone).
# Seuls les SVG servis par le site (/static/content/) sont concernés, après nettoyage par bleach.
DIAGRAM = re.compile(r'(<img alt="[^"]*" src="(/static/content/[\w/.-]+\.svg)">)')


def render_markdown(text):
    html = markdown.markdown(text or "", extensions=["tables", "fenced_code"])
    clean = bleach.clean(html, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES, protocols={"http", "https"}, strip=True)
    clean = DIAGRAM.sub(r'<a class="figure-zoom" href="\2">\1</a>', clean)
    clean = FIG_MARKER.sub(r'<div class="fig" data-fig="\1"></div>', clean)
    return CALC_MARKER.sub(r'<div class="calc" data-calc="\1"></div>', clean)


# Énoncé, choix et explication d'une question (US-109) : Markdown restreint, ni lien, ni image, ni tableau, ni titre.
QUESTION_TAGS = {"p", "code", "pre", "strong", "em"}
SINGLE_PARAGRAPH = re.compile(r"^<p>((?:(?!</?p>).)*)</p>$", re.S)


def render_question_text(text):
    """Texte d'une question en HTML sûr ; un seul paragraphe est rendu en ligne (pour un <legend> ou un <span>)."""
    html = markdown.markdown(text or "", extensions=["fenced_code"])
    clean = bleach.clean(html, tags=QUESTION_TAGS, attributes={}, strip=True).strip()
    single = SINGLE_PARAGRAPH.match(clean)
    return single.group(1) if single else clean


def question_plain_text(text):
    """Texte d'une question sans balisage, pour une option de liste déroulante (qui ne peut pas contenir de HTML)."""
    import html

    return html.unescape(re.sub(r"<[^>]+>", "", render_question_text(text)))
