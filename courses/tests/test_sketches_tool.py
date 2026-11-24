"""US-114 (formation `esp32`, C17, C20) : tools/sketches.py compile chaque croquis, dans ses deux langues, au poste."""
from pathlib import Path

import pytest
from django.conf import settings

from tools import sketches

INI = "[env:esp32dev]\nplatform = https://example.invalid/platform-espressif32.zip\nboard = esp32dev\nframework = arduino\n"
BLINK_FR = "// Fait clignoter la LED\nconst uint8_t LED_PIN = 2;\nvoid setup() { pinMode(LED_PIN, OUTPUT); }\nvoid loop() {}\n"
BLINK_EN = "// Blinks the LED\nconst uint8_t LED_PIN = 2;\nvoid setup() { pinMode(LED_PIN, OUTPUT); }\nvoid loop() {}\n"


@pytest.fixture
def tree(tmp_path):
    (tmp_path / "platformio.ini").write_text(INI, encoding="utf-8")
    blink = tmp_path / "m2" / "blink"
    blink.mkdir(parents=True)
    (blink / "main.fr.cpp").write_text(BLINK_FR, encoding="utf-8")
    (blink / "main.en.cpp").write_text(BLINK_EN, encoding="utf-8")
    (blink / "notes.txt").write_text("pas un croquis", encoding="utf-8")
    web = tmp_path / "m9" / "web"
    web.mkdir(parents=True)
    (web / "main.fr.cpp").write_text('#include "secrets.h"\nvoid setup() {}\nvoid loop() {}\n', encoding="utf-8")
    (web / "secrets.example.h").write_text('#define WIFI_SSID "mon-reseau"\n', encoding="utf-8")
    return tmp_path


def test_discover_lists_each_sketch_in_each_language(tree):
    assert [(s.name, s.lang) for s in sketches.discover(tree)] == [("m2/blink", "en"), ("m2/blink", "fr"), ("m9/web", "fr")]


def test_a_project_holds_the_reference_ini_and_the_sketch_as_main_cpp(tree, tmp_path_factory):
    blink_fr = next(s for s in sketches.discover(tree) if s.lang == "fr")

    project = sketches.project(blink_fr, tree / "platformio.ini", tmp_path_factory.mktemp("build"))

    assert (project / "platformio.ini").read_text(encoding="utf-8") == INI
    assert (project / "src" / "main.cpp").read_text(encoding="utf-8") == BLINK_FR


def test_a_sketch_with_example_secrets_compiles_against_them(tree, tmp_path_factory):
    web = next(s for s in sketches.discover(tree) if s.name == "m9/web")

    project = sketches.project(web, tree / "platformio.ini", tmp_path_factory.mktemp("build"))

    assert (project / "include" / "secrets.h").read_text(encoding="utf-8") == '#define WIFI_SSID "mon-reseau"\n'


def test_compile_all_runs_platformio_once_per_sketch_and_language(tree):
    calls = []

    def runner(project):
        calls.append(Path(project).joinpath("src", "main.cpp").read_text(encoding="utf-8"))
        return 0

    assert sketches.compile_all(tree, runner) == []
    assert len(calls) == 3
    assert BLINK_FR in calls and BLINK_EN in calls


def test_compile_all_stops_at_the_first_failure_and_names_it(tree):
    calls = []

    def runner(project):
        calls.append(project)
        return 1

    assert sketches.compile_all(tree, runner) == ["m2/blink (en)"]
    assert len(calls) == 1


def test_the_command_fails_when_a_sketch_does_not_compile(tree):
    assert sketches.main(["--root", str(tree)], runner=lambda project: 1) != 0
    assert sketches.main(["--root", str(tree)], runner=lambda project: 0) == 0


def test_deployment_never_compiles_sketches():
    deploy = (settings.BASE_DIR / "deploy.sh").read_text(encoding="utf-8")

    assert "sketches" not in deploy
    assert "pio" not in deploy.replace("pip", "")
