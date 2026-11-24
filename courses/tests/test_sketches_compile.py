"""US-114 et critère 61 (formation `esp32`, C4, C17) : vraie compilation PlatformIO avec le platformio.ini de référence.

Justification de l'éventuel saut (DoD, critère 2) : PlatformIO est un outil du poste de développement (C17), absent du
serveur et de requirements*.txt ; sans lui, ce test est ignoré. Il dure 2 à 3 minutes (une compilation complète par croquis).
"""
import shutil

import pytest
from django.conf import settings

from tools import sketches

REFERENCE_INI = settings.BASE_DIR / "content" / "esp32" / "sketches" / "platformio.ini"

GOOD = """#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_SSD1306.h>
#include <Adafruit_BME280.h>

// Broche de la LED et réglages de la MLI
const uint8_t LED_PIN = 25;
const uint32_t PWM_FREQ_HZ = 5000;
const uint8_t PWM_BITS = 8;

Adafruit_SSD1306 screen(128, 64, &Wire, -1);
Adafruit_BME280 sensor;

void setup() {
  Serial.begin(115200);
  ledcAttach(LED_PIN, PWM_FREQ_HZ, PWM_BITS);
}

void loop() {
  ledcWrite(LED_PIN, 128);
}
"""
# API du cœur 2.x, retirée en 3.x (C3) : la compilation doit échouer.
REMOVED_API = GOOD.replace("ledcAttach(LED_PIN, PWM_FREQ_HZ, PWM_BITS);", "ledcSetup(0, PWM_FREQ_HZ, PWM_BITS);")

pytestmark = pytest.mark.skipif(sketches.pio() is None, reason="PlatformIO absent du poste (outil de développement, C17)")


def tree(root, code):
    shutil.copyfile(REFERENCE_INI, root / "platformio.ini")
    folder = root / "m6" / "pwm"
    folder.mkdir(parents=True)
    (folder / "main.fr.cpp").write_text(code, encoding="utf-8")
    return root


def test_a_core_3_sketch_with_the_course_libraries_compiles_with_the_reference_ini(tmp_path):
    assert sketches.compile_all(tree(tmp_path, GOOD)) == []


def test_a_sketch_using_a_function_removed_from_core_3_does_not_compile(tmp_path):
    assert sketches.compile_all(tree(tmp_path, REMOVED_API)) == ["m6/pwm (fr)"]
