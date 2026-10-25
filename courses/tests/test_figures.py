"""Figures interactives (grill F1 à F15) : emplacement `[[fig:<nom>]]`, carte et fichiers générés."""
import shutil
import subprocess
from pathlib import Path

import pytest

from config.uploads import ACTIVE_SVG
from courses.figures import FIGURES
from courses.rendering import render_markdown

ROOT = Path(__file__).resolve().parents[2]


def generated(name):
    return ROOT / "templates" / "figures" / f"{name}.svg", ROOT / "static" / "acad" / "js" / "figures" / f"{name}.js"


def test_registry_describes_each_figure_by_its_drawing_card_and_script():
    """Modèle de données (PRD) : registre fermé `nom → dessin, carte, script` ; aucune entité en base."""
    from courses.figures import REGISTRY, Figure

    assert REGISTRY == {
        "rc_lowpass": Figure(
            drawing="figures/rc_lowpass.svg", card="figures/rc_lowpass.html", script="acad/js/figures/rc_lowpass.js",
        ),
        "rc_highpass": Figure(
            drawing="figures/rc_highpass.svg", card="figures/rc_highpass.html", script="acad/js/figures/rc_highpass.js",
        ),
        "rc_cutoff": Figure(
            drawing="figures/rc_cutoff.svg", card="figures/rc_cutoff.html", script="acad/js/figures/rc_cutoff.js",
        ),
        "rc_phase": Figure(
            drawing="figures/rc_phase.svg", card="figures/rc_phase.html", script="acad/js/figures/rc_phase.js",
        ),
    }
    assert FIGURES == ("rc_lowpass", "rc_highpass", "rc_cutoff", "rc_phase")


@pytest.mark.django_db
def test_section_view_receives_the_scripts_from_the_registry(client, enrolled, module):
    """Modèle de données : la vue lit le script dans le registre, pas dans un nom de fichier reconstruit."""
    from courses.models import Section

    section = Section.objects.create(module=module, title_fr="Passe-bas", order=1, body_md_fr="[[fig:rc_lowpass]]")
    client.force_login(enrolled)

    assert client.get(f"/fr/sections/{section.public_id}/").context["figure_scripts"] == ["acad/js/figures/rc_lowpass.js"]


@pytest.mark.parametrize("name", FIGURES)
def test_each_figure_has_its_generated_files_within_budget(name):
    """US-91 et F8 : dessin ≤ 80 Ko, script ≤ 8 Ko."""
    svg, js = generated(name)

    assert svg.is_file() and js.is_file()
    assert svg.stat().st_size <= 80_000
    assert js.stat().st_size <= 8_000


@pytest.mark.parametrize("name", FIGURES)
def test_each_figure_drawing_is_inert_and_carries_no_text(name):
    """US-88 et F11 : aucun script ni gestionnaire d'événement ; aucun texte (un seul dessin pour les deux langues)."""
    data = generated(name)[0].read_bytes()

    assert data.lstrip().startswith(b"<svg")
    assert not ACTIVE_SVG.search(data)
    assert b"<text" not in data


@pytest.mark.parametrize("name", FIGURES)
def test_each_figure_drawing_has_only_finite_coordinates(name):
    """US-91 : une pièce mal décrite (dimension manquante) sortait des tracés « NaN », refusés par le navigateur."""
    assert b"NaN" not in generated(name)[0].read_bytes()


@pytest.mark.skipif(shutil.which("node") is None, reason="Node n'existe que sur le poste de développement (F6)")
@pytest.mark.parametrize("name", FIGURES)
def test_each_figure_rebuilds_byte_for_byte(name, tmp_path):
    """US-91 : build.mjs est déterministe ; les fichiers committés sont bien sa sortie."""
    subprocess.run(["node", str(ROOT / "tools" / "figures" / name / "build.mjs"), "--out", str(tmp_path)], check=True)

    for path in generated(name):
        assert (tmp_path / path.name).read_bytes() == path.read_bytes()


