"""Schémas de la formation « Moteurs électriques et commande » (`moteurs`), tous originaux, symboles CEI (IEC 60617).

Usage : python -m tools.schemas moteurs
Écrit les schémas des sections dans static/content/moteurs/m<N>/ et ceux des questions sur schéma dans
content/moteurs/p<P>/m<N>/schemas/ (p1 pour les modules 1 à 3, p2 pour 4 à 6, p3 pour 7 à 9, p4 pour 10 à 12).
Réseau 230/400 V, 50 Hz ; schémas développés verticaux, puissance et commande séparées (M2).
"""
import math

from .common import ACCENT, INK, PAPER, ROOT, SOFT, Drawing, block, fmt, terminal, transformer

SLUG = "moteurs"

# Libellés anglais des schémas ; les virgules décimales restantes deviennent des points (tr).
EN = {
    # M1
    "perception": "perception", "non-lâcher": "cannot let go", "asphyxie": "breathing stops", "fibrillation": "fibrillation",
    "courant traversant le corps (mA)": "current through the body (mA)",
    "seuils indicatifs, 50 Hz, quelques secondes": "indicative thresholds, 50 Hz, a few seconds",
    "corps": "body", "main": "hand", "pieds": "feet", "sol": "ground", "phase": "phase",
    "I = 230 V / 1 000 Ω = 230 mA": "I = 230 V / 1,000 Ω = 230 mA",
    "arc": "arc", "conducteurs sous tension": "live conductors", "frontière d'arc": "arc flash boundary",
    "projection de métal fondu, chaleur, lumière, bruit": "molten metal, heat, light, noise",
    "écran facial": "face shield", "casque": "helmet", "vêtement ininflammable": "flame-resistant clothing",
    "gants isolants": "insulating gloves", "chaussures isolantes": "insulating shoes", "tapis isolant": "insulating mat",
    "défaut d'isolement": "insulation fault", "carcasse": "frame", "conducteur PE": "PE conductor", "prise de terre": "earth electrode",
    "courant de défaut": "fault current", "phase L": "line L", "neutre N": "neutral N", "tore": "toroid", "déclencheur": "trip",
    "I1 = I2 : rien": "I1 = I2: nothing", "I1 − I2 ≥ 30 mA : coupure": "I1 − I2 ≥ 30 mA: trip",
    "transformateur du distributeur": "supplier's transformer", "installation": "installation",
    "neutre à la terre": "neutral earthed", "masses à la terre": "frames earthed", "masses au neutre (PEN)": "frames to neutral (PEN)",
    "neutre isolé (ou impédant)": "neutral isolated (or impedance)", "contrôleur d'isolement": "insulation monitor",
    "TT : le DDR coupe au premier défaut": "TT: the RCD trips on the first fault",
    "TN : le disjoncteur coupe au premier défaut": "TN: the circuit breaker trips on the first fault",
    "IT : le premier défaut est signalé, pas coupé": "IT: the first fault is signalled, not cut",
    "1. séparer": "1. isolate", "2. condamner": "2. lock", "3. identifier": "3. identify", "4. vérifier": "4. verify",
    "5. mettre à la terre": "5. earth", "et en court-circuit": "and short-circuit",
    "sur une source connue": "on a known source", "sur l'équipement": "on the equipment", "de nouveau sur la source": "again on the source",
    "le VAT fonctionne": "the tester works", "absence de tension ?": "voltage absent?", "le VAT fonctionne encore": "the tester still works",
    "TBT": "ELV", "BT": "LV", "HTA": "HV-A", "HTB": "HV-B",
    "≤ 50 V alternatif": "≤ 50 V AC", "≤ 1 000 V alternatif": "≤ 1,000 V AC", "≤ 50 kV": "≤ 50 kV", "> 50 kV": "> 50 kV",
    "domaines de tension": "voltage ranges", "ce module : banc 24 V": "this module: 24 V bench", "moteurs : 400 V": "motors: 400 V",
    "symboles des schémas": "diagram symbols", "effets du courant": "effects of current", "installations BT": "LV installations",
    "appareillage BT": "LV switchgear", "équipement des machines": "machine equipment", "CEI (IEC) : normes internationales": "IEC: international standards",
    "adaptateur 230 V → 24 V CC": "230 V → 24 V DC adapter", "sectionneur": "isolator", "cadenas": "padlock", "étiquette": "tag", "lampe 24 V": "24 V lamp",
    # M2
    "commande": "control", "contact à fermeture": "make contact (NO)", "contact à ouverture": "break contact (NC)",
    "bouton marche": "start button", "bouton arrêt": "stop button", "bobine": "coil", "voyant": "indicator",
    "puissance": "power", "fusible": "fuse", "disjoncteur": "circuit breaker", "contact de contacteur": "contactor contact",
    "relais thermique": "overload relay", "moteur triphasé": "three-phase motor",
    "à fermeture": "make (NO)", "à ouverture": "break (NC)", "pôles de puissance": "power poles", "relais thermique : arrêt et signal": "overload relay: stop and signal",
    "plaque à bornes : entrées U1 V1 W1, sorties décalées W2 U2 V2": "terminal plate: inputs U1 V1 W1, outputs offset W2 U2 V2",
    "enroulement U": "winding U", "enroulement V": "winding V", "enroulement W": "winding W",
    "schéma de puissance": "power circuit", "schéma de commande": "control circuit", "arrêt": "stop", "marche": "start",
    "auto-maintien": "hold-in", "un trait = trois phases": "one line = three phases",
    "réseau 400 V": "400 V supply", "protection": "protection", "machine": "machine", "moteur": "motor",
    "étoile (Y)": "star (Y)", "triangle (Δ)": "delta (Δ)", "barrettes": "links",
    "chaque enroulement reçoit 400 / √3 = 230 V": "each winding gets 400 / √3 = 230 V", "chaque enroulement reçoit 230 V": "each winding gets 230 V",
    "réseau 400 V entre phases": "400 V line-to-line supply", "réseau 230 V entre phases": "230 V line-to-line supply",
    "tension supportée par un enroulement : 230 V": "voltage a winding can take: 230 V",
    "réseau 400 V → étoile": "400 V supply → star", "réseau 230 V → triangle": "230 V supply → delta",
    "MOTEUR ASYNCHRONE TRIPHASÉ": "THREE-PHASE INDUCTION MOTOR", "classe F": "class F", "service S1": "duty S1",
    "disjoncteur-moteur": "motor circuit breaker", "démarreur manuel": "manual starter", "bouton rotatif": "rotary knob",
    "démarreur télécommandé": "remote-controlled starter", "contacteur": "contactor", "boutons à distance": "remote buttons",
    "lampe H1": "lamp H1", "lampe H2": "lamp H2",
    # M3
    "centrale": "power plant", "transport": "transmission", "poste source": "primary substation", "distribution": "distribution",
    "poste HTA/BT": "HV/LV substation", "usine": "factory",
    "pertes en ligne (3 × R × I²) pour 100 kW": "line losses (3 × R × I²) for 100 kW", "pertes": "losses",
    "arrivée HTA 20 kV": "HV-A 20 kV incomer", "TGBT 400 V": "main LV board 400 V", "départ": "feeder", "éclairage": "lighting",
    "centre de commande des moteurs": "motor control centre", "tiroir": "drawer", "jeu de barres": "busbar",
    "P (active, kW)": "P (active, kW)", "Q (réactive, kvar)": "Q (reactive, kvar)", "S (apparente, kVA)": "S (apparent, kVA)",
    "avant": "before", "après": "after", "Qc fourni par les condensateurs": "Qc supplied by the capacitors",
    "TRANSFORMATEUR TRIPHASÉ": "THREE-PHASE TRANSFORMER", "charge (% de la puissance assignée)": "load (% of rated power)",
    "rendement (%)": "efficiency (%)", "maximum vers 40 %": "maximum around 40 %",
    "primaire en triangle (D)": "primary in delta (D)", "secondaire en étoile (y)": "secondary in star (y)", "neutre (n)": "neutral (n)",
    "tension simple V = 230 V": "phase voltage V = 230 V", "tension composée U = 400 V": "line voltage U = 400 V", "U = √3 × V": "U = √3 × V",
    "conducteur primaire": "primary conductor", "TC 200/5 A": "CT 200/5 A", "ampèremètre 5 A": "5 A ammeter",
    "transformateur de commande": "control transformer", "circuit de commande 24 V": "24 V control circuit",
    "adaptateur moulé 230 V → 12 V AC": "moulded 230 V → 12 V AC adapter",
    "1 440 tr/min": "1,440 rpm", "230/400 V : Δ sur 230 V, Y sur 400 V": "230/400 V: Δ on 230 V, Y on 400 V",
    "400/690 V : Δ sur 400 V": "400/690 V: Δ on 400 V", "avant : Q = 75 kvar": "before: Q = 75 kvar", "après : Q = 33 kvar": "after: Q = 33 kvar",
    "tiroir 1 : Q, KM, F → M1": "drawer 1: Q, KM, F → M1", "tiroir 2 : Q, KM, F → M2": "drawer 2: Q, KM, F → M2",
    "tiroir 3 : Q, KM, F → M3": "drawer 3: Q, KM, F → M3", "tiroir 4 : Q, KM, F → M4": "drawer 4: Q, KM, F → M4",
    "pertes à vide 1 kW": "no-load losses 1 kW", "pertes en charge 6,5 kW": "load losses 6.5 kW",
    "I = P / (√3 × U) : 144 A en 400 V, 2,9 A en 20 kV": "I = P / (√3 × U): 144 A at 400 V, 2.9 A at 20 kV",
    # M4 à M6
    "boutons": "buttons", "voyants": "indicators", "arrêt d'urgence": "emergency stop", "marche (de préférence)": "start (preferred)",
    "intervention anormale": "abnormal intervention", "danger, défaut": "danger, fault", "anormal, attention": "abnormal, caution",
    "normal, en marche": "normal, running", "action obligatoire": "mandatory action", "IEC 60204-1 : équipement électrique des machines": "IEC 60204-1: electrical equipment of machines",
    "manuel": "manual", "position": "position", "X : contact fermé": "X: contact closed", "déplacement": "travel", "fin de course": "limit switch",
    "contacts du fin de course": "limit switch contacts", "temps": "time", "pression (bar)": "pressure (bar)", "arrêt à 6 bar": "stop at 6 bar",
    "marche à 4 bar": "start at 4 bar", "hystérésis : 2 bar": "hysteresis: 2 bar", "capteur M18": "M18 sensor", "cible en acier": "steel target",
    "3 fils : brun, bleu, noir": "3 wires: brown, blue, black", "brun": "brown", "noir": "black", "bleu": "blue", "sortie : fil noir": "output: black wire",
    "barrage": "through-beam", "reflex": "retro-reflective", "proximité": "diffuse", "réflecteur": "reflector", "objet": "object",
    "capteur": "sensor", "aller": "out", "retour": "back", "température (°C)": "temperature (°C)", "résistance (Ω)": "resistance (Ω)",
    "138,5 Ω à 100 °C": "138.5 Ω at 100 °C", "disque à fentes": "slotted disc", "impulsions": "pulses", "fluide": "fluid",
    "bobine 24 V": "24 V coil", "noyau": "plunger", "360° / 200 pas = 1,8° par pas": "360° / 200 steps = 1.8° per step",
    "commande par impulsions": "pulse control", "position connue sans capteur": "position known without a sensor",
    "alimentation 24 V": "24 V supply", "brun +24 V, bleu 0 V, noir vers la LED": "brown +24 V, blue 0 V, black to the LED",
    "B : champ (N vers S)": "B: field (N to S)", "I : courant (vers vous)": "I: current (towards you)", "couple → rotation": "torque → rotation",
    "carcasse": "frame", "inducteur (pôles)": "field (poles)", "induit": "armature", "collecteur et balais": "commutator and brushes",
    "lames du collecteur": "commutator segments", "balais en carbone": "carbon brushes", "les balais s'usent : on les contrôle": "brushes wear: check them",
    "induit : 2 bornes": "armature: 2 terminals", "inducteur : aimants": "field: magnets", "petits moteurs : 6 à 48 V": "small motors: 6 to 48 V",
    "couple (N·m)": "torque (N·m)", "vitesse (tr/min)": "speed (rpm)", "inducteur série (gros fil)": "series field (thick wire)",
    "inducteur shunt": "shunt field", "(fil fin)": "(thin wire)", "fort couple au démarrage": "high starting torque",
    "vitesse presque constante": "almost constant speed", "temps (s)": "time (s)", "courant (× In)": "current (× In)", "I / In": "I / In",
    "sens horaire": "clockwise", "sens antihoraire": "anticlockwise", "tension (V)": "voltage (V)",
    "rapport cyclique 30 % → tension moyenne 3,6 V": "duty cycle 30 % → average voltage 3.6 V", "alimentation 12 V": "12 V supply",
    "tout le banc reste en 12 V": "the whole bench stays at 12 V", "champ tournant": "rotating field", "à 50 Hz : 3 000 tr/min": "at 50 Hz: 3,000 rpm",
    "pour une paire de pôles": "for one pole pair", "p = 1 (2 pôles)": "p = 1 (2 poles)", "p = 2 (4 pôles)": "p = 2 (4 poles)",
    "p = 3 (6 pôles)": "p = 3 (6 poles)", "p = 4 (8 pôles)": "p = 4 (8 poles)", "3 000 tr/min": "3,000 rpm", "1 500 tr/min": "1,500 rpm",
    "1 000 tr/min": "1,000 rpm", "750 tr/min": "750 rpm", "anneau": "end ring", "barres": "bars", "couple moteur": "motor torque",
    "couple (× Cn)": "torque (× Tn)", "nominal": "rated", "maximal": "maximum", "au démarrage ≈ 0,9 × Cn": "at start ≈ 0.9 × Tn",
    "bagues": "slip rings", "résistances de démarrage": "starting resistors", "synchrone": "synchronous", "asynchrone": "induction",
    "charge (× nominale)": "load (× rated)", "principal": "main", "auxiliaire": "auxiliary", "bague de déphasage": "shading ring",
    "petits ventilateurs, pompes": "small fans, pumps", "rendement faible": "low efficiency", "classe B": "class B", "classe H": "class H",
    "température maximale des enroulements": "maximum winding temperature", "charge": "load", "S1 : continu": "S1: continuous",
    "S3 : intermittent (40 %)": "S3: intermittent (40 %)", "aligné": "aligned", "décalage parallèle": "parallel offset", "défaut angulaire": "angular misalignment",
    "un défaut d'alignement use les roulements": "misalignment wears the bearings", "presse-étoupe": "cable gland", "boîte à bornes": "terminal box",
    "≈ 2,7 Ω": "≈ 2.7 Ω", "trois valeurs égales à quelques % près": "three values equal within a few %",
    "moteur ne démarre pas": "motor does not start", "tension aux bornes ?": "voltage at the terminals?", "protection déclenchée ?": "protection tripped?",
    "enroulements : résistances égales ?": "windings: equal resistances?", "isolement et roulements": "insulation and bearings",
    "mesures toujours": "always measure", "moteur consigné": "with the motor locked out", "moteur débranché": "motor disconnected", "charge": "load", "on ne touche jamais au côté 230 V": "never touch the 230 V side",
}


