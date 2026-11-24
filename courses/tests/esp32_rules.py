"""Règles propres au contenu de la formation `esp32` (US-115), testées sur des témoins (test_esp32_content_rules.py)."""
import re

from courses.tests.content_rules import practical_problems

FENCE = re.compile(r"^```[ \t]*(\w*)[ \t]*\n(.*?)^```[ \t]*$", re.M | re.S)
CODE_LANGS = {"cpp", "c++", "arduino"}
# Fonctions retirées du cœur Arduino-ESP32 3.x (C3).
REMOVED_API = re.compile(r"\b(ledcSetup|ledcAttachPin|hallRead)\s*\(")
CONSTANT = re.compile(r"\bconst\s+\w+\s+(\w+)\s*=\s*(\d+)\s*;")
PIN_CALL = re.compile(r"\b(pinMode|digitalWrite|digitalRead|analogRead|ledcAttach|touchRead|dacWrite)\s*\(\s*(\w+)\s*(?:,\s*(\w+))?")
FLASH_PINS = range(6, 12)       # reliées à la Flash du module (C14)
INPUT_ONLY_PINS = range(34, 40)  # entrées seules
WIFI_LITERAL = re.compile(r'WiFi\.(?:begin|softAP)\s*\([^)]*"[^)]*\)')
EXTERNAL = re.compile(r"https?://(?:www\.)?(?:youtube\.com|youtu\.be|wokwi\.com|tinkercad\.com)[^\s)\"]*")
# Chaînes et commentaires lus en une seule passe, dans leur ordre d'apparition : « // » dans une chaîne (http://)
# n'ouvre pas de commentaire, et des guillemets dans un commentaire n'ouvrent pas de chaîne.
TOKEN = re.compile(r'"(?:\\.|[^"\\\n])*"|//[^\n]*|/\*.*?\*/', re.S)
ESP32_HEADINGS = {
    "fr": ("## Variante kit complet", "## Variante multimètre seul", "## Sécurité"),
    "en": ("## Full kit variant", "## Multimeter-only variant", "## Safety"),
}


def code_blocks(markdown):
    """Blocs de code C++ d'un texte Markdown (les blocs ini ou texte ne viennent pas des croquis)."""
    return [body for lang, body in FENCE.findall(markdown) if lang.lower() in CODE_LANGS]


def _contains(lines, block):
    return any(lines[i:i + len(block)] == block for i in range(len(lines) - len(block) + 1))


def orphan_code_blocks(markdown, sketches):
    """Première ligne de chaque bloc C++ qui n'est ni un croquis ni un extrait contigu d'un croquis."""
    sketch_lines = [s.splitlines() for s in sketches]
    orphans = []
    for body in code_blocks(markdown):
        block = body.splitlines()
        if not any(_contains(lines, block) for lines in sketch_lines):
            orphans.append(block[0] if block else "")
    return orphans


def _code_only(source):
    code = TOKEN.sub(lambda m: '""' if m.group(0).startswith('"') else "", source)
    return [line.strip() for line in code.splitlines()]


def sketch_pair_differences(fr, en):
    """Lignes du croquis FR dont le code diffère du croquis EN, commentaires et chaînes retirés (C20)."""
    a, b = _code_only(fr), _code_only(en)
    differences = [x for x, y in zip(a, b) if x != y]
    if len(a) != len(b):
        differences.append(f"{len(a)} lignes contre {len(b)}")
    return differences


def removed_api_calls(code):
    return REMOVED_API.findall(code)


def forbidden_pins(code):
    """Broches de la Flash utilisées, ou broches d'entrée seule utilisées en sortie (C9, C14)."""
    constants = {name: int(value) for name, value in CONSTANT.findall(code)}
    problems = []
    for call, pin, mode in PIN_CALL.findall(code):
        number = int(pin) if pin.isdigit() else constants.get(pin)
        if number is None:
            continue
        if number in FLASH_PINS:
            problems.append(f"GPIO {number} (Flash)")
        elif number in INPUT_ONLY_PINS and (call in ("digitalWrite", "ledcAttach", "dacWrite")
                                           or (call == "pinMode" and mode.startswith("OUTPUT"))):
            problems.append(f"GPIO {number} en sortie")
    return problems


def wifi_credentials_in_code(code):
    """Identifiants Wi-Fi écrits en clair : ils vont dans secrets.h (C16)."""
    return WIFI_LITERAL.findall(code)


def external_links(text):
    """Liens vers une vidéo ou un simulateur (C10, C11)."""
    return EXTERNAL.findall(text)


def code_reading_shortfalls(questions_by_dir, minimum):
    """Minimum de questions de lecture de code au quiz, module par module (C7)."""
    shortfalls = []
    for folder, questions in questions_by_dir.items():
        count = sum(q["usage"] == "quiz" and q["type"] in ("single", "multiple", "truefalse")
                    and "```" in q["prompt"]["fr"] for q in questions)
        if count < minimum:
            shortfalls.append(f"{folder} : {count} questions de lecture de code au quiz, {minimum} attendues")
    return shortfalls


def esp32_practical_problems(text, lang):
    """Mini-projet : sécurité en tête, variantes kit complet et multimètre seul, 12 V au plus (C9, C10)."""
    return practical_problems(text, lang, "12 V", headings=ESP32_HEADINGS)


PLATFORM = re.compile(r"^platform\s*=\s*(.+)$", re.M)
LIB_DEPS = re.compile(r"^lib_deps\s*=\s*\n((?:[ \t]+\S.*\n?)+)", re.M)
EXACT = re.compile(r"@\s*\d+\.\d+\.\d+\s*$")


def reference_ini_problems(text):
    """platformio.ini de référence (C4, C16) : plateforme et bibliothèques à une version exacte, carte et vitesse fixées."""
    problems = []
    platform = PLATFORM.search(text)
    if not platform or not EXACT.search(platform.group(1)):
        problems.append(f"plateforme non figée : {platform.group(1).strip() if platform else 'absente'}")
    libs = LIB_DEPS.search(text)
    for lib in (libs.group(1).splitlines() if libs else []):
        if lib.strip() and not EXACT.search(lib):
            problems.append(f"bibliothèque non figée : {lib.strip()}")
    for key, value in (("board", "esp32dev"), ("framework", "arduino"), ("monitor_speed", "115200")):
        if not re.search(rf"^{key}\s*=\s*{value}\s*$", text, re.M):
            problems.append(f"{key} = {value} manquant")
    return problems
