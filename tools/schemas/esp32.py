"""Schémas de la formation « Microcontrôleurs : l'ESP32 » (C12) : python -m tools.schemas esp32.

Tous originaux : carte DevKit 38 broches (ESP32-WROOM-32), symboles CEI, schémas fonctionnels, chronogrammes.
Écrit les schémas des sections dans static/content/esp32/[en/]m<N>/ et ceux des questions sur schéma dans
content/esp32/p<P>/m<N>/schemas/ ; jamais de SVG retouché à la main.
"""
from .common import ACCENT, INK, PAPER, ROOT, SOFT, Drawing, block, fmt
from .moteurs import timing

SLUG = "esp32"

# Libellés anglais des schémas (tr) ; les virgules décimales restantes deviennent des points.
EN = {
    # Catégories de broches de la carte DevKit (C12, C14)
    "Flash : ne pas utiliser": "Flash: do not use",
    "Entrée seule": "Input only",
    "Strapping : prudence": "Strapping: caution",
    "Broche sûre": "Safe pin",
    "Alimentation": "Power",
    "Liaison série USB": "USB serial link",
    # M1
    "Résistance": "Resistor", "Condensateur": "Capacitor", "Diode": "Diode",
    "limite le courant, fixe un état": "limits current, sets a state",
    "filtre l'alimentation 3,3 V": "filters the 3,3 V supply",
    "protège, roue libre": "protects, freewheeling",
    "commande 12 V": "switches 12 V",
    "Capteur": "Sensor", "Actionneur": "Actuator",
    "lire": "read", "calculer": "compute", "commander": "drive",
    "bouton, potentiomètre": "button, potentiometer", "LED, moteur, relais": "LED, motor, relay",
    "2 cœurs Xtensa LX6": "2 Xtensa LX6 cores", "jusqu'à 240 MHz": "up to 240 MHz",
    "SRAM 520 Ko": "SRAM 520 KB", "ROM 448 Ko": "ROM 448 KB", "Flash 4 Mo": "Flash 4 MB",
    "Périphériques": "Peripherals", "GPIO, ADC, DAC, MLI, Touch": "GPIO, ADC, DAC, PWM, Touch",
    "UART, I2C, SPI, I2S": "UART, I2C, SPI, I2S",
    "Wi-Fi 2,4 GHz, Bluetooth": "Wi-Fi 2,4 GHz, Bluetooth", "Gestion d'énergie": "Power management",
    "module ESP32-WROOM-32": "ESP32-WROOM-32 module",
    "programme (garde sans courant)": "program (kept without power)",
    "variables (effacée à la coupure)": "variables (erased at power-off)",
    "démarrage (gravée en usine)": "boot code (factory-programmed)",
    "Port USB": "USB port", "Pont USB-série": "USB-serial bridge", "Régulateur 3,3 V": "3,3 V regulator",
    "Module ESP32-WROOM-32": "ESP32-WROOM-32 module", "antenne": "antenna",
    "bouton EN (redémarrage)": "EN button (restart)", "bouton BOOT (téléversement)": "BOOT button (upload)", "série": "serial",
    "ordinateur": "computer", "puce": "chip", "broche 5V": "5V pin", "broche 3V3": "3V3 pin",
    "Légende": "Key",
    "Capteur 5 V": "5 V sensor", "vers GPIO 34": "to GPIO 34", "jamais 5 V sur une broche": "never 5 V on a pin",
    "USB 5 V": "USB 5 V", "batterie 12 V": "12 V battery", "moteur": "motor",
    "masse commune": "common ground", "GND reliés": "GND joined",
    "au plus 12 mA environ": "about 12 mA at most",
    "VS Code + PlatformIO": "VS Code + PlatformIO", "compiler": "build", "téléverser": "upload",
    "moniteur série": "serial monitor", "câble USB": "USB cable", "carte ESP32": "ESP32 board",
    "mon-projet": "my-project", "réglages du projet": "project settings", "votre programme": "your program",
    "vos en-têtes (.h)": "your headers (.h)", "vos bibliothèques": "your libraries",
    "mise sous tension": "power-up", "une seule fois": "once only", "sans fin": "forever",
    "réglages : broches, série": "settings: pins, serial", "lire, calculer, commander": "read, compute, drive",
    "le programme ne s'arrête jamais": "the program never stops",
    "1. Compilation": "1. Build", "2. Téléversement": "2. Upload", "3. Redémarrage": "3. Restart",
    "GPIO 6 à 11 : reliées à la mémoire Flash": "GPIO 6 to 11: wired to the Flash memory",
    "GPIO 34, 35, 36, 39 : ni sortie, ni tirage interne": "GPIO 34, 35, 36, 39: no output, no internal pull",
    "GPIO 0, 2, 5, 12, 15 : lues au démarrage": "GPIO 0, 2, 5, 12, 15: read at boot",
    "les autres : LED, bouton, MOSFET": "all others: LED, button, MOSFET",
    "PlatformIO traduit le C++ en code machine": "PlatformIO turns C++ into machine code",
    "le code est écrit dans la Flash": "the code is written to Flash",
    "le programme démarre : setup puis loop": "the program starts: setup then loop",
    "Moniteur série à 115 200 bit/s": "Serial monitor at 115200 bit/s",
    "Modèle, cœurs, fréquence, Flash": "Model, cores, frequency, Flash",
    "LED sur GPIO 25": "LED on GPIO 25", "DevKitC V4": "DevKitC V4",
    "antenne (vers le bord)": "antenna (towards the edge)", "Régulateur 3,3 V (AMS1117)": "3,3 V regulator (AMS1117)",
    "LED rouge : carte sous tension": "red LED: board powered", "Pont USB-série (CP2102 ou CH340)": "USB-serial bridge (CP2102 or CH340)",
    "Port micro-USB": "Micro-USB port",
    "puce ESP32": "ESP32 chip", "2 cœurs, 240 MHz": "2 cores, 240 MHz", "bus interne": "internal bus",
    "Registres GPIO": "GPIO registers", "matrice": "matrix", "et": "and", "plot": "pad", "broches": "pins",
    "de la carte": "of the board",
    "anode (patte longue)": "anode (long leg)", "cathode (méplat)": "cathode (flat side)",
    "HIGH : la LED s'allume ; LOW : elle s'éteint": "HIGH: the LED lights; LOW: it goes out",
    # M2
    "niveau haut (1)": "high level (1)", "niveau bas (0)": "low level (0)", "broche": "pin",
    "HIGH : vers 3,3 V": "HIGH: towards 3,3 V", "LOW : vers GND": "LOW: towards GND",
    "un seul des deux interrupteurs est fermé": "only one of the two switches is closed",
    "aux bornes de R": "across R", "aux bornes de la LED": "across the LED",
    "R = 1,3 V / 4 mA ≈ 325 Ω, on choisit 330 Ω": "R = 1,3 V / 4 mA ≈ 325 Ω, choose 330 Ω",
    "source : HIGH allume": "source: HIGH lights", "puits : LOW allume": "sink: LOW lights",
    "le courant sort de la broche": "current leaves the pin", "le courant entre dans la broche": "current enters the pin",
    "temps (ms)": "time (ms)",
    "Arduino : digitalWrite": "Arduino: digitalWrite", "ESP-IDF : gpio_set_level": "ESP-IDF: gpio_set_level",
    "registre GPIO_OUT_W1TS": "GPIO_OUT_W1TS register", "plus simple": "simpler", "plus proche du matériel": "closer to the hardware",
    "un bit par broche": "one bit per pin",
    "GPIO_ENABLE : bit 25": "GPIO_ENABLE: bit 25", "GPIO_OUT : bit 25": "GPIO_OUT: bit 25", "GPIO_IN : bit 25": "GPIO_IN: bit 25",
    "1 = sortie": "1 = output", "1 = HIGH, 0 = LOW": "1 = HIGH, 0 = LOW", "tampon d'entrée : compare aux seuils": "input buffer: compares with the thresholds",
    "niveau écrit": "level written", "1 = mettre à 1": "1 = set to 1", "1 = mettre à 0": "1 = clear to 0", "niveau lu": "level read",
    "un bit par broche : le bit 25 commande GPIO 25": "one bit per pin: bit 25 drives GPIO 25",
    "hors de la puce": "outside the chip", "tampon": "buffer", "fermé": "closed", "ouvert": "open",
    "broche GPIO 4": "pin GPIO 4",
    "roue libre": "freewheeling",
    "rappel 10 kΩ : MOSFET bloqué pendant le démarrage ; masse commune": "10 kΩ pull-down: MOSFET off during boot; common ground",
    "GPIO LOW : MOSFET bloqué, moteur arrêté": "GPIO LOW: MOSFET off, motor stopped",
    "GPIO HIGH : MOSFET passant, moteur en marche": "GPIO HIGH: MOSFET on, motor running",
    "MOSFET logic-level : passant dès 3,3 V sur la grille": "logic-level MOSFET: on from 3,3 V on the gate",
    "vert": "green", "orange": "amber", "rouge": "red", "temps (s)": "time (s)",
    "lampe 12 V": "12 V lamp", "feu tricolore": "traffic light",
    # M3
    "bouton": "button", "niveau inconnu : la broche flotte": "unknown level: the pin floats",
    "lu comme 1": "read as 1", "lu comme 0": "read as 0", "zone indéterminée": "undefined zone",
    "tirage vers la masse (pull-down)": "pull-down to ground", "tirage vers 3,3 V (pull-up)": "pull-up to 3,3 V",
    "relâché : LOW, appuyé : HIGH": "released: LOW, pressed: HIGH", "relâché : HIGH, appuyé : LOW": "released: HIGH, pressed: LOW",
    "dans la puce": "inside the chip", 
    "1. lire les entrées": "1. read the inputs", "2. calculer": "2. compute", "3. écrire les sorties": "3. write the outputs",
    "loop() recommence": "loop() starts again",
    "rebonds": "bounces", "appui": "press", "relâché": "released", "appuyé": "pressed", "état stable": "stable state",
    "attendre 20 ms": "wait 20 ms", "changement lu ?": "change read?", "relire": "read again", "toujours changé ?": "still changed?",
    "accepter le nouvel état": "accept the new state", "oui": "yes", "non": "no",
    "front descendant : appui": "falling edge: press", "front montant : relâchement": "rising edge: release",
    "LED (bascule)": "LED (toggle)",
    "ÉTEINT": "OFF", "ALLUMÉ": "ON", "ROUGE": "RED", "ORANGE": "AMBER", "VERT": "GREEN", "CYCLE": "CYCLE", "VEILLE": "STANDBY",
    "appui sur le bouton": "button press", "orange clignotant": "flashing amber", "vert, orange, rouge": "green, amber, red",
    "capteur 5 V": "5 V sensor", "3,33 V au plus": "3,33 V at most",
    "5 V : interdit": "5 V: forbidden", "3,33 V : lu comme 1": "3,33 V: read as 1", "0 V : lu comme 0": "0 V: read as 0",
    "feu tricolore et bouton": "traffic light and button",
    # M4
    "bouton ignoré": "button ignored", "delay(500)": "delay(500)", "lecture du bouton": "button read",
    "loop() bloquée pendant delay": "loop() blocked during delay",
    "millis() : millisecondes depuis le démarrage": "millis(): milliseconds since start-up",
    "4 294 967 295 ms ≈ 49,7 jours, puis retour à 0": "4294967295 ms ≈ 49,7 days, then back to 0",
    "maintenant − dernier ≥ période ?": "now − last ≥ period?", "inverser la LED": "toggle the LED",
    "dernier = maintenant": "last = now", "continuer la boucle": "carry on with the loop",
    "LED 1 : 500 ms": "LED 1: 500 ms", "LED 2 : 120 ms": "LED 2: 120 ms",
    "programme principal": "main program", "routine d'interruption (ISR)": "interrupt routine (ISR)",
    "front sur la broche": "edge on the pin", "retour au programme": "back to the program",
    "courte : quelques lignes": "short: a few lines", "volatile : variables partagées": "volatile: shared variables",
    "IRAM_ATTR : en mémoire rapide": "IRAM_ATTR: in fast memory", "jamais delay ni Serial": "never delay nor Serial",
    "horloge 80 MHz": "80 MHz clock", "compteur à 1 MHz": "counter at 1 MHz", "alarme à 1 000 000": "alarm at 1000000",
    "ISR chaque seconde": "ISR every second", "attente aléatoire": "random wait", "temps de réaction": "reaction time",
    # M5
    "repos": "idle", "départ": "start", "arrêt": "stop", "bit": "bit", "bits de données, poids faible d'abord": "data bits, least significant first",
    "ordinateur": "computer", "pont USB-série": "USB-serial bridge", "même vitesse aux deux bouts": "same speed at both ends",
    "115 200 bit/s des deux côtés : texte lisible": "115200 bit/s on both sides: readable text",
    "9 600 d'un côté, 115 200 de l'autre : caractères illisibles": "9600 on one side, 115200 on the other: unreadable characters",
    "caractère": "character", "code ASCII (décimal)": "ASCII code (decimal)",
    "tampon de réception": "receive buffer", "available() : octets en attente": "available(): bytes waiting",
    "read() : le plus ancien, ou -1": "read(): the oldest one, or -1",
    "lire jusqu'à Entrée": "read up to Enter", "comparer à une commande connue": "compare with a known command",
    "agir et répondre": "act and reply", "commande inconnue : message d'erreur": "unknown command: error message",
    "trace : valeurs à chaque étape": "trace: values at each step",
    "carte A": "board A", "carte B": "board B", "TX vers RX, RX vers TX, GND commun": "TX to RX, RX to TX, common GND",
    # M6
    "tension (V)": "voltage (V)", "valeur lue": "value read", "4 096 niveaux, pas de 0,8 mV": "4096 levels, 0,8 mV steps",
    "idéal": "ideal", "réel : moins précis près de 0 V et de 3,3 V": "real: less accurate near 0 V and 3,3 V",
    "curseur vers GPIO 34": "wiper to GPIO 34",
    "rapport cyclique": "duty cycle", "tension moyenne": "average voltage",
    "MLI 5 kHz sur la grille": "5 kHz PWM on the gate", "vitesse": "speed",
    "fréquence = hauteur du son": "frequency = pitch", "buzzer passif": "passive buzzer",
    "électrode": "electrode", "doigt": "finger", "capacité plus grande": "larger capacitance",
    "sans doigt": "no finger", "avec doigt": "with finger", "seuil": "threshold", "temps": "time",
    "dacWrite : 256 niveaux de 0 à 3,3 V": "dacWrite: 256 levels from 0 to 3,3 V",
    "potentiomètre": "potentiometer", "touche tactile": "touch key",
    # M7
    "fils": "wires", "UART : 2 fils, 1 appareil": "UART: 2 wires, 1 device", "I2C : 2 fils, jusqu'à 127 appareils": "I2C: 2 wires, up to 127 devices",
    "SPI : 4 fils, très rapide": "SPI: 4 wires, very fast", "horloge partagée": "shared clock", "adresse de 7 bits": "7-bit address",
    "écran OLED (0x3C)": "OLED display (0x3C)", "capteur BME280 (0x76)": "BME280 sensor (0x76)", "tirages de 4,7 kΩ": "4,7 kΩ pull-ups",
    "départ": "start", "adresse": "address", "lecture/écriture": "read/write", "acquittement": "acknowledge", "donnée": "data",
    "128 colonnes": "128 columns", "64 lignes": "64 rows", "origine (0, 0)": "origin (0, 0)", "écran OLED": "OLED display",
    "température": "temperature", "humidité": "humidity", "pression": "pressure",
    "carte microSD": "microSD card", "CS de chaque appareil": "CS of each device", "un CS par appareil": "one CS per device",
    "journal.csv": "log.csv", "station de mesure": "measuring station",
    # M8
    "Flash : programme et Preferences": "Flash: program and Preferences", "SRAM : variables": "SRAM: variables",
    "mémoire RTC : 8 Ko": "RTC memory: 8 KB", "coupure": "power-off", "veille profonde": "deep sleep", "garde": "kept", "perd": "lost",
    "espace de noms « reglages »": "namespace \"reglages\"", "clé": "key", "valeur": "value",
    "environ 100 000 écritures par cellule": "about 100000 writes per cell",
    "actif + Wi-Fi": "active + Wi-Fi", "actif": "active", "veille légère": "light sleep",
    "courant (échelle logarithmique)": "current (log scale)",
    "pile de 2 000 mAh": "2000 mAh battery", "réveil : setup() recommence": "wake-up: setup() starts again",
    "mesurer": "measure", "dormir 10 s": "sleep 10 s", "minuterie": "timer", "toucher": "touch", "broche RTC": "RTC pin",
    "broches RTC (réveil ext0)": "RTC pins (ext0 wake-up)", "autres broches": "other pins",
    "bootCount en mémoire RTC : 1, 2, 3…": "bootCount in RTC memory: 1, 2, 3…", "enregistreur sobre": "frugal logger",
    # M9
    "station : rejoint la box": "station: joins the router", "point d'accès : crée son réseau": "access point: creates its network",
    "box Wi-Fi": "Wi-Fi router", "téléphone": "phone", "réseau local": "local network",
    "connexion…": "connecting…", "connecté : adresse IP": "connected: IP address", "perte : nouvelle tentative": "lost: new attempt",
    "excellent": "excellent", "bon": "good", "faible": "weak", "inutilisable": "unusable",
    "navigateur": "browser", "requête": "request", "réponse 200 : page HTML": "response 200: HTML page",
    "route": "route", "action": "action", "page d'accueil": "home page", "allumer la lampe": "switch the lamp on", "éteindre la lampe": "switch the lamp off",
    "mesure en JSON": "measurement as JSON", "lampe 12 V": "12 V lamp", "tableau de bord": "dashboard",
    "Allumer": "On", "Éteindre": "Off", "Tension": "Voltage", "toutes les 2 s": "every 2 s",
    "secrets.h : jamais partagé": "secrets.h: never shared", "secrets.example.h : sans valeurs": "secrets.example.h: no values",
    "réseau local seulement": "local network only", "Internet : pas d'accès entrant": "Internet: no incoming access",
    "Bluetooth basse consommation": "Bluetooth Low Energy", "cadre officiel d'Espressif": "Espressif's official framework",
    "système temps réel, tâches": "real-time system, tasks", "cœur 0 : Wi-Fi": "core 0: Wi-Fi", "cœur 1 : loop()": "core 1: loop()",
    "buzzer": "buzzer",
    "Recherche sur le bus I2C...": "Scanning the I2C bus...", "Appareil trouvé en 0x3C": "Device found at 0x3C",
    "Appareil trouvé en 0x76": "Device found at 0x76", "2 appareils": "2 devices", "autre appareil": "other device",
    "réveil": "wake-up", "mémoire RTC": "RTC memory", "Tension : 1,65 V": "Voltage: 1,65 V",
    "temps_ms;tension_mV": "time_ms;voltage_mV",
    "valeur écrite": "value written", "niveau=1 etat=0": "level=1 state=0", "niveau=0 etat=1": "level=0 state=1",
    "niveau=1 etat=1": "level=1 state=1",
}