# --- Symboles CEI (IEC 60617), dessinés verticalement : chaque symbole va de (x, y) à (x, y + 44) ---------------------


def contact(d, x, y, kind="no", label=None, marks=None, tag=None):
    """Contact vertical. kind : no (fermeture), nc (ouverture), main (contacteur), breaker, isolator.
    marks : repères (haut, bas) écrits à gauche ; tag : nom de l'appareil (KM1, Q1…) écrit à droite."""
    d.wire((x, y), (x, y + 14)); d.wire((x, y + 30), (x, y + 44))
    if kind == "nc":
        d.wire((x, y + 14), (x + 11, y + 14)); d.wire((x, y + 30), (x + 11, y + 11))
    else:
        d.wire((x, y + 30), (x - 12, y + 12))
    if kind == "main":
        d.add(f'<path d="M{fmt(x - 5)} {fmt(y + 14)} a5 5 0 0 0 10 0" fill="none" stroke="{INK}" stroke-width="2"/>')
    elif kind == "breaker":
        d.wire((x - 5, y + 9), (x + 5, y + 19)); d.wire((x - 5, y + 19), (x + 5, y + 9))
    elif kind == "isolator":
        d.wire((x - 6, y + 14), (x + 6, y + 14))
    if marks:
        d.text(x - 8, y + 9, marks[0], anchor="end", size=11, color=SOFT)
        d.text(x - 8, y + 43, marks[1], anchor="end", size=11, color=SOFT)
    if tag:
        d.text(x + 16, y + 26, tag, anchor="start", weight="600", color=ACCENT)
    if label:
        d.text(x, y + 62, label, size=12)


def button(d, x, y, kind="no", label=None, marks=None, tag=None):
    """Bouton-poussoir : contact et organe de manœuvre (trait pointillé terminé par un T)."""
    contact(d, x, y, kind, label, marks, tag)
    mid = (x - 6, y + 21) if kind == "no" else (x + 5, y + 20)
    end = x - 26
    d.add(f'<line x1="{fmt(mid[0])}" y1="{fmt(mid[1])}" x2="{fmt(end)}" y2="{fmt(mid[1])}" stroke="{INK}" stroke-width="1.5" stroke-dasharray="3 3"/>')
    d.wire((end, mid[1] - 7), (end, mid[1] + 7))


def coil(d, x, y, label=None, tag=None):
    """Bobine de contacteur (rectangle), de (x, y) à (x, y + 44), bornes A1 en haut et A2 en bas."""
    d.wire((x, y), (x, y + 12)); d.wire((x, y + 32), (x, y + 44))
    d.add(f'<rect x="{fmt(x - 16)}" y="{fmt(y + 12)}" width="32" height="20" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>')
    d.text(x - 20, y + 9, "A1", anchor="end", size=11, color=SOFT); d.text(x - 20, y + 43, "A2", anchor="end", size=11, color=SOFT)
    if tag:
        d.text(x + 22, y + 27, tag, anchor="start", weight="600", color=ACCENT)
    if label:
        d.text(x, y + 62, label, size=12)


def indicator(d, x, y, label=None, tag=None):
    """Voyant (cercle barré d'une croix), de (x, y) à (x, y + 44)."""
    d.lamp((x, y), (x, y + 44))
    if tag:
        d.text(x + 20, y + 27, tag, anchor="start", weight="600", color=ACCENT)
    if label:
        d.text(x, y + 62, label, size=12)


def fuse(d, x, y, label=None, tag=None):
    d.wire((x, y), (x, y + 44))
    d.add(f'<rect x="{fmt(x - 7)}" y="{fmt(y + 8)}" width="14" height="28" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>')
    d.wire((x, y + 8), (x, y + 36))
    if tag:
        d.text(x + 14, y + 26, tag, anchor="start", weight="600", color=ACCENT)
    if label:
        d.text(x, y + 62, label, size=12)


def thermal(d, x, y, label=None, tag=None):
    """Élément thermique d'un relais de surcharge : rectangle et ligne brisée."""
    d.wire((x, y), (x, y + 8)); d.wire((x, y + 36), (x, y + 44))
    d.add(f'<rect x="{fmt(x - 9)}" y="{fmt(y + 8)}" width="18" height="28" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>')
    d.wire((x, y + 8), (x, y + 15), (x - 5, y + 15), (x - 5, y + 29), (x, y + 29), (x, y + 36))
    if tag:
        d.text(x + 16, y + 26, tag, anchor="start", weight="600", color=ACCENT)
    if label:
        d.text(x, y + 62, label, size=12)


def motor(d, cx, cy, r=26, phases="3~"):
    d.add(f'<circle cx="{fmt(cx)}" cy="{fmt(cy)}" r="{r}" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>')
    d.text(cx, cy - 2, "M", weight="700", size=15)
    d.text(cx, cy + 15, phases, size=12)


def three(d, x, y, symbol, gap=22, tag=None, link=True, **kw):
    """Trois pôles identiques côte à côte (schéma de puissance), reliés mécaniquement par un pointillé."""
    for k in range(3):
        symbol(d, x + gap * k, y, **kw)
    if link:
        d.add(f'<line x1="{fmt(x - 6)}" y1="{fmt(y + 21)}" x2="{fmt(x + 2 * gap)}" y2="{fmt(y + 21)}" stroke="{INK}" stroke-width="1.5" stroke-dasharray="3 3"/>')
    if tag:
        d.text(x + 2 * gap + 14, y + 26, tag, anchor="start", weight="600", color=ACCENT)


def person(d, x, y, scale=1.0, color=INK):
    """Silhouette schématique (tête, tronc, bras, jambes) ; (x, y) = sommet de la tête."""
    s = scale
    d.add(f'<circle cx="{fmt(x)}" cy="{fmt(y + 10 * s)}" r="{fmt(10 * s)}" fill="{PAPER}" stroke="{color}" stroke-width="2"/>')
    d.wire((x, y + 20 * s), (x, y + 62 * s), color=color)
    d.wire((x - 26 * s, y + 34 * s), (x, y + 28 * s), (x + 26 * s, y + 34 * s), color=color)
    d.wire((x - 16 * s, y + 100 * s), (x, y + 62 * s), (x + 16 * s, y + 100 * s), color=color)


def bars(d, x, y, w, h, items, vmax, unit_label, log=False):
    """Barres horizontales : items = [(libellé, valeur, texte de valeur)]."""
    import math
    row = h / len(items)
    for k, (label, value, shown) in enumerate(items):
        top = y + k * row + 6
        frac = (math.log10(value) + 1) / (math.log10(vmax) + 1) if log else value / vmax
        d.add(f'<rect x="{fmt(x)}" y="{fmt(top)}" width="{fmt(w * frac)}" height="{fmt(row - 14)}" rx="4" fill="{ACCENT}" opacity="{0.35 + 0.65 * (k + 1) / len(items):.2f}"/>')
        d.text(x - 8, top + row / 2 - 2, label, anchor="end", size=12, weight="600")
        d.text(x + w * frac + 8, top + row / 2 - 2, shown, anchor="start", size=12, color=ACCENT, weight="600")
    d.text(x + w / 2, y + h + 18, unit_label, size=11, color=SOFT)


def chain(d, x, y, labels, w=96, h=44, gap=22, size=11):
    for k, label in enumerate(labels):
        bx = x + k * (w + gap)
        block(d, bx, y, w, h, label, size=size)
        if k < len(labels) - 1:
            d.arrow((bx + w, y + h / 2), (bx + w + gap, y + h / 2), color=INK)


# --- Module 1 : la sécurité électrique --------------------------------------------------------------------------------


def m1_seuils():
    d = Drawing(560, 250, "Seuils indicatifs des effets d'un courant alternatif 50 Hz traversant le corps, de la perception à la fibrillation")
    bars(d, 150, 20, 300, 176, [("perception", 0.5, "0,5 mA"), ("non-lâcher", 10, "10 mA"), ("asphyxie", 30, "30 mA"),
                                ("fibrillation", 75, "75 mA")], 100, "courant traversant le corps (mA)", log=True)
    d.text(280, 236, "seuils indicatifs, 50 Hz, quelques secondes", size=11, color=SOFT)
    return d


def m1_corps():
    d = Drawing(520, 270, "Contact direct : le courant passe par la main, le corps et les pieds, puis revient à la source par le sol")
    d.ac_source((70, 200), (70, 80), "230 V", side=-1)
    d.wire((70, 80), (70, 50), (230, 50), (230, 90))
    d.text(150, 40, "phase", size=12, color=SOFT)
    person(d, 300, 70, scale=1.2)
    d.wire((230, 90), (269, 111), color=ACCENT)
    d.text(240, 125, "main", size=11, color=SOFT)
    d.resistor((380, 70), (380, 190), "corps", "≈ 1 kΩ")
    d.wire((300, 190), (300, 225), (70, 225), (70, 200)); d.ground((300, 225))
    d.text(300, 262, "I = 230 V / 1 000 Ω = 230 mA", weight="600", color=ACCENT)
    d.text(330, 208, "pieds", size=11, color=SOFT)
    return d


def m1_arc():
    d = Drawing(520, 240, "Arc électrique entre deux conducteurs sous tension et frontière d'arc à ne pas franchir sans équipement")
    d.add(f'<rect x="60" y="60" width="16" height="120" fill="#dfe8ea" stroke="{INK}" stroke-width="2"/>')
    d.add(f'<rect x="140" y="60" width="16" height="120" fill="#dfe8ea" stroke="{INK}" stroke-width="2"/>')
    d.add(f'<polyline points="76,110 92,100 100,122 112,98 122,124 140,112" fill="none" stroke="{ACCENT}" stroke-width="3"/>')
    d.text(108, 50, "arc", weight="700", color=ACCENT)
    d.text(108, 200, "conducteurs sous tension", size=12)
    d.add(f'<line x1="290" y1="40" x2="290" y2="200" stroke="{SOFT}" stroke-dasharray="6 4" stroke-width="2"/>')
    d.arrow((160, 150), (288, 150), "frontière d'arc", color=INK, offset=(0, -10))
    person(d, 420, 50, scale=1.0, color=SOFT)
    d.text(260, 228, "projection de métal fondu, chaleur, lumière, bruit", size=11, color=SOFT)
    return d


def m1_epi():
    d = Drawing(520, 260, "Équipements de protection individuelle pour un travail au voisinage de pièces nues sous tension")
    person(d, 260, 30, scale=1.8)
    items = [("casque", (160, 36), (246, 40)), ("écran facial", (160, 70), (250, 58)), ("gants isolants", (150, 130), (215, 120)),
             ("vêtement ininflammable", (370, 100), (275, 100)), ("chaussures isolantes", (370, 210), (280, 210)), ("tapis isolant", (150, 236), (230, 236))]
    for label, at, to in items:
        d.text(at[0], at[1], label, anchor="end" if at[0] < 260 else "start", size=12, weight="600")
        d.wire((at[0] + (6 if at[0] < 260 else -6), at[1] - 4), to, color=SOFT, width=1.5)
    d.wire((200, 240), (320, 240), color=ACCENT, width=5)
    return d


def m1_defaut():
    d = Drawing(560, 270, "Défaut d'isolement : la phase touche la carcasse du moteur ; le conducteur PE ramène le courant de défaut à la terre")
    d.wire((40, 40), (200, 40)); d.text(30, 45, "L", anchor="end", weight="600")
    d.wire((40, 70), (200, 70)); d.text(30, 75, "N", anchor="end", weight="600")
    d.add(f'<rect x="200" y="30" width="150" height="110" rx="10" fill="#eef4f3" stroke="{INK}" stroke-width="2"/>')
    d.text(275, 130, "carcasse", size=12, color=SOFT)
    motor(d, 275, 82)
    d.add(f'<polyline points="220,40 232,58 222,62 236,82" fill="none" stroke="{ACCENT}" stroke-width="3"/>')
    d.text(130, 105, "défaut d'isolement", size=12, color=ACCENT, weight="600")
    d.wire((350, 120), (420, 120), (420, 210), color=ACCENT); d.ground((420, 210))
    d.text(430, 160, "conducteur PE", anchor="start", size=12, weight="600", color=ACCENT)
    d.text(420, 250, "prise de terre", size=12)
    person(d, 150, 150, scale=0.8, color=SOFT)
    d.arrow((420, 140), (420, 190), "courant de défaut", offset=(-70, 0))
    return d


