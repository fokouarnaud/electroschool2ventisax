"""US-115 (formation `esp32`, C3, C7, C9, C11, C17, C20) : règles propres au contenu, vérifiées sur des témoins."""
from courses.tests.esp32_rules import (
    code_reading_shortfalls,
    esp32_practical_problems,
    external_links,
    forbidden_pins,
    orphan_code_blocks,
    reference_ini_problems,
    removed_api_calls,
    sketch_pair_differences,
    wifi_credentials_in_code,
)

BLINK_FR = """#include <Arduino.h>

// Broche de la LED
const uint8_t LED_PIN = 2;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.println("Démarrage");
}

void loop() {
  digitalWrite(LED_PIN, HIGH);
}
"""
BLINK_EN = BLINK_FR.replace("// Broche de la LED", "// LED pin").replace('"Démarrage"', '"Starting"')


# --- Blocs de code des sections : croquis entier ou extrait contigu d'un croquis de la même langue --------------------


def test_a_whole_sketch_or_a_contiguous_extract_is_accepted():
    section = f"```cpp\n{BLINK_FR}```\n\nPuis :\n\n```cpp\nvoid loop() {{\n  digitalWrite(LED_PIN, HIGH);\n}}\n```"
    assert orphan_code_blocks(section, [BLINK_FR]) == []


def test_a_code_block_that_is_in_no_sketch_is_reported():
    section = "```cpp\nconst uint8_t LED_PIN = 4;\n```"
    assert orphan_code_blocks(section, [BLINK_FR]) == ["const uint8_t LED_PIN = 4;"]


def test_a_non_contiguous_extract_is_reported():
    section = "```cpp\nconst uint8_t LED_PIN = 2;\nvoid loop() {\n```"
    assert orphan_code_blocks(section, [BLINK_FR]) == ["const uint8_t LED_PIN = 2;"]


def test_ini_and_text_blocks_are_not_checked_against_sketches():
    assert orphan_code_blocks("```ini\n[env:esp32dev]\n```\n\n```text\n97\n```", [BLINK_FR]) == []


# --- Croquis FR et EN : même code une fois commentaires et chaînes retirés (C20) ---------------------------------


def test_sketches_differing_only_by_comments_and_strings_are_the_same_program():
    assert sketch_pair_differences(BLINK_FR, BLINK_EN) == []


def test_sketches_with_different_code_are_reported():
    assert sketch_pair_differences(BLINK_FR, BLINK_EN.replace("= 2;", "= 4;")) == ["const uint8_t LED_PIN = 2;"]


# --- API du cœur 3.x (C3) et broches (C9) ------------------------------------------------------------------------


def test_functions_removed_from_core_3_are_found():
    code = "ledcSetup(0, 5000, 8);\nledcAttachPin(25, 0);\nint h = hallRead();\nledcAttach(25, 5000, 8);"
    assert removed_api_calls(code) == ["ledcSetup", "ledcAttachPin", "hallRead"]


def test_flash_pins_and_outputs_on_input_only_pins_are_found():
    code = ("const uint8_t BAD = 6;\nconst uint8_t SENSOR = 34;\nconst uint8_t LED = 2;\n"
            "pinMode(BAD, OUTPUT);\npinMode(SENSOR, INPUT);\npinMode(35, OUTPUT);\ndigitalWrite(LED, HIGH);\n"
            "int v = analogRead(SENSOR);\ndigitalRead(11);")
    assert forbidden_pins(code) == ["GPIO 6 (Flash)", "GPIO 35 en sortie", "GPIO 11 (Flash)"]


def test_safe_pins_are_accepted():
    assert forbidden_pins(BLINK_FR + "\npinMode(34, INPUT);\nint t = touchRead(4);\nledcAttach(25, 5000, 8);") == []


def test_wifi_credentials_written_in_the_code_are_found():
    assert wifi_credentials_in_code('WiFi.begin("maison", "secret123");') == ['WiFi.begin("maison", "secret123")']
    assert wifi_credentials_in_code('#include "secrets.h"\nWiFi.begin(WIFI_SSID, WIFI_PASSWORD);') == []


