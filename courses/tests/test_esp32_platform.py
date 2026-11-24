"""Formation `esp32` (grill C1 à C23), livraison 1 : plateforme sans contenu (US-107 à US-117)."""
import pytest

from courses.models import Formation

CODE_PATH = 'd="M7 8l-4 4l4 4"'  # tracé propre à templates/icons/code.svg (Tabler 3.31.0)


# --- US-107 / modèle de données : icône `code` dans la liste fermée ----------------------------------------------


@pytest.mark.django_db
def test_the_esp32_formation_accepts_the_code_icon():
    formation = Formation(title_fr="Microcontrôleurs : l'ESP32", slug="esp32", order=3, icon="code")

    formation.full_clean()


@pytest.mark.django_db
def test_the_catalogue_lists_the_three_formations_in_order_with_their_icons(client):
    Formation.objects.create(title_fr="Électronique", slug="electro", order=1, is_open=True, icon="cpu")
    Formation.objects.create(title_fr="Microcontrôleurs : l'ESP32", slug="esp32", order=3, is_open=True, icon="code")
    Formation.objects.create(title_fr="Moteurs électriques et commande", slug="moteurs", order=2, is_open=True,
                             icon="engine")

    html = client.get("/fr/catalogue/").content.decode()

    cards = html.split('class="course-card"')[1:]
    assert [("Électronique" in c, "Moteurs" in c, "ESP32" in c) for c in cards] == [
        (True, False, False), (False, True, False), (False, False, True)]
    assert [CODE_PATH in card for card in cards] == [False, False, True]


# --- US-111 : quatre calculateurs d'`esp32`, script chargé seulement où il sert ----------------------------------


def test_esp32_calculators_become_inert_slots():
    from courses.rendering import render_markdown

    for kind in ("led", "adc", "pwm", "uart"):
        assert f'<div class="calc" data-calc="{kind}"></div>' in render_markdown(f"[[calc:{kind}]]")


def test_an_unknown_esp32_calculator_stays_text():
    from courses.rendering import render_markdown

    assert "data-calc" not in render_markdown("[[calc:i2c]]")


@pytest.mark.django_db
def test_esp32_calculator_script_loads_before_the_common_engine_only_where_needed(client, enrolled, module):
    from courses.models import Section

    led = Section.objects.create(module=module, title_fr="Résistance d'une LED", order=1, body_md_fr="[[calc:led]]")
    speed = Section.objects.create(module=module, title_fr="Glissement", order=2, body_md_fr="[[calc:speed]]")
    ohm = Section.objects.create(module=module, title_fr="Loi d'Ohm", order=3, body_md_fr="[[calc:ohm]]")
    client.force_login(enrolled)

    html = client.get(f"/fr/sections/{led.public_id}/").content.decode()
    assert 0 < html.index("calculators-esp32.js") < html.index("acad/js/calculators.js")
    assert "calculators-moteurs.js" not in html
    for other in (speed, ohm):
        assert "calculators-esp32.js" not in client.get(f"/fr/sections/{other.public_id}/").content.decode()


# --- US-120 : le platformio.ini de référence existe et fige ses versions ------------------------------------------


def test_the_reference_platformio_ini_pins_platform_board_speed_and_libraries():
    from django.conf import settings

    from courses.tests.esp32_rules import reference_ini_problems

    ini = settings.BASE_DIR / "content" / "esp32" / "sketches" / "platformio.ini"
    assert reference_ini_problems(ini.read_text(encoding="utf-8")) == []


# --- US-119 (C6) : les blocs de code défilent dans leur cadre ; leur style n'est chargé que là où il sert --------------


@pytest.mark.django_db
def test_code_css_loads_only_on_a_section_with_a_code_block(client, enrolled, module):
    from courses.models import Section

    with_code = Section.objects.create(module=module, title_fr="Blink", order=1, body_md_fr="```cpp\nvoid setup() {}\n```")
    without = Section.objects.create(module=module, title_fr="Loi d'Ohm", order=2, body_md_fr="U = R × I")
    client.force_login(enrolled)

    assert "acad/css/code.css" in client.get(f"/fr/sections/{with_code.public_id}/").content.decode()
    assert "acad/css/code.css" not in client.get(f"/fr/sections/{without.public_id}/").content.decode()


@pytest.mark.django_db
def test_code_css_loads_on_an_attempt_and_its_result_only_when_a_question_shows_code(client, enrolled, module, question_factory):
    from assessments.models import Assessment
    from assessments.services import start_attempt, submit_attempt

    question = question_factory(module)
    attempt = start_attempt(enrolled, Assessment.quiz_for(module))
    client.force_login(enrolled)
    assert "acad/css/code.css" not in client.get(f"/fr/tentatives/{attempt.public_id}/").content.decode()

    question.prompt_fr = "Qu'affiche ce programme ?\n\n```cpp\nSerial.println(97);\n```"
    question.save()
    assert "acad/css/code.css" in client.get(f"/fr/tentatives/{attempt.public_id}/").content.decode()
    submit_attempt(attempt)
    assert "acad/css/code.css" in client.get(f"/fr/tentatives/{attempt.public_id}/resultat/").content.decode()


def test_code_blocks_scroll_inside_their_frame():
    from django.conf import settings

    css = (settings.BASE_DIR / "static" / "acad" / "css" / "code.css").read_text(encoding="utf-8")
    assert "overflow-x: auto" in css