def m1_ddr():
    d = Drawing(540, 250, "Principe du DDR : un tore compare le courant aller et le courant retour ; au-delà de 30 mA d'écart, il coupe")
    d.wire((40, 80), (480, 80)); d.wire((40, 160), (480, 160))
    d.text(30, 85, "L", anchor="end", weight="600"); d.text(30, 165, "N", anchor="end", weight="600")
    d.add(f'<ellipse cx="200" cy="120" rx="22" ry="62" fill="none" stroke="{ACCENT}" stroke-width="5"/>')
    d.text(200, 46, "tore", weight="600", color=ACCENT)
    d.arrow((90, 68), (150, 68), "I1", offset=(0, -6)); d.arrow((150, 172), (90, 172), "I2", offset=(0, 18))
    d.wire((222, 120), (300, 120), color=SOFT); block(d, 300, 100, 92, 40, "déclencheur", size=11)
    d.text(270, 214, "I1 = I2 : rien", size=12)
    d.text(270, 236, "I1 − I2 ≥ 30 mA : coupure", size=12, weight="600", color=ACCENT)
    return d


def _earthing(d, system):
    d.text(40, 34, "transformateur du distributeur", anchor="start", size=11, color=SOFT)
    for k, name in enumerate(("L1", "L2", "L3", "N")):
        y = 60 + 26 * k
        d.wire((150, y), (420, y)); d.text(430, y + 4, name if not (system == "TN" and name == "N") else "PEN", anchor="start", size=11, weight="600")
    d.add(f'<rect x="40" y="48" width="100" height="100" rx="8" fill="#eef4f3" stroke="{INK}" stroke-width="2"/>')
    d.wire((140, 138), (150, 138))
    d.add(f'<rect x="300" y="170" width="90" height="46" rx="8" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>')
    d.text(345, 198, "installation", size=11)
    d.wire((345, 60), (345, 170))
    for k in range(4):
        d.dot((345, 60 + 26 * k))
    if system == "IT":
        d.wire((90, 148), (90, 170)); d.add(f'<rect x="80" y="170" width="20" height="26" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>')
        d.wire((90, 196), (90, 214)); d.ground((90, 214))
        d.text(110, 188, "neutre isolé (ou impédant)", anchor="start", size=11, color=SOFT)
    else:
        d.wire((90, 148), (90, 214)); d.ground((90, 214)); d.text(100, 200, "neutre à la terre", anchor="start", size=11, color=SOFT)
    if system == "TN":
        d.wire((390, 192), (410, 192), (410, 138), color=ACCENT); d.text(300, 242, "masses au neutre (PEN)", size=11, weight="600", color=ACCENT)
    else:
        d.wire((390, 192), (460, 192), (460, 214), color=ACCENT); d.ground((460, 214))
        d.text(360, 252, "masses à la terre", size=11, weight="600", color=ACCENT)


def m1_tt():
    d = Drawing(520, 280, "Schéma TT : neutre du transformateur et masses de l'installation reliés à deux prises de terre distinctes")
    _earthing(d, "TT")
    d.text(260, 272, "TT : le DDR coupe au premier défaut", weight="600")
    return d


def m1_tn():
    d = Drawing(520, 280, "Schéma TN : les masses sont reliées au neutre par le conducteur PEN ; un défaut devient un court-circuit")
    _earthing(d, "TN")
    d.text(260, 272, "TN : le disjoncteur coupe au premier défaut", weight="600")
    return d


def m1_it():
    d = Drawing(520, 280, "Schéma IT : neutre isolé ou relié par une impédance ; le premier défaut est seulement signalé")
    _earthing(d, "IT")
    d.text(260, 272, "IT : le premier défaut est signalé, pas coupé", weight="600")
    return d


def m1_etapes():
    d = Drawing(680, 160, "Les cinq étapes de la consignation : séparer, condamner, identifier, vérifier l'absence de tension, mettre à la terre")
    chain(d, 14, 40, ("1. séparer", "2. condamner", "3. identifier", "4. vérifier", "5. mettre à la terre"), w=124, gap=13, size=12)
    d.text(608, 108, "et en court-circuit", size=11, color=SOFT)
    return d


def m1_vat():
    d = Drawing(620, 170, "Vérifier l'absence de tension : essayer le VAT sur une source connue, mesurer, puis l'essayer de nouveau")
    for k, (top, bottom) in enumerate((("sur une source connue", "le VAT fonctionne"), ("sur l'équipement", "absence de tension ?"),
                                       ("de nouveau sur la source", "le VAT fonctionne encore"))):
        x = 20 + 200 * k
        block(d, x, 40, 180, 50, top, size=12)
        d.text(x + 90, 118, bottom, size=12, weight="600", color=ACCENT if k == 1 else INK)
        if k < 2:
            d.arrow((x + 180, 65), (x + 200, 65), color=INK)
    return d


def m1_domaines():
    d = Drawing(560, 230, "Domaines de tension en alternatif : TBT jusqu'à 50 V, BT jusqu'à 1 000 V, puis HTA et HTB")
    spans = (("TBT", "≤ 50 V alternatif", 70), ("BT", "≤ 1 000 V alternatif", 150), ("HTA", "≤ 50 kV", 110), ("HTB", "> 50 kV", 110))
    x = 50
    for k, (name, rule, w) in enumerate(spans):
        d.add(f'<rect x="{x}" y="60" width="{w}" height="50" fill="{ACCENT}" opacity="{0.25 + 0.2 * k:.2f}" stroke="{INK}" stroke-width="1.5"/>')
        d.text(x + w / 2, 91, name, weight="700")
        d.text(x + w / 2, 132, rule, size=11, color=SOFT)
        x += w
    d.text(280, 40, "domaines de tension", weight="600")
    d.arrow((85, 180), (85, 145), color=ACCENT); d.text(85, 198, "ce module : banc 24 V", size=12, weight="600", color=ACCENT)
    d.arrow((260, 180), (260, 145), color=ACCENT); d.text(260, 216, "moteurs : 400 V", size=12, weight="600", color=ACCENT)
    return d


def m1_normes():
    d = Drawing(600, 250, "Normes internationales CEI utiles au travail sur les moteurs : symboles, effets du courant, installations, appareillage, machines")
    block(d, 170, 20, 260, 44, "CEI (IEC) : normes internationales", size=12)
    items = (("IEC 60617", "symboles des schémas"), ("IEC 60479", "effets du courant"), ("IEC 60364", "installations BT"),
             ("IEC 60947", "appareillage BT"), ("IEC 60204-1", "équipement des machines"))
    for k, (code, what) in enumerate(items):
        x = 10 + 118 * k
        d.wire((300, 64), (300, 90), (x + 52, 90), (x + 52, 110), color=SOFT, width=1.5)
        block(d, x, 110, 104, 40, code, size=12)
        d.text(x + 52, 172, what, size=11)
    return d


def m1_banc():
    d = Drawing(560, 230, "Banc de consignation 24 V : adaptateur, sectionneur cadenassable et lampe")
    block(d, 10, 70, 190, 60, "adaptateur 230 V → 24 V CC", size=12)
    d.wire((200, 85), (230, 85)); d.wire((200, 115), (230, 115))
    d.add(f'<rect x="230" y="50" width="90" height="100" rx="8" fill="#eef4f3" stroke="{INK}" stroke-width="2"/>')
    d.text(275, 170, "sectionneur", size=12, weight="600")
    d.add(f'<path d="M262 100 v-12 a13 13 0 0 1 26 0 v12" fill="none" stroke="{ACCENT}" stroke-width="3"/><rect x="256" y="100" width="38" height="28" rx="4" fill="{ACCENT}"/>')
    d.text(340, 60, "cadenas", anchor="start", size=12, color=ACCENT, weight="600")
    d.add(f'<rect x="250" y="190" width="50" height="26" rx="3" fill="#fff0c2" stroke="{INK}" stroke-width="1.5"/>')
    d.text(310, 208, "étiquette", anchor="start", size=12)
    d.wire((320, 85), (450, 85), (450, 92)); d.lamp((450, 92), (450, 120)); d.wire((450, 120), (450, 115), (320, 115))
    d.text(470, 110, "lampe 24 V", anchor="start", size=12)
    return d


# --- Module 2 : lire les schémas et les plaques signalétiques ---------------------------------------------------------


def m2_symboles_commande():
    d = Drawing(720, 200, "Symboles CEI du circuit de commande : contacts à fermeture et à ouverture, boutons-poussoirs, bobine, voyant")
    contact(d, 70, 40, "no", "contact à fermeture"); contact(d, 190, 40, "nc", "contact à ouverture")
    button(d, 330, 40, "no", "bouton marche"); button(d, 450, 40, "nc", "bouton arrêt")
    coil(d, 560, 40, "bobine"); indicator(d, 660, 40, "voyant")
    d.text(360, 180, "commande", weight="700", color=ACCENT)
    return d


def m2_symboles_puissance():
    d = Drawing(740, 210, "Symboles CEI du circuit de puissance : fusible, disjoncteur, sectionneur, contact de contacteur, relais thermique, moteur")
    fuse(d, 60, 40, "fusible"); contact(d, 170, 40, "breaker", "disjoncteur"); contact(d, 280, 40, "isolator", "sectionneur")
    contact(d, 410, 40, "main", "contact de contacteur"); thermal(d, 545, 40, "relais thermique")
    motor(d, 665, 62); d.text(665, 122, "moteur triphasé", size=12)
    d.text(370, 190, "puissance", weight="700", color=ACCENT)
    return d


def m2_contacts():
    d = Drawing(600, 220, "Repérage CEI des contacts : 1-2 pour la puissance, 13-14 à fermeture, 21-22 à ouverture, A1-A2 bobine, 95-96 et 97-98 relais thermique")
    three(d, 50, 40, contact, kind="main", tag=None)
    for k, (top, bottom) in enumerate((("1", "2"), ("3", "4"), ("5", "6"))):
        d.text(50 + 22 * k, 34, top, size=11, color=SOFT); d.text(50 + 22 * k, 100, bottom, size=11, color=SOFT)
    d.text(72, 130, "pôles de puissance", size=12)
    contact(d, 210, 40, "no", "à fermeture", marks=("13", "14")); contact(d, 300, 40, "nc", "à ouverture", marks=("21", "22"))
    coil(d, 390, 40, "bobine")
    contact(d, 490, 40, "nc", marks=("95", "96")); contact(d, 550, 40, "no", marks=("97", "98"))
    d.text(520, 130, "relais thermique : arrêt et signal", size=11)
    return d


def m2_bornes():
    d = Drawing(520, 230, "Plaque à bornes d'un moteur triphasé : entrées U1 V1 W1 en haut, sorties W2 U2 V2 décalées en bas")
    for k, (top, bottom) in enumerate((("U1", "W2"), ("V1", "U2"), ("W1", "V2"))):
        x = 160 + 100 * k
        terminal(d, (x, 60)); terminal(d, (x, 140))
        d.text(x, 44, top, weight="700", color=ACCENT); d.text(x, 170, bottom, weight="700", color=ACCENT)
    d.add(f'<rect x="130" y="30" width="260" height="150" rx="10" fill="none" stroke="{INK}" stroke-width="2"/>')
    d.text(260, 212, "plaque à bornes : entrées U1 V1 W1, sorties décalées W2 U2 V2", size=11, color=SOFT)
    return d


def m2_puissance():
    d = Drawing(420, 400, "Schéma de puissance d'un démarrage direct : sectionneur Q1, contacteur KM1, relais thermique F1, moteur M1")
    for k, name in enumerate(("L1", "L2", "L3")):
        d.text(120 + 30 * k, 26, name, weight="600")
        d.wire((120 + 30 * k, 34), (120 + 30 * k, 60))
    three(d, 120, 60, contact, gap=30, tag="Q1", kind="isolator")
    for k in range(3):
        d.wire((120 + 30 * k, 104), (120 + 30 * k, 130))
    three(d, 120, 130, contact, gap=30, tag="KM1", kind="main")
    for k in range(3):
        d.wire((120 + 30 * k, 174), (120 + 30 * k, 200))
    three(d, 120, 200, thermal, gap=30, tag="F1", link=False)
    for k in range(3):
        d.wire((120 + 30 * k, 244), (120 + 30 * k, 270), (150, 300 if k != 1 else 300))
    motor(d, 150, 326); d.text(190, 330, "M1", anchor="start", weight="600", color=ACCENT)
    d.text(210, 390, "schéma de puissance", weight="600")
    return d


