import pytest

from accounts.models import User


@pytest.mark.django_db
def test_login_page_is_in_english_under_en_prefix(client):
    html = client.get("/en/connexion/").content.decode()
    assert "Sign in" in html
    assert "Se connecter" not in html


@pytest.mark.django_db
def test_login_page_stays_in_french_under_fr_prefix(client):
    html = client.get("/fr/connexion/").content.decode()
    assert "Se connecter" in html


@pytest.mark.django_db
def test_learner_dashboard_interface_is_translated(client, enrolled, partie, module):
    client.force_login(enrolled)
    html = client.get("/en/").content.decode()
    assert "My courses" in html or "Hello" in html
    assert "Part 1 exam" in html
    assert "Examen de la Partie" not in html


@pytest.mark.django_db
def test_empty_dashboard_message_is_translated(client, learner):
    client.force_login(learner)
    html = client.get("/en/").content.decode()
    assert "No course yet" in html


@pytest.mark.django_db
def test_trainer_table_is_translated(client, promotion):
    trainer = User.objects.create_user(username="macaire", password="x-Secret-123", role=User.Role.TRAINER)
    promotion.trainers.add(trainer)
    client.force_login(trainer)
    html = client.get("/en/formateur/").content.decode()
    assert "Learner progress" in html
    assert "Export as CSV" in html


@pytest.mark.django_db
def test_pluralised_attempts_left_is_translated(client, enrolled, partie, module):
    client.force_login(enrolled)
    html = client.get(f"/en/examen/{partie.public_id}/").content.decode()
    assert "3 attempts left" in html


def _po_entries(path):
    """Lecteur minimal de .po : renvoie (msgid, msgstr, fuzzy) pour chaque entrée hors en-tête."""
    entries, current, field, fuzzy = [], {}, None, False

    def flush():
        if current.get("msgid"):
            entries.append((current["msgid"], current.get("msgstr", "") or current.get("msgstr[0]", ""), fuzzy))

    for line in path.read_text(encoding="utf-8").splitlines() + [""]:
        if not line.strip():
            flush()
            current, field, fuzzy = {}, None, False
        elif line.startswith("#,") and "fuzzy" in line:
            fuzzy = True
        elif line.startswith("#"):
            continue
        elif line.startswith('"'):
            current[field] += line[1:-1]
        else:
            field, _, value = line.partition(" ")
            current[field] = value[1:-1]
    return entries


def test_every_interface_string_has_a_reviewed_english_translation(settings):
    po = settings.BASE_DIR / "locale" / "en" / "LC_MESSAGES" / "django.po"
    entries = _po_entries(po)
    assert len(entries) > 50
    missing = [msgid for msgid, msgstr, fuzzy in entries if not msgstr or fuzzy]
    assert missing == []


@pytest.mark.django_db
def test_untranslated_module_title_is_marked_as_french_on_english_pages(client, enrolled, partie, module):
    client.force_login(enrolled)
    html = client.get("/en/").content.decode()
    assert '<span lang="fr">Sécurité dans les travaux</span>' in html


@pytest.mark.django_db
def test_translated_module_title_carries_no_language_override(client, enrolled, partie, module):
    module.title_en = "Safety at work"
    module.save()
    client.force_login(enrolled)
    html = client.get("/en/").content.decode()
    assert "<span>Safety at work</span>" in html


@pytest.mark.django_db
def test_french_pages_never_add_a_language_override(client, enrolled, partie, module):
    client.force_login(enrolled)
    html = client.get("/fr/").content.decode()
    assert "<span>Sécurité dans les travaux</span>" in html


# --- Sélecteur de langue : le bouton choisi l'emporte toujours (signalé le 2026-11-24) ---------------------------------
# /i18n/setlang/ n'a pas de préfixe de langue : Django y active la langue du cookie ou du navigateur, et `resolve()` ne
# reconnaît que le préfixe de la langue active. Arrivé sur une page /en/ par un lien avec un cookie (ou un navigateur)
# en français, un clic sur FR renvoyait sur la même page /en/.


@pytest.mark.django_db
@pytest.mark.parametrize(
    "cookie, accept, page, chosen, expected",
    [
        ("fr", "", "/en/catalogue/", "fr", "/fr/catalogue/"),
        ("", "fr-FR,fr;q=0.9", "/en/catalogue/", "fr", "/fr/catalogue/"),
        ("en", "", "/fr/catalogue/", "en", "/en/catalogue/"),
        ("", "en-US,en;q=0.9", "/fr/connexion/", "en", "/en/connexion/"),
        ("fr", "", "/en/?formation=abc", "fr", "/fr/?formation=abc"),
        ("en", "", "/en/catalogue/", "fr", "/fr/catalogue/"),
    ],
)
def test_language_button_switches_the_page_whatever_the_cookie_or_browser_language(client, cookie, accept, page, chosen, expected):
    if cookie:
        client.cookies["django_language"] = cookie
    headers = {"HTTP_ACCEPT_LANGUAGE": accept} if accept else {}
    response = client.post("/i18n/setlang/", {"language": chosen, "next": page}, **headers)
    assert response.status_code == 302
    assert response["Location"] == expected
    assert response.cookies["django_language"].value == chosen


@pytest.mark.django_db
def test_language_button_refuses_a_foreign_next_url(client):
    client.cookies["django_language"] = "fr"
    response = client.post("/i18n/setlang/", {"language": "fr", "next": "https://example.com/en/"})
    assert response.status_code == 302
    assert "example.com" not in response["Location"]