def test_figure_marker_becomes_an_inert_slot():
    """US-88 : un paragraphe réduit à `[[fig:rc_lowpass]]` devient un emplacement inerte, après bleach."""
    html = render_markdown("Observez :\n\n[[fig:rc_lowpass]]")

    assert '<div class="fig" data-fig="rc_lowpass"></div>' in html
    assert "[[fig" not in html


def test_unknown_figure_stays_plain_text():
    html = render_markdown("[[fig:rm-rf]]")

    assert "data-fig" not in html
    assert "[[fig:rm-rf]]" in html


def test_figure_marker_inside_a_sentence_is_not_expanded():
    assert "data-fig" not in render_markdown("Le marqueur [[fig:rc_lowpass]] doit être seul sur sa ligne.")


@pytest.fixture
def figure_section(module):
    from courses.models import Section

    return Section.objects.create(
        module=module, title_fr="Le filtre passe-bas", order=1,
        body_md_fr="Avant.\n\n[[fig:rc_lowpass]]\n\nAprès.", body_md_en="Before.\n\n[[fig:rc_lowpass]]\n\nAfter.",
    )


@pytest.mark.django_db
def test_section_replaces_the_slot_with_the_figure_card(client, enrolled, figure_section):
    """US-88 et US-82 : la vue remplace l'emplacement par la carte, dessin intégré et légende de correspondance."""
    client.force_login(enrolled)
    html = client.get(f"/fr/sections/{figure_section.public_id}/").content.decode()

    assert 'class="fig" data-fig="rc_lowpass"' in html
    assert '<svg xmlns="http://www.w3.org/2000/svg" class="iso-svg"' in html
    assert "Vanne étranglée" in html and "100 nF" in html
    assert html.index("Avant.") < html.index("iso-svg") < html.index("Après.")


@pytest.mark.django_db
def test_figure_card_is_translated(client, enrolled, figure_section):
    """US-86 : cadre, consigne et légende traduits ; un seul dessin pour les deux langues."""
    client.force_login(enrolled)
    en = client.get(f"/en/sections/{figure_section.public_id}/").content.decode()

    assert "Throttled valve:</strong>" in en and "Vanne étranglée" not in en
    assert 'data-play="Play"' in en and 'data-pause="Pause"' in en


@pytest.mark.django_db
def test_lowpass_card_names_the_series_and_the_ground_branch(client, enrolled, figure_section):
    """Mêmes pièces que le passe-haut, autrement disposées : vanne en série (R), soufflet vers la masse (C)."""
    client.force_login(enrolled)
    fr = client.get(f"/fr/sections/{figure_section.public_id}/").content.decode()
    en = client.get(f"/en/sections/{figure_section.public_id}/").content.decode()

    assert "résistance R = 1 kΩ, en série" in fr and "condensateur C = 100 nF, vers la masse" in fr
    assert "resistor R = 1 kΩ, in series" in en and "capacitor C = 100 nF, to ground" in en
    assert 'id="fig-rc_lowpass-freq"' in fr


@pytest.mark.django_db
def test_highpass_card_maps_the_bench_to_the_circuit_in_both_languages(client, enrolled, module):
    """Passe-haut : cloche à membrane en série (C), vanne vers le bac (R vers la masse), manomètre aux bornes de la vanne (Vs)."""
    from courses.models import Section

    section = Section.objects.create(
        module=module, title_fr="Le filtre passe-haut", order=1,
        body_md_fr="[[fig:rc_highpass]]", body_md_en="[[fig:rc_highpass]]",
    )
    client.force_login(enrolled)
    fr = client.get(f"/fr/sections/{section.public_id}/").content.decode()
    en = client.get(f"/en/sections/{section.public_id}/").content.decode()

    assert 'class="fig" data-fig="rc_highpass"' in fr and 'id="fig-rc_highpass-freq"' in fr
    assert "Cloche à membrane :</strong>" in fr and "condensateur C = 100 nF, en série" in fr
    assert "Membrane bell:</strong>" in en and "capacitor C = 100 nF, in series" in en
    assert "Throttled valve:</strong>" in en and "resistor R = 1 kΩ, to ground" in en
    assert "Cloche à membrane" not in en
    assert 'src="/static/acad/js/figures/rc_highpass.js' in fr and "figures/rc_lowpass.js" not in fr