def m2_commande():
    d = Drawing(420, 420, "Schéma de commande d'un démarrage direct : arrêt S1, marche S2 doublé par le contact d'auto-maintien KM1, bobine KM1")
    d.text(150, 24, "24 V", weight="600")
    fuse(d, 150, 34, tag="F2")
    contact(d, 150, 78, "nc", marks=("95", "96"), tag="F1")
    button(d, 150, 122, "nc", marks=("1", "2"), tag="S1")
    d.wire((150, 166), (150, 180), (230, 180), (230, 194)); d.dot((150, 180))
    button(d, 150, 180, "no", marks=("3", "4"), tag="S2")
    contact(d, 230, 194, "no", marks=("13", "14"), tag="KM1")
    d.wire((230, 238), (230, 254), (150, 254)); d.wire((150, 224), (150, 270)); d.dot((150, 254))
    coil(d, 150, 270, tag="KM1")
    d.wire((150, 314), (150, 340)); d.text(150, 356, "0 V", weight="600")
    d.text(60, 150, "arrêt", anchor="end", size=12, color=SOFT); d.text(60, 208, "marche", anchor="end", size=12, color=SOFT)
    d.text(300, 222, "auto-maintien", anchor="start", size=12, color=ACCENT, weight="600")
    d.text(210, 405, "schéma de commande", weight="600")
    return d


def m2_unifilaire():
    d = Drawing(560, 200, "Schéma unifilaire d'un départ moteur : un seul trait barré de trois traits représente les trois phases")
    d.wire((30, 90), (530, 90), width=2.5)
    for x in (60, 470):
        for k in range(3):
            d.wire((x + 6 * k - 6, 98), (x + 6 * k + 2, 82))
    block(d, 100, 66, 90, 48, "Q1", size=12); block(d, 220, 66, 90, 48, "KM1", size=12); block(d, 340, 66, 90, 48, "F1", size=12)
    motor(d, 510, 90, r=22)
    d.text(280, 160, "un trait = trois phases", size=12, color=SOFT)
    return d


def m2_synoptique():
    d = Drawing(620, 150, "Schéma synoptique d'un départ moteur : réseau, protection, commande, moteur, machine")
    chain(d, 12, 50, ("réseau 400 V", "protection", "commande", "moteur", "machine"), w=104, gap=18, size=12)
    return d


def _plate(d, x0, coupling):
    tops, bottoms = ("U1", "V1", "W1"), ("W2", "U2", "V2")
    for k in range(3):
        x = x0 + 60 * k
        terminal(d, (x, 70)); terminal(d, (x, 140))
        d.text(x, 56, tops[k], size=12, weight="700"); d.text(x, 166, bottoms[k], size=12, weight="700")
    d.add(f'<rect x="{x0 - 30}" y="40" width="180" height="140" rx="10" fill="none" stroke="{INK}" stroke-width="2"/>')
    if coupling == "Y":
        d.wire((x0, 140), (x0 + 120, 140), color=ACCENT, width=6)
    else:
        for k in range(3):
            d.wire((x0 + 60 * k, 70), (x0 + 60 * k, 140), color=ACCENT, width=6)


def m2_etoile():
    d = Drawing(480, 250, "Couplage étoile : une barrette relie W2, U2 et V2 ; chaque enroulement reçoit 400 / √3 = 230 V")
    _plate(d, 180, "Y")
    d.text(240, 22, "étoile (Y)", weight="700", color=ACCENT)
    d.text(240, 212, "réseau 400 V entre phases", size=12)
    d.text(240, 236, "chaque enroulement reçoit 400 / √3 = 230 V", size=12, weight="600")
    return d


def m2_triangle():
    d = Drawing(480, 250, "Couplage triangle : trois barrettes verticales ; chaque enroulement reçoit la tension entre phases, 230 V")
    _plate(d, 180, "D")
    d.text(240, 22, "triangle (Δ)", weight="700", color=ACCENT)
    d.text(240, 212, "réseau 230 V entre phases", size=12)
    d.text(240, 236, "chaque enroulement reçoit 230 V", size=12, weight="600")
    return d


def m2_plaque():
    d = Drawing(540, 270, "Plaque signalétique d'un moteur asynchrone triphasé de 2,2 kW, 230/400 V, 1 440 tr/min")
    d.add(f'<rect x="40" y="20" width="460" height="230" rx="12" fill="#eef4f3" stroke="{INK}" stroke-width="2"/>')
    d.text(270, 50, "MOTEUR ASYNCHRONE TRIPHASÉ", weight="700")
    rows = (("230 V Δ / 400 V Y", "8,3 A / 4,8 A"), ("2,2 kW", "1 440 tr/min"), ("cos φ 0,81", "50 Hz"),
            ("η 82 %", "IP55"), ("classe F", "service S1"))
    for k, (left, right) in enumerate(rows):
        y = 88 + 34 * k
        d.text(70, y, left, anchor="start", size=13, weight="600"); d.text(470, y, right, anchor="end", size=13, weight="600")
        d.wire((60, y + 12), (480, y + 12), color=SOFT, width=1)
    return d


def m2_tensions():
    d = Drawing(560, 210, "Choisir le couplage : un enroulement supporte 230 V ; sur un réseau 400 V on couple en étoile, sur 230 V en triangle")
    block(d, 150, 20, 260, 44, "tension supportée par un enroulement : 230 V", size=11)
    d.wire((280, 64), (280, 84), (150, 84), (150, 110), color=SOFT); d.wire((280, 84), (410, 84), (410, 110), color=SOFT)
    block(d, 40, 110, 220, 50, "réseau 400 V → étoile", size=12); block(d, 300, 110, 220, 50, "réseau 230 V → triangle", size=12)
    d.text(150, 190, "230/400 V : Δ sur 230 V, Y sur 400 V", size=11, color=SOFT)
    d.text(410, 190, "400/690 V : Δ sur 400 V", size=11, color=SOFT)
    return d


def m2_manuel():
    d = Drawing(400, 330, "Démarreur manuel : un disjoncteur-moteur Q1 à bouton rotatif protège et commande directement le moteur")
    for k in range(3):
        d.wire((140 + 30 * k, 30), (140 + 30 * k, 70))
    three(d, 140, 70, contact, gap=30, kind="breaker")
    for k in range(3):
        d.wire((140 + 30 * k, 114), (140 + 30 * k, 124))
    three(d, 140, 124, thermal, gap=30, link=False, tag="Q1")
    for k in range(3):
        d.wire((140 + 30 * k, 168), (140 + 30 * k, 190), (170, 220))
    motor(d, 170, 246)
    d.text(80, 92, "bouton rotatif", anchor="end", size=12, color=SOFT)
    d.text(200, 310, "disjoncteur-moteur", weight="600"); d.text(200, 290, "démarreur manuel", size=12, color=SOFT)
    return d


def m2_telecommande():
    d = Drawing(560, 200, "Démarreur télécommandé : contacteur et relais thermique, pilotés à distance par des boutons marche et arrêt")
    block(d, 30, 70, 110, 50, "disjoncteur", size=12); block(d, 170, 70, 110, 50, "contacteur", size=12); block(d, 310, 70, 110, 50, "relais thermique", size=11)
    d.arrow((140, 95), (170, 95), color=INK); d.arrow((280, 95), (310, 95), color=INK); d.arrow((420, 95), (466, 95), color=INK)
    motor(d, 492, 95, r=24)
    block(d, 170, 150, 110, 36, "boutons à distance", size=11)
    d.add(f'<line x1="225" y1="150" x2="225" y2="120" stroke="{ACCENT}" stroke-width="2" stroke-dasharray="4 3"/>')
    d.text(280, 40, "démarreur télécommandé", weight="600")
    return d


def m2_lampes():
    d = Drawing(460, 300, "Circuit 24 V du mini-projet : S1 allume H1 ; S2 à ouverture éteint H2 quand on l'actionne")
    d.text(60, 30, "+24 V", weight="600"); d.wire((60, 40), (380, 40))
    for x, kind, tag, lamp in ((140, "no", "S1", "lampe H1"), (300, "nc", "S2", "lampe H2")):
        d.wire((x, 40), (x, 70)); button(d, x, 70, kind, tag=tag); d.wire((x, 114), (x, 140)); indicator(d, x, 140, lamp)
        d.wire((x, 184), (x, 240))
    d.wire((60, 240), (380, 240)); d.text(60, 262, "0 V", weight="600")
    return d


# --- Module 3 : transformateurs et distribution ----------------------------------------------------------------------


def m3_chaine():
    d = Drawing(700, 200, "De la centrale à l'usine : transport à très haute tension, poste source, distribution HTA, poste de transformation, 400 V")
    chain(d, 8, 40, ("centrale", "transport", "poste source", "distribution", "poste HTA/BT", "usine"), w=100, gap=18, size=12)
    for k, voltage in enumerate(("20 kV", "400 kV", "→ 20 kV", "20 kV", "→ 400 V", "400 V")):
        d.text(58 + 118 * k, 110, voltage, size=12, weight="600", color=ACCENT)
    return d


def m3_pertes_ligne():
    d = Drawing(560, 210, "Pertes en ligne pour transporter 100 kW, 0,1 Ω par conducteur : 6,25 kW en 400 V, 2,5 W en 20 kV")
    bars(d, 120, 30, 320, 110, [("400 V", 6250, "6,25 kW"), ("20 kV", 2.5, "2,5 W")], 10000, "pertes en ligne (3 × R × I²) pour 100 kW", log=True)
    d.text(280, 190, "I = P / (√3 × U) : 144 A en 400 V, 2,9 A en 20 kV", size=12, color=SOFT)
    return d


def m3_poste():
    d = Drawing(560, 300, "Poste de transformation d'une usine : arrivée HTA 20 kV, transformateur 630 kVA, TGBT 400 V et ses départs")
    d.text(150, 26, "arrivée HTA 20 kV", weight="600")
    d.wire((150, 34), (150, 60)); contact(d, 150, 60, "isolator")
    d.wire((150, 104), (150, 118))
    d.add(f'<circle cx="150" cy="134" r="16" fill="none" stroke="{INK}" stroke-width="2"/><circle cx="150" cy="156" r="16" fill="none" stroke="{INK}" stroke-width="2"/>')
    d.text(176, 150, "630 kVA", anchor="start", weight="600", color=ACCENT)
    d.wire((150, 172), (150, 200)); d.wire((60, 200), (500, 200), width=4); d.text(500, 190, "TGBT 400 V", anchor="end", size=12, weight="600")
    for k, label in enumerate(("moteur", "moteur", "éclairage", "départ")):
        x = 100 + 110 * k
        d.wire((x, 200), (x, 214)); contact(d, x, 214, "breaker"); d.wire((x, 258), (x, 270))
        d.text(x, 288, label, size=11)
    return d


def m3_mcc():
    d = Drawing(520, 280, "Centre de commande des moteurs : un jeu de barres alimente des tiroirs, chacun équipé d'un départ moteur complet")
    d.add(f'<rect x="80" y="20" width="360" height="240" rx="8" fill="#eef4f3" stroke="{INK}" stroke-width="2"/>')
    d.wire((100, 40), (100, 240), color=ACCENT, width=5); d.text(112, 34, "jeu de barres", anchor="start", size=11, color=ACCENT, weight="600")
    for k in range(4):
        y = 50 + 50 * k
        d.add(f'<rect x="140" y="{y}" width="270" height="40" rx="5" fill="{PAPER}" stroke="{INK}" stroke-width="1.5"/>')
        d.text(160, y + 25, f"tiroir {k + 1} : Q, KM, F → M{k + 1}", anchor="start", size=12)
        d.wire((100, y + 20), (140, y + 20))
    d.text(260, 275, "centre de commande des moteurs", size=12, weight="600")
    return d


def m3_triangle():
    d = Drawing(520, 270, "Triangle des puissances : P active, Q réactive, S apparente ; cos φ = P / S")
    d.wire((80, 210), (400, 210), color=ACCENT, width=3); d.wire((400, 210), (400, 60), color=INK, width=3); d.wire((80, 210), (400, 60), color=INK, width=3)
    d.text(240, 236, "P (active, kW)", weight="600", color=ACCENT)
    d.text(412, 140, "Q (réactive, kvar)", anchor="start", weight="600")
    d.text(200, 118, "S (apparente, kVA)", anchor="end", weight="600")
    d.add(f'<path d="M140 210 A60 60 0 0 0 134 185" fill="none" stroke="{ACCENT}" stroke-width="2"/>')
    d.text(150, 196, "φ", anchor="start", weight="700", color=ACCENT)
    d.text(260, 30, "S² = P² + Q²   cos φ = P / S", weight="600")
    return d


def m3_compensation():
    d = Drawing(560, 290, "Compensation : des condensateurs fournissent Qc ; Q passe de 75 à 33 kvar pour 100 kW, cos φ de 0,8 à 0,95")
    x0, y0, k = 80, 250, 2.6  # 1 kW = 2,6 px
    d.wire((x0, y0), (x0 + 100 * k, y0), color=ACCENT, width=3); d.text(x0 + 50 * k, y0 + 24, "P = 100 kW", weight="600", color=ACCENT)
    d.wire((x0 + 100 * k, y0), (x0 + 100 * k, y0 - 75 * k), width=3); d.wire((x0, y0), (x0 + 100 * k, y0 - 75 * k), color=SOFT, width=2)
    d.wire((x0, y0), (x0 + 100 * k, y0 - 33 * k), width=3)
    d.text(x0 + 100 * k + 12, y0 - 60 * k, "avant : Q = 75 kvar", anchor="start", size=12)
    d.text(x0 + 100 * k + 12, y0 - 18 * k, "après : Q = 33 kvar", anchor="start", size=12, weight="600")
    d.add(f'<line x1="{fmt(x0 + 100 * k + 6)}" y1="{fmt(y0 - 75 * k)}" x2="{fmt(x0 + 100 * k + 6)}" y2="{fmt(y0 - 33 * k)}" stroke="{ACCENT}" stroke-width="4"/>')
    d.text(x0 + 100 * k - 10, y0 - 54 * k, "Qc", anchor="end", weight="700", color=ACCENT)
    d.text(280, 24, "Qc = P × (tan φ1 − tan φ2) ≈ 42 kvar", weight="600")
    d.text(150, 196, "cos φ 0,8", size=11, color=SOFT); d.text(200, 232, "cos φ 0,95", size=11, color=ACCENT)
    return d


