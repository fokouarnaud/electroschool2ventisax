"""US-64 (formation `moteurs`) : les règles propres au contenu, vérifiées sur des textes témoins avant tout contenu réel."""
from courses.tests.content_rules import (
    links_to_other_formation_sections,
    numeric_shortfalls,
    practical_problems,
    rockwell_addresses,
    us_mains_values,
)

SAFE_FR = "## Sécurité\nTout se câble en 24 V.\n## Variante oscilloscope\n...\n## Variante multimètre seul\n..."
SAFE_EN = "## Safety\nEverything is wired at 24 V.\n## Oscilloscope variant\n...\n## Multimeter-only variant\n..."


def test_a_mini_project_with_safety_first_both_variants_and_24_volts_passes():
    assert practical_problems(SAFE_FR, "fr", "24 V") == []
    assert practical_problems(SAFE_EN, "en", "24 V") == []


def test_a_mini_project_whose_safety_comes_after_the_variants_is_refused():
    text = "## Variante oscilloscope\n...\n## Variante multimètre seul\n...\n## Sécurité\n24 V"
    assert practical_problems(text, "fr", "24 V") == ["la sécurité vient avant les variantes"]


def test_a_mini_project_without_its_multimeter_variant_is_refused():
    text = "## Safety\n24 V\n## Oscilloscope variant\n..."
    assert practical_problems(text, "en", "24 V") == ["titre manquant : ## Multimeter-only variant"]


def test_a_mini_project_that_never_states_its_voltage_is_refused():
    text = SAFE_FR.replace("24 V", "basse tension")
    assert practical_problems(text, "fr", "24 V") == ["tension « 24 V » absente"]


def test_american_mains_values_are_found_and_iec_values_are_not():
    text = "Réseau 400 V 50 Hz. Aux États-Unis : 60 Hz, 460 V, 120 V. Un relais 24 V."
    assert us_mains_values(text) == ["60 Hz", "460 V", "120 V"]
    assert us_mains_values("Réseau 230/400 V, 50 Hz, moteur de 1 460 tr/min.") == []


def test_rockwell_plc_addresses_are_found_and_iec_addresses_are_not():
    assert rockwell_addresses("Entrée I:1/0, sortie O:2/3.") == ["I:1/0", "O:2/3"]
    assert rockwell_addresses("Entrée %IX0.0, sortie %QX0.1, mémoire %MX0.2 ; Siemens I0.0, Schneider %I0.0.") == []


def test_links_into_another_formation_are_found_but_its_catalogue_page_is_allowed():
    text = "Voir [la diode](/fr/sections/1234/) et [le module](/en/modules/abcd/) ou [la fiche](/fr/catalogue/)."
    assert links_to_other_formation_sections(text) == ["/fr/sections/1234/", "/en/modules/abcd/"]


def test_numeric_minimum_is_checked_module_by_module():
    questions = {
        "p1/m1": [{"usage": "quiz", "type": "numeric"}] * 2,
        "p1/m3": [{"usage": "quiz", "type": "numeric"}] * 3 + [{"usage": "exam", "type": "numeric"}],
    }
    assert numeric_shortfalls(questions, {"p1/m1": 2, "p1/m3": 4}) == ["p1/m3 : 3 numériques au quiz, 4 attendues"]


def test_scanning_a_content_folder_reports_each_faulty_file(tmp_path):
    """US-78 : le garde-fou parcourt tout le dossier d'une formation, Markdown et JSON, et nomme chaque fichier fautif."""
    from courses.tests.content_rules import scan_folder

    (tmp_path / "p1" / "m1").mkdir(parents=True)
    (tmp_path / "p1" / "m1" / "01-effets.fr.md").write_text("Rappel : [la diode](/fr/sections/abc/).", encoding="utf-8")
    (tmp_path / "p1" / "m1" / "02-ok.fr.md").write_text("Voir [la fiche](/fr/catalogue/), réseau 400 V 50 Hz.", encoding="utf-8")
    (tmp_path / "p1" / "m1" / "questions.json").write_text('[{"prompt": {"fr": "Entrée I:1/0 à 60 Hz"}}]', encoding="utf-8")

    assert scan_folder(tmp_path) == [
        "01-effets.fr.md : lien vers une section d'une autre formation /fr/sections/abc/",
        "questions.json : réseau américain 60 Hz",
        "questions.json : adresse Rockwell I:1/0",
    ]