# --- Liens externes (C10, C11) -------------------------------------------------------------------------------------


def test_links_to_videos_and_simulators_are_found():
    text = "[vidéo](https://www.youtube.com/watch?v=x) [court](https://youtu.be/x) [sim](https://wokwi.com/projects/1)"
    assert external_links(text) == ["https://www.youtube.com/watch?v=x", "https://youtu.be/x", "https://wokwi.com/projects/1"]
    assert external_links("[catalogue](/fr/catalogue/) et [Espressif](https://docs.espressif.com/)") == []


# --- Minimum de lecture de code au quiz (C7) ----------------------------------------------------------------------


def test_code_reading_minimum_is_checked_module_by_module():
    reading = {"usage": "quiz", "type": "single", "prompt": {"fr": "Qu'affiche ce programme ?\n\n```cpp\nSerial.println(97);\n```"}}
    plain = {"usage": "quiz", "type": "single", "prompt": {"fr": "Quelle broche ?"}}
    exam = dict(reading, usage="exam")
    questions = {"p1/m1": [reading] * 3, "p1/m2": [reading, reading, plain, exam]}
    assert code_reading_shortfalls(questions, 3) == ["p1/m2 : 2 questions de lecture de code au quiz, 3 attendues"]


# --- Mini-projet (C9, C10) ------------------------------------------------------------------------------------------

SAFE_FR = "## Sécurité\nAu plus 12 V CC.\n## Variante kit complet\n...\n## Variante multimètre seul\n..."
SAFE_EN = "## Safety\nAt most 12 V DC.\n## Full kit variant\n...\n## Multimeter-only variant\n..."


def test_a_mini_project_with_safety_first_and_both_variants_passes():
    assert esp32_practical_problems(SAFE_FR, "fr") == []
    assert esp32_practical_problems(SAFE_EN, "en") == []


def test_a_mini_project_without_its_kit_variant_or_its_voltage_is_refused():
    text = "## Sécurité\nBasse tension.\n## Variante multimètre seul\n..."
    assert esp32_practical_problems(text, "fr") == ["titre manquant : ## Variante kit complet", "tension « 12 V » absente"]


# --- US-120 (C4, C16) : platformio.ini de référence, versions figées ------------------------------------------------

GOOD_INI = """[env:esp32dev]
platform = espressif32 @ 8.0.0
board = esp32dev
framework = arduino
monitor_speed = 115200
lib_deps =
    adafruit/Adafruit SSD1306 @ 2.5.17
    adafruit/Adafruit GFX Library @ 1.13.0
    adafruit/Adafruit BME280 Library @ 2.3.0
"""


def test_a_reference_ini_with_pinned_versions_passes():
    assert reference_ini_problems(GOOD_INI) == []


def test_an_unpinned_platform_or_library_is_refused():
    text = GOOD_INI.replace("espressif32 @ 8.0.0", "espressif32").replace("BME280 Library @ 2.3.0", "BME280 Library @ ^2.3.0")
    assert reference_ini_problems(text) == ["plateforme non figée : espressif32",
                                            "bibliothèque non figée : adafruit/Adafruit BME280 Library @ ^2.3.0"]


def test_a_reference_ini_without_the_serial_speed_or_the_board_is_refused():
    text = GOOD_INI.replace("monitor_speed = 115200\n", "").replace("board = esp32dev", "board = esp32-s3-devkitc-1")
    assert reference_ini_problems(text) == ["board = esp32dev manquant", "monitor_speed = 115200 manquant"]


def test_a_url_inside_a_string_is_not_taken_for_a_comment():
    fr = r'Serial.printf("Ouvrez http://%s/\n", ip);  // adresse de la carte' + "\n"
    en = r'Serial.printf("Open http://%s/\n", ip);  // board address' + "\n"
    assert sketch_pair_differences(fr, en) == []


def test_quotes_inside_a_comment_do_not_open_a_string():
    fr = '// espace de noms « reglages »\nprefs.begin("reglages", false);\n'
    en = '// namespace "reglages"\nprefs.begin("reglages", false);\n'
    assert sketch_pair_differences(fr, en) == []