def m3_plaque_transfo():
    d = Drawing(540, 250, "Plaque d'un transformateur de distribution : 630 kVA, 20 kV / 410 V, couplage Dyn11, tension de court-circuit 4 %")
    d.add(f'<rect x="40" y="20" width="460" height="210" rx="12" fill="#eef4f3" stroke="{INK}" stroke-width="2"/>')
    d.text(270, 50, "TRANSFORMATEUR TRIPHASÉ", weight="700")
    rows = (("630 kVA", "50 Hz"), ("20 kV / 410 V", "18,2 A / 887 A"), ("Dyn11", "ucc 4 %"), ("pertes à vide 1 kW", "pertes en charge 6,5 kW"))
    for k, (left, right) in enumerate(rows):
        y = 90 + 36 * k
        d.text(70, y, left, anchor="start", size=13, weight="600"); d.text(470, y, right, anchor="end", size=13, weight="600")
        d.wire((60, y + 12), (480, y + 12), color=SOFT, width=1)
    return d


def m3_rendement():
    d = Drawing(520, 270, "Rendement d'un transformateur de 630 kVA selon sa charge : supérieur à 98 %, maximal vers 40 % de charge")
    pts = []
    for p in range(5, 121, 5):
        x = p / 100
        s = 630 * x
        eta = s / (s + 1.0 + 6.5 * x * x) * 100
        pts.append((p, eta))
    d.graph(70, 40, 380, 170, (0, 120), (97, 99.5), [(pts, ACCENT, "")], "charge (% de la puissance assignée)", "rendement (%)",
            marks=(((39, 99.2), "maximum vers 40 %"),), xticks=((25, "25"), (50, "50"), (75, "75"), (100, "100")),
            yticks=((97.5, "97,5"), (98, "98"), (98.5, "98,5"), (99, "99")))
    return d


def m3_dyn11():
    d = Drawing(560, 260, "Couplage Dyn11 : primaire en triangle (D), secondaire en étoile (y) avec neutre sorti (n)")
    tri = ((140, 60), (80, 170), (200, 170))
    for a, b in ((0, 1), (1, 2), (2, 0)):
        d.inductor(tri[a], tri[b])
    d.text(140, 220, "primaire en triangle (D)", weight="600")
    c = (420, 120)
    for k, end in enumerate(((420, 40), (350, 165), (490, 165))):
        d.inductor(c, end)
    d.dot(c); d.wire(c, (420, 200)); d.text(432, 196, "neutre (n)", anchor="start", size=12, color=ACCENT, weight="600")
    d.text(420, 236, "secondaire en étoile (y)", weight="600")
    return d


def m3_tensions_triphase():
    d = Drawing(520, 250, "Réseau 400 V : 230 V entre une phase et le neutre (tension simple), 400 V entre deux phases (tension composée)")
    for k, name in enumerate(("L1", "L2", "L3", "N")):
        y = 50 + 40 * k
        d.wire((60, y), (300, y)); d.text(50, y + 5, name, anchor="end", weight="600")
    d.arrow((330, 50), (330, 90), "", color=INK); d.arrow((330, 90), (330, 50), "", color=INK)
    d.text(345, 75, "tension composée U = 400 V", anchor="start", size=12, weight="600")
    d.arrow((260, 90), (260, 170), "", color=ACCENT); d.arrow((260, 170), (260, 90), "", color=ACCENT)
    d.text(345, 140, "tension simple V = 230 V", anchor="start", size=12, weight="600", color=ACCENT)
    d.wire((262, 140), (340, 140), color=ACCENT, width=1)
    d.text(260, 232, "U = √3 × V", weight="700")
    return d


def m3_tc():
    d = Drawing(520, 240, "Transformateur de courant 200/5 A : le conducteur traverse le tore ; le secondaire alimente un ampèremètre 5 A")
    d.wire((40, 110), (480, 110), width=4); d.text(60, 98, "conducteur primaire", anchor="start", size=12)
    d.add(f'<ellipse cx="240" cy="110" rx="22" ry="52" fill="none" stroke="{ACCENT}" stroke-width="6"/>')
    d.text(240, 40, "TC 200/5 A", weight="700", color=ACCENT)
    d.wire((262, 130), (340, 130), (340, 170)); d.wire((262, 145), (300, 145), (300, 210), (400, 210), (400, 190))
    d.add(f'<circle cx="370" cy="180" r="18" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>'); d.text(370, 186, "A", weight="700")
    d.wire((340, 170), (352, 180)); d.wire((388, 180), (400, 190))
    d.text(420, 226, "ampèremètre 5 A", size=12)
    return d


def m3_commande_24v():
    d = Drawing(520, 260, "Transformateur de commande 400 V / 24 V : il isole le circuit de commande du réseau et l'alimente en très basse tension")
    p1, p2, s1, s2 = transformer(d, 200, 80, n_p=2, n_s=1)
    d.wire(p1, (180, 50), (90, 50)); d.wire(p2, (180, 180), (90, 180)); terminal(d, (90, 50), "L1", anchor="end"); terminal(d, (90, 180), "L2", anchor="end")
    d.wire(s1, (220, 50), (300, 50)); fuse(d, 300, 50, tag="F3"); d.wire((300, 94), (300, 110)); block(d, 330, 90, 160, 50, "circuit de commande 24 V", size=11)
    d.wire((300, 110), (330, 110)); d.wire(s2, (220, 160), (410, 160), (410, 140))
    d.text(140, 230, "400 V", weight="600"); d.text(260, 230, "24 V", weight="600", color=ACCENT)
    d.text(260, 252, "transformateur de commande", size=12, color=SOFT)
    return d


def m3_banc():
    d = Drawing(560, 240, "Banc du mini-projet : adaptateur moulé 230 V vers 12 V AC, charge résistive, ampèremètre et voltmètre au secondaire")
    block(d, 10, 70, 200, 70, "adaptateur moulé 230 V → 12 V AC", size=11)
    d.wire((210, 85), (260, 85)); d.meter((260, 85), (330, 85), "A"); d.wire((330, 85), (420, 85), (420, 92))
    d.resistor((420, 92), (420, 140), "charge"); d.wire((420, 140), (420, 160), (210, 160), (210, 125))
    d.wire((370, 85), (370, 100)); d.meter((370, 100), (370, 150), "V"); d.wire((370, 150), (370, 160))
    d.text(100, 200, "on ne touche jamais au côté 230 V", size=12, weight="600", color=ACCENT)
    return d


# --- Module 4 : appareils de commande et capteurs ---------------------------------------------------------------------

STATE = {"rouge": "#c0392b", "jaune": "#e0b100", "vert": "#2e8b57", "bleu": "#2f6db5", "blanc": "#fcfefe", "noir": "#13212c", "gris": "#8a979f"}


def m4_couleurs():
    d = Drawing(600, 250, "Couleurs des boutons et des voyants selon l'IEC 60204-1 : rouge pour l'arrêt d'urgence, blanc ou noir pour marche et arrêt")
    d.text(150, 28, "boutons", weight="700"); d.text(450, 28, "voyants", weight="700")
    rows_b = (("rouge", "arrêt d'urgence"), ("blanc", "marche (de préférence)"), ("noir", "arrêt"), ("jaune", "intervention anormale"))
    rows_v = (("rouge", "danger, défaut"), ("jaune", "anormal, attention"), ("vert", "normal, en marche"), ("bleu", "action obligatoire"))
    for k, (color, label) in enumerate(rows_b):
        y = 60 + 44 * k
        d.add(f'<circle cx="60" cy="{y}" r="15" fill="{STATE[color]}" stroke="{INK}" stroke-width="2"/>')
        d.text(88, y + 5, label, anchor="start", size=12)
    for k, (color, label) in enumerate(rows_v):
        y = 60 + 44 * k
        d.add(f'<circle cx="360" cy="{y}" r="15" fill="{STATE[color]}" stroke="{INK}" stroke-width="2" opacity="0.9"/>')
        d.text(388, y + 5, label, anchor="start", size=12)
    d.text(300, 238, "IEC 60204-1 : équipement électrique des machines", size=11, color=SOFT)
    return d


def m4_selecteur():
    d = Drawing(520, 230, "Sélecteur à trois positions manuel, 0, auto : le tableau dit quel contact est fermé dans chaque position")
    d.add(f'<circle cx="110" cy="110" r="46" fill="#eef4f3" stroke="{INK}" stroke-width="2"/>')
    d.wire((110, 110), (80, 76), width=5)
    for label, (x, y) in (("manuel", (52, 56)), ("0", (110, 52)), ("auto", (168, 56))):
        d.text(x, y, label, size=12, weight="600")
    d.text(300, 50, "position", anchor="start", weight="600")
    for k, label in enumerate(("manuel", "0", "auto")):
        d.text(380 + 50 * k, 50, label, size=11)
    for r, (contact_name, states) in enumerate((("13-14", ("X", "", "")), ("23-24", ("", "", "X")))):
        y = 90 + 40 * r
        d.text(300, y, contact_name, anchor="start", weight="600", color=ACCENT)
        for k, s in enumerate(states):
            d.add(f'<rect x="{360 + 50 * k}" y="{y - 18}" width="40" height="28" fill="{PAPER}" stroke="{SOFT}"/>')
            d.text(380 + 50 * k, y + 2, s, weight="700", color=ACCENT)
    d.text(260, 210, "X : contact fermé", size=11, color=SOFT)
    return d


def m4_fin_course():
    d = Drawing(520, 230, "Fin de course à galet : la came de la pièce mobile appuie sur le galet et fait basculer ses contacts")
    d.add(f'<rect x="40" y="40" width="200" height="30" rx="4" fill="#dfe8ea" stroke="{INK}" stroke-width="2"/>')
    d.add(f'<path d="M150 70 l20 24 h30 l20 -24 z" fill="#dfe8ea" stroke="{INK}" stroke-width="2"/>')
    d.arrow((60, 24), (140, 24), "déplacement", offset=(0, -6))
    d.add(f'<circle cx="185" cy="110" r="12" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>')
    d.wire((185, 122), (185, 140), width=3)
    d.add(f'<rect x="150" y="140" width="70" height="60" rx="6" fill="#eef4f3" stroke="{INK}" stroke-width="2"/>')
    d.text(185, 220, "fin de course", size=12, weight="600")
    contact(d, 330, 70, "no", marks=("13", "14"), tag="S3"); contact(d, 430, 70, "nc", marks=("21", "22"))
    d.text(380, 160, "contacts du fin de course", size=11, color=SOFT)
    return d


def m4_pressostat():
    d = Drawing(620, 270, "Pressostat d'un compresseur : il démarre le moteur sous 4 bar et l'arrête à 6 bar ; l'écart est l'hystérésis")
    pts = [(0, 6), (10, 4)]
    t, p, rising = 10, 4.0, True
    while t < 60:
        t += 2 if rising else 10
        p = 6 if rising else 4
        pts.append((t, p)); rising = not rising
    d.graph(70, 30, 380, 180, (0, 62), (0, 7), [(pts, ACCENT, "")], "temps", "pression (bar)",
            yticks=((4, "4"), (6, "6")))
    d.text(470, 64, "arrêt à 6 bar", anchor="start", size=12, weight="600")
    d.text(470, 116, "marche à 4 bar", anchor="start", size=12, weight="600")
    d.text(260, 262, "hystérésis : 2 bar", size=12, color=SOFT)
    return d


def m4_inductif():
    d = Drawing(520, 220, "Capteur inductif : il détecte une cible métallique sans contact, en deçà de sa portée nominale sn")
    d.add(f'<rect x="40" y="80" width="150" height="50" rx="6" fill="#eef4f3" stroke="{INK}" stroke-width="2"/>')
    d.add(f'<rect x="190" y="84" width="16" height="42" fill="{ACCENT}"/>')
    d.text(115, 110, "capteur M18", size=12, weight="600")
    for k in range(3):
        d.add(f'<path d="M{212 + 16 * k} 84 q14 21 0 42" fill="none" stroke="{SOFT}" stroke-width="2"/>')
    d.add(f'<rect x="300" y="70" width="24" height="70" fill="#dfe8ea" stroke="{INK}" stroke-width="2"/>')
    d.text(312, 160, "cible en acier", size=12)
    d.arrow((206, 50), (298, 50), "sn = 8 mm", color=INK, offset=(0, -8)); d.arrow((298, 50), (206, 50), color=INK)
    d.wire((40, 105), (20, 105)); d.text(28, 200, "3 fils : brun, bleu, noir", anchor="start", size=11, color=SOFT)
    return d