PIN_H = 25
# Carte ESP32-DevKitC V4 et ses clones 38 broches (ESP32-WROOM-32), sérigraphie de haut en bas : (libellé, catégorie)
LEFT_PINS = [("3V3", "pwr"), ("EN", "pwr"), ("SVP 36", "in"), ("SVN 39", "in"), ("34", "in"), ("35", "in"), ("32", "ok"),
             ("33", "ok"), ("25", "ok"), ("26", "ok"), ("27", "ok"), ("14", "ok"), ("12", "strap"), ("GND", "pwr"),
             ("13", "ok"), ("SD2 9", "flash"), ("SD3 10", "flash"), ("CMD 11", "flash"), ("5V", "pwr")]
RIGHT_PINS = [("GND", "pwr"), ("23", "ok"), ("22", "ok"), ("TXD 1", "uart"), ("RXD 3", "uart"), ("21", "ok"), ("GND", "pwr"),
              ("19", "ok"), ("18", "ok"), ("5", "strap"), ("17", "ok"), ("16", "ok"), ("4", "ok"), ("0", "strap"),
              ("2", "strap"), ("15", "strap"), ("SD1 8", "flash"), ("SD0 7", "flash"), ("CLK 6", "flash")]


def pin_box(d, x, y, kind, marks=True):
    """Pastille d'une broche (22 × 18) : la catégorie se lit aux hachures et aux libellés, jamais à la couleur seule."""
    fill = "#dfe8ea" if kind in ("pwr", "uart") and marks else PAPER
    d.add(f'<rect x="{fmt(x)}" y="{fmt(y)}" width="22" height="18" rx="3" fill="{fill}" stroke="{INK}" stroke-width="1.5"/>')
    if not marks:
        return
    if kind == "flash":  # croix : interdite
        d.add(f'<path d="M{fmt(x + 4)} {fmt(y + 3)} l14 12 M{fmt(x + 18)} {fmt(y + 3)} l-14 12" stroke="{INK}" stroke-width="1.5"/>')
    elif kind == "in":  # hachures obliques : entrée seule
        d.add(f'<path d="M{fmt(x + 3)} {fmt(y + 15)} l8 -12 M{fmt(x + 9)} {fmt(y + 15)} l8 -12 M{fmt(x + 15)} {fmt(y + 15)} l5 -8" '
              f'stroke="{SOFT}" stroke-width="1.5"/>')
    elif kind == "strap":  # point d'exclamation : prudence au démarrage
        d.text(x + 11, y + 14, "!", size=13, weight="700", color=ACCENT)


def devkit(d, x, y, marks=True, zones=()):
    """Carte DevKit 38 broches vue de dessus ; zones = libellés des broches à rendre cliquables (question sur schéma)."""
    width = 150
    board_h = len(LEFT_PINS) * PIN_H + 30
    d.add(f'<rect x="{fmt(x)}" y="{fmt(y)}" width="{width}" height="{board_h}" rx="10" fill="#eef4f3" stroke="{INK}" stroke-width="2"/>')
    d.add(f'<rect x="{fmt(x + 30)}" y="{fmt(y + 8)}" width="{width - 60}" height="70" rx="4" fill="#c9d8dd" stroke="{INK}" stroke-width="1.5"/>')
    d.text(x + width / 2, y + 48, "ESP32", size=13, weight="700")
    d.text(x + width / 2, y + 100, "DevKitC V4", size=10, color=SOFT)
    d.add(f'<rect x="{fmt(x + 55)}" y="{fmt(y + board_h - 22)}" width="40" height="18" rx="3" fill="{PAPER}" stroke="{INK}" stroke-width="1.5"/>')
    d.text(x + width / 2, y + board_h - 9, "USB", size=10, weight="600")
    # boutons EN (à gauche du port USB) et BOOT (à droite), comme sur la carte
    for bx, name in ((x + 22, "EN"), (x + width - 44, "BOOT")):
        d.add(f'<rect x="{fmt(bx)}" y="{fmt(y + board_h - 46)}" width="22" height="18" rx="3" fill="{PAPER}" stroke="{INK}" stroke-width="1.5"/>')
        d.add(f'<circle cx="{fmt(bx + 11)}" cy="{fmt(y + board_h - 37)}" r="5" fill="none" stroke="{INK}" stroke-width="1.5"/>')
        d.text(bx + 11, y + board_h - 52, name, size=9, weight="600")
    for side, pins in (("left", LEFT_PINS), ("right", RIGHT_PINS)):
        for i, (label, kind) in enumerate(pins):
            py = y + 18 + i * PIN_H
            bx = x - 11 if side == "left" else x + width - 11
            pin_box(d, bx, py, kind, marks)
            tx, anchor = (bx - 6, "end") if side == "left" else (bx + 28, "start")
            d.text(tx, py + 14, label, anchor=anchor, size=11, weight="600" if kind != "pwr" else "700")
            if label in zones:
                zx = bx - 62 if side == "left" else bx - 2
                d.zone(zones[label], zx, py - 3, 88, 24)
    return board_h


def legend(d, x, y):
    d.text(x, y, "Légende", anchor="start", size=12, weight="700")
    for i, (kind, text) in enumerate((("flash", "Flash : ne pas utiliser"), ("in", "Entrée seule"),
                                      ("strap", "Strapping : prudence"), ("ok", "Broche sûre"), ("pwr", "Alimentation"))):
        pin_box(d, x, y + 12 + i * 26, kind)
        d.text(x + 30, y + 26 + i * 26, text, anchor="start", size=12)


def arrow_right(d, x1, x2, y, label=None):
    d.arrow((x1, y), (x2, y), label=label, color=INK)


# --- M1 L'ESP32 et sa carte ------------------------------------------------------------------------------------------


def m1_composants():
    d = Drawing(560, 250, "Les composants connus autour de l'ESP32 : résistance, condensateur, diode et MOSFET l'interfacent, le protègent et commandent la puissance")
    block(d, 220, 85, 120, 80, "ESP32", size=15)
    items = [((30, 25), "Résistance", "limite le courant, fixe un état"), ((330, 25), "Condensateur", "filtre l'alimentation 3,3 V"),
             ((30, 185), "Diode", "protège, roue libre"), ((330, 185), "MOSFET", "commande 12 V")]
    for (bx, by), name, role in items:
        block(d, bx + 20, by, 160, 40, name, size=12)
        d.text(bx + 100, by + 58 if by > 100 else by - 8, role, size=11, color=SOFT)
        d.wire((bx + 100, by + 40) if by < 100 else (bx + 100, by), (280, 125), color=SOFT, width=1.5)
    return d


def m1_chaine():
    d = Drawing(560, 170, "Chaîne d'un système à microcontrôleur : un capteur est lu, le programme calcule, un actionneur est commandé")
    block(d, 20, 50, 140, 60, "Capteur", size=13)
    block(d, 210, 50, 140, 60, "ESP32", size=14)
    block(d, 400, 50, 140, 60, "Actionneur", size=13)
    arrow_right(d, 160, 208, 80)
    d.text(184, 40, "lire", size=12, weight="600")
    arrow_right(d, 350, 398, 80)
    d.text(374, 40, "commander", size=12, weight="600")
    d.text(280, 135, "calculer", size=12, weight="600", color=ACCENT)
    d.text(90, 135, "bouton, potentiomètre", size=11, color=SOFT)
    d.text(470, 135, "LED, moteur, relais", size=11, color=SOFT)
    return d


def m1_architecture():
    d = Drawing(560, 300, "Architecture du module ESP32-WROOM-32 : processeur double cœur, mémoires, périphériques, radio et gestion d'énergie")
    d.add(f'<rect x="20" y="20" width="520" height="260" rx="12" fill="{PAPER}" stroke="{INK}" stroke-width="2" stroke-dasharray="6 4"/>')
    d.text(280, 42, "module ESP32-WROOM-32", size=12, color=SOFT)
    block(d, 40, 60, 150, 70, "CPU", size=14)
    d.text(115, 150, "2 cœurs Xtensa LX6", size=11); d.text(115, 165, "jusqu'à 240 MHz", size=11, color=SOFT)
    for i, label in enumerate(("Flash 4 Mo", "SRAM 520 Ko", "ROM 448 Ko")):
        block(d, 230, 60 + i * 50, 140, 38, label, size=12)
    block(d, 400, 60, 120, 70, "Wi-Fi", size=13)
    d.text(460, 150, "Wi-Fi 2,4 GHz, Bluetooth", size=11)
    block(d, 40, 200, 300, 60, "Périphériques", size=13)
    d.text(190, 248, "GPIO, ADC, DAC, MLI, Touch", size=10, color=SOFT)
    block(d, 370, 200, 150, 60, "Gestion d'énergie", size=12)
    d.wire((190, 95), (228, 95), width=2); d.wire((60, 130), (60, 198), width=2)
    return d


def m1_memoires():
    d = Drawing(560, 210, "Les trois mémoires : la Flash garde le programme sans courant, la SRAM porte les variables et s'efface à la coupure, la ROM contient le démarrage")
    rows = (("Flash 4 Mo", "programme (garde sans courant)", 400), ("SRAM 520 Ko", "variables (effacée à la coupure)", 52),
            ("ROM 448 Ko", "démarrage (gravée en usine)", 45))
    for i, (name, role, length) in enumerate(rows):
        y = 30 + i * 58
        d.text(130, y + 22, name, anchor="end", size=12, weight="600")
        d.add(f'<rect x="140" y="{y}" width="{length}" height="30" rx="4" fill="{ACCENT if i == 0 else "#c9d8dd"}" stroke="{INK}" stroke-width="1.5"/>')
        d.text(150 + (length if i else 0), y + (50 if i == 0 else 20), role, anchor="start", size=11, color=SOFT if i else INK)
    return d


