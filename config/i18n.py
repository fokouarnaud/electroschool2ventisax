"""Sélecteur de langue : traduit l'URL de retour depuis la langue de son propre préfixe.

/i18n/setlang/ n'a pas de préfixe de langue : `LocaleMiddleware` y active la langue du cookie ou du navigateur, et
`translate_url` ne résout que les URL préfixées par la langue active. Sans ce correctif, un visiteur arrivé sur une page
/en/ avec un cookie ou un navigateur en français restait sur /en/ après avoir cliqué FR (et inversement).
"""

from urllib.parse import urlsplit

from django.utils import translation
from django.views.i18n import set_language as django_set_language


def set_language(request):
    next_url = request.POST.get("next", request.GET.get("next", ""))
    page_language = translation.get_language_from_path(urlsplit(next_url).path) if next_url else None
    if not page_language:
        return django_set_language(request)
    with translation.override(page_language):
        return django_set_language(request)