def m4_pnp_npn():
    d = Drawing(600, 260, "Capteur 3 fils : en PNP, la sortie (noir) fournit le +24 V à la charge reliée au 0 V ; en NPN, la charge est reliée au +24 V")
    for x0, kind in ((30, "PNP"), (320, "NPN")):
        block(d, x0, 90, 90, 70, kind, size=14)
        d.wire((x0 + 90, 105), (x0 + 200, 105)); d.text(x0 + 150, 98, "brun", size=11)
        d.wire((x0 + 90, 125), (x0 + 160, 125), color=ACCENT, width=3); d.text(x0 + 130, 140, "noir", size=11, color=ACCENT)
        d.wire((x0 + 90, 145), (x0 + 200, 145)); d.text(x0 + 150, 160, "bleu", size=11)
        d.text(x0 + 220, 109, "+24 V", anchor="start", size=12, weight="600"); d.text(x0 + 220, 149, "0 V", anchor="start", size=12, weight="600")
        if kind == "PNP":
            d.wire((x0 + 160, 125), (x0 + 160, 180)); d.resistor((x0 + 160, 180), (x0 + 160, 230), "charge"); d.wire((x0 + 160, 230), (x0 + 200, 230), (x0 + 200, 145))
        else:
            d.wire((x0 + 160, 125), (x0 + 160, 180)); d.resistor((x0 + 160, 180), (x0 + 160, 230), "charge"); d.wire((x0 + 160, 230), (x0 + 240, 230), (x0 + 240, 60), (x0 + 200, 60), (x0 + 200, 105))
    d.text(300, 30, "sortie : fil noir", weight="600", color=ACCENT)
    return d


def m4_photo():
    d = Drawing(600, 260, "Trois montages de cellule photoélectrique : barrage, reflex sur réflecteur, proximité sur l'objet lui-même")
    for k, (name, y) in enumerate((("barrage", 50), ("reflex", 130), ("proximité", 210))):
        d.text(30, y + 4, name, anchor="start", weight="600")
        block(d, 140, y - 18, 70, 36, "E" if k == 0 else "E/R", size=12)
        if k == 0:
            d.arrow((210, y), (470, y), color=ACCENT); block(d, 470, y - 18, 70, 36, "R", size=12)
        elif k == 1:
            d.arrow((210, y - 6), (470, y - 6), color=ACCENT); d.arrow((470, y + 6), (210, y + 6), color=ACCENT)
            d.add(f'<rect x="470" y="{y - 20}" width="14" height="40" fill="#dfe8ea" stroke="{INK}" stroke-width="2"/>'); d.text(500, y + 4, "réflecteur", anchor="start", size=11)
        else:
            d.arrow((210, y - 6), (380, y - 6), color=ACCENT); d.arrow((380, y + 6), (210, y + 6), color=ACCENT)
            d.add(f'<rect x="380" y="{y - 22}" width="40" height="44" rx="4" fill="#dfe8ea" stroke="{INK}" stroke-width="2"/>'); d.text(430, y + 4, "objet", anchor="start", size=11)
    return d


def m4_ultrasons():
    d = Drawing(520, 220, "Capteur à ultrasons : il mesure le temps aller-retour de l'écho ; d = v × t / 2 avec v ≈ 340 m/s")
    block(d, 40, 80, 90, 50, "capteur", size=12)
    for k in range(3):
        d.add(f'<path d="M{140 + 18 * k} 80 q16 25 0 50" fill="none" stroke="{ACCENT}" stroke-width="2"/>')
    d.add(f'<rect x="400" y="50" width="20" height="110" fill="#dfe8ea" stroke="{INK}" stroke-width="2"/>'); d.text(410, 180, "objet", size=12)
    d.arrow((140, 150), (398, 150), "aller", color=INK, offset=(0, 18)); d.arrow((398, 60), (140, 60), "retour", color=INK)
    d.text(260, 210, "d = v × t / 2", weight="700")
    return d


def m4_pt100():
    d = Drawing(520, 270, "Sonde Pt100 : sa résistance vaut 100 Ω à 0 °C et augmente d'environ 0,385 Ω par degré")
    pts = [(t, 100 * (1 + 0.00385 * t)) for t in range(0, 201, 10)]
    d.graph(70, 30, 380, 190, (0, 210), (90, 185), [(pts, ACCENT, "Pt100")], "température (°C)", "résistance (Ω)",
            marks=(((100, 138.5), "138,5 Ω à 100 °C"),), xticks=((50, "50"), (100, "100"), (150, "150"), (200, "200")),
            yticks=((100, "100"), (138.5, "138,5"), (177, "177")))
    return d


def m4_codeur():
    d = Drawing(560, 230, "Codeur incrémental : un disque à fentes coupe un faisceau ; chaque fente donne une impulsion")
    d.add(f'<circle cx="120" cy="115" r="80" fill="#eef4f3" stroke="{INK}" stroke-width="2"/>')
    for k in range(24):
        a = 2 * math.pi * k / 24
        x1, y1 = 120 + 62 * math.cos(a), 115 + 62 * math.sin(a); x2, y2 = 120 + 76 * math.cos(a), 115 + 76 * math.sin(a)
        d.wire((x1, y1), (x2, y2), color=INK, width=3)
    d.add(f'<circle cx="120" cy="115" r="8" fill="{INK}"/>')
    d.text(120, 215, "disque à fentes", size=12)
    pts, x = [], 0
    for k in range(8):
        pts += [(x, 0), (x, 1), (x + 1, 1), (x + 1, 0), (x + 2, 0)]; x += 2
    d.graph(260, 60, 260, 90, (0, 16), (0, 1.5), [(pts, ACCENT, "")], "temps", "impulsions")
    return d


def m4_electrovanne():
    d = Drawing(520, 230, "Électrovanne : la bobine alimentée attire le noyau, qui ouvre le passage du fluide")
    d.add(f'<rect x="40" y="130" width="440" height="40" fill="#dfe8ea" stroke="{INK}" stroke-width="2"/>')
    d.arrow((60, 150), (200, 150), "fluide", color=ACCENT, offset=(0, -26)); d.arrow((320, 150), (460, 150), color=ACCENT)
    d.add(f'<rect x="230" y="40" width="60" height="70" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>')
    for k in range(5):
        d.wire((230, 50 + 12 * k), (290, 56 + 12 * k), color=ACCENT, width=1.5)
    d.add(f'<rect x="250" y="70" width="20" height="80" fill="{SOFT}" stroke="{INK}" stroke-width="2"/>')
    d.text(310, 70, "bobine 24 V", anchor="start", size=12, weight="600"); d.text(310, 100, "noyau", anchor="start", size=12)
    coil(d, 430, 20, tag="YV1")
    return d


def m4_pas_a_pas():
    d = Drawing(520, 240, "Moteur pas à pas : 200 pas par tour, soit 1,8° par impulsion ; il avance d'un pas à chaque impulsion")
    d.add(f'<circle cx="130" cy="120" r="80" fill="#eef4f3" stroke="{INK}" stroke-width="2"/>')
    for k in range(12):
        a = 2 * math.pi * k / 12
        d.wire((130 + 50 * math.cos(a), 120 + 50 * math.sin(a)), (130 + 70 * math.cos(a), 120 + 70 * math.sin(a)), width=4)
    d.add(f'<circle cx="130" cy="120" r="30" fill="{PAPER}" stroke="{ACCENT}" stroke-width="3"/>')
    d.text(320, 90, "360° / 200 pas = 1,8° par pas", anchor="start", weight="600")
    d.text(320, 130, "commande par impulsions", anchor="start", size=12)
    d.text(320, 160, "position connue sans capteur", anchor="start", size=12, color=SOFT)
    return d


def m4_banc():
    d = Drawing(520, 230, "Banc du mini-projet : capteur inductif PNP alimenté en 24 V, sortie reliée à une LED et sa résistance")
    block(d, 20, 40, 130, 50, "alimentation 24 V", size=11)
    d.wire((150, 55), (420, 55)); d.wire((150, 75), (170, 75), (170, 200), (420, 200))
    block(d, 220, 110, 80, 50, "PNP", size=13)
    d.wire((240, 55), (240, 110)); d.wire((260, 160), (260, 200)); d.wire((300, 135), (380, 135), (380, 140), color=ACCENT, width=3)
    d.diode((380, 140), (380, 175), kind="led"); d.wire((380, 175), (380, 180)); d.resistor((380, 180), (380, 200), "1 kΩ")
    d.text(200, 225, "brun +24 V, bleu 0 V, noir vers la LED", size=11, color=SOFT)
    return d


# --- Module 5 : les moteurs à courant continu ------------------------------------------------------------------------


def _poles(d, cx, cy, gap=70):
    d.add(f'<rect x="{cx - gap - 50}" y="{cy - 50}" width="50" height="100" rx="6" fill="#c9d8dd" stroke="{INK}" stroke-width="2"/>')
    d.add(f'<rect x="{cx + gap}" y="{cy - 50}" width="50" height="100" rx="6" fill="#c9d8dd" stroke="{INK}" stroke-width="2"/>')
    d.text(cx - gap - 25, cy + 6, "N", weight="700", size=18); d.text(cx + gap + 25, cy + 6, "S", weight="700", size=18)


def m5_laplace():
    d = Drawing(520, 240, "Force de Laplace : un conducteur parcouru par un courant dans un champ magnétique subit une force F = B × I × L")
    _poles(d, 200, 120)
    for y in (90, 120, 150):
        d.arrow((130, y), (270, y), color=SOFT)
    d.add(f'<circle cx="200" cy="120" r="12" fill="{PAPER}" stroke="{ACCENT}" stroke-width="3"/><circle cx="200" cy="120" r="3" fill="{ACCENT}"/>')
    d.arrow((200, 106), (200, 40), "F", color=ACCENT, offset=(14, 0))
    d.text(380, 100, "B : champ (N vers S)", anchor="start", size=12); d.text(380, 125, "I : courant (vers vous)", anchor="start", size=12)
    d.text(380, 150, "F = B × I × L", anchor="start", weight="700")
    return d


def m5_spire():
    d = Drawing(520, 240, "Une spire dans le champ : les deux côtés subissent des forces opposées et la spire tourne")
    _poles(d, 200, 120)
    d.add(f'<line x1="160" y1="150" x2="240" y2="90" stroke="{ACCENT}" stroke-width="4"/>')
    d.add(f'<circle cx="160" cy="150" r="9" fill="{PAPER}" stroke="{INK}" stroke-width="2"/><circle cx="240" cy="90" r="9" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>')
    d.arrow((160, 150), (160, 200), "F", color=ACCENT, offset=(14, 0)); d.arrow((240, 90), (240, 40), "F", color=ACCENT, offset=(14, 0))
    d.add(f'<path d="M250 160 A70 70 0 0 1 150 160" fill="none" stroke="{INK}" stroke-width="2" stroke-dasharray="4 3"/>')
    d.text(390, 120, "couple → rotation", anchor="start", weight="600")
    return d


def m5_coupe():
    d = Drawing(520, 270, "Coupe d'un moteur à courant continu : inducteur (pôles), induit tournant, collecteur et balais")
    d.add(f'<circle cx="200" cy="135" r="110" fill="#eef4f3" stroke="{INK}" stroke-width="3"/>')
    d.add(f'<rect x="104" y="95" width="34" height="80" rx="6" fill="#c9d8dd" stroke="{INK}" stroke-width="2"/><rect x="262" y="95" width="34" height="80" rx="6" fill="#c9d8dd" stroke="{INK}" stroke-width="2"/>')
    d.add(f'<circle cx="200" cy="135" r="56" fill="#dfe8ea" stroke="{INK}" stroke-width="2"/>')
    d.add(f'<circle cx="200" cy="135" r="20" fill="{PAPER}" stroke="{ACCENT}" stroke-width="4"/>')
    d.text(370, 60, "carcasse", anchor="start", size=12); d.wire((365, 56), (300, 56), color=SOFT, width=1)
    d.text(370, 110, "inducteur (pôles)", anchor="start", size=12); d.wire((365, 106), (296, 120), color=SOFT, width=1)
    d.text(370, 160, "induit", anchor="start", size=12); d.wire((365, 156), (250, 156), color=SOFT, width=1)
    d.text(370, 210, "collecteur et balais", anchor="start", size=12, color=ACCENT, weight="600"); d.wire((365, 206), (218, 145), color=ACCENT, width=1)
    return d


def m5_collecteur():
    d = Drawing(520, 230, "Collecteur et balais : les balais fixes frottent sur les lames du collecteur et inversent le courant dans chaque spire au bon moment")
    d.add(f'<circle cx="200" cy="115" r="70" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>')
    for k in range(8):
        a = 2 * math.pi * k / 8
        d.wire((200 + 30 * math.cos(a), 115 + 30 * math.sin(a)), (200 + 70 * math.cos(a), 115 + 70 * math.sin(a)), width=2)
    d.add(f'<circle cx="200" cy="115" r="30" fill="#eef4f3" stroke="{INK}" stroke-width="2"/>')
    d.add(f'<rect x="100" y="100" width="30" height="30" fill="{SOFT}" stroke="{INK}" stroke-width="2"/><rect x="270" y="100" width="30" height="30" fill="{SOFT}" stroke="{INK}" stroke-width="2"/>')
    d.wire((100, 115), (60, 115)); d.wire((300, 115), (340, 115)); d.text(50, 120, "+", anchor="end", weight="700", color=ACCENT); d.text(350, 120, "−", anchor="start", weight="700")
    d.text(400, 100, "lames du collecteur", anchor="start", size=12); d.text(400, 130, "balais en carbone", anchor="start", size=12)
    d.text(200, 215, "les balais s'usent : on les contrôle", size=11, color=SOFT)
    return d


def m5_ap_symbole():
    d = Drawing(480, 220, "Moteur à aimants permanents : pas d'enroulement inducteur, seulement deux bornes vers l'induit")
    motor(d, 160, 110, r=40, phases="=")
    d.wire((120, 110), (60, 110)); d.wire((200, 110), (260, 110)); terminal(d, (60, 110), "+", anchor="end"); terminal(d, (260, 110), "−")
    d.text(340, 90, "induit : 2 bornes", anchor="start", size=12); d.text(340, 120, "inducteur : aimants", anchor="start", size=12)
    d.text(240, 200, "petits moteurs : 6 à 48 V", size=11, color=SOFT)
    return d


