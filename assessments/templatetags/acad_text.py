"""Texte d'une question (énoncé, choix, explication) en Markdown restreint (US-109)."""
from django import template
from django.utils.safestring import mark_safe

from courses.rendering import question_plain_text, render_question_text

register = template.Library()


@register.filter
def qtext(text):
    """HTML nettoyé par bleach dans render_question_text : seules p, code, pre, strong et em peuvent sortir."""
    return mark_safe(render_question_text(text))


@register.filter
def qplain(text):
    """Texte brut (échappé ensuite par le gabarit) : le code d'une option de liste perd ses accents graves."""
    return question_plain_text(text)
