"""Règles propres au contenu d'une formation (US-64), appliquées par test_content_files.py et testées sur des témoins."""
import re

PRACTICAL_HEADINGS = {
    "fr": ("## Variante oscilloscope", "## Variante multimètre seul", "## Sécurité"),
    "en": ("## Oscilloscope variant", "## Multimeter-only variant", "## Safety"),
}
# Réseaux et tensions américains écartés par M2 (la formation `moteurs` travaille en 230/400 V, 50 Hz).
US_MAINS = re.compile(r"(?<![\d,.])(60 Hz|460 V|120 V)\b")
# Adressage Rockwell du livre (I:1/0) écarté par M7 au profit de l'IEC 61131-3 (%IX0.0).
ROCKWELL = re.compile(r"\b[IO]:\d+/\d+\b")
# Un lien Markdown vers un module ou une section : réservé à sa propre formation (M11).
SECTION_LINK = re.compile(r"\]\((/(?:fr|en)/(?:sections|modules)/[^)\s]*)\)")


def practical_problems(text, lang, voltage):
    """Mini-projet : sécurité en tête, deux variantes de mesure, tension de travail écrite."""
    variant_a, variant_b, safety = PRACTICAL_HEADINGS[lang]
    problems = [f"titre manquant : {h}" for h in (variant_a, variant_b, safety) if h not in text]
    if not problems and text.find(safety) > min(text.find(variant_a), text.find(variant_b)):
        problems.append("la sécurité vient avant les variantes")
    if voltage not in text:
        problems.append(f"tension « {voltage} » absente")
    return problems


def us_mains_values(text):
    return US_MAINS.findall(text)


def rockwell_addresses(text):
    return ROCKWELL.findall(text)


def links_to_other_formation_sections(text):
    return SECTION_LINK.findall(text)


def numeric_shortfalls(questions_by_dir, minimums):
    """Minimum de questions numériques au quiz, module par module (M4)."""
    shortfalls = []
    for folder, minimum in minimums.items():
        count = sum(q["usage"] == "quiz" and q["type"] == "numeric" for q in questions_by_dir.get(folder, []))
        if count < minimum:
            shortfalls.append(f"{folder} : {count} numériques au quiz, {minimum} attendues")
    return shortfalls


def scan_folder(folder):
    """Problèmes de tous les Markdown et JSON d'une formation (M2, M7, M11), fichier par fichier, dans l'ordre des noms."""
    problems = []
    for path in sorted(list(folder.rglob("*.md")) + list(folder.rglob("*.json")), key=lambda p: p.name):
        text = path.read_text(encoding="utf-8")
        problems += [f"{path.name} : lien vers une section d'une autre formation {link}" for link in links_to_other_formation_sections(text)]
        problems += [f"{path.name} : réseau américain {value}" for value in us_mains_values(text)]
        problems += [f"{path.name} : adresse Rockwell {address}" for address in rockwell_addresses(text)]
    return problems