def m5_caracteristique():
    d = Drawing(520, 260, "Moteur à aimants permanents : sa vitesse baisse un peu, en ligne droite, quand le couple demandé augmente")
    d.graph(70, 30, 380, 180, (0, 1.1), (0, 3200), [([(0, 3000), (1, 2400)], ACCENT, "12 V"), ([(0, 1500), (1, 900)], SOFT, "6 V")],
            "couple (N·m)", "vitesse (tr/min)", xticks=((0.5, "0,5"), (1, "1")), yticks=((1500, "1500"), (3000, "3000")))
    return d


def _dc_field(d, kind):
    d.text(40, 40, "+", weight="700", color=ACCENT); d.text(40, 200, "−", weight="700")
    d.wire((50, 36), (240, 36)); d.wire((50, 196), (240, 196))
    motor(d, 240, 116, r=26, phases="=")
    if kind == "serie":
        d.wire((240, 36), (240, 50)); d.inductor((240, 50), (240, 90)); d.wire((240, 142), (240, 196))
        d.text(270, 74, "inducteur série (gros fil)", anchor="start", size=12, weight="600")
    else:
        d.wire((240, 36), (240, 90)); d.wire((240, 142), (240, 196))
        d.dot((240, 36)); d.dot((240, 196)); d.wire((240, 36), (360, 36), (360, 96)); d.inductor((360, 96), (360, 136)); d.wire((360, 136), (360, 196), (240, 196))
        d.text(376, 120, "inducteur shunt", anchor="start", size=12, weight="600"); d.text(376, 140, "(fil fin)", anchor="start", size=11, color=SOFT)


def m5_serie():
    d = Drawing(520, 230, "Moteur série : l'inducteur est en série avec l'induit ; fort couple au démarrage, vitesse très variable, jamais à vide")
    _dc_field(d, "serie")
    d.text(270, 222, "fort couple au démarrage", size=12, weight="600")
    return d


def m5_shunt():
    d = Drawing(520, 230, "Moteur shunt : l'inducteur est en parallèle sur l'induit ; vitesse presque constante quelle que soit la charge")
    _dc_field(d, "shunt")
    d.text(270, 222, "vitesse presque constante", size=12, weight="600")
    return d


def m5_fcem():
    d = Drawing(520, 240, "Modèle de l'induit : la tension appliquée U se partage entre la chute R × I et la force contre-électromotrice E")
    d.battery((60, 190), (60, 60), "U", side=-1)
    d.wire((60, 60), (60, 40), (200, 40)); d.resistor((200, 40), (300, 40), "R")
    d.wire((300, 40), (380, 40), (380, 70))
    d.add(f'<circle cx="380" cy="115" r="30" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>'); d.text(380, 121, "E", weight="700", color=ACCENT)
    d.wire((380, 145), (380, 210), (60, 210), (60, 190))
    d.arrow((140, 60), (180, 60), "I", offset=(0, 18))
    d.text(260, 232, "U = E + R × I", weight="700")
    return d


def m5_demarrage():
    d = Drawing(520, 260, "Courant de démarrage : à l'arrêt E = 0, le courant vaut U / R, plusieurs fois le courant nominal ; il baisse quand le moteur prend de la vitesse")
    pts = [(t / 10, 1 + 9 * math.exp(-t / 6)) for t in range(0, 41)]
    d.graph(70, 30, 380, 180, (0, 4.2), (0, 11), [(pts, ACCENT, "I / In", (1.4, 3.2))], "temps (s)", "courant (× In)",
            xticks=((1, "1"), (2, "2"), (3, "3"), (4, "4")), yticks=((1, "1"), (5, "5"), (10, "10")))
    return d


def m5_inversion():
    d = Drawing(520, 230, "Inverser le sens d'un moteur à aimants : inverser la polarité de l'induit, par exemple avec un inverseur à deux circuits")
    for x0, label, sign in ((40, "sens horaire", ("+", "−")), (290, "sens antihoraire", ("−", "+"))):
        motor(d, x0 + 100, 110, r=30, phases="=")
        d.wire((x0 + 70, 110), (x0 + 20, 110)); d.wire((x0 + 130, 110), (x0 + 180, 110))
        d.text(x0 + 12, 115, sign[0], anchor="end", weight="700", color=ACCENT); d.text(x0 + 188, 115, sign[1], anchor="start", weight="700")
        d.add(f'<path d="M{x0 + 80} 70 A30 30 0 0 {1 if label == "sens horaire" else 0} {x0 + 120} 70" fill="none" stroke="{ACCENT}" stroke-width="2"/>')
        d.text(x0 + 100, 180, label, size=12, weight="600")
    return d


def m5_mli():
    d = Drawing(560, 260, "Variation de vitesse par MLI : le transistor hache la tension ; la tension moyenne vaut le rapport cyclique × 12 V")
    pts, t = [], 0
    for k in range(4):
        pts += [(t, 0), (t, 12), (t + 3, 12), (t + 3, 0), (t + 10, 0)]; t += 10
    d.graph(70, 30, 400, 170, (0, 41), (0, 14), [(pts, ACCENT, "")], "temps", "tension (V)", yticks=((12, "12"), (3.6, "3,6")))
    d.add(f'<line x1="70" y1="{fmt(30 + 170 - 3.6 / 14 * 170)}" x2="470" y2="{fmt(30 + 170 - 3.6 / 14 * 170)}" stroke="{SOFT}" stroke-dasharray="5 4" stroke-width="2"/>')
    d.text(300, 240, "rapport cyclique 30 % → tension moyenne 3,6 V", size=12, weight="600")
    return d


def m5_banc():
    d = Drawing(520, 230, "Banc du mini-projet : alimentation 12 V, ampèremètre en série, voltmètre aux bornes du moteur 12 V")
    block(d, 20, 70, 130, 60, "alimentation 12 V", size=12)
    d.wire((150, 85), (220, 85)); d.meter((220, 85), (290, 85), "A"); d.wire((290, 85), (380, 85), (380, 95))
    motor(d, 380, 120, r=24, phases="=")
    d.wire((380, 144), (380, 170), (150, 170), (150, 115))
    d.wire((330, 85), (330, 100)); d.meter((330, 100), (330, 150), "V"); d.wire((330, 150), (330, 170))
    d.text(260, 210, "tout le banc reste en 12 V", size=12, color=ACCENT, weight="600")
    return d


# --- Module 6 : les moteurs à courant alternatif ---------------------------------------------------------------------


def m6_champ():
    d = Drawing(520, 260, "Trois bobines décalées de 120°, alimentées en triphasé, créent un champ magnétique qui tourne")
    for k, name in enumerate(("U", "V", "W")):
        a = -math.pi / 2 + 2 * math.pi * k / 3
        x, y = 160 + 90 * math.cos(a), 130 + 90 * math.sin(a)
        d.add(f'<circle cx="{fmt(x)}" cy="{fmt(y)}" r="22" fill="#c9d8dd" stroke="{INK}" stroke-width="2"/>')
        d.text(x, y + 5, name, weight="700")
    d.add(f'<path d="M160 70 A60 60 0 1 1 103 150" fill="none" stroke="{ACCENT}" stroke-width="3"/>')
    d.arrow((112, 160), (100, 148), color=ACCENT)
    d.text(340, 110, "champ tournant", anchor="start", weight="700", color=ACCENT)
    d.text(340, 140, "à 50 Hz : 3 000 tr/min", anchor="start", size=12); d.text(340, 165, "pour une paire de pôles", anchor="start", size=12)
    return d


def m6_vitesses():
    d = Drawing(520, 230, "Vitesse de synchronisme à 50 Hz selon le nombre de paires de pôles : 3 000, 1 500, 1 000 et 750 tr/min")
    bars(d, 170, 20, 260, 160, [("p = 1 (2 pôles)", 3000, "3 000 tr/min"), ("p = 2 (4 pôles)", 1500, "1 500 tr/min"),
                                ("p = 3 (6 pôles)", 1000, "1 000 tr/min"), ("p = 4 (8 pôles)", 750, "750 tr/min")], 3000, "ns = 60 × f / p")
    return d


def m6_cage():
    d = Drawing(520, 220, "Rotor à cage d'écureuil : des barres d'aluminium reliées à chaque bout par un anneau de court-circuit")
    d.add(f'<ellipse cx="120" cy="110" rx="26" ry="70" fill="none" stroke="{INK}" stroke-width="3"/><ellipse cx="380" cy="110" rx="26" ry="70" fill="none" stroke="{INK}" stroke-width="3"/>')
    for k in range(7):
        y = 50 + 20 * k
        d.wire((120 + 26 * math.sqrt(max(0, 1 - ((y - 110) / 70) ** 2)), y), (380 - 26 * math.sqrt(max(0, 1 - ((y - 110) / 70) ** 2)), y), color=ACCENT, width=3)
    d.wire((40, 110), (94, 110), width=5); d.wire((406, 110), (470, 110), width=5)
    d.text(120, 205, "anneau", size=12); d.text(250, 205, "barres", size=12, color=ACCENT, weight="600"); d.text(380, 205, "anneau", size=12)
    return d


def m6_couple():
    d = Drawing(560, 290, "Couple d'un moteur asynchrone selon sa vitesse : couple de démarrage, couple maximal, point de fonctionnement près du synchronisme")
    pts = []
    for n in range(0, 1500, 15):
        g = (1500 - n) / 1500
        c = 2 * 2.6 / (g / 0.18 + 0.18 / g) if g > 0 else 0
        pts.append((n, c))
    pts.append((1500, 0))
    d.graph(70, 30, 420, 200, (0, 1560), (0, 3), [(pts, ACCENT, "couple moteur", (300, 1.4))], "vitesse (tr/min)", "couple (× Cn)",
            marks=(((1440, 1.0), "nominal"), ((1230, 2.6), "maximal")), xticks=((750, "750"), (1500, "1500")), yticks=((1, "1"), (2, "2")))
    d.text(80, 280, "au démarrage ≈ 0,9 × Cn", anchor="start", size=12, color=SOFT)
    return d


def m6_rotor_bobine():
    d = Drawing(520, 230, "Moteur à rotor bobiné : des bagues et des balais relient le rotor à des résistances qu'on retire au démarrage")
    motor(d, 140, 115, r=40)
    for k in range(3):
        y = 85 + 30 * k
        d.add(f'<rect x="200" y="{y - 8}" width="20" height="16" fill="{SOFT}" stroke="{INK}" stroke-width="1.5"/>')
        d.wire((180, y), (200, y)); d.wire((220, y), (300, y)); d.resistor((300, y), (380, y)); d.wire((380, y), (420, y))
    d.wire((420, 85), (420, 145), width=3)
    d.text(210, 190, "bagues", size=12); d.text(340, 190, "résistances de démarrage", size=12, weight="600")
    return d


def m6_synchrone():
    d = Drawing(520, 250, "Moteur synchrone : sa vitesse reste égale à la vitesse de synchronisme quelle que soit la charge")
    d.graph(70, 30, 380, 170, (0, 1.2), (1300, 1600), [([(0, 1500), (1.1, 1500)], ACCENT, "synchrone", (0.15, 1520)),
                                                        ([(0, 1495), (1.1, 1420)], SOFT, "asynchrone", (0.55, 1405))],
            "charge (× nominale)", "vitesse (tr/min)", yticks=((1500, "1500"), (1420, "1420")), xticks=((1, "1"),))
    return d


def m6_monophase():
    d = Drawing(520, 240, "Moteur monophasé à condensateur : un enroulement auxiliaire en série avec un condensateur crée le décalage qui fait démarrer")
    d.text(40, 40, "L", weight="700"); d.text(40, 210, "N", weight="700")
    d.wire((50, 36), (360, 36)); d.wire((50, 206), (360, 206))
    d.wire((160, 36), (160, 100)); d.inductor((160, 100), (160, 140)); d.wire((160, 140), (160, 206))
    d.text(180, 125, "principal", anchor="start", size=12, weight="600")
    d.wire((320, 36), (320, 60)); d.capacitor((320, 60), (320, 100), "C", "8 µF"); d.inductor((320, 110), (320, 150)); d.wire((320, 100), (320, 110)); d.wire((320, 150), (320, 206))
    d.text(340, 140, "auxiliaire", anchor="start", size=12, weight="600")
    d.dot((160, 36)); d.dot((160, 206))
    return d


def m6_bague():
    d = Drawing(480, 230, "Moteur à bague de déphasage : une spire en cuivre sur une partie de chaque pôle retarde le flux et fait démarrer le rotor")
    d.add(f'<rect x="120" y="40" width="110" height="60" rx="6" fill="#c9d8dd" stroke="{INK}" stroke-width="2"/>')
    d.add(f'<rect x="196" y="40" width="24" height="60" fill="none" stroke="{ACCENT}" stroke-width="4"/>')
    d.add(f'<circle cx="175" cy="160" r="45" fill="#eef4f3" stroke="{INK}" stroke-width="2"/>')
    d.text(250, 70, "bague de déphasage", anchor="start", size=12, weight="600", color=ACCENT)
    d.text(250, 165, "petits ventilateurs, pompes", anchor="start", size=12)
    d.text(250, 190, "rendement faible", anchor="start", size=12, color=SOFT)
    return d


def m6_classes():
    d = Drawing(520, 220, "Classes d'isolation : température maximale des enroulements, 130 °C en B, 155 °C en F, 180 °C en H")
    bars(d, 110, 20, 300, 140, [("classe B", 130, "130 °C"), ("classe F", 155, "155 °C"), ("classe H", 180, "180 °C")], 180, "température maximale des enroulements")
    return d