@pytest.mark.django_db
def test_figure_controls_are_hidden_without_javascript(client, enrolled, figure_section):
    """US-87 : sans JavaScript, aucune commande inopérante n'est affichée."""
    client.force_login(enrolled)
    html = client.get(f"/fr/sections/{figure_section.public_id}/").content.decode()

    assert "data-fig-controls hidden" in html


def test_hidden_controls_stay_hidden_despite_the_grid_layout():
    """US-87 : `.fig-controls { display: grid }` l'emportait sur l'attribut `hidden` ; sans JavaScript, les commandes s'affichaient."""
    css = (ROOT / "static" / "acad" / "css" / "figures.css").read_text(encoding="utf-8")

    assert ".fig-controls[hidden] { display: none; }" in css


@pytest.mark.django_db
def test_figure_script_loads_only_on_sections_with_a_figure(client, enrolled, module, figure_section):
    """US-89 : script externe chargé seulement où une figure est présente ; aucun script en ligne."""
    from courses.models import Section

    plain = Section.objects.create(module=module, title_fr="Texte", order=2, body_md_fr="Du texte.")
    client.force_login(enrolled)
    html = client.get(f"/fr/sections/{figure_section.public_id}/").content.decode()

    assert 'src="/static/acad/js/figures/rc_lowpass.js' in html
    assert "figures.css" in html
    assert "<script>" not in html
    assert "figures/rc_lowpass.js" not in client.get(f"/fr/sections/{plain.public_id}/").content.decode()


@pytest.mark.django_db
def test_active_drawing_is_never_rendered(client, enrolled, figure_section, monkeypatch):
    """US-88 : un dessin modifié et devenu actif n'est pas intégré (contrôle `inert_svg` à chaque affichage)."""
    from courses import figures

    monkeypatch.setattr(figures, "drawing", lambda name: '<svg onload="alert(1)"></svg>')
    client.force_login(enrolled)
    html = client.get(f"/fr/sections/{figure_section.public_id}/").content.decode()

    assert "onload" not in html


@pytest.mark.django_db
def test_figure_is_only_reachable_through_an_enrolled_section(client, figure_section):
    """US-92 : un anonyme est renvoyé vers la connexion, comme pour le reste du cours."""
    response = client.get(f"/fr/sections/{figure_section.public_id}/")

    assert response.status_code == 302 and "iso-svg" not in response.content.decode()


@pytest.mark.parametrize("name", FIGURES)
def test_figure_script_never_calls_the_server(name):
    """US-92 : la figure n'enregistre rien ; aucun appel réseau ni stockage local dans son script."""
    script = generated(name)[1].read_text(encoding="utf-8")

    for forbidden in ("fetch(", "XMLHttpRequest", "sendBeacon", "localStorage", "sessionStorage", "htmx"):
        assert forbidden not in script


LOWPASS = ROOT / "content" / "electro" / "p2" / "m6"
RECIT = {"fr": "## Ce qui se passe dans le circuit", "en": "## What happens in the circuit"}


@pytest.mark.parametrize("lang", ["fr", "en"])
def test_lowpass_section_carries_the_figure_under_its_corrected_story(lang):
    """US-90 et F10 : récit corrigé puis figure, entre le schéma CEI et la courbe de réponse."""
    text = (LOWPASS / f"03-passe-bas.{lang}.md").read_text(encoding="utf-8")

    assert "\n[[fig:rc_lowpass]]\n" in text
    assert text.index("passe-bas.svg") < text.index(RECIT[lang]) < text.index("[[fig:rc_lowpass]]") < text.index("passe-bas-courbe.svg")