def m1_carte():
    d = Drawing(620, 330, "Carte ESP32-DevKitC V4 vue de dessus : module ESP32-WROOM-32 et son antenne en haut, régulateur 3,3 V, pont USB-série, LED rouge d'alimentation, port micro-USB entre les boutons EN et BOOT, 19 broches de chaque côté")
    x0, x1, y0, y1 = 210, 410, 15, 315
    d.add(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" rx="10" fill="#eef4f3" stroke="{INK}" stroke-width="2"/>')
    for i in range(19):  # les deux rangées de 19 broches
        for px in (x0 + 12, x1 - 12):
            d.add(f'<circle cx="{px}" cy="{fmt(y0 + 22 + i * 15)}" r="3.5" fill="{PAPER}" stroke="{INK}" stroke-width="1.5"/>')
    d.add(f'<rect x="250" y="25" width="120" height="125" rx="4" fill="#c9d8dd" stroke="{INK}" stroke-width="1.5"/>')
    d.add(f'<rect x="250" y="25" width="120" height="24" fill="{PAPER}" stroke="{INK}" stroke-width="1.5" stroke-dasharray="4 3"/>')
    d.text(310, 100, "ESP32", size=13, weight="700")
    block(d, 240, 175, 50, 36, "3,3 V", size=10)
    block(d, 300, 200, 55, 50, "série", size=10)
    d.add(f'<circle cx="378" cy="180" r="6" fill="{PAPER}" stroke="{ACCENT}" stroke-width="2.5"/>')
    d.add(f'<rect x="290" y="285" width="40" height="24" rx="3" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>')
    for bx in (232, 368):
        d.add(f'<rect x="{bx}" y="275" width="22" height="22" rx="3" fill="{PAPER}" stroke="{ACCENT}" stroke-width="2"/>')
        d.add(f'<circle cx="{bx + 11}" cy="286" r="5" fill="none" stroke="{ACCENT}" stroke-width="1.5"/>')
    # légendes à gauche et à droite, reliées à leur pièce
    left = ((37, (250, 37), "antenne (vers le bord)"), (95, (250, 95), "Module ESP32-WROOM-32"),
            (193, (240, 193), "Régulateur 3,3 V (AMS1117)"), (286, (232, 286), "bouton EN (redémarrage)"))
    right = ((120, (378, 174), "LED rouge : carte sous tension"), (225, (355, 225), "Pont USB-série (CP2102 ou CH340)"),
             (286, (390, 286), "bouton BOOT (téléversement)"), (318, (330, 300), "Port micro-USB"))
    for ty, target, label in left:
        d.wire((200, ty), (target[0] - 2, target[1]), color=SOFT, width=1.2)
        d.text(196, ty + 4, label, anchor="end", size=11, weight="600")
    for ty, target, label in right:
        d.wire((420, ty), (target[0] + 2, target[1]), color=SOFT, width=1.2)
        d.text(424, ty + 4, label, anchor="start", size=11, weight="600")
    return d


def m1_bloc():
    d = Drawing(640, 330, "Schéma bloc fonctionnel : le CPU écrit dans les registres GPIO et les périphériques par le bus interne ; la matrice GPIO et l'IO MUX aiguillent chaque signal vers un plot d'entrée-sortie, relié à une broche du module puis à une broche de la carte")
    d.add(f'<rect x="20" y="20" width="510" height="285" rx="12" fill="{PAPER}" stroke="{INK}" stroke-width="2" stroke-dasharray="6 4"/>')
    d.text(120, 296, "puce ESP32", size=11, color=SOFT)
    block(d, 35, 120, 115, 60, "CPU", size=14)
    d.text(92, 198, "2 cœurs, 240 MHz", size=10, color=SOFT)
    d.wire((172, 45), (172, 275), width=5)
    d.text(172, 38, "bus interne", size=10, color=SOFT)
    d.wire((150, 150), (170, 150), width=2)
    block(d, 195, 55, 125, 60, "Registres GPIO", size=11)
    d.text(257, 132, "ENABLE, OUT, IN", size=10, color=SOFT)
    block(d, 195, 175, 125, 70, "Périphériques", size=11)
    d.text(257, 262, "UART, I2C, SPI, LEDC", size=10, color=SOFT)
    d.wire((174, 85), (193, 85), width=2)
    d.wire((174, 210), (193, 210), width=2)
    d.add(f'<rect x="345" y="45" width="70" height="230" rx="6" fill="#dfe8ea" stroke="{INK}" stroke-width="2"/>')
    for k, word in enumerate(("matrice", "GPIO", "et", "IO MUX")):
        d.text(380, 140 + k * 16, word, size=11, weight="600")
    d.arrow((320, 85), (343, 85), color=INK)
    d.arrow((320, 210), (343, 210), color=INK)
    for k, (y, pin, board) in enumerate(((75, "GPIO 4", "G4"), (160, "GPIO 25", "G25"), (245, "GPIO 34", "G34"))):
        d.wire((415, y), (438, y), width=2)
        block(d, 438, y - 18, 80, 36, "plot", size=11)
        d.text(478, y + 32, pin, size=10, color=SOFT)
        d.wire((518, y), (568, y), color=ACCENT if k == 1 else INK, width=2.5)
        d.add(f'<rect x="525" y="{y - 5}" width="10" height="10" fill="{INK}"/>')
        node(d, 573, y, board, anchor="start")
    d.text(598, 300, "broches", size=10, color=SOFT)
    d.text(598, 314, "de la carte", size=10, color=SOFT)
    return d


def m1_cablage():
    d = Drawing(560, 300, "Câblage du premier programme : GPIO 25 (G25), résistance de 330 Ω, anode de la LED, cathode vers la broche GND de la carte")
    d.add(f'<rect x="330" y="20" width="200" height="262" rx="10" fill="#eef4f3" stroke="{INK}" stroke-width="2"/>')
    d.text(440, 272, "ESP32-DevKitC V4", size=10, color=SOFT)
    rows = ("G33", "G25", "G26", "G27", "G14", "G12", "GND", "G13")
    for i, label in enumerate(rows):
        py = 32 + i * 28
        used = label in ("G25", "GND")
        d.add(f'<rect x="319" y="{py}" width="22" height="18" rx="3" fill="{"#d7ecea" if used else PAPER}" '
              f'stroke="{ACCENT if used else INK}" stroke-width="{2.5 if used else 1.5}"/>')
        d.text(350, py + 14, label, anchor="start", size=11, weight="700" if used else "400", color=INK if used else SOFT)
    y_pin, y_gnd = 32 + 28 + 9, 32 + 6 * 28 + 9
    d.wire((319, y_pin), (270, y_pin))
    d.resistor((270, y_pin), (190, y_pin), "R", "330 Ω")
    d.diode((190, y_pin), (100, y_pin), "LED", kind="led")
    d.wire((100, y_pin), (60, y_pin), (60, y_gnd), (319, y_gnd))
    d.text(190, y_pin + 34, "anode (patte longue)", size=10, color=SOFT)
    d.text(100, y_pin + 50, "cathode (méplat)", size=10, color=SOFT)
    d.arrow((280, y_pin + 70), (130, y_pin + 70), label="≈ 3,9 mA", offset=(0, -8))
    d.text(190, y_gnd + 30, "HIGH : la LED s'allume ; LOW : elle s'éteint", size=11, weight="600", color=ACCENT)
    return d


def m1_alimentation():
    d = Drawing(560, 170, "Alimentation de la carte : le 5 V de l'USB passe par le régulateur qui fournit 3,3 V à la puce ; broches 5V et 3V3")
    block(d, 20, 55, 110, 50, "ordinateur", size=12)
    block(d, 210, 55, 120, 50, "Régulateur 3,3 V", size=11)
    block(d, 420, 55, 120, 50, "puce", size=13)
    arrow_right(d, 130, 208, 80, "USB 5 V")
    arrow_right(d, 330, 418, 80, "3,3 V")
    d.dot((170, 80)); d.wire((170, 80), (170, 130)); d.text(170, 150, "broche 5V", size=11, weight="600")
    d.dot((375, 80)); d.wire((375, 80), (375, 130)); d.text(375, 150, "broche 3V3", size=11, weight="600")
    return d


def m1_brochage():
    d = Drawing(560, 560, "Brochage de la carte DevKit 38 broches : broches de la Flash, entrées seules, broches de strapping, broches sûres et alimentation")
    devkit(d, 190, 30)
    legend(d, 400, 400)
    return d


def m1_categories():
    d = Drawing(560, 260, "Les quatre catégories de broches et leur règle d'usage")
    rows = (("flash", "Flash : ne pas utiliser", "GPIO 6 à 11 : reliées à la mémoire Flash"),
            ("in", "Entrée seule", "GPIO 34, 35, 36, 39 : ni sortie, ni tirage interne"),
            ("strap", "Strapping : prudence", "GPIO 0, 2, 5, 12, 15 : lues au démarrage"),
            ("ok", "Broche sûre", "les autres : LED, bouton, MOSFET"))
    for i, (kind, name, rule) in enumerate(rows):
        y = 30 + i * 55
        pin_box(d, 30, y, kind)
        d.text(65, y + 14, name, anchor="start", size=13, weight="700")
        d.text(65, y + 34, rule, anchor="start", size=12, color=SOFT)
    return d


def m1_regle_tension():
    d = Drawing(560, 200, "Règle des 3,3 V : un signal de 5 V passe par un pont diviseur avant d'atteindre une broche")
    block(d, 20, 60, 120, 50, "Capteur 5 V", size=12)
    d.wire((140, 85), (190, 85))
    d.resistor((190, 85), (290, 85), "R1", "1 kΩ")
    d.wire((290, 85), (420, 85)); d.dot((320, 85))
    d.resistor((320, 85), (320, 165), "R2", "2 kΩ")
    d.ground((320, 165))
    block(d, 420, 60, 120, 50, "vers GPIO 34", size=12)
    d.text(370, 75, "3,33 V", size=12, weight="700", color=ACCENT)
    d.text(280, 30, "jamais 5 V sur une broche", size=12, weight="600", color=ACCENT)
    return d


def m1_masse_commune():
    d = Drawing(560, 210, "Masse commune : l'ESP32 sur USB et la charge sur batterie 12 V ont leurs GND reliés")
    block(d, 30, 40, 130, 50, "USB 5 V", size=12)
    block(d, 210, 40, 130, 50, "ESP32", size=14)
    block(d, 400, 40, 130, 50, "batterie 12 V", size=12)
    block(d, 400, 120, 130, 40, "moteur", size=12)
    d.wire((160, 65), (208, 65))
    d.wire((95, 90), (95, 185), (465, 185), (465, 160), color=ACCENT, width=3)
    d.wire((275, 90), (275, 185), color=ACCENT, width=3)
    d.wire((465, 90), (465, 120))
    d.text(280, 203, "masse commune", size=12, weight="700", color=ACCENT)
    return d


def m1_courant_broche():
    d = Drawing(560, 190, "Une broche ne fournit que quelques milliampères : au plus 12 mA environ par LED, un MOSFET au-delà")
    block(d, 20, 60, 110, 50, "GPIO", size=13)
    d.wire((130, 85), (170, 85))
    d.resistor((170, 85), (270, 85), "R", "330 Ω")
    d.diode((270, 85), (350, 85), "LED", None, kind="led")
    d.wire((350, 85), (390, 85)); d.ground((390, 85))
    d.arrow((180, 120), (330, 120), label="au plus 12 mA environ", offset=(0, 22))
    return d


def m1_outils():
    d = Drawing(560, 190, "La chaîne d'outils : VS Code et PlatformIO compilent, téléversent par USB, puis le moniteur série dialogue avec la carte")
    block(d, 20, 40, 150, 60, "VS Code + PlatformIO", size=11)
    block(d, 380, 40, 160, 60, "carte ESP32", size=13)
    d.arrow((170, 60), (378, 60), label="téléverser", color=INK)
    d.arrow((378, 85), (170, 85), label="moniteur série", color=ACCENT, offset=(0, 22))
    d.text(95, 130, "compiler", size=12, weight="600")
    d.text(275, 160, "câble USB", size=11, color=SOFT)
    return d


def m1_projet():
    d = Drawing(560, 210, "Structure d'un projet PlatformIO : platformio.ini, src/main.cpp, include et lib")
    rows = (("mon-projet/", "", 0), ("platformio.ini", "réglages du projet", 1), ("src/main.cpp", "votre programme", 1),
            ("include/", "vos en-têtes (.h)", 1), ("lib/", "vos bibliothèques", 1))
    for i, (name, role, level) in enumerate(rows):
        y = 40 + i * 34
        x = 40 + level * 30
        if level:
            d.wire((50, y - 22), (50, y - 5), (x - 4, y - 5), color=SOFT, width=1.5)
        d.text(x, y, name, anchor="start", size=13, weight="700" if i in (0, 2) else "600", color=ACCENT if i == 2 else INK)
        d.text(260, y, role, anchor="start", size=12, color=SOFT)
    return d


def m1_setup_loop():
    d = Drawing(560, 260, "Déroulement d'un programme Arduino : setup s'exécute une seule fois à la mise sous tension, puis loop se répète sans fin")
    block(d, 200, 15, 160, 40, "mise sous tension", size=12)
    block(d, 200, 85, 160, 50, "setup()", size=14)
    block(d, 200, 175, 160, 50, "loop()", size=14)
    d.arrow((280, 55), (280, 83), color=INK); d.arrow((280, 135), (280, 173), color=INK)
    d.wire((360, 200), (420, 200), (420, 160), (370, 160), color=ACCENT, width=2.5)
    d.arrow((372, 160), (362, 190), color=ACCENT)
    d.text(380, 115, "une seule fois", anchor="start", size=11, color=SOFT)
    d.text(430, 185, "sans fin", anchor="start", size=12, weight="600", color=ACCENT)
    d.text(30, 115, "réglages : broches, série", anchor="start", size=11)
    d.text(30, 205, "lire, calculer, commander", anchor="start", size=11)
    d.text(280, 250, "le programme ne s'arrête jamais", size=11, color=SOFT)
    return d


def m1_televersement():
    d = Drawing(560, 200, "Les trois étapes du téléversement : compilation, écriture dans la Flash, redémarrage")
    for i, (name, detail) in enumerate((("Compilation", "PlatformIO traduit le C++ en code machine"),
                                        ("Téléversement", "le code est écrit dans la Flash"),
                                        ("Redémarrage", "le programme démarre : setup puis loop"))):
        x = 20 + i * 180
        block(d, x, 40, 160, 50, f"{i + 1}. {name}", size=12)
        d.text(x + 80, 120, detail, size=10, color=SOFT)
        if i < 2:
            arrow_right(d, x + 160, x + 178, 65)
    return d


def m1_identite():
    d = Drawing(560, 180, "Montage du mini-projet : la carte reliée à l'ordinateur par USB affiche sa carte d'identité dans le moniteur série")
    block(d, 20, 50, 150, 60, "ordinateur", size=13)
    block(d, 380, 50, 160, 60, "carte ESP32", size=13)
    d.wire((170, 80), (378, 80), width=3); d.text(275, 70, "câble USB", size=11, color=SOFT)
    d.text(95, 140, "Moniteur série à 115 200 bit/s", size=11, weight="600", color=ACCENT)
    d.text(460, 140, "LED sur GPIO 25", size=11)
    d.text(95, 160, "Modèle, cœurs, fréquence, Flash", size=10, color=SOFT)
    return d


def q_m1_flash():
    d = Drawing(420, 560, "Carte DevKit 38 broches sans légende")
    devkit(d, 135, 30, marks=False, zones={"SD2 9": "flash", "34": "entree", "12": "strapping", "25": "sure", "4": "sure-droite"})
    return d


def nmos(d, x, y, label="Q1"):
    """MOSFET canal N à enrichissement (CEI) : grille à (x, y), drain en (x + 40, y - 40), source en (x + 40, y + 40)."""
    d.wire((x, y), (x + 22, y)); d.wire((x + 22, y - 18), (x + 22, y + 18), width=2.5)
    for k in (-14, 0, 14):
        d.wire((x + 30, y + k - 6), (x + 30, y + k + 6), width=2.5)
    d.wire((x + 30, y - 14), (x + 40, y - 14), (x + 40, y - 40)); d.wire((x + 30, y + 14), (x + 40, y + 14), (x + 40, y + 40))
    d.wire((x + 40, y + 14), (x + 40, y)); d.arrow((x + 40, y), (x + 31, y), color=INK)
    d.text(x + 50, y + 5, label, anchor="start", size=12, weight="600")
    return (x, y), (x + 40, y - 40), (x + 40, y + 40)


def led_branch(d, x, y_top, y_bottom, label=None, value=None):
    """Résistance puis LED, de haut en bas."""
    mid = (y_top + y_bottom) / 2
    d.resistor((x, y_top), (x, mid), label, value)
    d.diode((x, mid), (x, y_bottom), "LED", kind="led", side=-1)


def node(d, x, y, label, anchor="end"):
    d.add(f'<circle cx="{fmt(x)}" cy="{fmt(y)}" r="5" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>')
    d.text(x - 12 if anchor == "end" else x + 12, y + 5, label, anchor=anchor, weight="600")


# --- M2 Sorties numériques -------------------------------------------------------------------------------------------


def m2_niveaux():
    d = Drawing(520, 200, "Une sortie numérique ne connaît que deux niveaux : 3,3 V pour le niveau haut, 0 V pour le niveau bas")
    d.wire((70, 150), (150, 150), (150, 60), (280, 60), (280, 150), (360, 150), (360, 60), (460, 60), color=ACCENT, width=3)
    d.wire((60, 160), (480, 160), color=SOFT, width=1)
    d.text(60, 64, "3,3 V", anchor="end", size=12, weight="600"); d.text(60, 154, "0 V", anchor="end", size=12, weight="600")
    d.text(215, 48, "niveau haut (1)", size=12); d.text(110, 182, "niveau bas (0)", size=12)
    return d


def m2_sortie_interne():
    d = Drawing(520, 240, "Dans la puce, une sortie relie la broche soit au 3,3 V, soit à GND, par deux interrupteurs dont un seul est fermé")
    d.text(200, 28, "3,3 V", weight="600"); d.wire((200, 35), (200, 60))
    d.switch((200, 60), (200, 110), "HIGH : vers 3,3 V", closed=True, side=-1)
    d.wire((200, 110), (200, 130)); d.dot((200, 120)); d.wire((200, 120), (379, 120))
    node(d, 384, 120, "broche", anchor="start")
    d.switch((200, 130), (200, 180), "LOW : vers GND", closed=False, side=-1)
    d.wire((200, 180), (200, 195)); d.ground((200, 195))
    d.text(380, 220, "un seul des deux interrupteurs est fermé", size=11, color=SOFT)
    return d


def m2_led_montage():
    d = Drawing(480, 260, "Montage d'une LED sur une sortie : la broche, la résistance de limitation, la LED, puis la masse")
    node(d, 120, 40, "GPIO 25")
    d.wire((120, 45), (120, 60)); led_branch(d, 120, 60, 200, "R", "330 Ω"); d.wire((120, 200), (120, 215)); d.ground((120, 215))
    d.arrow((260, 70), (260, 190), label="3,94 mA", offset=(46, 0))
    return d


def m2_led_calcul():
    d = Drawing(520, 190, "Partage de la tension : sur 3,3 V, la LED rouge garde 2,0 V et la résistance reçoit le reste, 1,3 V")
    d.add(f'<rect x="60" y="60" width="160" height="40" fill="#c9d8dd" stroke="{INK}" stroke-width="1.5"/>')
    d.add(f'<rect x="220" y="60" width="246" height="40" fill="{ACCENT}" stroke="{INK}" stroke-width="1.5"/>')
    d.text(140, 85, "1,3 V", weight="700"); d.text(343, 85, "2,0 V", weight="700", color=PAPER)
    d.text(140, 125, "aux bornes de R", size=11); d.text(343, 125, "aux bornes de la LED", size=11)
    d.text(263, 40, "3,3 V", weight="700")
    d.text(263, 165, "R = 1,3 V / 4 mA ≈ 325 Ω, on choisit 330 Ω", size=12, color=SOFT)
    return d


def m2_source():
    d = Drawing(340, 260, "Logique directe (source) : la LED va de la broche à la masse ; HIGH l'allume, le courant sort de la broche")
    d.text(90, 30, "GPIO", weight="600"); d.wire((90, 38), (90, 60))
    led_branch(d, 90, 60, 200, "R"); d.wire((90, 200), (90, 215)); d.ground((90, 215))
    d.text(240, 110, "source : HIGH allume", size=12, weight="600", color=ACCENT)
    d.text(240, 135, "le courant sort de la broche", size=11, color=SOFT)
    return d


def m2_puits():
    d = Drawing(340, 260, "Logique inversée (puits) : la LED va du 3,3 V à la broche ; LOW l'allume, le courant entre dans la broche")
    d.text(90, 30, "3,3 V", weight="600"); d.wire((90, 38), (90, 60))
    led_branch(d, 90, 60, 200, "R"); d.wire((90, 200), (90, 220)); d.text(90, 240, "GPIO", weight="600")
    d.text(240, 110, "puits : LOW allume", size=12, weight="600", color=ACCENT)
    d.text(240, 135, "le courant entre dans la broche", size=11, color=SOFT)
    return d


def m2_blink():
    d = Drawing(560, 150, "Chronogramme du clignotement : 500 ms allumée, 500 ms éteinte, une période de 1 s")
    timing(d, 110, 20, 400, [("GPIO 25", [(0, 5), (10, 15)])], span=20, marks=((5, "500"), (10, "1000"), (15, "1500")))
    d.text(310, 135, "temps (ms)", size=11, color=SOFT)
    return d


def m2_blink_montage():
    d = Drawing(480, 230, "Montage du clignotant : une LED et sa résistance de 330 Ω sur GPIO 25")
    block(d, 30, 60, 120, 100, "ESP32", size=14)
    d.wire((150, 80), (260, 80)); d.text(205, 72, "GPIO 25", size=11, weight="600")
    led_branch(d, 260, 80, 180, "R", "330 Ω"); d.wire((260, 180), (260, 200), (90, 200), (90, 160))
    d.text(175, 220, "GND", size=11, weight="600")
    return d


def m2_trois_niveaux():
    d = Drawing(560, 230, "Trois façons d'écrire sur une broche, du plus simple au plus proche du matériel : Arduino, ESP-IDF, registre")
    for i, label in enumerate(("Arduino : digitalWrite", "ESP-IDF : gpio_set_level", "registre GPIO_OUT_W1TS")):
        block(d, 40 + i * 30, 30 + i * 60, 300, 44, label, size=12)
    d.arrow((410, 40), (410, 190), color=SOFT)
    d.text(420, 44, "plus simple", anchor="start", size=11); d.text(420, 194, "plus proche du matériel", anchor="start", size=11)
    return d


def m2_broche_interne():
    d = Drawing(660, 320, "Structure d'une broche dans la puce : GPIO_ENABLE autorise la sortie, GPIO_OUT ferme l'interrupteur vers 3,3 V ou vers GND, deux résistances de tirage d'environ 45 kΩ se branchent par programme, le tampon d'entrée recopie le niveau dans GPIO_IN")
    d.add(f'<rect x="10" y="10" width="520" height="290" rx="12" fill="{PAPER}" stroke="{INK}" stroke-width="2" stroke-dasharray="6 4"/>')
    d.text(80, 292, "dans la puce", size=11, color=SOFT)
    block(d, 20, 38, 150, 36, "GPIO_ENABLE : bit 25", size=10)
    block(d, 20, 102, 150, 36, "GPIO_OUT : bit 25", size=10)
    block(d, 20, 232, 150, 36, "GPIO_IN : bit 25", size=10)
    d.arrow((170, 56), (300, 56), label="1 = sortie", color=INK)
    d.arrow((170, 120), (300, 120), label="1 = HIGH, 0 = LOW", color=INK)
    # étage de sortie : deux interrupteurs, jamais fermés ensemble
    d.text(330, 26, "3,3 V", size=12, weight="600"); d.wire((330, 32), (330, 66))
    d.switch((330, 66), (330, 102), "P", closed=True, side=-1)
    d.wire((330, 102), (330, 138)); d.dot((330, 120))
    d.switch((330, 138), (330, 174), "N", closed=False, side=-1)
    d.wire((330, 174), (330, 186)); d.ground((330, 186))
    d.wire((330, 120), (555, 120))
    node(d, 560, 120, "GPIO 25", anchor="start")
    # tirages internes, branchés par programme
    d.text(440, 26, "3,3 V", size=12, weight="600"); d.wire((440, 32), (440, 36))
    d.resistor((440, 36), (440, 82), "≈ 45 kΩ")
    d.switch((440, 82), (440, 118), "pull-up")
    d.dot((440, 120))
    d.switch((440, 122), (440, 158), "pull-down")
    d.resistor((440, 158), (440, 204), "≈ 45 kΩ")
    d.ground((440, 204))
    d.text(455, 232, "IO_MUX : FUN_WPU, FUN_WPD", size=9, color=SOFT)
    # tampon d'entrée
    d.dot((375, 120)); d.wire((375, 120), (375, 250), (342, 250))
    d.add(f'<polygon points="342,236 342,264 314,250" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>')
    d.arrow((314, 250), (172, 250), color=INK)
    d.text(330, 285, "tampon d'entrée : compare aux seuils", size=10, color=SOFT)
    return d


def m2_registres():
    d = Drawing(620, 330, "Les registres d'une broche : GPIO_ENABLE choisit la direction, GPIO_OUT le niveau écrit, W1TS et W1TC changent un bit sans toucher aux autres, GPIO_IN donne le niveau lu ; chacun a son adresse en mémoire")
    rows = (("GPIO_ENABLE_REG", "0x3FF44020", "1 = sortie", "1"), ("GPIO_OUT_REG", "0x3FF44004", "niveau écrit", "1"),
            ("GPIO_OUT_W1TS_REG", "0x3FF44008", "1 = mettre à 1", "1"), ("GPIO_OUT_W1TC_REG", "0x3FF4400C", "1 = mettre à 0", "0"),
            ("GPIO_IN_REG", "0x3FF4403C", "niveau lu", "1"))
    bits = (28, 27, 26, 25, 24, 23, 22)
    for k, b in enumerate(bits):
        d.text(232 + k * 30, 28, str(b), size=10, color=SOFT)
    d.text(196, 28, "bit", size=10, color=SOFT)
    for i, (name, address, role, value) in enumerate(rows):
        y = 40 + i * 52
        d.text(170, y + 16, name, anchor="end", size=11, weight="700")
        d.text(170, y + 32, address, anchor="end", size=10, color=SOFT)
        d.text(206, y + 22, "…", size=13, color=SOFT)
        for k, b in enumerate(bits):
            x = 218 + k * 30
            hot = b == 25
            d.add(f'<rect x="{x}" y="{y}" width="28" height="34" fill="{ACCENT if hot else PAPER}" stroke="{INK}" stroke-width="1.5"/>')
            d.text(x + 14, y + 23, value if hot else "0", size=13, weight="700", color=PAPER if hot else INK)
        d.text(440, y + 22, "…", size=13, color=SOFT)
        d.text(460, y + 22, role, anchor="start", size=11)
    d.text(310, 318, "un bit par broche : le bit 25 commande GPIO 25", size=12, weight="600", color=ACCENT)
    return d


def m2_mosfet():
    d = Drawing(560, 300, "Commander un moteur 12 V : GPIO 26, résistance de grille 220 Ω, rappel 10 kΩ, MOSFET, diode de roue libre, masse commune")
    d.text(360, 24, "+12 V", weight="600"); d.wire((360, 30), (360, 63))
    d.add(f'<circle cx="360" cy="85" r="22" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>'); d.text(360, 90, "M", weight="700")
    d.wire((360, 107), (360, 130))
    d.diode((440, 130), (440, 50)); d.wire((440, 50), (360, 50)); d.wire((440, 130), (360, 130))
    d.text(452, 95, "roue libre", anchor="start", size=11, color=ACCENT, weight="600")
    gate, drain, source = nmos(d, 320, 170)
    d.wire(drain, (360, 130))
    d.wire(source, (360, 240)); d.ground((360, 240))
    node(d, 120, 170, "GPIO 26"); d.wire((125, 170), (150, 170))
    d.resistor((150, 170), (250, 170), "220 Ω")
    d.wire((250, 170), gate); d.dot((280, 170)); d.resistor((280, 170), (280, 240), "10 kΩ", side=-1); d.ground((280, 240))
    d.text(280, 288, "rappel 10 kΩ : MOSFET bloqué pendant le démarrage ; masse commune", size=11, color=SOFT)
    return d


def m2_mosfet_etats():
    d = Drawing(560, 170, "Le MOSFET en commutation : grille à 0 V, il est bloqué ; grille à 3,3 V, il est passant")
    block(d, 20, 40, 255, 50, "GPIO LOW : MOSFET bloqué, moteur arrêté", size=11)
    block(d, 285, 40, 255, 50, "GPIO HIGH : MOSFET passant, moteur en marche", size=11)
    d.text(280, 130, "MOSFET logic-level : passant dès 3,3 V sur la grille", size=11, color=SOFT)
    return d


def m2_feu():
    d = Drawing(560, 270, "Le feu tricolore : trois LED avec leur résistance sur GPIO 25, 26 et 27")
    block(d, 30, 60, 120, 140, "ESP32", size=14)
    for i, (pin, color) in enumerate((("25", "vert"), ("26", "orange"), ("27", "rouge"))):
        x = 280 + i * 100
        y = 80 + i * 30
        d.wire((150, y), (x - 30, y), (x - 30, 50), (x, 50), (x, 60))
        d.text(165, y - 6, pin, anchor="start", size=10, weight="600")
        led_branch(d, x, 60, 200)
        d.wire((x, 200), (x, 225))
        d.text(x + 30, 40, color, size=12, weight="600")
    d.wire((280, 225), (480, 225)); d.wire((90, 200), (90, 225), (280, 225)); d.text(380, 250, "GND", size=11, weight="600")
    return d


def m2_feu_chrono():
    d = Drawing(560, 200, "Cycle du feu : vert 5 s, orange 2 s, rouge 5 s, puis le cycle recommence")
    timing(d, 110, 0, 400, [("vert", [(0, 5)]), ("orange", [(5, 7)]), ("rouge", [(7, 12)])], span=12,
           marks=((5, "5"), (7, "7"), (12, "12")))
    d.text(310, 192, "temps (s)", size=11, color=SOFT)
    return d


def m2_carrefour():
    d = Drawing(560, 230, "Montage du mini-projet : le feu tricolore sur GPIO 25 à 27 et une lampe 12 V commandée par MOSFET sur GPIO 32")
    block(d, 30, 60, 120, 110, "ESP32", size=14)
    block(d, 230, 30, 140, 60, "feu tricolore", size=12)
    block(d, 230, 130, 140, 60, "MOSFET", size=12)
    block(d, 420, 130, 110, 60, "lampe 12 V", size=12)
    arrow_right(d, 150, 228, 60, "25, 26, 27"); arrow_right(d, 150, 228, 160, "GPIO 32"); d.wire((370, 160), (420, 160))
    d.text(280, 215, "masse commune", size=11, weight="600", color=ACCENT)
    return d


def q_m2_puits():
    d = Drawing(600, 260, "Trois montages de LED sans légende")
    for i, (top, bottom, name) in enumerate((("GPIO", "GND", "source"), ("3,3 V", "GPIO", "puits"), ("3,3 V", "GND", "fixe"))):
        x = 100 + i * 200
        d.text(x, 30, top, weight="600"); d.wire((x, 38), (x, 60))
        led_branch(d, x, 60, 200); d.wire((x, 200), (x, 220)); d.text(x, 240, bottom, weight="600")
        d.zone(name, x - 70, 15, 140, 235)
    return d


def button(d, x, y1, y2, label="S1"):
    """Bouton-poussoir à fermeture, vertical, de (x, y1) à (x, y2)."""
    mid = (y1 + y2) / 2
    d.wire((x, y1), (x, mid - 14)); d.wire((x, mid + 14), (x, y2))
    d.add(f'<circle cx="{fmt(x)}" cy="{fmt(mid - 14)}" r="2.5" fill="{INK}"/><circle cx="{fmt(x)}" cy="{fmt(mid + 14)}" r="2.5" fill="{INK}"/>')
    d.wire((x - 9, mid - 16), (x - 9, mid + 16), width=2.5); d.wire((x - 9, mid), (x - 26, mid)); d.wire((x - 26, mid - 6), (x - 26, mid + 6))
    d.text(x + 14, mid + 5, label, anchor="start", weight="600")


def state(d, x, y, label, accent=False):
    d.add(f'<ellipse cx="{fmt(x)}" cy="{fmt(y)}" rx="58" ry="24" fill="{"#d7ecea" if accent else "#eef4f3"}" stroke="{ACCENT if accent else INK}" stroke-width="2"/>')
    d.text(x, y + 5, label, size=12, weight="700")


# --- M3 Entrées numériques -------------------------------------------------------------------------------------------


def m3_flottant():
    d = Drawing(480, 240, "Une entrée reliée à un bouton seul flotte quand le bouton est relâché : son niveau est inconnu")
    d.text(120, 30, "3,3 V", weight="600"); d.wire((120, 38), (120, 60))
    button(d, 120, 60, 140)
    d.wire((120, 140), (120, 170)); node(d, 120, 175, "GPIO 4")
    d.text(330, 170, "?", size=34, weight="700", color=ACCENT)
    d.text(330, 215, "niveau inconnu : la broche flotte", size=12, color=SOFT)
    return d


def m3_seuils():
    d = Drawing(520, 230, "Seuils d'une entrée de l'ESP32 : au-dessus de 2,5 V environ elle lit 1, en dessous de 0,8 V environ elle lit 0, entre les deux le niveau est indéterminé")
    d.add(f'<rect x="120" y="30" width="120" height="60" fill="#d7ecea" stroke="{INK}" stroke-width="1.5"/>')
    d.add(f'<rect x="120" y="90" width="120" height="70" fill="{PAPER}" stroke="{INK}" stroke-width="1.5" stroke-dasharray="5 4"/>')
    d.add(f'<rect x="120" y="160" width="120" height="40" fill="#c9d8dd" stroke="{INK}" stroke-width="1.5"/>')
    for y, label in ((30, "3,3 V"), (90, "2,5 V"), (160, "0,8 V"), (200, "0 V")):
        d.text(110, y + 5, label, anchor="end", size=12, weight="600")
    d.text(260, 65, "lu comme 1", anchor="start", size=12, weight="600")
    d.text(260, 130, "zone indéterminée", anchor="start", size=12, color=SOFT)
    d.text(260, 185, "lu comme 0", anchor="start", size=12, weight="600")
    return d


def pull_figure(title, inside, outside, code, result):
    """Un câblage de bouton, intérieur de la puce compris : tampon d'entrée, tirages internes (interrupteurs ouverts ou
    fermés), broche au bord de la puce, puis les composants extérieurs. inside ∈ {None, "up", "down"},
    outside ∈ {"down", "up", None} (résistance externe de 10 kΩ vers GND, vers 3,3 V, ou aucune)."""
    d = Drawing(600, 320, title)
    d.add(f'<rect x="15" y="6" width="285" height="269" rx="12" fill="#eef4f3" stroke="{INK}" stroke-width="2" stroke-dasharray="6 4"/>')
    d.text(80, 266, "dans la puce", size=11, color=SOFT)
    d.text(450, 266, "hors de la puce", size=11, color=SOFT)
    block(d, 25, 130, 95, 36, "GPIO_IN", size=11)
    d.add(f'<polygon points="175,134 175,162 150,148" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>')
    d.arrow((150, 148), (122, 148), color=INK)
    d.text(162, 182, "tampon", size=10, color=SOFT)
    d.wire((175, 148), (292, 148))
    # tirages internes : on ne les branche que par programme
    up, down = inside == "up", inside == "down"
    d.text(230, 32, "3,3 V", size=12, weight="600"); d.wire((230, 38), (230, 42))
    d.resistor((230, 42), (230, 82), "≈ 45 kΩ", side=-1)
    d.switch((230, 82), (230, 118), closed=up)
    d.wire((230, 118), (230, 160)); d.dot((230, 148))
    d.switch((230, 160), (230, 196), closed=down)
    d.resistor((230, 196), (230, 236), "≈ 45 kΩ", side=-1); d.ground((230, 236))
    d.text(248, 104, "fermé" if up else "ouvert", anchor="start", size=10, weight="700" if up else "400", color=ACCENT if up else SOFT)
    d.text(248, 182, "fermé" if down else "ouvert", anchor="start", size=10, weight="700" if down else "400", color=ACCENT if down else SOFT)
    # la broche, à la frontière
    d.add(f'<rect x="292" y="140" width="16" height="16" fill="{ACCENT}" stroke="{INK}" stroke-width="1.5"/>')
    d.text(318, 136, "broche GPIO 4", anchor="start", size=11, weight="700")
    d.wire((308, 148), (440, 148)); d.dot((440, 148))
    # composants extérieurs
    if outside == "up":
        d.text(440, 32, "3,3 V", size=12, weight="600"); d.wire((440, 38), (440, 50))
        d.resistor((440, 50), (440, 120), "R", "10 kΩ"); d.wire((440, 120), (440, 148))
    button_down = outside == "up" or inside == "up"
    if button_down:
        button(d, 440, 158, 222); d.wire((440, 148), (440, 158)); d.ground((440, 222))
    else:
        d.text(440, 32, "3,3 V", size=12, weight="600"); d.wire((440, 38), (440, 60)); button(d, 440, 60, 124); d.wire((440, 124), (440, 148))
    if outside == "down":
        d.resistor((440, 148), (440, 222), "R", "10 kΩ"); d.ground((440, 222))
    d.text(450, 290, code, size=12, weight="700", color=ACCENT)
    d.text(450, 310, result, size=11, weight="600")
    return d


def m3_pull_down():
    return pull_figure("Tirage externe vers la masse (pull-down) : dans la puce, les deux tirages internes sont ouverts ; hors de la puce, une résistance de 10 kΩ relie la broche à GND et le bouton la relie au 3,3 V",
                       None, "down", "pinMode(4, INPUT)", "relâché : LOW, appuyé : HIGH")


def m3_pull_up():
    return pull_figure("Tirage externe vers 3,3 V (pull-up) : dans la puce, les deux tirages internes sont ouverts ; hors de la puce, une résistance de 10 kΩ relie la broche au 3,3 V et le bouton la relie à GND",
                       None, "up", "pinMode(4, INPUT)", "relâché : HIGH, appuyé : LOW")


def m3_pullup_interne():
    return pull_figure("Tirage interne vers 3,3 V : INPUT_PULLUP ferme l'interrupteur de la résistance d'environ 45 kΩ vers 3,3 V ; hors de la puce, seul le bouton relie la broche à GND",
                       "up", None, "pinMode(4, INPUT_PULLUP)", "relâché : HIGH, appuyé : LOW")


def m3_pulldown_interne():
    return pull_figure("Tirage interne vers la masse : INPUT_PULLDOWN ferme l'interrupteur de la résistance d'environ 45 kΩ vers GND ; hors de la puce, seul le bouton relie la broche au 3,3 V",
                       "down", None, "pinMode(4, INPUT_PULLDOWN)", "relâché : LOW, appuyé : HIGH")


def m3_lire_ecrire():
    d = Drawing(560, 180, "Structure de loop() : lire toutes les entrées, calculer, puis écrire toutes les sorties")
    for i, label in enumerate(("1. lire les entrées", "2. calculer", "3. écrire les sorties")):
        block(d, 20 + i * 180, 40, 160, 50, label, size=12)
        if i < 2:
            arrow_right(d, 180 + i * 180, 198 + i * 180, 65)
    d.wire((500, 90), (500, 130), (100, 130), (100, 92), color=ACCENT, width=2)
    d.text(300, 155, "loop() recommence", size=11, color=ACCENT, weight="600")
    return d


def m3_bouton_led():
    d = Drawing(520, 240, "Montage bouton et LED : le bouton entre GPIO 4 et GND (tirage interne), la LED et sa résistance sur GPIO 25")
    block(d, 180, 60, 140, 120, "ESP32", size=14)
    d.wire((180, 90), (100, 90)); d.text(150, 82, "GPIO 4", size=11, weight="600"); button(d, 100, 90, 170); d.ground((100, 170))
    d.wire((320, 90), (420, 90)); d.text(370, 82, "GPIO 25", size=11, weight="600"); led_branch(d, 420, 90, 190, "R", "330 Ω")
    d.wire((420, 190), (420, 200)); d.ground((420, 200))
    return d


def m3_rebonds():
    d = Drawing(560, 170, "Rebonds d'un bouton : à l'appui, le contact s'ouvre et se ferme plusieurs fois pendant quelques millisecondes avant de se stabiliser")
    pts = [(60, 50), (200, 50), (200, 110), (210, 110), (210, 50), (218, 50), (218, 110), (224, 110), (224, 55), (229, 55), (229, 110), (480, 110)]
    d.wire(*pts, color=ACCENT, width=2.5)
    d.text(50, 55, "relâché", anchor="end", size=11); d.text(50, 115, "appuyé", anchor="end", size=11)
    d.add(f'<rect x="195" y="35" width="40" height="90" fill="none" stroke="{SOFT}" stroke-dasharray="4 3"/>')
    d.text(215, 145, "rebonds", size=12, weight="600"); d.text(380, 100, "état stable", size=11, color=SOFT)
    return d


def m3_antirebond():
    d = Drawing(560, 240, "Anti-rebond logiciel : un changement n'est accepté que s'il est encore là 20 ms plus tard")
    block(d, 20, 30, 150, 44, "changement lu ?", size=12)
    block(d, 210, 30, 140, 44, "attendre 20 ms", size=12)
    block(d, 390, 30, 150, 44, "toujours changé ?", size=12)
    block(d, 390, 150, 150, 44, "accepter le nouvel état", size=11)
    arrow_right(d, 170, 208, 52, "oui"); arrow_right(d, 350, 388, 52)
    d.arrow((465, 74), (465, 148), label="oui", color=INK, offset=(18, 0))
    d.text(95, 100, "non", size=11, color=SOFT)
    return d


def m3_front():
    d = Drawing(560, 210, "Fronts : le bouton (tirage interne) passe de HIGH à LOW à l'appui (front descendant) et de LOW à HIGH au relâchement (front montant)")
    timing(d, 150, 10, 360, [("GPIO 4", [(0, 3), (6, 12)]), ("LED (bascule)", [(3, 12)])], span=12, row_h=60)
    d.text(258, 190, "front descendant : appui", size=11, weight="600", color=ACCENT)
    return d


def m3_bascule():
    d = Drawing(560, 170, "Bascule : chaque appui inverse l'état de la LED, quel que soit le temps pendant lequel le bouton reste enfoncé")
    for i, (label, on) in enumerate((("ÉTEINT", False), ("ALLUMÉ", True), ("ÉTEINT", False), ("ALLUMÉ", True))):
        state(d, 70 + i * 140, 70, label, accent=on)
        if i < 3:
            arrow_right(d, 128 + i * 140, 152 + i * 140, 70)
            d.text(140 + i * 140, 115, "appui", size=11, color=SOFT)
    return d


def m3_etats():
    d = Drawing(560, 250, "Machine à états du cycle : chaque appui fait passer à l'état suivant ; après le vert, tout s'éteint")
    pos = {"ÉTEINT": (110, 60), "ROUGE": (450, 60), "ORANGE": (450, 190), "VERT": (110, 190)}
    for name, (x, y) in pos.items():
        state(d, x, y, name, accent=name != "ÉTEINT")
    d.arrow((170, 60), (390, 60), label="appui", color=INK)
    d.arrow((450, 86), (450, 164), label="appui", color=INK, offset=(30, 0))
    d.arrow((390, 190), (170, 190), label="appui", color=INK, offset=(0, 22))
    d.arrow((110, 164), (110, 86), label="appui", color=INK, offset=(-30, 0))
    return d


def m3_veille():
    d = Drawing(560, 200, "Deux modes : un appui passe du cycle normal au mode veille, orange clignotant, et inversement")
    state(d, 140, 90, "CYCLE", accent=True); state(d, 420, 90, "VEILLE")
    d.arrow((198, 80), (362, 80), label="appui sur le bouton", color=INK)
    d.arrow((362, 100), (198, 100), label="appui sur le bouton", color=INK, offset=(0, 22))
    d.text(140, 150, "vert, orange, rouge", size=11, color=SOFT); d.text(420, 150, "orange clignotant", size=11, color=SOFT)
    return d


def m3_diviseur_entree():
    d = Drawing(560, 210, "Lire un capteur 5 V sur une entrée numérique : un pont diviseur 10 kΩ et 20 kΩ ramène le niveau haut à 3,33 V au plus")
    block(d, 20, 60, 120, 50, "capteur 5 V", size=12)
    d.wire((140, 85), (180, 85)); d.resistor((180, 85), (290, 85), "R1", "10 kΩ")
    d.wire((290, 85), (420, 85)); d.dot((330, 85)); d.resistor((330, 85), (330, 170), "R2", "20 kΩ"); d.ground((330, 170))
    node(d, 425, 85, "GPIO 4", anchor="start")
    d.text(380, 70, "3,33 V au plus", size=11, weight="600", color=ACCENT)
    return d


def m3_niveaux_5v():
    d = Drawing(520, 170, "Sans pont, 5 V détruirait l'entrée ; avec le pont, le niveau haut vaut 3,33 V et le niveau bas reste 0 V")
    for i, (label, color) in enumerate((("5 V : interdit", "#c9d8dd"), ("3,33 V : lu comme 1", "#d7ecea"), ("0 V : lu comme 0", PAPER))):
        block(d, 30 + i * 160, 50, 140, 50, label, size=11)
    d.wire((40, 120), (160, 60), color=ACCENT, width=2); d.wire((40, 60), (160, 120), color=ACCENT, width=2)
    return d


def m3_feu_bouton():
    d = Drawing(560, 230, "Montage du mini-projet : le feu tricolore sur GPIO 25, 26 et 27 et un bouton entre GPIO 4 et GND")
    block(d, 200, 60, 140, 120, "ESP32", size=14)
    d.wire((200, 100), (110, 100)); d.text(160, 92, "GPIO 4", size=11, weight="600"); button(d, 110, 100, 180); d.ground((110, 180))
    block(d, 400, 70, 140, 60, "feu tricolore", size=12); arrow_right(d, 340, 398, 100, "25, 26, 27")
    return d


def q_m3_pullup():
    d = Drawing(560, 260, "Montage d'un bouton et d'une LED sans légende")
    d.text(120, 24, "3,3 V", weight="600"); d.wire((120, 30), (120, 50))
    d.resistor((120, 50), (120, 120)); d.wire((120, 120), (120, 140)); d.dot((120, 140)); d.wire((120, 140), (260, 140))
    button(d, 120, 140, 210, ""); d.ground((120, 210))
    block(d, 260, 110, 100, 60, "ESP32", size=13)
    d.wire((360, 140), (440, 140)); led_branch(d, 440, 140, 230); d.ground((440, 230))
    d.zone("tirage", 95, 50, 50, 70); d.zone("bouton", 85, 145, 70, 60); d.zone("r-led", 415, 140, 50, 45); d.zone("led", 415, 186, 50, 44)
    return d


# --- M4 Temporisations et interruptions ------------------------------------------------------------------------------


def m4_delay():
    d = Drawing(560, 200, "Avec delay, le programme attend sans rien faire : un appui pendant l'attente n'est pas vu")
    timing(d, 150, 0, 360, [("LED", [(0, 5)]), ("bouton", [(2, 3)])], span=10, row_h=55, marks=((5, "500 ms"),))
    d.add(f'<rect x="150" y="125" width="180" height="22" fill="#c9d8dd" stroke="{INK}" stroke-width="1"/>')
    d.text(240, 141, "delay(500)", size=11, weight="600")
    d.text(258, 185, "bouton ignoré", size=12, weight="600", color=ACCENT)
    return d


def m4_boucle_delay():
    d = Drawing(560, 160, "Une boucle qui appelle delay passe presque tout son temps à attendre")
    block(d, 20, 50, 120, 44, "lecture du bouton", size=11)
    block(d, 170, 50, 360, 44, "delay(500)", size=12)
    d.text(280, 130, "loop() bloquée pendant delay", size=12, color=SOFT)
    return d


def m4_millis():
    d = Drawing(560, 170, "millis renvoie le nombre de millisecondes écoulées depuis le démarrage de la carte")
    d.arrow((60, 90), (500, 90), color=INK)
    for k, v in enumerate(("0", "1000", "2000", "3000")):
        x = 80 + k * 130
        d.wire((x, 82), (x, 98)); d.text(x, 120, v, size=12, weight="600")
    d.text(280, 50, "millis() : millisecondes depuis le démarrage", size=12, color=ACCENT, weight="600")
    return d


def m4_debordement():
    d = Drawing(560, 170, "Un compteur de 32 bits revient à 0 après 4 294 967 295 ms, soit environ 49,7 jours")
    d.wire((60, 130), (420, 40), color=ACCENT, width=3); d.wire((420, 40), (420, 130), color=ACCENT, width=2)
    d.wire((420, 130), (500, 110), color=ACCENT, width=3)
    d.text(280, 160, "4 294 967 295 ms ≈ 49,7 jours, puis retour à 0", size=12, weight="600")
    return d


def m4_sans_bloquer():
    d = Drawing(560, 230, "Clignoter sans bloquer : à chaque tour, on compare le temps écoulé à la période ; la boucle ne s'arrête jamais")
    block(d, 170, 20, 220, 44, "maintenant − dernier ≥ période ?", size=11)
    block(d, 330, 100, 200, 40, "inverser la LED", size=12)
    block(d, 330, 160, 200, 40, "dernier = maintenant", size=12)
    block(d, 30, 160, 200, 40, "continuer la boucle", size=12)
    d.arrow((380, 64), (420, 98), label="oui", color=INK, offset=(22, 0)); d.arrow((430, 140), (430, 158), color=INK)
    d.arrow((200, 64), (130, 158), label="non", color=INK, offset=(-22, 0)); d.arrow((330, 180), (232, 180), color=INK)
    return d


def m4_rythmes():
    d = Drawing(560, 190, "Deux LED à deux rythmes : chacune a sa période et son instant de dernier changement")
    timing(d, 150, 0, 360, [("LED 1 : 500 ms", [(0, 5), (10, 15)]), ("LED 2 : 120 ms", [(0, 1.2), (2.4, 3.6), (4.8, 6), (7.2, 8.4), (9.6, 10.8), (12, 13.2), (14.4, 15.6), (16.8, 18)])],
           span=20, row_h=60)
    return d


def m4_interruption():
    d = Drawing(560, 210, "Une interruption suspend le programme principal, exécute une courte routine, puis rend la main")
    block(d, 20, 40, 520, 40, "programme principal", size=12)
    block(d, 220, 140, 180, 44, "routine d'interruption (ISR)", size=11)
    d.arrow((230, 80), (260, 138), label="front sur la broche", color=ACCENT, offset=(-70, 0))
    d.arrow((370, 138), (400, 82), label="retour au programme", color=INK, offset=(78, 0))
    return d


def m4_isr_regles():
    d = Drawing(560, 200, "Règles d'une routine d'interruption : courte, variables partagées volatile, IRAM_ATTR, jamais de delay ni de Serial")
    for i, rule in enumerate(("courte : quelques lignes", "volatile : variables partagées", "IRAM_ATTR : en mémoire rapide", "jamais delay ni Serial")):
        block(d, 30 + (i % 2) * 260, 30 + (i // 2) * 80, 240, 50, rule, size=11)
    return d


def m4_timer():
    d = Drawing(560, 180, "Timer matériel : l'horloge de 80 MHz est divisée pour compter à 1 MHz ; l'alarme à 1 000 000 déclenche la routine chaque seconde")
    for i, label in enumerate(("horloge 80 MHz", "compteur à 1 MHz", "alarme à 1 000 000", "ISR chaque seconde")):
        block(d, 10 + i * 140, 60, 125, 50, label, size=10)
        if i < 3:
            arrow_right(d, 135 + i * 140, 148 + i * 140, 85)
    return d


def m4_timer_chrono():
    d = Drawing(560, 170, "Chronogramme : le timer déclenche la routine toutes les secondes, et la LED change d'état à chaque fois")
    timing(d, 150, 0, 360, [("ISR", [(1, 1.08), (2, 2.08), (3, 3.08)]), ("LED", [(1, 2), (3, 4)])], span=4, row_h=55,
           marks=((1, "1 s"), (2, "2 s"), (3, "3 s")))
    return d


def m4_reaction():
    d = Drawing(560, 200, "Mini-projet : après une attente aléatoire, la LED s'allume ; l'appui sur le bouton arrête le chronomètre")
    timing(d, 150, 0, 360, [("LED", [(4, 10)]), ("bouton", [(6.5, 7.5)])], span=10, row_h=55)
    d.text(240, 160, "attente aléatoire", size=11, color=SOFT); d.arrow((294, 150), (384, 150), label="temps de réaction", offset=(0, 40))
    return d


def q_m4_sourd():
    d = Drawing(560, 170, "Chronogramme d'un clignotant écrit avec delay, sans légende")
    timing(d, 110, 0, 420, [("LED", [(0, 5)])], span=10, row_h=55)
    d.add(f'<rect x="110" y="75" width="210" height="26" fill="#c9d8dd" stroke="{INK}" stroke-width="1"/>')
    d.text(215, 93, "delay(500)", size=11, weight="600")
    d.add(f'<rect x="320" y="75" width="40" height="26" fill="{PAPER}" stroke="{INK}" stroke-width="1"/>')
    d.text(340, 93, "loop", size=10)
    d.zone("delay", 110, 70, 210, 36); d.zone("lecture", 320, 70, 40, 36); d.zone("haut", 110, 0, 210, 40); d.zone("fin", 360, 70, 170, 36)
    return d


# --- M5 Le terminal série --------------------------------------------------------------------------------------------


def m5_trame():
    d = Drawing(560, 200, "Trame série 8N1 du caractère a (code 97) : un bit de départ à 0, huit bits de données poids faible d'abord, un bit d'arrêt à 1")
    bits = [1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1]  # repos, départ, 97 = 0b01100001 poids faible d'abord, arrêt, repos
    x, pts = 40, []
    for b in bits:
        y = 50 if b else 110
        pts += [(x, y), (x + 40, y)]
        x += 40
    d.wire(*pts, color=ACCENT, width=2.5)
    for i, label in ((0, "repos"), (1, "départ"), (10, "arrêt")):
        d.text(60 + i * 40, 140, label, size=10)
    d.text(260, 175, "bits de données, poids faible d'abord", size=11, color=SOFT)
    for k, b in enumerate((1, 0, 0, 0, 0, 1, 1, 0)):
        d.text(140 + k * 40, 35, str(b), size=11, weight="700")
    return d


def m5_pont():
    d = Drawing(560, 170, "Le moniteur série : l'ESP32 et l'ordinateur dialoguent par l'UART 0 et le pont USB-série, à la même vitesse aux deux bouts")
    block(d, 20, 50, 130, 60, "ESP32", size=14); block(d, 215, 50, 130, 60, "pont USB-série", size=11); block(d, 410, 50, 130, 60, "ordinateur", size=12)
    d.arrow((150, 70), (213, 70), label="TX", color=INK); d.arrow((213, 92), (150, 92), label="RX", color=INK, offset=(0, 22))
    d.wire((345, 80), (410, 80), width=3); d.text(378, 70, "USB", size=10)
    d.text(280, 150, "même vitesse aux deux bouts", size=12, weight="600", color=ACCENT)
    return d


def m5_vitesses():
    d = Drawing(560, 160, "La vitesse doit être la même des deux côtés : à 115 200 bit/s partout, le texte est lisible ; sinon il est remplacé par des caractères illisibles")
    block(d, 20, 30, 520, 44, "115 200 bit/s des deux côtés : texte lisible", size=12)
    block(d, 20, 95, 520, 44, "9 600 d'un côté, 115 200 de l'autre : caractères illisibles", size=12)
    return d


def m5_sorties():
    d = Drawing(560, 190, "Ce qu'affichent print, println et printf dans le moniteur série")
    for i, (code, out) in enumerate((('print("U = ")', "U = "), ("println(3.3)", "3.30 ⏎"), ('printf("%d mA\\n", 12)', "12 mA ⏎"))):
        y = 30 + i * 52
        block(d, 20, y, 250, 40, code, size=11)
        d.add(f'<rect x="310" y="{y}" width="230" height="40" rx="6" fill="#173f58"/>')
        d.text(325, y + 25, out, anchor="start", size=12, weight="600", color=PAPER)
    return d


def m5_ascii():
    d = Drawing(560, 170, "Chaque caractère est envoyé sous la forme de son code ASCII : a vaut 97, A vaut 65, 0 vaut 48, Entrée vaut 10")
    d.text(90, 40, "caractère", size=12, weight="700"); d.text(90, 110, "code ASCII (décimal)", size=11, weight="700")
    for i, (c, v) in enumerate((("a", "97"), ("b", "98"), ("A", "65"), ("0", "48"), ("1", "49"), ("⏎", "10"))):
        x = 200 + i * 60
        block(d, x - 25, 20, 50, 34, c, size=14); block(d, x - 25, 90, 50, 34, v, size=12)
    return d


def m5_tampon():
    d = Drawing(560, 180, "Les caractères reçus attendent dans un tampon : available donne leur nombre, read rend le plus ancien, ou -1 si le tampon est vide")
    for i, c in enumerate("led1⏎"):
        block(d, 100 + i * 60, 50, 50, 44, c, size=14)
    d.text(250, 30, "tampon de réception", size=12, weight="600")
    d.text(100, 130, "read() : le plus ancien, ou -1", anchor="start", size=11, color=ACCENT, weight="600")
    d.text(100, 155, "available() : octets en attente", anchor="start", size=11)
    return d


def m5_commande():
    d = Drawing(560, 230, "Lire une commande : lire une ligne jusqu'à Entrée, la comparer aux commandes connues, agir et répondre")
    block(d, 180, 20, 200, 40, "lire jusqu'à Entrée", size=12)
    block(d, 180, 90, 200, 40, "comparer à une commande connue", size=11)
    block(d, 30, 170, 220, 40, "agir et répondre", size=12); block(d, 310, 170, 220, 40, "commande inconnue : message d'erreur", size=10)
    d.arrow((280, 60), (280, 88), color=INK); d.arrow((240, 130), (150, 168), label="oui", color=INK, offset=(-24, 0))
    d.arrow((320, 130), (420, 168), label="non", color=INK, offset=(24, 0))
    return d


def m5_trace():
    d = Drawing(560, 190, "Déboguer : afficher les valeurs à chaque étape montre où le programme s'écarte de ce qu'on attend")
    d.add(f'<rect x="40" y="30" width="480" height="130" rx="8" fill="#173f58"/>')
    for i, line in enumerate(("niveau=1 etat=0", "niveau=0 etat=1", "niveau=0 etat=1", "niveau=1 etat=1")):
        d.text(60, 58 + i * 26, line, anchor="start", size=12, color=PAPER)
    d.text(280, 182, "trace : valeurs à chaque étape", size=11, color=SOFT)
    return d


def m5_serial2():
    d = Drawing(560, 200, "Deux cartes reliées par l'UART 2 : le TX de l'une va au RX de l'autre, et les masses sont communes")
    block(d, 30, 40, 150, 120, "carte A", size=13); block(d, 380, 40, 150, 120, "carte B", size=13)
    d.wire((180, 70), (380, 120), width=2); d.wire((180, 120), (380, 70), width=2); d.wire((180, 145), (380, 145), width=2)
    d.text(190, 64, "TX 17", anchor="start", size=10, weight="600"); d.text(190, 114, "RX 16", anchor="start", size=10, weight="600")
    d.text(370, 64, "RX 16", anchor="end", size=10, weight="600"); d.text(370, 114, "TX 17", anchor="end", size=10, weight="600")
    d.text(280, 140, "GND", size=10, weight="600")
    d.text(280, 190, "TX vers RX, RX vers TX, GND commun", size=11, color=ACCENT, weight="600")
    return d


def m5_pupitre():
    d = Drawing(560, 180, "Mini-projet : depuis le moniteur série, on commande le feu tricolore et on lit l'état du bouton")
    block(d, 20, 60, 150, 60, "ordinateur", size=12); block(d, 210, 60, 140, 60, "ESP32", size=14); block(d, 390, 30, 150, 50, "feu tricolore", size=12)
    block(d, 390, 110, 150, 50, "bouton", size=12)
    d.arrow((170, 80), (208, 80), color=INK); d.arrow((208, 100), (170, 100), color=INK)
    d.wire((350, 80), (390, 55)); d.wire((350, 100), (390, 135))
    return d


def q_m5_tx():
    d = Drawing(560, 220, "Liaison série entre deux cartes, sans légende")
    block(d, 30, 40, 150, 140, "ESP32", size=13); block(d, 380, 40, 150, 140, "", size=13)
    for i, name in enumerate(("TX", "RX", "GND", "3V3")):
        y = 70 + i * 30
        d.add(f'<rect x="166" y="{y - 9}" width="18" height="18" fill="{PAPER}" stroke="{INK}" stroke-width="1.5"/>')
        d.zone(name.lower(), 150, y - 13, 50, 26)
    d.wire((184, 70), (380, 100), width=2); d.wire((184, 100), (380, 70), width=2); d.wire((184, 130), (380, 130), width=2)
    for y, label in ((70, "TX"), (100, "RX"), (130, "GND")):
        d.text(392, y + 5, label, anchor="start", size=12, weight="700")
    return d


# --- M6 Analogique et tactile ----------------------------------------------------------------------------------------


def m6_adc():
    d = Drawing(560, 230, "Le convertisseur analogique-numérique de 12 bits traduit une tension de 0 à 3,3 V en une valeur de 0 à 4 095")
    d.graph(80, 20, 420, 170, (0, 3.3), (0, 4095), [([(0, 0), (3.3, 4095)], ACCENT, "")], "tension (V)", "valeur lue",
            xticks=((0, "0"), (1.65, "1,65"), (3.3, "3,3")), yticks=((0, "0"), (2048, "2048"), (4095, "4095")))
    d.text(300, 225, "4 096 niveaux, pas de 0,8 mV", size=11, color=SOFT)
    return d


def m6_adc_reel():
    d = Drawing(560, 240, "La mesure réelle de l'ESP32 s'écarte de la droite idéale près de 0 V et de 3,3 V : analogReadMilliVolts corrige une partie de l'écart")
    real = [(0, 0), (0.15, 0), (0.5, 450), (1.0, 1060), (1.65, 1860), (2.5, 2950), (3.0, 3650), (3.15, 4095), (3.3, 4095)]
    d.graph(80, 20, 420, 170, (0, 3.3), (0, 4095), [([(0, 0), (3.3, 4095)], SOFT, ""), (real, ACCENT, "")],
            "tension (V)", "valeur lue", xticks=((0, "0"), (3.3, "3,3")), yticks=((0, "0"), (4095, "4095")))
    d.text(290, 225, "réel : moins précis près de 0 V et de 3,3 V", size=11, color=ACCENT, weight="600")
    return d


def m6_potentiometre():
    d = Drawing(480, 240, "Un potentiomètre de 10 kΩ entre 3,3 V et GND : son curseur donne une tension de 0 à 3,3 V lue par GPIO 34")
    d.text(150, 24, "3,3 V", weight="600"); d.wire((150, 30), (150, 60))
    d.resistor((150, 60), (150, 200), "10 kΩ", side=-1); d.ground((150, 200))
    d.arrow((215, 130), (162, 130), color=INK); d.wire((215, 130), (300, 130)); node(d, 305, 130, "GPIO 34", anchor="start")
    d.text(260, 120, "curseur vers GPIO 34", size=10, color=SOFT)
    return d


def m6_mli():
    d = Drawing(560, 240, "Modulation de largeur d'impulsion : à fréquence fixe, le rapport cyclique règle la tension moyenne")
    timing(d, 150, 0, 360, [("25 %", [(0, 1), (4, 5), (8, 9)]), ("50 %", [(0, 2), (4, 6), (8, 10)]), ("75 %", [(0, 3), (4, 7), (8, 11)])], span=12, row_h=60)
    d.text(330, 232, "rapport cyclique", size=11, color=SOFT)
    return d


def m6_mli_moyenne():
    d = Drawing(560, 170, "Tension moyenne d'un signal MLI de 3,3 V : 25 % donne 0,83 V, 50 % donne 1,65 V, 75 % donne 2,48 V")
    for i, (duty, v) in enumerate((("25 %", "0,83 V"), ("50 %", "1,65 V"), ("75 %", "2,48 V"))):
        x = 40 + i * 170
        block(d, x, 30, 150, 40, duty, size=13); block(d, x, 100, 150, 40, v, size=13)
        d.arrow((x + 75, 70), (x + 75, 98), color=INK)
    return d


def m6_moteur_mli():
    d = Drawing(560, 260, "Varier la vitesse d'un moteur 12 V : la MLI de 5 kHz attaque la grille du MOSFET ; la diode de roue libre reste indispensable")
    d.text(380, 24, "+12 V", weight="600"); d.wire((380, 30), (380, 53))
    d.add(f'<circle cx="380" cy="75" r="22" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>'); d.text(380, 80, "M", weight="700")
    d.wire((380, 97), (380, 120)); d.diode((460, 120), (460, 40)); d.wire((460, 40), (380, 40)); d.wire((460, 120), (380, 120))
    gate, drain, source = nmos(d, 340, 160); d.wire(drain, (380, 120)); d.wire(source, (380, 220)); d.ground((380, 220))
    node(d, 120, 160, "GPIO 26"); d.wire((125, 160), (180, 160)); d.resistor((180, 160), (270, 160), "220 Ω"); d.wire((270, 160), gate)
    d.text(200, 245, "MLI 5 kHz sur la grille", size=11, weight="600", color=ACCENT)
    return d


def m6_vitesse():
    d = Drawing(560, 200, "La vitesse du moteur suit à peu près le rapport cyclique ; en dessous d'un seuil, le moteur ne démarre pas")
    d.graph(80, 20, 420, 140, (0, 100), (0, 100), [([(0, 0), (15, 0), (100, 95)], ACCENT, "")], "rapport cyclique", "vitesse",
            xticks=((0, "0 %"), (50, "50 %"), (100, "100 %")), yticks=())
    return d


def m6_buzzer():
    d = Drawing(560, 200, "Un buzzer passif sur GPIO 27 : ledcWriteTone fixe la fréquence, donc la hauteur du son")
    node(d, 120, 100, "GPIO 27"); d.wire((125, 100), (200, 100))
    d.add(f'<circle cx="240" cy="100" r="34" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>'); d.text(240, 105, "♪", size=20, weight="700")
    d.wire((274, 100), (320, 100)); d.ground((320, 100))
    d.text(240, 160, "buzzer passif", size=12, weight="600"); d.text(450, 100, "fréquence = hauteur du son", size=11, color=ACCENT, weight="600")
    return d


def m6_touch():
    d = Drawing(560, 210, "Capteur tactile : un doigt approché de l'électrode ajoute sa capacité ; la mesure de l'ESP32 change")
    d.add(f'<rect x="120" y="120" width="160" height="16" rx="4" fill="#c9d8dd" stroke="{INK}" stroke-width="1.5"/>'); d.text(200, 160, "électrode", size=12)
    d.add(f'<ellipse cx="200" cy="70" rx="28" ry="40" fill="{PAPER}" stroke="{ACCENT}" stroke-width="2"/>'); d.text(200, 75, "doigt", size=11, weight="600")
    d.wire((280, 128), (380, 128)); node(d, 385, 128, "T0 (GPIO 4)", anchor="start")
    d.text(200, 195, "capacité plus grande", size=11, color=ACCENT, weight="600")
    return d


def m6_touch_valeurs():
    d = Drawing(560, 220, "Valeurs lues par touchRead sur l'ESP32 : elles chutent quand on touche ; un seuil entre les deux niveaux détecte le contact")
    pts = [(0, 60), (3, 60), (3.2, 15), (6, 15), (6.2, 60), (10, 60)]
    d.graph(80, 20, 420, 160, (0, 10), (0, 80), [(pts, ACCENT, ""), ([(0, 35), (10, 35)], SOFT, "seuil")], "temps", "valeur lue",
            xticks=(), yticks=((60, "sans doigt"), (15, "avec doigt")))
    return d


def m6_dac():
    d = Drawing(560, 220, "Le convertisseur numérique-analogique : dacWrite donne 256 niveaux de tension entre 0 et 3,3 V sur GPIO 25 ou 26")
    pts = []
    for k in range(9):
        pts += [(k * 32, k * 32 * 3.3 / 255), ((k + 1) * 32, k * 32 * 3.3 / 255)]
    d.graph(80, 20, 420, 160, (0, 288), (0, 3.4), [(pts, ACCENT, "")], "valeur écrite", "tension (V)",
            xticks=((0, "0"), (128, "128"), (255, "255")), yticks=((0, "0"), (3.3, "3,3")))
    d.text(300, 212, "dacWrite : 256 niveaux de 0 à 3,3 V", size=11, color=SOFT)
    return d


def m6_dac_rampe():
    d = Drawing(560, 180, "Une rampe produite par le DAC : la valeur augmente de 0 à 255 puis recommence, ce qui donne une dent de scie")
    d.wire((60, 140), (200, 40), (200, 140), (340, 40), (340, 140), (480, 40), color=ACCENT, width=2.5)
    d.text(40, 44, "3,3 V", anchor="end", size=11); d.text(40, 144, "0 V", anchor="end", size=11)
    return d


def m6_variateur():
    d = Drawing(560, 200, "Mini-projet : le potentiomètre règle la luminosité d'une LED par MLI ; une touche tactile l'allume et l'éteint")
    block(d, 20, 30, 140, 50, "potentiomètre", size=12); block(d, 20, 120, 140, 50, "touche tactile", size=12)
    block(d, 210, 60, 140, 80, "ESP32", size=14); block(d, 400, 75, 140, 50, "LED", size=13)
    d.arrow((160, 55), (208, 85), label="GPIO 34", color=INK); d.arrow((160, 145), (208, 115), label="T0", color=INK, offset=(0, 26))
    d.arrow((350, 100), (398, 100), label="MLI", color=INK)
    return d


def q_m6_touch():
    d = Drawing(420, 560, "Carte DevKit 38 broches sans légende")
    devkit(d, 135, 30, marks=False, zones={"4": "touch", "25": "dac", "34": "entree", "22": "scl", "26": "autre"})
    return d


def device(d, x, y, w, h, label, sub=None):
    block(d, x, y, w, h, label, size=11)
    if sub:
        d.text(x + w / 2, y + h + 14, sub, size=10, color=SOFT)


# --- M7 Bus I2C et SPI -----------------------------------------------------------------------------------------------


def m7_bus():
    d = Drawing(560, 200, "Trois liaisons série de l'ESP32 : l'UART relie deux appareils, l'I2C en relie beaucoup sur deux fils, le SPI va plus vite avec quatre fils")
    for i, (name, detail) in enumerate((("UART", "UART : 2 fils, 1 appareil"), ("I2C", "I2C : 2 fils, jusqu'à 127 appareils"), ("SPI", "SPI : 4 fils, très rapide"))):
        y = 25 + i * 58
        block(d, 20, y, 110, 42, name, size=13)
        d.text(150, y + 26, detail, anchor="start", size=12)
    return d


def m7_horloge():
    d = Drawing(560, 170, "Bus synchrone : un fil d'horloge partagé dit au récepteur quand lire chaque bit, sans vitesse convenue à l'avance")
    timing(d, 150, 0, 360, [("SCL", [(k + 0.5, k + 1) for k in range(8)]), ("SDA", [(0, 2), (3, 5), (6, 8)])], span=8, row_h=55)
    d.text(330, 160, "horloge partagée", size=11, color=SOFT)
    return d


def m7_i2c():
    d = Drawing(560, 260, "Bus I2C : SDA (GPIO 21) et SCL (GPIO 22) relient tous les appareils ; deux résistances de tirage les maintiennent au niveau haut ; chaque appareil a son adresse")
    block(d, 20, 140, 110, 70, "ESP32", size=13)
    d.wire((130, 160), (520, 160)); d.wire((130, 190), (520, 190))
    d.text(140, 154, "SDA 21", anchor="start", size=10, weight="600"); d.text(140, 184, "SCL 22", anchor="start", size=10, weight="600")
    d.text(200, 30, "3,3 V", weight="600"); d.wire((180, 36), (220, 36))
    d.resistor((180, 36), (180, 160), side=-1); d.resistor((220, 36), (220, 190)); d.dot((180, 160)); d.dot((220, 190))
    d.text(170, 100, "tirages de 4,7 kΩ", anchor="end", size=10, color=ACCENT, weight="600")
    for x, label in ((290, "écran OLED (0x3C)"), (420, "capteur BME280 (0x76)")):
        block(d, x, 70, 110, 50, label.split(" (")[0], size=11); d.text(x + 55, 136, "0x" + label.split("0x")[1].rstrip(")"), size=10, weight="600")
        d.wire((x + 40, 120), (x + 40, 160)); d.wire((x + 70, 120), (x + 70, 190)); d.dot((x + 40, 160)); d.dot((x + 70, 190))
    return d


def m7_trame_i2c():
    d = Drawing(560, 150, "Une trame I2C : départ, adresse de 7 bits, bit de lecture ou d'écriture, acquittement de l'appareil, puis les données")
    parts = (("départ", 60), ("adresse", 150), ("R/W", 50), ("ACK", 50), ("donnée", 150))
    x = 20
    for label, w in parts:
        block(d, x, 50, w - 6, 40, label, size=11); x += w
    d.text(140, 120, "adresse de 7 bits", size=10, color=SOFT); d.text(340, 120, "acquittement", size=10, color=SOFT)
    return d


def m7_oled():
    d = Drawing(560, 230, "Écran OLED de 128 colonnes sur 64 lignes : l'origine (0, 0) est en haut à gauche ; x va vers la droite, y vers le bas")
    d.add(f'<rect x="120" y="30" width="320" height="160" rx="6" fill="#173f58" stroke="{INK}" stroke-width="2"/>')
    d.text(140, 60, "23,5 °C", anchor="start", size=22, weight="700", color=PAPER)
    d.arrow((120, 210), (440, 210), label="128 colonnes", color=INK, offset=(0, 16))
    d.arrow((100, 30), (100, 190), color=INK); d.text(90, 115, "64 lignes", anchor="end", size=11)
    d.dot((120, 30)); d.text(120, 22, "origine (0, 0)", anchor="start", size=10)
    return d


def m7_oled_montage():
    d = Drawing(560, 200, "Câblage de l'écran OLED I2C : VCC sur 3V3, GND sur GND, SDA sur GPIO 21, SCL sur GPIO 22")
    block(d, 20, 50, 140, 110, "ESP32", size=14); block(d, 390, 60, 150, 90, "écran OLED", size=12)
    for i, (a, b) in enumerate((("3V3", "VCC"), ("GND", "GND"), ("21", "SDA"), ("22", "SCL"))):
        y = 70 + i * 22
        d.wire((160, y), (390, y)); d.text(170, y - 4, a, anchor="start", size=10, weight="600"); d.text(380, y - 4, b, anchor="end", size=10, weight="600")
    return d


def m7_bme280():
    d = Drawing(560, 200, "Le capteur BME280 sur le même bus I2C mesure la température, l'humidité et la pression")
    block(d, 20, 60, 130, 80, "ESP32", size=14); block(d, 210, 60, 130, 80, "BME280", size=13)
    d.wire((150, 90), (210, 90)); d.wire((150, 110), (210, 110))
    for i, (name, value) in enumerate((("température", "23,5 °C"), ("humidité", "48 %"), ("pression", "1 013 hPa"))):
        block(d, 380, 30 + i * 52, 160, 40, f"{value}", size=12); d.text(372, 54 + i * 52, name, anchor="end", size=10)
    return d


def m7_scanner():
    d = Drawing(560, 180, "Le scanner I2C interroge les 127 adresses une à une ; un appareil présent répond par un acquittement")
    d.add(f'<rect x="40" y="25" width="480" height="120" rx="8" fill="#173f58"/>')
    for i, line in enumerate(("Recherche sur le bus I2C...", "Appareil trouvé en 0x3C", "Appareil trouvé en 0x76", "2 appareils")):
        d.text(60, 55 + i * 25, line, anchor="start", size=12, color=PAPER)
    return d


def m7_spi():
    d = Drawing(560, 240, "Bus SPI : MOSI, MISO et SCK sont partagés ; chaque appareil a sa propre ligne CS, mise au niveau bas pour lui parler")
    block(d, 20, 70, 120, 110, "ESP32", size=14)
    for i, (name, pin) in enumerate((("MOSI", "23"), ("MISO", "19"), ("SCK", "18"))):
        y = 90 + i * 24
        d.wire((140, y), (520, y)); d.text(150, y - 4, f"{name} {pin}", anchor="start", size=10, weight="600")
    for x, label, cs in ((300, "carte microSD", "CS 5"), (430, "autre appareil", "CS 15")):
        block(d, x, 170, 100, 46, label, size=10)
        for i in range(3):
            d.wire((x + 20 + i * 25, 90 + i * 24), (x + 20 + i * 25, 170)); d.dot((x + 20 + i * 25, 90 + i * 24))
    d.wire((140, 160), (250, 160), (250, 230), (350, 230), (350, 216)); d.text(150, 155, "CS 5", anchor="start", size=10, weight="600")
    d.text(280, 30, "un CS par appareil", size=12, color=ACCENT, weight="600")
    return d


def m7_spi_chrono():
    d = Drawing(560, 210, "Chronogramme SPI : CS descend pour choisir l'appareil, puis un bit circule sur MOSI à chaque coup d'horloge")
    timing(d, 150, 0, 360, [("CS", [(0, 1), (9, 10)]), ("SCK", [(k + 1.5, k + 2) for k in range(8)]), ("MOSI", [(1, 3), (5, 7)])], span=10, row_h=55)
    return d


def m7_sd():
    d = Drawing(560, 190, "Câblage du module microSD en SPI : CS sur GPIO 5, MOSI sur 23, MISO sur 19, SCK sur 18, alimentation 3,3 V")
    block(d, 20, 40, 140, 130, "ESP32", size=14); block(d, 390, 50, 150, 110, "carte microSD", size=12)
    for i, (a, b) in enumerate((("3V3", "VCC"), ("GND", "GND"), ("5", "CS"), ("23", "MOSI"), ("19", "MISO"), ("18", "SCK"))):
        y = 58 + i * 18
        d.wire((160, y), (390, y)); d.text(170, y - 3, a, anchor="start", size=9, weight="600"); d.text(380, y - 3, b, anchor="end", size=9, weight="600")
    return d


def m7_journal():
    d = Drawing(560, 180, "Le journal journal.csv sur la carte microSD : une ligne par mesure, valeurs séparées par des points-virgules")
    d.add(f'<rect x="40" y="25" width="480" height="130" rx="8" fill="{PAPER}" stroke="{INK}" stroke-width="1.5"/>')
    for i, line in enumerate(("temps_ms;tension_mV", "5000;1650", "10000;1702", "15000;1688")):
        d.text(60, 55 + i * 26, line, anchor="start", size=12, weight="700" if i == 0 else "400")
    return d


def m7_station():
    d = Drawing(560, 200, "Mini-projet : station de mesure ; le BME280 et l'écran OLED sur le bus I2C, la carte microSD sur le bus SPI")
    block(d, 210, 60, 140, 80, "ESP32", size=14)
    block(d, 20, 30, 140, 50, "BME280", size=12); block(d, 20, 120, 140, 50, "écran OLED", size=12); block(d, 400, 75, 140, 50, "carte microSD", size=12)
    d.arrow((160, 55), (208, 85), label="I2C", color=INK); d.arrow((208, 115), (160, 145), label="I2C", color=INK, offset=(0, 26)); d.arrow((350, 100), (398, 100), label="SPI", color=INK)
    return d


def q_m7_tirages():
    d = Drawing(560, 260, "Bus I2C sans légende")
    block(d, 20, 140, 110, 70, "ESP32", size=13)
    d.wire((130, 160), (520, 160)); d.wire((130, 190), (520, 190))
    d.text(200, 30, "3,3 V", weight="600"); d.wire((180, 36), (220, 36))
    d.resistor((180, 36), (180, 160), side=-1); d.resistor((220, 36), (220, 190)); d.dot((180, 160)); d.dot((220, 190))
    for x in (290, 420):
        block(d, x, 70, 110, 50, "", size=11)
        d.wire((x + 40, 120), (x + 40, 160)); d.wire((x + 70, 120), (x + 70, 190)); d.dot((x + 40, 160)); d.dot((x + 70, 190))
    d.zone("tirages", 160, 50, 80, 90); d.zone("esp32", 20, 140, 110, 70); d.zone("appareil1", 290, 70, 110, 50); d.zone("appareil2", 420, 70, 110, 50)
    return d


# --- M8 Mémoire et énergie -------------------------------------------------------------------------------------------


def m8_memoires():
    d = Drawing(560, 200, "Trois mémoires utiles au programme : la Flash garde le programme et les Preferences, la SRAM les variables, la mémoire RTC de 8 Ko survit à la veille profonde")
    for i, (label, color) in enumerate((("Flash : programme et Preferences", ACCENT), ("SRAM : variables", "#c9d8dd"), ("mémoire RTC : 8 Ko", "#dfe8ea"))):
        d.add(f'<rect x="40" y="{30 + i * 52}" width="480" height="40" rx="6" fill="{color}" stroke="{INK}" stroke-width="1.5"/>')
        d.text(280, 55 + i * 52, label, size=12, weight="700", color=PAPER if i == 0 else INK)
    return d


def m8_survie():
    d = Drawing(560, 200, "Ce qui survit : la Flash garde tout ; la SRAM perd tout à la coupure comme en veille profonde ; la mémoire RTC garde ses données en veille profonde, pas à la coupure")
    d.text(270, 30, "coupure", size=12, weight="700"); d.text(430, 30, "veille profonde", size=12, weight="700")
    for i, (name, cut, sleep) in enumerate((("Flash", "garde", "garde"), ("SRAM", "perd", "perd"), ("mémoire RTC", "perd", "garde"))):
        y = 50 + i * 46
        block(d, 40, y, 150, 36, name, size=12)
        for x, state in ((270, cut), (430, sleep)):
            d.text(x, y + 23, state, size=12, weight="600", color=ACCENT if state == "garde" else SOFT)
    return d


def m8_nvs():
    d = Drawing(560, 200, "Preferences range des paires clé et valeur dans un espace de noms, en Flash ; elles survivent à la coupure")
    d.add(f'<rect x="40" y="30" width="480" height="140" rx="10" fill="{PAPER}" stroke="{INK}" stroke-width="2" stroke-dasharray="6 4"/>')
    d.text(280, 52, "espace de noms « reglages »", size=12, weight="600")
    for i, (k, v) in enumerate((("bootCount", "17"), ("seuil", "30"), ("ville", "Douala"))):
        block(d, 80, 70 + i * 32, 160, 26, k, size=11); block(d, 300, 70 + i * 32, 160, 26, v, size=11)
    d.text(160, 186, "clé", size=10, color=SOFT); d.text(380, 186, "valeur", size=10, color=SOFT)
    return d


def m8_usure():
    d = Drawing(560, 160, "La Flash s'use : environ 100 000 écritures par cellule ; on n'écrit qu'en cas de changement, jamais à chaque tour de boucle")
    d.wire((60, 120), (500, 120), color=SOFT, width=1)
    d.wire((60, 40), (420, 40), (500, 120), color=ACCENT, width=3)
    d.text(280, 140, "environ 100 000 écritures par cellule", size=12, weight="600")
    return d


def m8_modes():
    d = Drawing(560, 230, "Consommation typique de l'ESP32 : environ 100 mA actif avec Wi-Fi, 20 mA actif, 0,8 mA en veille légère, 10 µA en veille profonde")
    rows = (("actif + Wi-Fi", "≈ 100 mA", 320), ("actif", "≈ 20 mA", 240), ("veille légère", "≈ 0,8 mA", 140), ("veille profonde", "≈ 10 µA", 40))
    for i, (name, value, w) in enumerate(rows):
        y = 25 + i * 45
        d.text(140, y + 22, name, anchor="end", size=12)
        d.add(f'<rect x="150" y="{y}" width="{w}" height="30" rx="4" fill="{ACCENT if i == 3 else "#c9d8dd"}" stroke="{INK}" stroke-width="1.5"/>')
        d.text(160 + w, y + 21, value, anchor="start", size=12, weight="700")
    d.text(300, 215, "courant (échelle logarithmique)", size=10, color=SOFT)
    return d


def m8_autonomie():
    d = Drawing(560, 170, "Autonomie sur une pile de 2 000 mAh : environ 20 heures à 100 mA, environ 23 ans à 10 µA ; la veille profonde change tout")
    block(d, 20, 50, 160, 60, "pile de 2 000 mAh", size=12)
    block(d, 240, 20, 300, 50, "100 mA : 20 h", size=13); block(d, 240, 90, 300, 50, "10 µA : 200 000 h ≈ 23 ans", size=13)
    d.wire((180, 80), (240, 45)); d.wire((180, 80), (240, 115))
    return d


def m8_cycle():
    d = Drawing(560, 180, "Cycle d'un appareil sur pile : réveil, mesure en une fraction de seconde, puis veille profonde pendant 10 s")
    timing(d, 150, 0, 360, [("actif", [(0, 0.5), (10.5, 11)]), ("veille profonde", [(0.5, 10.5)])], span=12, row_h=60)
    return d


def m8_reveil_timer():
    d = Drawing(560, 200, "Après une veille profonde, la puce redémarre : setup s'exécute de nouveau, et loop n'est jamais atteinte si setup se rendort")
    block(d, 20, 70, 140, 50, "setup()", size=14); block(d, 210, 70, 140, 50, "mesurer", size=12); block(d, 400, 70, 140, 50, "dormir 10 s", size=12)
    arrow_right(d, 160, 208, 95); arrow_right(d, 350, 398, 95)
    d.wire((470, 120), (470, 165), (90, 165), (90, 122), color=ACCENT, width=2)
    d.text(280, 185, "réveil : setup() recommence", size=11, color=ACCENT, weight="600")
    return d


def m8_reveils():
    d = Drawing(560, 190, "Sources de réveil d'une veille profonde : la minuterie, le toucher d'une broche tactile, le niveau d'une broche RTC")
    block(d, 360, 70, 180, 60, "veille profonde", size=12)
    for i, label in enumerate(("minuterie", "toucher", "broche RTC")):
        block(d, 20, 20 + i * 55, 160, 40, label, size=12)
        d.arrow((180, 40 + i * 55), (358, 100), color=INK)
    return d


def m8_rtc_gpio():
    d = Drawing(560, 200, "Seules les broches RTC peuvent réveiller la puce par leur niveau : GPIO 0, 2, 4, 12 à 15, 25 à 27 et 32 à 39")
    rtc = ("0", "2", "4", "12", "13", "14", "15", "25", "26", "27", "32", "33", "34", "35", "36", "39")
    other = ("5", "16", "17", "18", "19", "21", "22", "23")
    d.text(30, 35, "broches RTC (réveil ext0)", anchor="start", size=12, weight="700")
    for i, pin in enumerate(rtc):
        block(d, 30 + (i % 8) * 62, 45 + (i // 8) * 40, 54, 30, pin, size=11)
    d.text(30, 155, "autres broches", anchor="start", size=12, weight="700", color=SOFT)
    for i, pin in enumerate(other):
        d.text(50 + i * 60, 180, pin, size=12, color=SOFT)
    return d


def m8_rtc_data():
    d = Drawing(560, 170, "Une variable marquée RTC_DATA_ATTR est rangée en mémoire RTC : elle survit à la veille profonde et compte les réveils")
    for i, v in enumerate(("1", "2", "3", "4")):
        x = 40 + i * 130
        block(d, x, 50, 100, 50, f"bootCount = {v}", size=11)
        if i < 3:
            d.arrow((x + 100, 75), (x + 128, 75), color=ACCENT)
    d.text(280, 140, "bootCount en mémoire RTC : 1, 2, 3…", size=12, weight="600")
    return d


def m8_enregistreur():
    d = Drawing(560, 180, "Mini-projet : un enregistreur sobre se réveille toutes les 10 s, mesure, retient le maximum en Preferences et se rendort")
    for i, label in enumerate(("réveil", "mesurer", "Preferences", "dormir 10 s")):
        block(d, 15 + i * 137, 60, 120, 50, label, size=12)
        if i < 3:
            arrow_right(d, 135 + i * 137, 150 + i * 137, 85)
    d.text(280, 150, "enregistreur sobre", size=12, color=ACCENT, weight="600")
    return d


def q_m8_ext0():
    d = Drawing(420, 560, "Carte DevKit 38 broches sans légende")
    devkit(d, 135, 30, marks=False, zones={"33": "rtc", "23": "a", "16": "b", "17": "c", "5": "d"})
    return d


# --- M9 Wi-Fi et serveur web -----------------------------------------------------------------------------------------


def m9_modes():
    d = Drawing(560, 210, "Deux modes Wi-Fi : en station, l'ESP32 rejoint la box comme un téléphone ; en point d'accès, il crée son propre réseau")
    block(d, 20, 40, 120, 50, "box Wi-Fi", size=12); block(d, 210, 40, 120, 50, "ESP32", size=13); d.wire((140, 65), (210, 65), width=2)
    d.text(175, 110, "station : rejoint la box", size=11, color=ACCENT, weight="600")
    block(d, 210, 140, 120, 50, "ESP32", size=13); block(d, 410, 140, 120, 50, "téléphone", size=12); d.wire((330, 165), (410, 165), width=2)
    d.text(370, 130, "point d'accès : crée son réseau", size=11, color=ACCENT, weight="600")
    return d


def m9_reseau():
    d = Drawing(560, 200, "Sur le réseau local, la box donne une adresse IP à l'ESP32 ; le téléphone l'atteint par cette adresse")
    block(d, 210, 20, 140, 50, "box Wi-Fi", size=12)
    block(d, 40, 120, 160, 50, "ESP32", size=13); block(d, 360, 120, 160, 50, "téléphone", size=12)
    d.wire((240, 70), (120, 120), width=2); d.wire((320, 70), (440, 120), width=2)
    d.text(120, 190, "192.168.1.42", size=12, weight="700", color=ACCENT); d.text(440, 190, "192.168.1.17", size=12)
    d.text(280, 110, "réseau local", size=11, color=SOFT)
    return d


def m9_connexion():
    d = Drawing(560, 200, "Se connecter : WiFi.begin lance la connexion ; WiFi.status devient WL_CONNECTED ; en cas de perte, on relance")
    block(d, 20, 70, 150, 50, "connexion…", size=12); block(d, 210, 70, 150, 50, "connecté : adresse IP", size=11); block(d, 400, 70, 150, 50, "perte : nouvelle tentative", size=10)
    arrow_right(d, 170, 208, 95); arrow_right(d, 360, 398, 95)
    d.wire((475, 120), (475, 160), (95, 160), (95, 122), color=ACCENT, width=2)
    return d


def m9_rssi():
    d = Drawing(560, 170, "Force du signal (RSSI, en dBm) : vers -50 dBm excellent, -67 dBm bon, -80 dBm faible, au-delà de -90 dBm inutilisable")
    for i, (value, label) in enumerate((("-50", "excellent"), ("-67", "bon"), ("-80", "faible"), ("-90", "inutilisable"))):
        x = 40 + i * 125
        d.add(f'<rect x="{x}" y="{100 - (4 - i) * 18}" width="40" height="{(4 - i) * 18}" fill="{ACCENT if i < 2 else "#c9d8dd"}" stroke="{INK}" stroke-width="1.5"/>')
        d.text(x + 20, 120, f"{value} dBm", size=11, weight="600"); d.text(x + 20, 140, label, size=10, color=SOFT)
    return d


def m9_requete():
    d = Drawing(560, 180, "Une requête web : le navigateur demande /on ; le serveur de l'ESP32 exécute la route et renvoie une page avec le code 200")
    block(d, 20, 60, 140, 60, "navigateur", size=12); block(d, 400, 60, 140, 60, "ESP32", size=13)
    d.arrow((160, 75), (398, 75), label="GET /on", color=INK); d.arrow((398, 105), (160, 105), label="réponse 200 : page HTML", color=ACCENT, offset=(0, 22))
    return d


def m9_routes():
    d = Drawing(560, 190, "Chaque route du serveur appelle sa fonction : / renvoie la page d'accueil, /on et /off commandent la lampe, /mesure renvoie du JSON")
    d.text(130, 30, "route", size=12, weight="700"); d.text(380, 30, "action", size=12, weight="700")
    for i, (route, action) in enumerate((("/", "page d'accueil"), ("/on", "allumer la lampe"), ("/off", "éteindre la lampe"), ("/mesure", "mesure en JSON"))):
        y = 42 + i * 36
        block(d, 60, y, 140, 28, route, size=12); block(d, 280, y, 200, 28, action, size=11)
    return d


def m9_commande():
    d = Drawing(560, 200, "Commander la lampe 12 V depuis un téléphone : la route /on met GPIO 26 au niveau haut, le MOSFET allume la lampe")
    block(d, 20, 70, 120, 60, "téléphone", size=12); block(d, 200, 70, 120, 60, "ESP32", size=13)
    block(d, 370, 20, 120, 46, "MOSFET", size=12); block(d, 370, 120, 120, 46, "lampe 12 V", size=12)
    d.arrow((140, 100), (198, 100), label="/on", color=INK); d.arrow((320, 90), (368, 45), label="GPIO 26", color=INK, offset=(-10, -8))
    d.wire((430, 66), (430, 120), width=2)
    return d


def m9_page():
    d = Drawing(400, 260, "La page servie par l'ESP32, vue sur un téléphone : la tension mesurée et deux boutons")
    d.add(f'<rect x="100" y="10" width="200" height="240" rx="22" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>')
    d.text(200, 60, "tableau de bord", size=13, weight="700")
    d.text(200, 100, "Tension : 1,65 V", size=12)
    for i, label in enumerate(("Allumer", "Éteindre")):
        d.add(f'<rect x="130" y="{130 + i * 50}" width="140" height="36" rx="18" fill="{ACCENT if i == 0 else PAPER}" stroke="{ACCENT}" stroke-width="2"/>')
        d.text(200, 153 + i * 50, label, size=12, weight="700", color=PAPER if i == 0 else ACCENT)
    return d


def m9_json():
    d = Drawing(560, 170, "La route /mesure renvoie un texte JSON que la page relit toutes les 2 s, sans recharger toute la page")
    d.add(f'<rect x="40" y="30" width="480" height="70" rx="8" fill="#173f58"/>')
    d.text(60, 72, '{"tension_mV": 1650, "lampe": true}', anchor="start", size=14, color=PAPER)
    d.text(280, 135, "toutes les 2 s", size=12, color=ACCENT, weight="600")
    return d


def m9_secrets():
    d = Drawing(560, 190, "Les identifiants Wi-Fi vivent dans secrets.h, jamais partagé ; secrets.example.h, sans valeurs, montre la forme attendue")
    rows = (("mon-projet/", "", 0), ("src/main.cpp", "", 1), ("include/secrets.h", "secrets.h : jamais partagé", 1), ("include/secrets.example.h", "secrets.example.h : sans valeurs", 1))
    for i, (name, role, level) in enumerate(rows):
        y = 40 + i * 36
        d.text(40 + level * 30, y, name, anchor="start", size=13, weight="700" if i == 2 else "600", color=ACCENT if i == 2 else INK)
        d.text(320, y, role, anchor="start", size=11, color=SOFT)
    return d


def m9_local():
    d = Drawing(560, 200, "Le serveur reste sur le réseau local : aucun accès entrant depuis Internet, aucune redirection de port sur la box")
    d.add(f'<rect x="30" y="30" width="330" height="140" rx="12" fill="#eef4f3" stroke="{ACCENT}" stroke-width="2" stroke-dasharray="6 4"/>')
    d.text(195, 52, "réseau local seulement", size=12, weight="600", color=ACCENT)
    block(d, 50, 80, 120, 50, "ESP32", size=12); block(d, 210, 80, 120, 50, "téléphone", size=12)
    block(d, 410, 80, 130, 50, "Internet", size=12); d.wire((360, 105), (410, 105), width=2)
    d.wire((375, 92), (395, 118), color=ACCENT, width=3); d.wire((395, 92), (375, 118), color=ACCENT, width=3)
    d.text(475, 160, "Internet : pas d'accès entrant", size=10, color=SOFT)
    return d


def m9_ouvertures():
    d = Drawing(560, 180, "Pour aller plus loin : le Bluetooth basse consommation, le cadre officiel ESP-IDF, le système temps réel FreeRTOS")
    for i, (name, detail) in enumerate((("BLE", "Bluetooth basse consommation"), ("ESP-IDF", "cadre officiel d'Espressif"), ("FreeRTOS", "système temps réel, tâches"))):
        x = 20 + i * 180
        block(d, x, 40, 160, 50, name, size=13); d.text(x + 80, 115, detail, size=10, color=SOFT)
    return d


def m9_freertos():
    d = Drawing(560, 170, "Sous Arduino, FreeRTOS fait déjà tourner deux tâches : le Wi-Fi sur le cœur 0, loop sur le cœur 1")
    block(d, 40, 50, 220, 60, "cœur 0 : Wi-Fi", size=12); block(d, 300, 50, 220, 60, "cœur 1 : loop()", size=12)
    d.text(280, 140, "FreeRTOS", size=12, weight="600", color=ACCENT)
    return d


def m9_tableau():
    d = Drawing(560, 200, "Mini-projet : un tableau de bord web ; le téléphone lit la tension du potentiomètre et commande la lampe 12 V")
    block(d, 20, 70, 130, 60, "téléphone", size=12); block(d, 210, 70, 130, 60, "ESP32", size=13)
    block(d, 400, 20, 140, 46, "potentiomètre", size=11); block(d, 400, 130, 140, 46, "lampe 12 V", size=12)
    d.arrow((150, 90), (208, 90), color=INK); d.arrow((208, 110), (150, 110), color=INK)
    d.wire((340, 85), (400, 45)); d.wire((340, 115), (400, 153))
    d.text(280, 190, "tableau de bord", size=11, color=ACCENT, weight="600")
    return d


def q_m9_route():
    d = Drawing(560, 260, "Montage commandé par un serveur web, sans légende des transistors")
    block(d, 20, 90, 140, 80, "ESP32", size=13)
    d.add(f'<rect x="20" y="20" width="200" height="56" rx="6" fill="#173f58"/>')
    d.text(30, 42, 'server.on("/on", ...)', anchor="start", size=11, color=PAPER); d.text(30, 64, "→ digitalWrite(26, HIGH)", anchor="start", size=11, color=PAPER)
    for i, (y, pin, load) in enumerate(((110, "GPIO 26", "lampe 12 V"), (170, "GPIO 27", "buzzer"))):
        d.wire((160, y), (300, y)); d.text(170, y - 5, pin, anchor="start", size=10, weight="600")
        block(d, 300, y - 20, 70, 40, "", size=11)
        d.wire((370, y), (420, y)); block(d, 420, y - 20, 120, 40, load, size=11)
        d.zone(f"q{i + 1}", 300, y - 20, 70, 40)
    d.zone("esp32", 20, 90, 140, 80); d.zone("lampe", 420, 90, 120, 40)
    return d


SECTION_DIAGRAMS = {
    1: [m1_composants, m1_chaine, m1_architecture, m1_bloc, m1_memoires, m1_carte, m1_alimentation, m1_brochage, m1_categories,
        m1_regle_tension, m1_masse_commune, m1_courant_broche, m1_outils, m1_projet, m1_setup_loop, m1_cablage, m1_televersement,
        m1_identite],
    2: [m2_niveaux, m2_sortie_interne, m2_led_montage, m2_led_calcul, m2_source, m2_puits, m2_blink,
        m2_blink_montage, m2_trois_niveaux, m2_broche_interne, m2_registres, m2_mosfet, m2_mosfet_etats, m2_feu, m2_feu_chrono, m2_carrefour],
    3: [m3_flottant, m3_seuils, m3_pull_down, m3_pullup_interne, m3_pull_up, m3_pulldown_interne, m3_lire_ecrire, m3_bouton_led, m3_rebonds,
        m3_antirebond, m3_front, m3_bascule, m3_etats, m3_veille, m3_diviseur_entree, m3_niveaux_5v, m3_feu_bouton],
    4: [m4_delay, m4_boucle_delay, m4_millis, m4_debordement, m4_sans_bloquer, m4_rythmes, m4_interruption, m4_isr_regles,
        m4_timer, m4_timer_chrono, m4_reaction],
    5: [m5_trame, m5_pont, m5_vitesses, m5_sorties, m5_ascii, m5_tampon, m5_commande, m5_trace, m5_serial2, m5_pupitre],
    6: [m6_adc, m6_adc_reel, m6_potentiometre, m6_mli, m6_mli_moyenne, m6_moteur_mli, m6_vitesse, m6_buzzer, m6_touch,
        m6_touch_valeurs, m6_dac, m6_dac_rampe, m6_variateur],
    7: [m7_bus, m7_horloge, m7_i2c, m7_trame_i2c, m7_oled, m7_oled_montage, m7_bme280, m7_scanner, m7_spi, m7_spi_chrono,
        m7_sd, m7_journal, m7_station],
    8: [m8_memoires, m8_survie, m8_nvs, m8_usure, m8_modes, m8_autonomie, m8_cycle, m8_reveil_timer, m8_reveils, m8_rtc_gpio,
        m8_rtc_data, m8_enregistreur],
    9: [m9_modes, m9_reseau, m9_connexion, m9_rssi, m9_requete, m9_routes, m9_commande, m9_page, m9_json, m9_secrets, m9_local,
        m9_ouvertures, m9_freertos, m9_tableau],
}
QUESTION_DIAGRAMS = {1: q_m1_flash, 2: q_m2_puits, 3: q_m3_pullup, 4: q_m4_sourd, 5: q_m5_tx, 6: q_m6_touch, 7: q_m7_tirages, 8: q_m8_ext0, 9: q_m9_route}

PARTS = {"p1": range(1, 4), "p2": range(4, 7), "p3": range(7, 10)}


def question_dir(module):
    """Dossier des schémas des questions sur schéma : content/esp32/<partie>/m<N>/schemas."""
    part = next((slug for slug, modules in PARTS.items() if module in modules), None)
    if part is None:
        raise ValueError(f"module {module} hors des parties 1 à 3")
    return ROOT / "content" / SLUG / part / f"m{module}" / "schemas"