def m6_service():
    d = Drawing(560, 250, "Types de service : S1 continu à charge constante, S3 intermittent, marche et repos alternés")
    d.graph(70, 30, 200, 120, (0, 10), (0, 1.3), [([(0, 1), (10, 1)], ACCENT, "")], "temps", "charge")
    d.text(170, 180, "S1 : continu", weight="600")
    pts = []
    for k in range(5):
        pts += [(2 * k, 1), (2 * k + 0.8, 1), (2 * k + 0.8, 0), (2 * k + 2, 0)]
    d.graph(320, 30, 200, 120, (0, 10), (0, 1.3), [(pts, ACCENT, "")], "temps", "charge")
    d.text(420, 180, "S3 : intermittent (40 %)", weight="600")
    return d


def m6_alignement():
    d = Drawing(560, 230, "Alignement de l'accouplement : les deux arbres doivent être dans le prolongement l'un de l'autre, sans décalage ni angle")
    for x0, label, dy, ang in ((20, "aligné", 0, 0), (200, "décalage parallèle", 14, 0), (380, "défaut angulaire", 0, 8)):
        block(d, x0, 70, 60, 50, "M", size=13)
        d.wire((x0 + 60, 95), (x0 + 85, 95), width=6)
        d.add(f'<g transform="rotate({ang} {x0 + 100} 95)"><rect x="{x0 + 85}" y="{78 + dy}" width="30" height="34" fill="{SOFT}"/>'
              f'<line x1="{x0 + 115}" y1="{95 + dy}" x2="{x0 + 150}" y2="{95 + dy}" stroke="{INK}" stroke-width="6"/></g>')
        d.text(x0 + 80, 170, label, size=12, weight="600", color=INK if label == "aligné" else ACCENT)
    d.text(280, 215, "un défaut d'alignement use les roulements", size=11, color=SOFT)
    return d


def m6_raccordement():
    d = Drawing(520, 240, "Boîte à bornes : câble par un presse-étoupe, barrettes selon le couplage, conducteur PE sur la borne de terre")
    d.add(f'<rect x="120" y="40" width="280" height="160" rx="10" fill="#eef4f3" stroke="{INK}" stroke-width="2"/>')
    for k in range(3):
        terminal(d, (180 + 60 * k, 90)); terminal(d, (180 + 60 * k, 140))
    d.wire((180, 140), (300, 140), color=ACCENT, width=6)
    d.ground((360, 150)); d.text(360, 190, "PE", weight="700", color=ACCENT)
    d.add(f'<rect x="80" y="100" width="40" height="40" rx="6" fill="{SOFT}" stroke="{INK}" stroke-width="2"/>')
    d.text(70, 220, "presse-étoupe", size=12)
    d.text(240, 30, "boîte à bornes", weight="600")
    return d


def m6_resistances():
    d = Drawing(520, 230, "Contrôle d'un moteur débranché : barrettes retirées, les trois enroulements doivent présenter la même résistance")
    for k, (top, bottom) in enumerate((("U1", "U2"), ("V1", "V2"), ("W1", "W2"))):
        y = 50 + 60 * k
        d.text(60, y + 5, top, weight="700"); d.wire((80, y), (120, y)); d.inductor((120, y), (200, y)); d.wire((200, y), (240, y)); d.text(260, y + 5, bottom, weight="700")
        d.text(330, y + 5, "≈ 2,7 Ω", anchor="start", size=12, color=ACCENT, weight="600")
    d.text(260, 220, "trois valeurs égales à quelques % près", size=12)
    return d


def m6_diagnostic():
    d = Drawing(600, 260, "Dépannage d'un moteur qui ne démarre pas : vérifier l'alimentation, la protection, puis le moteur lui-même, toujours consigné pour les mesures")
    labels = ("moteur ne démarre pas", "tension aux bornes ?", "protection déclenchée ?", "enroulements : résistances égales ?", "isolement et roulements")
    for k, label in enumerate(labels):
        y = 20 + 46 * k
        block(d, 150, y, 300, 34, label, size=12)
        if k < len(labels) - 1:
            d.arrow((300, y + 34), (300, y + 46), color=INK)
    d.text(470, 110, "mesures toujours", anchor="start", size=11, color=SOFT); d.text(470, 126, "moteur consigné", anchor="start", size=11, color=SOFT)
    return d


def m6_releve():
    d = Drawing(520, 220, "Mini-projet : ohmmètre entre U1 et U2 d'un moteur débranché, barrettes retirées")
    d.add(f'<rect x="100" y="40" width="240" height="140" rx="10" fill="none" stroke="{INK}" stroke-width="2"/>')
    for k, (top, bottom) in enumerate((("U1", "W2"), ("V1", "U2"), ("W1", "V2"))):
        x = 150 + 70 * k
        terminal(d, (x, 80)); terminal(d, (x, 140)); d.text(x, 68, top, size=12, weight="700"); d.text(x, 166, bottom, size=12, weight="700")
    d.wire((150, 80), (150, 20), (420, 20), (420, 95)); d.meter((420, 95), (420, 145), "Ω"); d.wire((420, 145), (420, 200), (220, 200), (220, 140), color=ACCENT)
    d.text(100, 214, "moteur débranché", anchor="start", size=11, color=SOFT)
    return d


SECTION_DIAGRAMS = {
    1: [m1_seuils, m1_corps, m1_arc, m1_epi, m1_defaut, m1_ddr, m1_tt, m1_tn, m1_it, m1_etapes, m1_vat, m1_domaines, m1_normes, m1_banc],
    2: [m2_symboles_commande, m2_symboles_puissance, m2_contacts, m2_bornes, m2_puissance, m2_commande, m2_unifilaire,
        m2_synoptique, m2_etoile, m2_triangle, m2_plaque, m2_tensions, m2_manuel, m2_telecommande, m2_lampes],
    3: [m3_chaine, m3_pertes_ligne, m3_poste, m3_mcc, m3_triangle, m3_compensation, m3_plaque_transfo, m3_rendement,
        m3_dyn11, m3_tensions_triphase, m3_tc, m3_commande_24v, m3_banc],
    4: [m4_couleurs, m4_selecteur, m4_fin_course, m4_pressostat, m4_inductif, m4_pnp_npn, m4_photo, m4_ultrasons, m4_pt100,
        m4_codeur, m4_electrovanne, m4_pas_a_pas, m4_banc],
    5: [m5_laplace, m5_spire, m5_coupe, m5_collecteur, m5_ap_symbole, m5_caracteristique, m5_serie, m5_shunt, m5_fcem,
        m5_demarrage, m5_inversion, m5_mli, m5_banc],
    6: [m6_champ, m6_vitesses, m6_cage, m6_couple, m6_rotor_bobine, m6_synchrone, m6_monophase, m6_bague, m6_classes,
        m6_service, m6_alignement, m6_raccordement, m6_resistances, m6_diagnostic, m6_releve],
}


# --- Questions sur schéma (M19) : sans légendes, zones en coordonnées du viewBox ---------------------------------------


def q_m1_sectionneur():
    d = Drawing(420, 300, "Départ moteur sans légendes : trois appareils en série entre le réseau et le moteur")
    for k in range(3):
        d.wire((150 + 30 * k, 20), (150 + 30 * k, 40))
    three(d, 150, 40, contact, gap=30, kind="isolator")
    for k in range(3):
        d.wire((150 + 30 * k, 84), (150 + 30 * k, 100))
    three(d, 150, 100, contact, gap=30, kind="main")
    for k in range(3):
        d.wire((150 + 30 * k, 144), (150 + 30 * k, 160))
    three(d, 150, 160, thermal, gap=30, link=False)
    for k in range(3):
        d.wire((150 + 30 * k, 204), (150 + 30 * k, 220), (180, 240))
    motor(d, 180, 262, r=22)
    d.zone("sectionneur", 130, 40, 90, 44); d.zone("contacteur", 130, 100, 90, 44); d.zone("relais", 130, 160, 90, 44)
    return d


def q_m2_plaques():
    d = Drawing(620, 210, "Trois plaques à bornes sans légendes, barrettes posées de trois façons")
    for n, (x0, links) in enumerate(((40, "Y"), (240, "D"), (440, "X"))):
        for k in range(3):
            x = x0 + 50 * k + 20
            terminal(d, (x, 70)); terminal(d, (x, 140))
        d.add(f'<rect x="{x0}" y="40" width="140" height="130" rx="10" fill="none" stroke="{INK}" stroke-width="2"/>')
        if links == "Y":
            d.wire((x0 + 20, 140), (x0 + 120, 140), color=ACCENT, width=6)
        elif links == "D":
            for k in range(3):
                d.wire((x0 + 20 + 50 * k, 70), (x0 + 20 + 50 * k, 140), color=ACCENT, width=6)
        else:
            d.wire((x0 + 20, 70), (x0 + 120, 70), color=ACCENT, width=6)
    d.zone("etoile", 40, 40, 140, 130); d.zone("triangle", 240, 40, 140, 130); d.zone("haut", 440, 40, 140, 130)
    return d


def q_m3_tc():
    d = Drawing(520, 240, "Mesure du courant d'une ligne sans légendes")
    d.wire((40, 110), (480, 110), width=4)
    d.add(f'<ellipse cx="160" cy="110" rx="20" ry="48" fill="none" stroke="{ACCENT}" stroke-width="6"/>')
    d.wire((180, 130), (260, 130), (260, 170)); d.wire((180, 145), (220, 145), (220, 210), (320, 210), (320, 190))
    d.add(f'<circle cx="290" cy="180" r="18" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>'); d.text(290, 186, "A", weight="700")
    d.wire((260, 170), (272, 180)); d.wire((308, 180), (320, 190))
    d.resistor((400, 110), (400, 200)); d.wire((400, 200), (400, 220))
    d.zone("tc", 130, 56, 60, 108); d.zone("ampèremètre", 266, 156, 48, 48); d.zone("charge", 380, 130, 40, 60)
    return d


def q_m4_pnp():
    d = Drawing(520, 240, "Capteur 3 fils et sa charge, sans légendes")
    block(d, 40, 80, 90, 70, "", size=12)
    d.wire((130, 95), (300, 95), (300, 40), (460, 40)); d.wire((130, 115), (250, 115), (250, 170)); d.resistor((250, 170), (250, 215))
    d.wire((250, 215), (460, 215)); d.wire((130, 135), (200, 135), (200, 215))
    d.zone("brun", 150, 82, 90, 26); d.zone("noir", 150, 108, 80, 20); d.zone("bleu", 140, 128, 50, 26)
    return d


def q_m5_collecteur():
    d = Drawing(480, 260, "Coupe d'un moteur à courant continu sans légendes")
    d.add(f'<circle cx="240" cy="130" r="110" fill="#eef4f3" stroke="{INK}" stroke-width="3"/>')
    d.add(f'<rect x="144" y="90" width="34" height="80" rx="6" fill="#c9d8dd" stroke="{INK}" stroke-width="2"/><rect x="302" y="90" width="34" height="80" rx="6" fill="#c9d8dd" stroke="{INK}" stroke-width="2"/>')
    d.add(f'<circle cx="240" cy="130" r="56" fill="#dfe8ea" stroke="{INK}" stroke-width="2"/>')
    d.add(f'<circle cx="240" cy="130" r="20" fill="{PAPER}" stroke="{ACCENT}" stroke-width="4"/>')
    d.zone("collecteur", 218, 108, 44, 44); d.zone("inducteur", 140, 86, 42, 88); d.zone("carcasse", 200, 22, 80, 40)
    return d


def q_m6_rotor():
    d = Drawing(560, 230, "Moteur asynchrone éclaté sans légendes : trois pièces côte à côte")
    d.add(f'<rect x="30" y="50" width="170" height="130" rx="14" fill="#c9d8dd" stroke="{INK}" stroke-width="2"/><circle cx="115" cy="115" r="46" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>')
    for k in range(5):
        y = 85 + 15 * k
        d.wire((270, y), (370, y), color=ACCENT, width=3)
    d.add(f'<rect x="262" y="75" width="10" height="80" fill="{INK}"/><rect x="368" y="75" width="10" height="80" fill="{INK}"/>')
    d.wire((230, 115), (262, 115), width=6); d.wire((378, 115), (420, 115), width=6)
    d.add(f'<path d="M450 70 l30 20 l0 50 l-30 20 z" fill="#dfe8ea" stroke="{INK}" stroke-width="2"/><circle cx="505" cy="115" r="30" fill="none" stroke="{INK}" stroke-width="2"/>')
    d.zone("stator", 30, 50, 170, 130); d.zone("rotor", 240, 70, 150, 90); d.zone("flasque", 440, 70, 100, 90)
    return d


QUESTION_DIAGRAMS = {1: q_m1_sectionneur, 2: q_m2_plaques, 3: q_m3_tc, 4: q_m4_pnp, 5: q_m5_collecteur, 6: q_m6_rotor}

PARTS = {"p1": range(1, 4), "p2": range(4, 7), "p3": range(7, 10), "p4": range(10, 13)}


def question_dir(module):
    """Dossier des schémas des questions sur schéma : content/moteurs/<partie>/m<N>/schemas."""
    part = next((slug for slug, modules in PARTS.items() if module in modules), None)
    if part is None:
        raise ValueError(f"module {module} hors des parties 1 à 4")
    return ROOT / "content" / SLUG / part / f"m{module}" / "schemas"