@pytest.mark.parametrize("lang", ["fr", "en"])
def test_lowpass_story_never_says_a_full_capacitor_sends_current_to_the_output(lang):
    """F1 : le récit du brief contenait cette erreur ; sans charge, aucun courant ne « monte vers la sortie »."""
    text = (LOWPASS / f"03-passe-bas.{lang}.md").read_text(encoding="utf-8").lower()

    for wrong in ("vers la sortie", "comme un mur", "towards the output", "like a wall"):
        assert wrong not in text


def test_every_figure_slot_in_the_content_is_a_known_figure():
    """US-90 : un emplacement inconnu resterait du texte visible ; tout `[[fig:…]]` du contenu est dans la liste fermée."""
    import re

    names = {m for path in (ROOT / "content").rglob("*.md") for m in re.findall(r"\[\[fig:([^\]]*)\]\]", path.read_text(encoding="utf-8"))}

    assert names <= set(FIGURES)


def test_markup_cannot_forge_a_figure_slot():
    html = render_markdown('<div class="fig" data-fig="rc_lowpass" onclick="alert(1)"></div>')

    assert "data-fig" not in html and "onclick" not in html


@pytest.mark.skipif(shutil.which("node") is None, reason="Node n'existe que sur le poste de développement (F6)")
def test_physical_models_of_the_figures_pass_their_hand_checked_literals():
    """US-85 : `pytest` lance aussi les tests `node --test` des modèles (tools/figures/<nom>/model.test.mjs)."""
    tests = sorted(str(p) for p in (ROOT / "tools" / "figures").glob("*/model.test.mjs"))
    result = subprocess.run(["node", "--test", *tests], capture_output=True, text=True, encoding="utf-8")

    assert tests and result.returncode == 0, result.stdout + result.stderr


@pytest.mark.parametrize("lang", ["fr", "en"])
def test_highpass_section_carries_the_figure_under_its_story(lang):
    """F10 : récit puis figure, entre le schéma CEI et la courbe de réponse du passe-haut."""
    text = (LOWPASS / f"04-passe-haut.{lang}.md").read_text(encoding="utf-8")

    assert "\n[[fig:rc_highpass]]\n" in text
    assert text.index("passe-haut.svg") < text.index(RECIT[lang]) < text.index("[[fig:rc_highpass]]") < text.index("passe-haut-courbe.svg")


@pytest.mark.parametrize("lang, insulator, wall", [
    ("fr", "aucun électron ne traverse", "comme un mur"),
    ("en", "no electron crosses", "like a wall"),
])
def test_highpass_story_keeps_the_charges_on_each_side_of_the_insulator(lang, insulator, wall):
    """F1 : le courant « passe » le condensateur sans qu'aucune charge ne traverse son isolant ; pas d'image du mur."""
    text = (LOWPASS / f"04-passe-haut.{lang}.md").read_text(encoding="utf-8").lower()

    assert insulator in text
    assert wall not in text


@pytest.mark.django_db
def test_cutoff_card_maps_both_gauges_to_the_circuit_in_both_languages(client, enrolled, module):
    """Fréquence de coupure : manomètre de la vanne (VR) et manomètre du nœud (Vs), aiguilles de crête égales à fc."""
    from courses.models import Section

    section = Section.objects.create(
        module=module, title_fr="La fréquence de coupure", order=1,
        body_md_fr="[[fig:rc_cutoff]]", body_md_en="[[fig:rc_cutoff]]",
    )
    client.force_login(enrolled)
    fr = client.get(f"/fr/sections/{section.public_id}/").content.decode()
    en = client.get(f"/en/sections/{section.public_id}/").content.decode()

    assert 'class="fig" data-fig="rc_cutoff"' in fr and 'id="fig-rc_cutoff-freq"' in fr
    assert "Manomètre de la vanne :</strong>" in fr and "Aiguilles de crête :</strong>" in fr
    assert "Valve gauge:</strong>" in en and "Peak needles:</strong>" in en and "Manomètre" not in en
    assert 'data-fig-preset="low">fc / 10<' in fr and 'data-fig-preset="high">10 × fc<' in fr
    assert "VR / Vin" in en and "Vout / Vin" in en
    assert 'src="/static/acad/js/figures/rc_cutoff.js' in fr and "figures/rc_lowpass.js" not in fr


@pytest.mark.parametrize("lang", ["fr", "en"])
def test_cutoff_section_carries_the_figure_under_its_story(lang):
    """F10 : récit puis figure, entre le schéma Xc = R et la courbe des repères par décade."""
    text = (LOWPASS / f"05-coupure.{lang}.md").read_text(encoding="utf-8")

    assert "\n[[fig:rc_cutoff]]\n" in text
    assert text.index("coupure.svg") < text.index(RECIT[lang]) < text.index("[[fig:rc_cutoff]]") < text.index("attenuation.svg")


@pytest.mark.parametrize("lang, pythagoras, half", [
    ("fr", "vr² + vc² = ve²", "et non la moitié"),
    ("en", "vr² + vc² = vin²", "not half"),
])
def test_cutoff_story_adds_the_two_amplitudes_by_pythagoras(lang, pythagoras, half):
    """F1 : à fc, chaque tension vaut 0,707 × Ve et non la moitié, car VR et Vc ne culminent pas au même instant."""
    text = (LOWPASS / f"05-coupure.{lang}.md").read_text(encoding="utf-8").lower()

    assert pythagoras in text
    assert half in text


@pytest.mark.django_db
def test_phase_card_maps_the_recorder_to_the_circuit_in_both_languages(client, enrolled, module):
    """Déphasage : traceur à deux voies (Ve, Vs aux bornes de C), réglette à 45° par graduation, accolade Δt."""
    from courses.models import Section

    section = Section.objects.create(
        module=module, title_fr="Le déphasage", order=1, body_md_fr="[[fig:rc_phase]]", body_md_en="[[fig:rc_phase]]",
    )
    client.force_login(enrolled)
    fr = client.get(f"/fr/sections/{section.public_id}/").content.decode()
    en = client.get(f"/en/sections/{section.public_id}/").content.decode()

    assert 'class="fig" data-fig="rc_phase"' in fr and 'id="fig-rc_phase-freq"' in fr
    assert "Réglette :</strong>" in fr and "45° par graduation" in fr and "Accolade :</strong>" in fr
    assert "Ruler:</strong>" in en and "45° per mark" in en and "Bracket:</strong>" in en and "Réglette" not in en
    assert 'data-fig-preset="x577">Xc = 577 Ω<' in fr
    assert "Δt / T" in en and "Vout lag" in en
    assert 'src="/static/acad/js/figures/rc_phase.js' in fr and "figures/rc_cutoff.js" not in fr


@pytest.mark.parametrize("lang, keep", [("fr", "## À retenir"), ("en", "## Key points")])
def test_phase_section_carries_the_figure_after_both_ways_to_get_the_angle(lang, keep):
    """F10 : schémas existants gardés (oscilloscope, triangle), puis récit et figure avant « À retenir »."""
    text = (LOWPASS / f"06-dephasage.{lang}.md").read_text(encoding="utf-8")

    assert "\n[[fig:rc_phase]]\n" in text
    assert text.index("dephasage.svg") < text.index("triangle-phi.svg") < text.index(RECIT[lang]) < text.index("[[fig:rc_phase]]") < text.index(keep)


@pytest.mark.parametrize("lang", ["fr", "en"])
def test_phase_story_links_the_current_lead_to_the_output_lag(lang):
    """F1 : φ = arctan(Xc / R) est l'avance du courant ; la sortie prise sur C retarde de 90° − φ."""
    text = (LOWPASS / f"06-dephasage.{lang}.md").read_text(encoding="utf-8")

    assert "90° − φ" in text
