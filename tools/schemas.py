"""Générateur des schémas du cours d'électronique (SVG inertes, symboles CEI).

Usage : python tools/schemas.py
Écrit les schémas des sections dans static/content/electro/m<N>/ et ceux des questions sur schéma dans
content/electro/p<P>/m<N>/schemas/ (p1 pour les modules 1 à 4, p2 pour les modules 5 à 7). Les zones des questions sur schéma sont affichées pour questions.json.
Tous les dessins sont originaux ; aucun n'est repris du livre de référence.
"""
import math
import re
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
INK, ACCENT, SOFT, PAPER = "#173f58", "#0d665e", "#7d93a0", "#fcfefe"
FONT = "system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
LANG = "fr"  # langue des libellés ; main() génère aussi la version anglaise

# Libellés anglais des schémas ; les virgules décimales restantes deviennent des points (tr).
EN = {
    "Le courant conventionnel sort par la borne + du générateur.": "Conventional current leaves through the + terminal of the source.",
    "en série": "in series", "en parallèle": "in parallel",
    "Req = R1 + R2 + R3 = 6,5 kΩ": "Req = R1 + R2 + R3 = 6.5 kΩ",
    "1/Req = 1/R1 + 1/R2  donc  Req = 3 kΩ": "1/Req = 1/R1 + 1/R2  so  Req = 3 kΩ",
    "À vide : Vs = 6 V. Chargé : Vs = 4 V.": "Unloaded: Vout = 6 V. Loaded: Vout = 4 V.",
    "Ve": "Vin", "Vs": "Vout", "Ve = 5 V": "Vin = 5 V",
    "Région P (trous)": "P region (holes)", "Région N (électrons)": "N region (electrons)",
    "zone de déplétion": "depletion zone", "Anode (A)": "Anode (A)", "Cathode (K)": "Cathode (K)",
    "sens passant": "forward direction", "bague = cathode": "band = cathode",
    "passante": "conducting", "bloquée": "blocked",
    "seuil ≈ 0,7 V": "threshold ≈ 0.7 V", "blocage en inverse : I ≈ 0": "reverse blocking: I ≈ 0",
    "Anode (+)": "Anode (+)", "Cathode (−)": "Cathode (−)",
    "patte longue = anode ; méplat du boîtier = cathode": "long leg = anode; flat edge = cathode",
    "seuil : rouge ≈ 1,8 V, vert ≈ 2,1 V, bleu ≈ 3 V": "threshold: red ≈ 1.8 V, green ≈ 2.1 V, blue ≈ 3 V",
    "Us ≈ 5,1 V même si E varie": "Vout ≈ 5.1 V even if E varies",
    "flèche sur l'émetteur, vers l'extérieur": "arrow on the emitter, pointing out",
    "flèche sur l'émetteur, vers l'intérieur": "arrow on the emitter, pointing in",
    "la grille commande le courant drain-source": "the gate controls the drain-source current",
    "droite de charge": "load line", "saturation": "saturation", "régime linéaire": "linear region",
    "blocage : IB = 0": "cut-off: IB = 0", "mode diode": "diode mode",
    "Bloqué : VCE ≈ VCC, IC = 0": "Cut off: VCE ≈ VCC, IC = 0", "Saturé : VCE ≈ 0,2 V": "Saturated: VCE ≈ 0.2 V",
    "RC (charge)": "RC (load)",
    "IC sat ≈ 88 mA ; β min = 100 ; IB = 2 × IC / β": "IC sat ≈ 88 mA; β min = 100; IB = 2 × IC / β",
    "début de saturation": "start of saturation", "relais 12 V": "12 V relay",
    "pénombre ; R élevée": "dim light; high R", "éclairement (lux)": "illuminance (lux)",
    "β total ≈ β1 × β2": "total β ≈ β1 × β2",
    "VGS(off) = −3 V : bloqué": "VGS(off) = −3 V: off", "VGS = 0 : conduit": "VGS = 0: on",
    "5 mA ; 10 V": "5 mA; 10 V", "50 mA ; 250 mW": "50 mA; 250 mW", "50 µA ; 7,5 mA": "50 µA; 7.5 mA",
    "τ = R × C = 1 s ; 63 %": "τ = R × C = 1 s; 63 %",
    # Partie 2
    "Ueff ≈ 7,07 V": "Urms ≈ 7.07 V", "Ucc = 20 V": "Upp = 20 V", "12 V eff": "12 V rms", "10 V eff": "10 V rms",
    "I = 10 mA eff": "I = 10 mA rms", "continu": "DC", "alternatif": "AC", "en phase : déphasage 0°": "in phase: 0° shift",
    "50 Hz : 3,18 kΩ": "50 Hz: 3.18 kΩ", "50 Hz : 31,4 Ω": "50 Hz: 31.4 Ω", "500 Hz : 314 Ω": "500 Hz: 314 Ω",
    "Voie 1 : 2 V/div": "Channel 1: 2 V/div", "Base de temps : 1 ms/div": "Timebase: 1 ms/div",
    "Ucc = 4 div × 2 V = 8 V": "Upp = 4 div × 2 V = 8 V", "GBF": "Generator", "voie 1": "channel 1", "voie 2": "channel 2",
    "masse commune": "common ground", "b = a : 45°": "b = a: 45°", "Vs / Ve": "Vout / Vin", "ve": "vin", "vs": "vout",
    "fc : Xc = R": "fc: Xc = R", "f0 ≈ 5 kHz : XL = XC ≈ 316 Ω": "f0 ≈ 5 kHz: XL = XC ≈ 316 Ω", "BP ≈ 796 Hz": "BW ≈ 796 Hz",
    "amplificateur": "amplifier", "station reçue": "received station", "C chargé : énergie électrique": "C charged: electric energy",
    "C déchargé": "C discharged", "I maximal : énergie magnétique": "I maximum: magnetic energy", "enveloppe": "envelope",
}


def tr(text):
    if LANG != "en":
        return text
    text = EN.get(text, text)
    return re.sub(r"(\d),(\d)", r"\1.\2", text)


def fmt(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


class Drawing:
    def __init__(self, width, height, title):
        self.w, self.h, self.title = width, height, title
        self.items, self.zones = [], {}

    # --- éléments de base ---------------------------------------------------------------------------------------------
    def add(self, markup):
        self.items.append(markup)

    def wire(self, *points, color=INK, width=2):
        pts = " ".join(f"{fmt(x)},{fmt(y)}" for x, y in points)
        self.add(f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linejoin="round"/>')

    def dot(self, p):
        self.add(f'<circle cx="{fmt(p[0])}" cy="{fmt(p[1])}" r="3.5" fill="{INK}"/>')

    def text(self, x, y, s, anchor="middle", size=13, color=INK, weight="400", italic=False):
        s = tr(s)
        style = ' font-style="italic"' if italic else ""
        self.add(
            f'<text x="{fmt(x)}" y="{fmt(y)}" text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" '
            f'fill="{color}"{style}>{escape(s)}</text>'
        )

    def arrow(self, a, b, label=None, color=ACCENT, offset=(0, -8)):
        """Flèche de courant ou de tension, de a vers b."""
        self.wire(a, b, color=color, width=2)
        ang = math.atan2(b[1] - a[1], b[0] - a[0])
        p1 = (b[0] - 9 * math.cos(ang - 0.45), b[1] - 9 * math.sin(ang - 0.45))
        p2 = (b[0] - 9 * math.cos(ang + 0.45), b[1] - 9 * math.sin(ang + 0.45))
        self.add(f'<polygon points="{fmt(b[0])},{fmt(b[1])} {fmt(p1[0])},{fmt(p1[1])} {fmt(p2[0])},{fmt(p2[1])}" fill="{color}"/>')
        if label:
            mid = ((a[0] + b[0]) / 2 + offset[0], (a[1] + b[1]) / 2 + offset[1])
            self.text(mid[0], mid[1], label, color=color, weight="600")

    def zone(self, name, x, y, w, h):
        self.zones[name] = {"x": round(x), "y": round(y), "w": round(w), "h": round(h)}

    # --- dipôles : dessinés horizontalement puis tournés entre a et b ---------------------------------------------------
    def _two(self, a, b, body, body_len):
        length = math.dist(a, b)
        ang = math.degrees(math.atan2(b[1] - a[1], b[0] - a[0]))
        lead = (length - body_len) / 2
        self.add(
            f'<g transform="translate({fmt(a[0])},{fmt(a[1])}) rotate({fmt(ang)})" fill="none" stroke="{INK}" stroke-width="2">'
            f'<line x1="0" y1="0" x2="{fmt(lead)}" y2="0"/>'
            f'<line x1="{fmt(lead + body_len)}" y1="0" x2="{fmt(length)}" y2="0"/>'
            f'<g transform="translate({fmt(lead)},0)">{body}</g></g>'
        )
        return ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)

    def _label(self, mid, a, b, label, value, side=1):
        if not (label or value):
            return
        vertical = abs(a[0] - b[0]) < 1
        if vertical:
            x = mid[0] + 18 * side
            anchor = "start" if side > 0 else "end"
            if label:
                self.text(x, mid[1] - 2, label, anchor=anchor, weight="600")
            if value:
                self.text(x, mid[1] + 14, value, anchor=anchor, color=SOFT, size=12)
        else:
            y = mid[1] - 16 * side if side > 0 else mid[1] + 26
            if label:
                self.text(mid[0], y - (12 if value and side > 0 else 0), label, weight="600")
            if value:
                self.text(mid[0], y + (0 if side > 0 else 14), value, color=SOFT, size=12)

    def resistor(self, a, b, label=None, value=None, side=1):
        mid = self._two(a, b, '<rect x="0" y="-7" width="36" height="14" rx="2" fill="#fcfefe"/>', 36)
        self._label(mid, a, b, label, value, side)
        return mid

    def ldr(self, a, b, label="LDR", value=None, side=1):
        body = ('<rect x="0" y="-7" width="36" height="14" rx="2" fill="#fcfefe"/><circle cx="18" cy="0" r="16"/>')
        mid = self._two(a, b, body, 36)
        vertical = abs(a[0] - b[0]) < 1
        sx = -1 if vertical else 1
        for k in (-8, 6):
            start = (mid[0] - 36 * sx + (k if not vertical else -6), mid[1] - 30 + (0 if not vertical else k + 30))
            end = (mid[0] - 14 * sx + (k if not vertical else -18), mid[1] - 12 + (0 if not vertical else k + 18))
            if vertical:
                start, end = (mid[0] - 40, mid[1] + k - 14), (mid[0] - 20, mid[1] + k - 4)
            self.arrow(start, end, color=ACCENT)
        self._label(mid, a, b, label, value, side)
        return mid

    def capacitor(self, a, b, label=None, value=None, side=1):
        body = '<line x1="0" y1="0" x2="12" y2="0"/><line x1="12" y1="-13" x2="12" y2="13"/><line x1="20" y1="-13" x2="20" y2="13"/><line x1="20" y1="0" x2="32" y2="0"/>'
        mid = self._two(a, b, body, 32)
        self._label(mid, a, b, label, value, side)
        return mid

    def battery(self, a, b, label=None, value=None, side=-1):
        """Générateur continu : de a (borne −) vers b (borne +)."""
        body = ('<line x1="0" y1="0" x2="12" y2="0"/><line x1="12" y1="-7" x2="12" y2="7" stroke-width="4"/>'
                '<line x1="20" y1="-15" x2="20" y2="15"/><line x1="20" y1="0" x2="32" y2="0"/>')
        mid = self._two(a, b, body, 32)
        vertical = abs(a[0] - b[0]) < 1
        plus = (mid[0] + 12, mid[1] + (-10 if b[1] < a[1] else 16)) if vertical else (mid[0] + 10, mid[1] - 18)
        self.text(plus[0], plus[1], "+", color=ACCENT, weight="700")
        self._label(mid, a, b, label, value, side)
        return mid

    def ac_source(self, a, b, label=None, value=None, side=-1):
        body = '<circle cx="16" cy="0" r="16" fill="#fcfefe"/><path d="M6 0 C 9 -9, 13 -9, 16 0 S 23 9, 26 0"/>'
        mid = self._two(a, b, body, 32)
        self._label(mid, a, b, label, value, side)
        return mid

    def diode(self, a, b, label=None, value=None, side=1, kind="diode"):
        """Diode passante de a (anode) vers b (cathode)."""
        bar = '<line x1="22" y1="-11" x2="22" y2="11"/>'
        if kind == "zener":
            bar = '<polyline points="18,-14 22,-11 22,11 26,14"/>'
        body = f'<polygon points="0,-11 0,11 22,0" fill="#fcfefe"/>{bar}'
        if kind == "led":
            body += ('<line x1="8" y1="-16" x2="18" y2="-27"/><polyline points="12,-27 18,-27 18,-21"/>'
                     '<line x1="16" y1="-14" x2="26" y2="-25"/><polyline points="20,-25 26,-25 26,-19"/>')
        mid = self._two(a, b, body, 22)
        self._label(mid, a, b, label, value, side)
        return mid

    def switch(self, a, b, label=None, closed=False, side=1):
        tip = "34,0" if closed else "32,-14"
        body = f'<circle cx="2" cy="0" r="2.5" fill="{INK}"/><circle cx="34" cy="0" r="2.5" fill="{INK}"/><line x1="2" y1="0" x2="{tip.split(",")[0]}" y2="{tip.split(",")[1]}"/>'
        mid = self._two(a, b, body, 36)
        self._label(mid, a, b, label, None, side)
        return mid

    def lamp(self, a, b, label=None, value=None, side=1, lit=False):
        fill = "#fff0c2" if lit else "#fcfefe"
        body = f'<circle cx="14" cy="0" r="14" fill="{fill}"/><line x1="4" y1="-10" x2="24" y2="10"/><line x1="4" y1="10" x2="24" y2="-10"/>'
        mid = self._two(a, b, body, 28)
        self._label(mid, a, b, label, value, side)
        return mid

    def coil(self, a, b, label="K", value=None, side=1):
        body = '<rect x="0" y="-9" width="30" height="18" fill="#fcfefe"/><line x1="0" y1="9" x2="30" y2="-9"/>'
        mid = self._two(a, b, body, 30)
        self._label(mid, a, b, label, value, side)
        return mid

    def inductor(self, a, b, label=None, value=None, side=1):
        """Bobine (symbole CEI : quatre demi-cercles)."""
        body = '<path d="M0 0 a5 5 0 0 1 10 0 a5 5 0 0 1 10 0 a5 5 0 0 1 10 0 a5 5 0 0 1 10 0"/>'
        mid = self._two(a, b, body, 40)
        self._label(mid, a, b, label, value, side)
        return mid

    def variable_capacitor(self, a, b, label=None, value=None, side=1):
        body = ('<line x1="0" y1="0" x2="12" y2="0"/><line x1="12" y1="-13" x2="12" y2="13"/><line x1="20" y1="-13" x2="20" y2="13"/>'
                '<line x1="20" y1="0" x2="32" y2="0"/><line x1="2" y1="16" x2="30" y2="-16"/><polyline points="22,-16 30,-16 30,-8"/>')
        mid = self._two(a, b, body, 32)
        self._label(mid, a, b, label, value, side)
        return mid

    def antenna(self, p):
        x, y = p
        self.wire((x, y), (x, y - 40))
        self.wire((x - 14, y - 58), (x, y - 40), (x + 14, y - 58))
        self.wire((x - 14, y - 58), (x + 14, y - 58))

    def meter(self, a, b, letter):
        """Ampèremètre (A) ou voltmètre (V) entre a et b ; la lettre ne tourne pas."""
        mid = self._two(a, b, '<circle cx="15" cy="0" r="15" fill="#fcfefe"/>', 30)
        self.text(mid[0], mid[1] + 5, letter, weight="700")
        return mid

    def ground(self, p):
        x, y = p
        self.wire((x, y), (x, y + 8))
        for i, half in enumerate((12, 8, 4)):
            self.wire((x - half, y + 8 + 5 * i), (x + half, y + 8 + 5 * i))

    # --- composants à trois broches -------------------------------------------------------------------------------------
    def bjt(self, cx, cy, kind="npn", labels=True, circle=True):
        """Transistor bipolaire ; renvoie les extrémités des broches B, C, E."""
        if circle:
            self.add(f'<circle cx="{fmt(cx + 2)}" cy="{fmt(cy)}" r="24" fill="#fcfefe" stroke="{INK}" stroke-width="2"/>')
        self.wire((cx - 40, cy), (cx - 10, cy))
        self.wire((cx - 10, cy - 15), (cx - 10, cy + 15), width=4)
        self.wire((cx - 10, cy - 7), (cx + 12, cy - 22), (cx + 12, cy - 42))
        self.wire((cx - 10, cy + 7), (cx + 12, cy + 22), (cx + 12, cy + 42))
        if kind == "npn":
            tip, back = (cx + 10, cy + 21), (cx - 1, cy + 14)
        else:
            tip, back = (cx - 7, cy + 9), (cx + 4, cy + 16)
        ang = math.atan2(tip[1] - back[1], tip[0] - back[0])
        p1 = (tip[0] - 10 * math.cos(ang - 0.5), tip[1] - 10 * math.sin(ang - 0.5))
        p2 = (tip[0] - 10 * math.cos(ang + 0.5), tip[1] - 10 * math.sin(ang + 0.5))
        self.add(f'<polygon points="{fmt(tip[0])},{fmt(tip[1])} {fmt(p1[0])},{fmt(p1[1])} {fmt(p2[0])},{fmt(p2[1])}" fill="{INK}"/>')
        b, c, e = (cx - 40, cy), (cx + 12, cy - 42), (cx + 12, cy + 42)
        if labels:
            self.text(cx - 34, cy - 8, "B", weight="700", color=ACCENT)
            self.text(cx + 24, cy - 30, "C", weight="700", color=ACCENT)
            self.text(cx + 24, cy + 38, "E", weight="700", color=ACCENT)
        return b, c, e

    def jfet(self, cx, cy, labels=True):
        """JFET canal N ; renvoie G, D, S."""
        self.add(f'<circle cx="{fmt(cx + 4)}" cy="{fmt(cy)}" r="24" fill="#fcfefe" stroke="{INK}" stroke-width="2"/>')
        self.wire((cx - 6, cy - 16), (cx - 6, cy + 16), width=4)
        self.wire((cx - 6, cy - 10), (cx + 14, cy - 10), (cx + 14, cy - 42))
        self.wire((cx - 6, cy + 10), (cx + 14, cy + 10), (cx + 14, cy + 42))
        self.wire((cx - 40, cy + 10), (cx - 6, cy + 10))
        self.add(f'<polygon points="{fmt(cx - 7)},{fmt(cy + 10)} {fmt(cx - 17)},{fmt(cy + 5)} {fmt(cx - 17)},{fmt(cy + 15)}" fill="{INK}"/>')
        g, d, s = (cx - 40, cy + 10), (cx + 14, cy - 42), (cx + 14, cy + 42)
        if labels:
            self.text(cx - 32, cy + 2, "G", weight="700", color=ACCENT)
            self.text(cx + 26, cy - 30, "D", weight="700", color=ACCENT)
            self.text(cx + 26, cy + 38, "S", weight="700", color=ACCENT)
        return g, d, s

    # --- courbes --------------------------------------------------------------------------------------------------------
    def graph(self, x, y, w, h, xr, yr, series, xlabel, ylabel, marks=(), xticks=(), yticks=()):
        """Repère et courbes : series = [(points en unités, couleur, légende)]."""
        def px(v):
            return x + (v - xr[0]) / (xr[1] - xr[0]) * w

        def py(v):
            return y + h - (v - yr[0]) / (yr[1] - yr[0]) * h

        x0, y0 = px(max(xr[0], 0)) if xr[0] < 0 else x, py(max(yr[0], 0)) if yr[0] < 0 else y + h
        self.arrow((x - 4, y0), (x + w + 14, y0), color=INK)
        self.arrow((x0, y + h + 4), (x0, y - 14), color=INK)
        self.text(x + w + 14, y0 - 10, xlabel, anchor="end", size=12)
        self.text(x0 + 8, y - 4, ylabel, anchor="start", size=12)
        for v, s in xticks:
            self.wire((px(v), y0 - 3), (px(v), y0 + 3))
            self.text(px(v), y0 + 16, s, size=11, color=SOFT)
        for v, s in yticks:
            self.wire((x0 - 3, py(v)), (x0 + 3, py(v)))
            self.text(x0 - 6, py(v) + 4, s, anchor="end", size=11, color=SOFT)
        for points, color, legend, *where in series:
            self.wire(*[(px(a), py(b)) for a, b in points], color=color, width=2.5)
            if legend and where:
                self.text(px(where[0][0]), py(where[0][1]), legend, anchor="start", size=12, color=color, weight="600")
            elif legend:
                lx, ly = points[-1]
                self.text(px(lx) - 4, py(ly) - 8, legend, anchor="end", size=12, color=color, weight="600")
        for (a, b), s in marks:
            self.add(f'<line x1="{fmt(px(a))}" y1="{fmt(py(b))}" x2="{fmt(px(a))}" y2="{fmt(y0)}" stroke="{SOFT}" stroke-dasharray="4 3"/>')
            self.text(px(a) + 6, py(b) - 6, s, anchor="start", size=12, color=ACCENT, weight="600")
        return px, py

    def svg(self):
        body = "".join(self.items)
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" width="{self.w}" height="{self.h}" role="img" '
            f'font-family="{FONT}">'
            + (f"<title>{escape(self.title)}</title>" if LANG == "fr" else "")  # en anglais, le texte alternatif de la page suffit
            + f'<rect width="{self.w}" height="{self.h}" rx="14" fill="{PAPER}"/>{body}</svg>\n'
        )


# ======================================================================================================================
# Schémas des sections. Chaque fonction renvoie un Drawing ; le nom du fichier est celui de la fonction.
# ======================================================================================================================

def loop(d, left, top, right, bottom):
    """Rectangle de câblage : coins du circuit."""
    return (left, top), (right, top), (right, bottom), (left, bottom)


# --- Module 1 : révision du courant continu ---------------------------------------------------------------------------

def m1_circuit_simple():
    d = Drawing(420, 220, "Circuit simple : pile, interrupteur et lampe")
    d.battery((60, 170), (60, 60), "E", "9 V")
    d.wire((60, 60), (60, 40), (150, 40))
    d.switch((150, 40), (230, 40), "K", closed=True)
    d.wire((230, 40), (340, 40), (340, 80))
    d.lamp((340, 80), (340, 150), "L", side=1, lit=True)
    d.wire((340, 150), (340, 190), (60, 190), (60, 170))
    d.arrow((260, 52), (310, 52), "I", offset=(0, 18))
    d.text(200, 212, "Le courant conventionnel sort par la borne + du générateur.", size=12, color=SOFT)
    return d


def m1_mesures():
    d = Drawing(460, 230, "Brancher un ampèremètre en série et un voltmètre en parallèle")
    d.battery((50, 170), (50, 60), "E", "12 V")
    d.wire((50, 60), (50, 40), (120, 40))
    d.meter((120, 40), (180, 40), "A")
    d.wire((180, 40), (300, 40), (300, 80))
    d.resistor((300, 80), (300, 150), "R", "1 kΩ", side=-1)
    d.wire((300, 150), (300, 190), (50, 190), (50, 170))
    d.dot((300, 70)); d.dot((300, 165))
    d.wire((300, 70), (390, 70), (390, 95))
    d.meter((390, 95), (390, 140), "V")
    d.wire((390, 140), (390, 165), (300, 165))
    d.text(150, 76, "en série", color=ACCENT, size=12, weight="600")
    d.text(420, 120, "en parallèle", anchor="start", color=ACCENT, size=12, weight="600")
    d.w = 520
    return d


def m1_ohm_circuit():
    d = Drawing(420, 220, "Résistance de 4,7 kΩ alimentée sous 12 V")
    d.battery((70, 165), (70, 65), "U", "12 V")
    d.wire((70, 65), (70, 40), (320, 40), (320, 75))
    d.resistor((320, 75), (320, 155), "R", "4,7 kΩ")
    d.wire((320, 155), (320, 190), (70, 190), (70, 165))
    d.arrow((170, 52), (240, 52), "I = ?", offset=(0, 20))
    return d


def m1_ohm_graph():
    d = Drawing(440, 260, "Caractéristique U = f(I) de deux résistances")
    d.graph(60, 30, 320, 180, (0, 10), (0, 20),
            [([(0, 0), (10, 10)], ACCENT, "R = 1 kΩ"), ([(0, 0), (9.5, 19)], INK, "R = 2 kΩ")],
            "I (mA)", "U (V)", marks=[((5, 10), "5 mA ; 10 V")],
            xticks=[(5, "5"), (10, "10")], yticks=[(10, "10"), (20, "20")])
    return d


def m1_serie():
    d = Drawing(480, 210, "Trois résistances en série")
    d.battery((50, 160), (50, 60), "E", "12 V")
    d.wire((50, 60), (50, 40), (90, 40))
    d.resistor((90, 40), (170, 40), "R1", "1 kΩ")
    d.resistor((170, 40), (270, 40), "R2", "2,2 kΩ")
    d.resistor((270, 40), (370, 40), "R3", "3,3 kΩ")
    d.wire((370, 40), (420, 40), (420, 180), (50, 180), (50, 160))
    d.arrow((400, 90), (400, 140), "I", offset=(14, 4))
    d.text(240, 205, "Req = R1 + R2 + R3 = 6,5 kΩ", size=13, color=ACCENT, weight="600")
    d.h = 220
    return d


def m1_parallele():
    d = Drawing(440, 230, "Deux résistances en parallèle")
    d.battery((50, 170), (50, 70), "E", "12 V")
    d.wire((50, 70), (50, 40), (330, 40))
    d.dot((200, 40)); d.dot((200, 190))
    d.wire((200, 40), (200, 80)); d.resistor((200, 80), (200, 150), "R1", "4 kΩ", side=-1); d.wire((200, 150), (200, 190))
    d.wire((330, 40), (330, 80)); d.resistor((330, 80), (330, 150), "R2", "12 kΩ"); d.wire((330, 150), (330, 190))
    d.wire((330, 190), (50, 190), (50, 170))
    d.text(250, 222, "1/Req = 1/R1 + 1/R2  donc  Req = 3 kΩ", size=13, color=ACCENT, weight="600")
    return d


def m1_puissance():
    d = Drawing(420, 220, "Puissance dissipée par une résistance")
    d.battery((70, 165), (70, 65), "U", "10 V")
    d.wire((70, 65), (70, 40), (320, 40), (320, 75))
    d.resistor((320, 75), (320, 155), "R", "100 Ω")
    d.wire((320, 155), (320, 190), (70, 190), (70, 165))
    d.arrow((170, 52), (240, 52), "I = 0,1 A", offset=(0, 20))
    d.text(200, 120, "P = U × I = 1 W", color=ACCENT, weight="700", size=15)
    return d


def m1_puissance_graph():
    d = Drawing(440, 260, "Puissance dissipée dans 100 Ω selon le courant")
    pts = [(i, 100 * (i / 1000) ** 2 * 1000) for i in range(0, 101, 5)]  # I en mA, P en mW
    d.graph(60, 30, 320, 180, (0, 100), (0, 1000), [(pts, ACCENT, "P = R × I²")], "I (mA)", "P (mW)",
            marks=[((50, 250), "50 mA ; 250 mW")], xticks=[(50, "50"), (100, "100")], yticks=[(500, "500"), (1000, "1000")])
    return d


def m1_diviseur():
    d = Drawing(420, 260, "Diviseur de tension à deux résistances")
    d.battery((70, 190), (70, 80), "Ve", "12 V")
    d.wire((70, 80), (70, 40), (230, 40), (230, 60))
    d.resistor((230, 60), (230, 120), "R1", "10 kΩ")
    d.dot((230, 135))
    d.wire((230, 120), (230, 150))
    d.resistor((230, 150), (230, 210), "R2", "4,7 kΩ")
    d.wire((230, 210), (230, 230), (70, 230), (70, 190))
    d.wire((230, 135), (350, 135))
    d.add('<circle cx="354" cy="135" r="4" fill="none" stroke="#173f58" stroke-width="2"/>')
    d.arrow((370, 225), (370, 145), "Vs", offset=(18, 0))
    d.dot((230, 230)); d.wire((230, 230), (350, 230))
    d.add('<circle cx="354" cy="230" r="4" fill="none" stroke="#173f58" stroke-width="2"/>')
    return d


def m1_diviseur_charge():
    d = Drawing(460, 260, "Diviseur de tension chargé par une résistance RL")
    d.battery((60, 190), (60, 80), "Ve", "12 V")
    d.wire((60, 80), (60, 40), (220, 40), (220, 60))
    d.resistor((220, 60), (220, 120), "R1", "10 kΩ")
    d.wire((220, 120), (220, 150)); d.dot((220, 135))
    d.resistor((220, 150), (220, 210), "R2", "10 kΩ")
    d.wire((220, 210), (220, 230), (60, 230), (60, 190))
    d.wire((220, 135), (360, 135), (360, 150))
    d.resistor((360, 150), (360, 210), "RL", "10 kΩ")
    d.wire((360, 210), (360, 230), (220, 230)); d.dot((220, 230))
    d.text(300, 254, "À vide : Vs = 6 V. Chargé : Vs = 4 V.", size=12, color=ACCENT, weight="600")
    return d


def m1_diviseur_courant():
    d = Drawing(530, 240, "Le courant se partage entre deux branches")
    d.battery((50, 180), (50, 70), "E", "6 V")
    d.wire((50, 70), (50, 40), (200, 40))
    d.arrow((90, 52), (150, 52), "I = 9 mA", offset=(0, 22))
    d.dot((200, 40)); d.wire((200, 40), (360, 40))
    d.wire((200, 40), (200, 90)); d.resistor((200, 90), (200, 160), "R1", "1 kΩ", side=-1); d.wire((200, 160), (200, 200))
    d.wire((360, 40), (360, 90)); d.resistor((360, 90), (360, 160), "R2", "2 kΩ"); d.wire((360, 160), (360, 200))
    d.wire((360, 200), (50, 200), (50, 180)); d.dot((200, 200))
    d.arrow((215, 60), (215, 85), "I1 = 6 mA", offset=(44, 4))
    d.arrow((375, 60), (375, 85), "I2 = 3 mA", offset=(44, 4))
    return d


def m1_trois_branches():
    d = Drawing(500, 230, "Loi des nœuds : I = I1 + I2 + I3")
    d.wire((40, 115), (160, 115))
    d.arrow((60, 103), (130, 103), "I", offset=(0, -8))
    d.dot((160, 115))
    for i, y in enumerate((50, 115, 180)):
        d.wire((160, 115), (220, y), (300, y))
        d.resistor((300, y), (390, y), f"R{i + 1}")
        d.wire((390, y), (440, y))
        d.arrow((230, y - 12), (280, y - 12), f"I{i + 1}", offset=(0, -6))
    d.wire((440, 50), (440, 180)); d.dot((440, 115))
    return d


def m1_rc_circuit():
    d = Drawing(440, 230, "Charge d'un condensateur à travers une résistance")
    d.battery((60, 170), (60, 70), "E", "10 V")
    d.wire((60, 70), (60, 40), (110, 40))
    d.switch((110, 40), (170, 40), "K")
    d.resistor((170, 40), (280, 40), "R", "10 kΩ")
    d.wire((280, 40), (340, 40), (340, 85))
    d.capacitor((340, 85), (340, 145), "C", "100 µF")
    d.wire((340, 145), (340, 190), (60, 190), (60, 170))
    d.arrow((400, 180), (400, 60), "Uc", offset=(20, 0))
    return d


def m1_rc_courbe():
    d = Drawing(460, 260, "Tension aux bornes du condensateur pendant la charge")
    pts = [(t / 10, 10 * (1 - math.exp(-t / 10))) for t in range(0, 51)]
    d.graph(60, 30, 330, 180, (0, 5), (0, 10), [(pts, ACCENT, "Uc(t)", (3, 8)), ([(0, 10), (5, 10)], SOFT, "E = 10 V", (2.6, 10.4))],
            "t (s)", "Uc (V)", marks=[((1, 6.3), "τ = R × C = 1 s ; 63 %")],
            xticks=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")], yticks=[(6.3, "6,3"), (10, "10")])
    return d


# --- Module 2 : la diode ----------------------------------------------------------------------------------------------

def m2_jonction():
    d = Drawing(460, 220, "Jonction PN : zone de déplétion au contact des deux régions")
    d.add('<rect x="60" y="50" width="160" height="110" fill="#fff1f1" stroke="#173f58" stroke-width="2"/>')
    d.add('<rect x="240" y="50" width="160" height="110" fill="#e3f4f1" stroke="#173f58" stroke-width="2"/>')
    d.add('<rect x="200" y="50" width="60" height="110" fill="#e9eff1" stroke="#7d93a0" stroke-dasharray="5 4"/>')
    for i in range(3):
        for j in range(3):
            d.text(90 + 40 * j, 85 + 30 * i, "+", size=18, color="#9d2b2b", weight="700")
            d.text(290 + 40 * j, 85 + 30 * i, "−", size=18, color=ACCENT, weight="700")
    d.text(140, 40, "Région P (trous)", weight="600")
    d.text(320, 40, "Région N (électrons)", weight="600")
    d.text(230, 185, "zone de déplétion", color=SOFT, size=12)
    d.wire((20, 105), (60, 105)); d.wire((400, 105), (440, 105))
    d.text(30, 96, "A", weight="700", color=ACCENT); d.text(430, 96, "K", weight="700", color=ACCENT)
    return d


def m2_symbole():
    d = Drawing(420, 200, "Symbole de la diode et repère de la cathode sur le boîtier")
    d.diode((60, 70), (360, 70))
    d.text(80, 52, "Anode (A)", anchor="start", weight="600")
    d.text(340, 52, "Cathode (K)", anchor="end", weight="600")
    d.arrow((150, 100), (270, 100), "sens passant", offset=(0, 18))
    d.add('<rect x="130" y="140" width="160" height="34" rx="6" fill="#e9eff1" stroke="#173f58" stroke-width="2"/>')
    d.add('<rect x="262" y="140" width="14" height="34" fill="#173f58"/>')
    d.wire((80, 157), (130, 157)); d.wire((290, 157), (340, 157))
    d.text(320, 196, "bague = cathode", size=12, color=ACCENT, weight="600")
    d.h = 210
    return d


def m2_directe():
    d = Drawing(440, 220, "Diode polarisée en direct : le courant passe et la lampe s'allume")
    d.battery((60, 165), (60, 65), "E", "6 V")
    d.wire((60, 65), (60, 40), (130, 40))
    d.diode((130, 40), (230, 40), "D", "passante")
    d.wire((230, 40), (340, 40), (340, 80))
    d.lamp((340, 80), (340, 150), "L", lit=True)
    d.wire((340, 150), (340, 190), (60, 190), (60, 165))
    d.arrow((250, 52), (310, 52), "I", offset=(0, 20))
    return d


def m2_inverse():
    d = Drawing(440, 220, "Diode polarisée en inverse : pas de courant, la lampe reste éteinte")
    d.battery((60, 165), (60, 65), "E", "6 V")
    d.wire((60, 65), (60, 40), (130, 40))
    d.diode((230, 40), (130, 40), "D", "bloquée")
    d.wire((230, 40), (340, 40), (340, 80))
    d.lamp((340, 80), (340, 150), "L")
    d.wire((340, 150), (340, 190), (60, 190), (60, 165))
    d.text(270, 70, "I = 0", color="#9d2b2b", weight="700")
    return d


def m2_caracteristique():
    d = Drawing(460, 270, "Caractéristique courant-tension d'une diode au silicium")
    pts = [(-2 + i * 0.1, 0) for i in range(20)] + [(v / 100, 0.002 * (math.exp(v / 100 / 0.06) - 1)) for v in range(0, 80)]
    pts = [p for p in pts if p[1] <= 40]
    d.graph(60, 30, 340, 190, (-2, 1.2), (-4, 40), [(pts, ACCENT, "")], "U (V)", "I (mA)",
            marks=[((0.7, 30), "seuil ≈ 0,7 V")], xticks=[(-1, "−1"), (0.7, "0,7"), (1, "1")], yticks=[(20, "20"), (40, "40")])
    d.text(150, 190, "blocage en inverse : I ≈ 0", size=12, color=SOFT)
    return d


def m2_mesure():
    d = Drawing(440, 230, "Mesurer la tension aux bornes d'une diode passante")
    d.battery((60, 170), (60, 70), "E", "5 V")
    d.wire((60, 70), (60, 40), (110, 40))
    d.resistor((110, 40), (210, 40), "R", "470 Ω")
    d.wire((210, 40), (280, 40), (280, 75))
    d.diode((280, 75), (280, 150), "D", side=-1)
    d.wire((280, 150), (280, 190), (60, 190), (60, 170))
    d.dot((280, 60)); d.dot((280, 170))
    d.wire((280, 60), (370, 60), (370, 90)); d.meter((370, 90), (370, 140), "V"); d.wire((370, 140), (370, 170), (280, 170))
    d.text(405, 120, "≈ 0,7 V", anchor="start", color=ACCENT, weight="700")
    d.w = 480
    return d


def m2_led_circuit():
    d = Drawing(440, 220, "LED protégée par une résistance série")
    d.battery((60, 165), (60, 65), "E", "9 V")
    d.wire((60, 65), (60, 40), (110, 40))
    d.resistor((110, 40), (220, 40), "R", "330 Ω")
    d.wire((220, 40), (330, 40), (330, 80))
    d.diode((330, 80), (330, 150), "LED", "2 V", kind="led", side=-1)
    d.wire((330, 150), (330, 190), (60, 190), (60, 165))
    d.arrow((240, 52), (300, 52), "I ≈ 21 mA", offset=(0, 20))
    return d


def m2_led_symbole():
    d = Drawing(420, 200, "Symbole de la LED et repérage des pattes")
    d.diode((60, 80), (360, 80), kind="led")
    d.text(80, 62, "Anode (+)", anchor="start", weight="600")
    d.text(340, 62, "Cathode (−)", anchor="end", weight="600")
    d.text(210, 140, "patte longue = anode ; méplat du boîtier = cathode", size=12, color=ACCENT, weight="600")
    d.text(210, 166, "seuil : rouge ≈ 1,8 V, vert ≈ 2,1 V, bleu ≈ 3 V", size=12, color=SOFT)
    return d


def m2_simple_alternance():
    d = Drawing(440, 220, "Redressement simple alternance")
    d.ac_source((60, 165), (60, 65), "~", "12 V")
    d.wire((60, 65), (60, 40), (140, 40))
    d.diode((140, 40), (240, 40), "D")
    d.wire((240, 40), (330, 40), (330, 75))
    d.resistor((330, 75), (330, 155), "R", "1 kΩ")
    d.wire((330, 155), (330, 190), (60, 190), (60, 165))
    d.arrow((390, 180), (390, 60), "Us", offset=(20, 0))
    return d


def m2_redresse_courbe():
    d = Drawing(460, 270, "Tension d'entrée et tension redressée")
    sine = [(t / 20, 12 * math.sin(2 * math.pi * t / 20 / 2)) for t in range(0, 81)]
    rect = [(t, max(0.0, v - 0.7)) for t, v in sine]
    d.graph(60, 30, 340, 200, (0, 4), (-13, 13), [(sine, SOFT, "Ue", (2.55, -11)), (rect, ACCENT, "Us", (2.1, 9))], "t", "U (V)",
            yticks=[(12, "12"), (-12, "−12")])
    return d


def m2_zener_regulateur():
    d = Drawing(460, 240, "Régulation par diode Zener")
    d.battery((60, 180), (60, 70), "E", "12 V")
    d.wire((60, 70), (60, 40), (110, 40))
    d.resistor((110, 40), (210, 40), "R", "330 Ω")
    d.wire((210, 40), (370, 40)); d.dot((260, 40))
    d.wire((260, 40), (260, 90)); d.diode((260, 160), (260, 90), "DZ", "5,1 V", kind="zener", side=-1); d.wire((260, 160), (260, 210))
    d.wire((370, 40), (370, 90)); d.resistor((370, 90), (370, 160), "RL"); d.wire((370, 160), (370, 210))
    d.wire((370, 210), (60, 210), (60, 180)); d.dot((260, 210))
    d.text(320, 234, "Us ≈ 5,1 V même si E varie", size=12, color=ACCENT, weight="600")
    return d


def m2_zener_courbe():
    d = Drawing(460, 270, "Caractéristique d'une diode Zener de 5,1 V")
    fwd = [(v / 100, min(30, 0.002 * (math.exp(v / 100 / 0.06) - 1))) for v in range(0, 76)]
    rev = [(-v / 10, 0) for v in range(0, 50)] + [(-5.1 - k * 0.01, -k * 1.0) for k in range(0, 31)]
    d.graph(60, 30, 340, 200, (-7, 1.2), (-30, 30), [(fwd, ACCENT, ""), (rev, ACCENT, "")], "U (V)", "I (mA)",
            marks=[((-5.1, -20), "Vz = 5,1 V")], xticks=[(-5.1, "−5,1"), (0.7, "0,7")], yticks=[(-20, "−20"), (20, "20")])
    return d


# --- Module 3 : le transistor -----------------------------------------------------------------------------------------

def m3_npn():
    d = Drawing(320, 200, "Symbole du transistor NPN")
    b, c, e = d.bjt(170, 100)
    d.text(160, 190, "flèche sur l'émetteur, vers l'extérieur", size=12, color=SOFT)
    return d


def m3_pnp():
    d = Drawing(320, 200, "Symbole du transistor PNP")
    b, c, e = d.bjt(170, 100, kind="pnp")
    d.text(160, 190, "flèche sur l'émetteur, vers l'intérieur", size=12, color=SOFT)
    return d


def m3_courants():
    d = Drawing(380, 240, "Courants du transistor : IE = IB + IC")
    b, c, e = d.bjt(190, 120)
    d.wire((80, 120), b); d.wire(c, (c[0], 30)); d.wire(e, (e[0], 210))
    d.arrow((90, 108), (140, 108), "IB", offset=(0, -8))
    d.arrow((c[0] + 16, 34), (c[0] + 16, 70), "IC", offset=(22, 0))
    d.arrow((e[0] + 16, 170), (e[0] + 16, 206), "IE", offset=(22, 0))
    return d


def m3_gain():
    d = Drawing(440, 260, "Le courant de collecteur est proportionnel au courant de base")
    d.graph(60, 30, 320, 180, (0, 100), (0, 20), [([(0, 0), (100, 15)], ACCENT, "β = 150")], "IB (µA)", "IC (mA)",
            marks=[((50, 7.5), "50 µA ; 7,5 mA")], xticks=[(50, "50"), (100, "100")], yticks=[(7.5, "7,5"), (15, "15")])
    return d


def m3_polarisation():
    d = Drawing(460, 260, "Polarisation par résistance de base")
    b, c, e = d.bjt(260, 140)
    d.wire(c, (c[0], 90)); d.resistor((c[0], 90), (c[0], 40), "RC", "1 kΩ", side=1); d.wire((c[0], 40), (c[0], 20), (400, 20))
    d.battery((400, 230), (400, 20), "VCC", "12 V", side=1)
    d.resistor((110, 140), b, "RB", "100 kΩ")
    d.wire((110, 140), (60, 140), (60, 160))
    d.battery((60, 230), (60, 160), "VBB", "5 V")
    d.wire(e, (e[0], 230)); d.wire((60, 230), (400, 230)); d.dot((e[0], 230))
    return d


def m3_polarisation_mesures():
    d = Drawing(500, 260, "Mesurer IB et IC avec deux ampèremètres")
    b, c, e = d.bjt(310, 140)
    d.wire(c, (c[0], 92)); d.meter((c[0], 92), (c[0], 56), "A"); d.wire((c[0], 56), (c[0], 20), (440, 20))
    d.battery((440, 230), (440, 20), "VCC", "12 V", side=1)
    d.meter((170, 140), (220, 140), "A"); d.wire((220, 140), b)
    d.resistor((90, 140), (170, 140), "RB")
    d.wire((90, 140), (70, 140), (70, 160)); d.battery((70, 230), (70, 160), "VBB")
    d.wire(e, (e[0], 230)); d.wire((70, 230), (440, 230)); d.dot((e[0], 230))
    d.text(195, 120, "IB", color=ACCENT, weight="700"); d.text(c[0] + 26, 78, "IC", anchor="start", color=ACCENT, weight="700")
    return d


def m3_regimes():
    d = Drawing(480, 280, "Réseau de sorties IC = f(VCE) et les trois régimes")
    series = []
    for k, ib in enumerate((20, 40, 60)):
        ic = ib * 0.15
        series.append(([(0, 0), (0.3, ic * 0.92), (0.6, ic), (12, ic * 1.05)], ACCENT if k == 2 else INK, f"IB = {ib} µA"))
    d.graph(70, 30, 340, 190, (0, 12), (0, 10), series, "VCE (V)", "IC (mA)", xticks=[(6, "6"), (12, "12")], yticks=[(3, "3"), (6, "6"), (9, "9")])
    d.text(110, 252, "saturation", size=12, color=SOFT, weight="600")
    d.text(260, 252, "régime linéaire", size=12, color=SOFT, weight="600")
    d.text(400, 252, "blocage : IB = 0", size=12, color=SOFT, weight="600")
    return d


def m3_droite_charge():
    d = Drawing(460, 270, "Droite de charge et point de fonctionnement")
    d.graph(60, 30, 330, 190, (0, 14), (0, 12),
            [([(0, 12), (12, 0)], ACCENT, "droite de charge", (7.5, 5)), ([(0, 0), (0.6, 5.8), (12, 6.2)], INK, "IB = 40 µA", (9, 7))],
            "VCE (V)", "IC (mA)", marks=[((6, 6), "Q")], xticks=[(6, "6"), (12, "12")], yticks=[(6, "6"), (12, "12")])
    return d


def m3_modele_diodes():
    d = Drawing(420, 220, "Modèle de test : un NPN se comporte comme deux diodes tête-bêche")
    d.wire((60, 110), (160, 110)); d.dot((160, 110))
    d.diode((160, 110), (300, 50), "B-C"); d.diode((160, 110), (300, 170), "B-E", side=-1)
    d.wire((300, 50), (360, 50)); d.wire((300, 170), (360, 170))
    d.text(70, 98, "B", anchor="start", weight="700", color=ACCENT)
    d.text(370, 55, "C", anchor="start", weight="700", color=ACCENT)
    d.text(370, 175, "E", anchor="start", weight="700", color=ACCENT)
    return d


def m3_test_be():
    d = Drawing(440, 230, "Tester la jonction base-émetteur en mode diode")
    b, c, e = d.bjt(270, 110, circle=True)
    d.add('<rect x="30" y="40" width="110" height="150" rx="14" fill="#e9eff1" stroke="#173f58" stroke-width="2"/>')
    d.text(85, 80, "0,65 V", size=18, weight="700", color=ACCENT)
    d.text(85, 104, "mode diode", size=12, color=SOFT)
    d.wire((140, 150), (200, 150), b, color="#9d2b2b")
    d.wire((140, 170), (300, 200), (e[0], e[1]), color=INK)
    d.text(170, 142, "+", color="#9d2b2b", weight="700")
    d.text(200, 196, "COM", color=INK, size=12, weight="600")
    return d


def m3_jfet():
    d = Drawing(320, 200, "Symbole du JFET canal N")
    d.jfet(170, 100)
    d.text(160, 190, "la grille commande le courant drain-source", size=12, color=SOFT)
    return d


def m3_jfet_courbe():
    d = Drawing(460, 270, "Courant de drain selon la tension grille-source")
    pts = [(-v / 10, 10 * (1 - (v / 10) / 4) ** 2) for v in range(0, 41)]
    d.graph(70, 30, 330, 190, (-5, 1), (0, 12), [(pts, ACCENT, "ID(VGS)", (-2.6, 5))], "VGS (V)", "ID (mA)",
            marks=[((-4, 0.2), "VGS(off) = −4 V"), ((0, 10), "IDSS = 10 mA")], xticks=[(-4, "−4"), (-2, "−2")], yticks=[(10, "10")])
    return d


# --- Module 4 : le transistor en commutation --------------------------------------------------------------------------

def m4_interrupteur():
    d = Drawing(460, 260, "Le transistor commande une lampe")
    b, c, e = d.bjt(270, 150)
    d.wire(c, (c[0], 100)); d.lamp((c[0], 100), (c[0], 40), "L", side=1, lit=True); d.wire((c[0], 40), (c[0], 20), (410, 20))
    d.battery((410, 235), (410, 20), "VCC", "9 V", side=1)
    d.resistor((140, 150), b, "RB", "10 kΩ")
    d.switch((80, 150), (140, 150), "K", closed=True)
    d.wire((80, 150), (50, 150), (50, 20), (c[0], 20)); d.dot((c[0], 20))
    d.wire(e, (e[0], 235), (410, 235))
    return d


def m4_bloque_sature():
    d = Drawing(520, 240, "Transistor bloqué ou saturé")
    for x0, title, on in ((20, "Bloqué : VCE ≈ VCC, IC = 0", False), (270, "Saturé : VCE ≈ 0,2 V", True)):
        d.add(f'<rect x="{x0}" y="20" width="230" height="200" rx="12" fill="{"#e3f4f1" if on else "#e9eff1"}"/>')
        d.text(x0 + 115, 44, title, size=12, weight="700", color=ACCENT if on else INK)
        d.wire((x0 + 150, 64), (x0 + 150, 80)); d.lamp((x0 + 150, 80), (x0 + 150, 130), lit=on)
        d.switch((x0 + 150, 130), (x0 + 150, 190), closed=on)
        d.wire((x0 + 150, 190), (x0 + 150, 205))
        d.text(x0 + 70, 166, "IB > 0" if on else "IB = 0", size=13, weight="600", color=ACCENT if on else SOFT)
    return d


def m4_calcul_rb():
    d = Drawing(480, 270, "Dimensionner la résistance de base")
    b, c, e = d.bjt(280, 160)
    d.wire(c, (c[0], 105)); d.resistor((c[0], 105), (c[0], 45), "RC (charge)", "100 Ω", side=1); d.wire((c[0], 45), (c[0], 25), (420, 25))
    d.battery((420, 240), (420, 25), "VCC", "9 V", side=1)
    d.resistor((140, 160), b, "RB", "?")
    d.wire((140, 160), (80, 160))
    d.add('<circle cx="76" cy="160" r="4" fill="none" stroke="#173f58" stroke-width="2"/>')
    d.text(60, 150, "Ve = 5 V", anchor="end", color=ACCENT, weight="600")
    d.wire(e, (e[0], 240), (420, 240))
    d.text(240, 265, "IC sat ≈ 88 mA ; β min = 100 ; IB = 2 × IC / β", size=12, color=ACCENT, weight="600")
    d.h = 280
    return d


def m4_saturation_courbe():
    d = Drawing(460, 270, "Au-delà d'un certain courant de base, IC n'augmente plus")
    pts = [(ib, min(88, ib * 100 / 1000)) for ib in range(0, 2001, 50)]
    d.graph(60, 30, 330, 190, (0, 2000), (0, 110), [(pts, ACCENT, "")], "IB (µA)", "IC (mA)",
            marks=[((880, 88), "début de saturation"), ((1760, 88), "IB × 2")], xticks=[(880, "880"), (1760, "1760")], yticks=[(88, "88")])
    return d


def m4_relais():
    d = Drawing(480, 260, "Commande d'un relais avec diode de roue libre")
    b, c, e = d.bjt(260, 170)
    d.wire(c, (c[0], 115)); d.dot((c[0], 115))
    d.coil((c[0], 115), (c[0], 55), "K", "relais 12 V", side=1); d.wire((c[0], 55), (c[0], 30), (420, 30)); d.dot((c[0], 30))
    d.wire((c[0], 115), (c[0] - 60, 115)); d.diode((c[0] - 60, 115), (c[0] - 60, 30), "D", side=-1); d.wire((c[0] - 60, 30), (c[0], 30))
    d.battery((420, 245), (420, 30), "VCC", "12 V", side=1)
    d.resistor((120, 170), b, "RB")
    d.wire((120, 170), (80, 170))
    d.wire(e, (e[0], 245), (420, 245))
    return d


def m4_led_transistor():
    d = Drawing(460, 260, "Une sortie de 5 V commande une LED par un transistor")
    b, c, e = d.bjt(270, 170)
    d.wire(c, (c[0], 120)); d.diode((c[0], 75), (c[0], 120), "LED", kind="led", side=1)
    d.resistor((c[0], 75), (c[0], 30), "R", "330 Ω", side=-1); d.wire((c[0], 30), (c[0], 20), (410, 20))
    d.battery((410, 240), (410, 20), "VCC", "9 V", side=1)
    d.resistor((140, 170), b, "RB", "4,7 kΩ")
    d.wire((140, 170), (90, 170)); d.add('<circle cx="86" cy="170" r="4" fill="none" stroke="#173f58" stroke-width="2"/>')
    d.text(70, 160, "5 V", anchor="end", color=ACCENT, weight="600")
    d.wire(e, (e[0], 240), (410, 240))
    return d


def m4_ldr():
    d = Drawing(480, 280, "Lampe automatique : une LDR commande le transistor")
    b, c, e = d.bjt(300, 170)
    d.wire(c, (c[0], 120)); d.lamp((c[0], 120), (c[0], 60), "L", side=1); d.wire((c[0], 60), (c[0], 30), (430, 30))
    d.battery((430, 255), (430, 30), "VCC", "9 V", side=1)
    d.wire((120, 30), (c[0], 30)); d.dot((c[0], 30))
    d.resistor((120, 30), (120, 120), "R1", "10 kΩ", side=-1)
    d.dot((120, 170)); d.wire((120, 120), (120, 170), b)
    d.ldr((120, 170), (120, 255), "LDR", side=1)
    d.wire((120, 255), (430, 255)); d.wire(e, (e[0], 255)); d.dot((e[0], 255))
    return d


def m4_ldr_courbe():
    d = Drawing(460, 270, "La résistance d'une LDR baisse quand l'éclairement augmente")
    pts = [(lx, 100 / (1 + lx / 10)) for lx in range(0, 501, 10)]
    d.graph(70, 30, 330, 190, (0, 500), (0, 100), [(pts, ACCENT, "")], "éclairement (lux)", "R (kΩ)",
            marks=[((10, 50), "pénombre ; R élevée")], xticks=[(100, "100"), (500, "500")], yticks=[(50, "50"), (100, "100")])
    return d


def m4_darlington():
    d = Drawing(420, 260, "Montage Darlington : les gains se multiplient")
    b1, c1, e1 = d.bjt(150, 100, labels=False)
    b2, c2, e2 = d.bjt(270, 170, labels=False)
    d.wire(e1, (e1[0], 170), b2)
    d.wire(c1, (c1[0], 30), (c2[0], 30), c2); d.dot((c2[0], 30))
    d.wire((c2[0], 30), (c2[0], 20)); d.wire(e2, (e2[0], 240))
    d.wire((60, 100), b1)
    d.text(70, 90, "B", weight="700", color=ACCENT); d.text(c2[0] + 14, 20, "C", anchor="start", weight="700", color=ACCENT)
    d.text(e2[0] + 14, 240, "E", anchor="start", weight="700", color=ACCENT)
    d.text(130, 240, "β total ≈ β1 × β2", size=13, color=ACCENT, weight="600")
    return d


def m4_cascade():
    d = Drawing(520, 260, "Deux étages : le second transistor inverse le premier")
    b1, c1, e1 = d.bjt(170, 170, labels=False)
    b2, c2, e2 = d.bjt(350, 170, labels=False)
    d.wire(c1, (c1[0], 110)); d.resistor((c1[0], 110), (c1[0], 40), "RC1", side=-1)
    d.wire(c2, (c2[0], 110)); d.lamp((c2[0], 110), (c2[0], 50), "L", side=1)
    d.wire((c1[0], 40), (c1[0], 25), (470, 25)); d.wire((c2[0], 50), (c2[0], 25)); d.dot((c2[0], 25))
    d.battery((470, 240), (470, 25), "VCC", side=1)
    d.dot((c1[0], 120)); d.wire((c1[0], 120), (250, 120), (250, 170)); d.resistor((250, 170), b2, "RB2")
    d.resistor((60, 170), b1, "RB1")
    d.wire(e1, (e1[0], 240)); d.wire(e2, (e2[0], 240)); d.wire((e1[0], 240), (470, 240))
    return d


def m4_jfet_interrupteur():
    d = Drawing(460, 260, "Le JFET comme interrupteur commandé en tension")
    g, dr, s = d.jfet(260, 160)
    d.wire(dr, (dr[0], 108)); d.diode((dr[0], 63), (dr[0], 108), "LED", kind="led", side=1)
    d.resistor((dr[0], 63), (dr[0], 25), "RD", "470 Ω", side=-1); d.wire((dr[0], 25), (410, 25))
    d.battery((410, 240), (410, 25), "VDD", "9 V", side=1)
    d.wire(s, (s[0], 240), (410, 240))
    d.switch((120, 170), g, "K")
    d.wire((120, 170), (60, 170), (60, 190)); d.battery((60, 190), (60, 240), "−5 V", side=-1); d.wire((60, 240), (s[0], 240))
    return d


def m4_jfet_blocage():
    d = Drawing(540, 270, "Pour bloquer un JFET canal N, VGS doit descendre sous VGS(off)")
    pts = [(-v / 10, 8 * (1 - (v / 10) / 3) ** 2) for v in range(0, 31)] + [(-3 - v / 10, 0) for v in range(0, 30)]
    d.graph(70, 30, 330, 190, (-6, 1), (0, 10), [(pts, ACCENT, "")], "VGS (V)", "ID (mA)",
            marks=[((-3, 3), "VGS(off) = −3 V : bloqué"), ((0, 8), "VGS = 0 : conduit")], xticks=[(-3, "−3"), (-5, "−5")], yticks=[(8, "8")])
    return d


# --- Partie 2 : outils de tracé ---------------------------------------------------------------------------------------

def sine(amp, t_end, period, phase_deg=0.0, steps=160):
    """Points (t, amp × sin(2π t / période + phase)) de 0 à t_end."""
    return [(t_end * k / steps, amp * math.sin(2 * math.pi * (t_end * k / steps) / period + math.radians(phase_deg)))
            for k in range(steps + 1)]


def log_curve(fn, lo, hi, steps=160):
    """Courbe en fonction de log10(f), de 10^lo à 10^hi."""
    return [(lo + (hi - lo) * k / steps, fn(10 ** (lo + (hi - lo) * k / steps))) for k in range(steps + 1)]


DECADES = [(1, "10"), (2, "100"), (3, "1 k"), (4, "10 k"), (5, "100 k")]
FC = 1 / (2 * math.pi * 1e3 * 100e-9)          # RC 1 kΩ, 100 nF : ≈ 1 591,5 Hz
F0 = 1 / (2 * math.pi * math.sqrt(10e-3 * 100e-9))  # LC 10 mH, 100 nF : ≈ 5 033 Hz


def lowpass(f):
    return 1 / math.sqrt(1 + (f / FC) ** 2)


def highpass(f):
    return (f / FC) / math.sqrt(1 + (f / FC) ** 2)


def rlc_current(f, r, u=1.0):
    """Courant (mA) dans un RLC série 10 mH, 100 nF sous u volts."""
    x = 2 * math.pi * f * 10e-3 - 1 / (2 * math.pi * f * 100e-9)
    return 1000 * u / math.sqrt(r ** 2 + x ** 2)


def series_loop(d, source, top, right):
    """Boucle série : source verticale à gauche (x = 60), composants en haut puis à droite."""
    d.wire((60, 65), (60, 40), (top[0], 40))
    d.wire((right, 190), (60, 190), (60, 165))


# --- Module 5 : le courant alternatif ---------------------------------------------------------------------------------

def m5_sinusoide():
    d = Drawing(480, 270, "Tension sinusoïdale de 50 Hz : amplitude Umax = 10 V et période T = 20 ms")
    px, py = d.graph(60, 30, 360, 190, (0, 44), (-12, 12), [(sine(10, 44, 20), ACCENT, "u(t)", (31, 10.5))], "t (ms)", "u (V)",
                     marks=[((5, 10), "Umax = 10 V")], xticks=[(10, "10"), (20, "20"), (40, "40")], yticks=[(10, "10"), (-10, "−10")])
    d.arrow((px(0.5), py(-11.2)), (px(20), py(-11.2)), "T = 20 ms", offset=(0, -8))
    return d


def m5_frequences():
    d = Drawing(480, 270, "Deux sinusoïdes : 50 Hz (T = 20 ms) et 100 Hz (T = 10 ms)")
    d.graph(60, 30, 360, 190, (0, 40), (-12, 12),
            [(sine(10, 40, 20), SOFT, "50 Hz", (21, 11)), (sine(6, 40, 10), ACCENT, "100 Hz", (31.5, 7.5))],
            "t (ms)", "u (V)", xticks=[(10, "10"), (20, "20"), (30, "30"), (40, "40")])
    return d


def m5_valeurs():
    d = Drawing(480, 270, "Valeurs d'une sinusoïde : Umax = 10 V, Ucc = 20 V, Ueff ≈ 7,07 V")
    px, py = d.graph(60, 30, 360, 190, (0, 30), (-12, 12),
                     [(sine(10, 26, 20), ACCENT, "u(t)", (6.5, -7)), ([(0, 7.07), (26, 7.07)], SOFT, "Ueff ≈ 7,07 V", (10.5, 8.4))],
                     "t (ms)", "u (V)", marks=[((5, 10), "Umax = 10 V")], yticks=[(10, "10"), (-10, "−10")])
    d.arrow((px(27.5), py(-10)), (px(27.5), py(10)), "Ucc = 20 V", offset=(-46, 26))
    d.arrow((px(27.5), py(10)), (px(27.5), py(-10)), color=ACCENT)
    return d


def m5_efficace():
    d = Drawing(540, 240, "Même éclat de la lampe sous 12 V continus et sous 12 V efficaces")
    for dx, kind in ((0, "dc"), (270, "ac")):
        if kind == "dc":
            d.battery((50 + dx, 160), (50 + dx, 60), "E", "12 V")
        else:
            d.ac_source((50 + dx, 160), (50 + dx, 60), "~", "12 V eff")
        d.wire((50 + dx, 60), (50 + dx, 35), (190 + dx, 35), (190 + dx, 70))
        d.lamp((190 + dx, 70), (190 + dx, 135), "L", lit=True)
        d.wire((190 + dx, 135), (190 + dx, 185), (50 + dx, 185), (50 + dx, 160))
    d.text(120, 220, "continu", weight="600", color=SOFT)
    d.text(390, 220, "alternatif", weight="600", color=SOFT)
    return d


def m5_r_circuit():
    d = Drawing(440, 230, "Résistance en alternatif : I = U / R avec les valeurs efficaces")
    d.ac_source((60, 165), (60, 65), "~", "10 V eff", side=1)
    series_loop(d, None, (150, 40), 330)
    d.meter((150, 40), (210, 40), "A")
    d.wire((210, 40), (330, 40), (330, 75))
    d.resistor((330, 75), (330, 155), "R", "1 kΩ")
    d.wire((330, 155), (330, 190))
    d.arrow((235, 52), (300, 52), "I = 10 mA eff", offset=(0, 22))
    return d


def m5_r_phase():
    d = Drawing(480, 260, "Dans une résistance, u et i passent par zéro et par leurs maximums en même temps")
    d.graph(60, 30, 360, 180, (0, 40), (-12, 12), [(sine(10, 40, 20), SOFT, "u", (5.8, 11)), (sine(6, 40, 20), ACCENT, "i", (4, 4))],
            "t (ms)", "u, i", xticks=[(10, "10"), (20, "20"), (30, "30"), (40, "40")])
    d.text(240, 245, "en phase : déphasage 0°", color=ACCENT, weight="600")
    return d


def m5_c_circuit():
    d = Drawing(440, 230, "Condensateur alimenté en alternatif : un courant circule")
    d.ac_source((60, 165), (60, 65), "~", "10 V eff", side=1)
    series_loop(d, None, (150, 40), 330)
    d.meter((150, 40), (210, 40), "A")
    d.wire((210, 40), (330, 40), (330, 85))
    d.capacitor((330, 85), (330, 145), "C", "1 µF")
    d.wire((330, 145), (330, 190))
    d.arrow((235, 52), (300, 52), "I", offset=(0, 22))
    return d


def m5_xc_courbe():
    d = Drawing(480, 270, "Réactance d'un condensateur de 1 µF : Xc baisse quand la fréquence monte")
    pts = [(f, 1 / (2 * math.pi * f * 1e-6) / 1000) for f in range(25, 1001, 5)]
    d.graph(60, 30, 360, 190, (0, 1000), (0, 7), [(pts, ACCENT, "Xc = 1 / (2π × f × C)", (300, 2.2))], "f (Hz)", "Xc (kΩ)",
            marks=[((50, 3.18), "50 Hz : 3,18 kΩ")],
            xticks=[(500, "500"), (1000, "1000")], yticks=[(3.18, "3,18")])
    return d


def m5_c_phase():
    d = Drawing(480, 260, "Dans un condensateur, i est en avance d'un quart de période (90°) sur u")
    px, py = d.graph(60, 30, 360, 180, (0, 40), (-12, 12), [(sine(10, 40, 20), SOFT, "u", (6, 11)), (sine(6, 40, 20, 90), ACCENT, "i", (1, 7.5))],
                     "t (ms)", "u, i", xticks=[(10, "10"), (20, "20"), (30, "30"), (40, "40")])
    d.arrow((px(20), py(-11.5)), (px(25), py(-11.5)), "T/4", offset=(0, -6))
    return d


def m5_l_circuit():
    d = Drawing(440, 230, "Bobine alimentée en alternatif : sa réactance XL limite le courant")
    d.ac_source((60, 165), (60, 65), "~", "10 V eff", side=1)
    series_loop(d, None, (150, 40), 330)
    d.meter((150, 40), (210, 40), "A")
    d.wire((210, 40), (330, 40), (330, 75))
    d.inductor((330, 75), (330, 155), "L", "100 mH")
    d.wire((330, 155), (330, 190))
    d.arrow((235, 52), (300, 52), "I", offset=(0, 22))
    return d


def m5_xl_courbe():
    d = Drawing(480, 270, "Réactance d'une bobine de 100 mH : XL monte avec la fréquence")
    pts = [(f, 2 * math.pi * f * 0.1) for f in range(0, 1001, 10)]
    d.graph(60, 30, 360, 190, (0, 1000), (0, 700), [(pts, ACCENT, "XL = 2π × f × L", (120, 420))], "f (Hz)", "XL (Ω)",
            marks=[((50, 31.4), "50 Hz : 31,4 Ω"), ((500, 314), "500 Hz : 314 Ω")],
            xticks=[(500, "500"), (1000, "1000")], yticks=[(314, "314"), (628, "628")])
    return d


def m5_l_phase():
    d = Drawing(480, 260, "Dans une bobine, i est en retard d'un quart de période (90°) sur u")
    px, py = d.graph(60, 30, 360, 180, (0, 40), (-12, 12), [(sine(10, 40, 20), SOFT, "u", (6, 11)), (sine(6, 40, 20, -90), ACCENT, "i", (11, 7.5))],
                     "t (ms)", "u, i", xticks=[(10, "10"), (20, "20"), (30, "30"), (40, "40")])
    d.arrow((px(5), py(-11.5)), (px(10), py(-11.5)), "T/4", offset=(0, -6))
    return d


def m5_ecran():
    d = Drawing(500, 300, "Écran d'oscilloscope : 4 divisions crête à crête et 5 divisions par période")
    x0, y0, div = 40, 30, 30
    d.add(f'<rect x="{x0}" y="{y0}" width="{10 * div}" height="{8 * div}" fill="#eef4f3" stroke="{INK}" stroke-width="2"/>')
    for i in range(1, 10):
        d.add(f'<line x1="{x0 + i * div}" y1="{y0}" x2="{x0 + i * div}" y2="{y0 + 8 * div}" stroke="{SOFT}" stroke-width="0.6" stroke-dasharray="2 3"/>')
    for j in range(1, 8):
        d.add(f'<line x1="{x0}" y1="{y0 + j * div}" x2="{x0 + 10 * div}" y2="{y0 + j * div}" stroke="{SOFT}" stroke-width="0.6" stroke-dasharray="2 3"/>')
    pts = [(x0 + 10 * div * k / 200, y0 + 4 * div - 2 * div * math.sin(2 * math.pi * (10 * k / 200) / 5)) for k in range(201)]
    d.wire(*pts, color=ACCENT, width=2.5)
    d.text(355, 70, "Voie 1 : 2 V/div", anchor="start", weight="600")
    d.text(355, 95, "Base de temps : 1 ms/div", anchor="start", size=12)
    d.text(355, 150, "Ucc = 4 div × 2 V = 8 V", anchor="start", size=12, color=ACCENT, weight="600")
    d.text(355, 175, "T = 5 div × 1 ms = 5 ms", anchor="start", size=12, color=ACCENT, weight="600")
    d.text(355, 200, "f = 1 / T = 200 Hz", anchor="start", size=12, color=ACCENT, weight="600")
    d.w = 540
    return d


def m5_banc():
    d = Drawing(540, 220, "Banc de mesure : GBF, circuit étudié et oscilloscope à deux voies")
    for x, label in ((20, "GBF"), (210, "Circuit"), (400, "Oscilloscope")):
        d.add(f'<rect x="{x}" y="70" width="120" height="64" rx="8" fill="#fcfefe" stroke="{INK}" stroke-width="2"/>')
        d.text(x + 60, 107, label, weight="600")
    d.wire((140, 90), (210, 90)); d.dot((170, 90))
    d.wire((170, 90), (170, 40), (440, 40), (440, 70))
    d.text(452, 60, "voie 1", anchor="start", size=12, color=ACCENT, weight="600")
    d.wire((330, 90), (400, 90))
    d.text(365, 82, "voie 2", size=12, color=ACCENT, weight="600")
    d.wire((80, 134), (80, 170), (460, 170), (460, 134)); d.wire((270, 134), (270, 170)); d.dot((270, 170))
    d.text(270, 195, "masse commune", size=12, color=SOFT)
    return d


# --- Module 6 : les filtres RC et RL ----------------------------------------------------------------------------------

def right_triangle(d, a_len, b_len, scale, labels, angle_label="θ"):
    """Triangle rectangle : côté a horizontal, côté b vertical, angle θ en bas à gauche."""
    ax, ay = 60, 200
    bx, cy = ax + a_len * scale, ay - b_len * scale
    d.add(f'<polygon points="{fmt(ax)},{fmt(ay)} {fmt(bx)},{fmt(ay)} {fmt(bx)},{fmt(cy)}" fill="#eef4f3" stroke="{INK}" stroke-width="2"/>')
    d.add(f'<polyline points="{fmt(bx - 12)},{fmt(ay)} {fmt(bx - 12)},{fmt(ay - 12)} {fmt(bx)},{fmt(ay - 12)}" fill="none" stroke="{INK}"/>')
    d.text((ax + bx) / 2, ay + 22, labels[0], weight="600")
    d.text(bx + 10, (ay + cy) / 2, labels[1], anchor="start", weight="600")
    d.text((ax + bx) / 2 - 12, (ay + cy) / 2 - 8, labels[2], anchor="end", weight="600", color=ACCENT)
    d.text(ax + 42, ay - 8, angle_label, color=ACCENT, weight="700")
    return bx


def m6_triangle():
    d = Drawing(500, 240, "Triangle rectangle de côtés 3, 4 et 5 : Pythagore et tangente")
    bx = right_triangle(d, 4, 3, 45, ("a = 4", "b = 3", "c = 5"))
    for i, line in enumerate(("c = √(a² + b²) = √25 = 5", "tan θ = b / a = 0,75", "θ = arctan 0,75 ≈ 36,9°")):
        d.text(bx + 60, 90 + 28 * i, line, anchor="start", size=12, color=INK if i < 2 else ACCENT, weight="600")
    return d


def m6_arctan():
    d = Drawing(480, 260, "Angle θ = arctan(b / a) selon le rapport b / a")
    pts = [(k / 20, math.degrees(math.atan(k / 20))) for k in range(0, 101)]
    d.graph(60, 30, 360, 180, (0, 5), (0, 95), [(pts, ACCENT, "θ (°)", (3.6, 72)), ([(0, 90), (5, 90)], SOFT, "90°", (4.4, 93))],
            "b / a", "θ (°)", marks=[((1, 45), "b = a : 45°"), ((0.577, 30), "30°")], xticks=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")],
            yticks=[(45, "45"), (90, "90")])
    return d


def rc_or_rl(d, first, second, out_label):
    """Source Ve à gauche, premier composant en haut, second vers la masse, sortie Vs à droite."""
    d.ac_source((60, 165), (60, 65), "Ve", "")
    d.wire((60, 65), (60, 40), (110, 40))
    first((110, 40), (230, 40))
    d.wire((230, 40), (400, 40)); d.dot((300, 40))
    d.wire((300, 40), (300, 80))
    second((300, 80), (300, 150))
    d.wire((300, 150), (300, 190)); d.dot((300, 190))
    d.wire((400, 190), (60, 190), (60, 165))
    for y in (40, 190):
        d.add(f'<circle cx="400" cy="{y}" r="4" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>')
    d.arrow((420, 180), (420, 50), out_label, offset=(18, 0))


def m6_rc_serie():
    d = Drawing(460, 230, "Circuit RC série sous 10 V : R = Xc = 1 kΩ")
    d.ac_source((60, 165), (60, 65), "~", "10 V", side=1)
    d.wire((60, 65), (60, 40), (110, 40))
    d.resistor((110, 40), (230, 40), "R", "1 kΩ")
    d.wire((230, 40), (330, 40), (330, 85))
    d.capacitor((330, 85), (330, 145), "C", "Xc = 1 kΩ")
    d.wire((330, 145), (330, 190), (60, 190), (60, 165))
    d.text(170, 90, "Ur ≈ 7,07 V", color=ACCENT, weight="600")
    d.text(250, 120, "Uc ≈ 7,07 V", color=ACCENT, weight="600", anchor="end")
    d.text(230, 215, "I = 10 V / 1,41 kΩ ≈ 7,07 mA", size=12, color=SOFT)
    return d


def m6_triangle_z():
    d = Drawing(500, 240, "Triangle des impédances : R et Xc à angle droit, Z sur l'hypoténuse")
    bx = right_triangle(d, 1, 1, 150, ("R = 1 kΩ", "Xc = 1 kΩ", "Z ≈ 1,41 kΩ"), "φ")
    d.text(bx + 100, 100, "Z = √(R² + Xc²)", anchor="start", size=12, weight="600")
    d.text(bx + 100, 128, "φ = arctan(Xc / R) = 45°", anchor="start", size=12, weight="600", color=ACCENT)
    d.w = 560
    return d


def m6_passe_bas():
    d = Drawing(480, 230, "Filtre passe-bas RC : la sortie est prise aux bornes du condensateur")
    rc_or_rl(d, lambda a, b: d.resistor(a, b, "R", "1 kΩ"), lambda a, b: d.capacitor(a, b, "C", "100 nF", side=-1), "Vs")
    return d


def m6_passe_bas_courbe():
    d = Drawing(480, 260, "Passe-bas RC 1 kΩ, 100 nF : les basses fréquences passent, les hautes sont atténuées")
    d.graph(60, 30, 360, 180, (1, 5), (0, 1.1), [(log_curve(lowpass, 1, 5), ACCENT, "Vs / Ve", (3.6, 0.45))], "f (Hz)", "Vs / Ve",
            marks=[((math.log10(FC), 0.707), "fc ≈ 1,6 kHz")], xticks=DECADES, yticks=[(1, "1"), (0.707, "0,707")])
    return d


def m6_passe_haut():
    d = Drawing(480, 230, "Filtre passe-haut RC : la sortie est prise aux bornes de la résistance")
    rc_or_rl(d, lambda a, b: d.capacitor(a, b, "C", "100 nF"), lambda a, b: d.resistor(a, b, "R", "1 kΩ", side=-1), "Vs")
    return d


def m6_passe_haut_courbe():
    d = Drawing(480, 260, "Passe-haut RC 1 kΩ, 100 nF : les basses fréquences sont atténuées, les hautes passent")
    d.graph(60, 30, 360, 180, (1, 5), (0, 1.1), [(log_curve(highpass, 1, 5), ACCENT, "Vs / Ve", (1.2, 0.3))], "f (Hz)", "Vs / Ve",
            marks=[((math.log10(FC), 0.707), "fc ≈ 1,6 kHz")], xticks=DECADES, yticks=[(1, "1"), (0.707, "0,707")])
    return d


def m6_coupure():
    d = Drawing(480, 260, "À la fréquence de coupure, la réactance Xc est égale à R")
    xc = log_curve(lambda f: min(5.0, 1 / (2 * math.pi * f * 100e-9) / 1000), 2.5, 4.5)
    d.graph(60, 30, 360, 180, (2.5, 4.5), (0, 5), [(xc, ACCENT, "Xc", (2.85, 4)), ([(2.5, 1), (4.5, 1)], SOFT, "R = 1 kΩ", (4.0, 1.25))],
            "f (Hz)", "(kΩ)", marks=[((math.log10(FC), 1), "fc : Xc = R")], xticks=[(3, "1 k"), (4, "10 k")], yticks=[(1, "1")])
    return d


def m6_attenuation():
    d = Drawing(500, 260, "Passe-bas : environ 99 % à fc / 10, 70,7 % à fc, 10 % à 10 × fc")
    lf = math.log10(FC)
    d.graph(60, 30, 380, 180, (1.5, 5), (0, 1.1), [(log_curve(lowpass, 1.5, 5), ACCENT, "")], "f (Hz)", "Vs / Ve",
            marks=[((lf - 1, 0.995), "99 %"), ((lf, 0.707), "70,7 %"), ((lf + 1, 0.0995), "10 %")],
            xticks=[(2, "100"), (3, "1 k"), (4, "10 k"), (5, "100 k")], yticks=[(1, "1"), (0.707, "0,707")])
    return d


def m6_dephasage():
    d = Drawing(480, 260, "Mesure du déphasage : φ = 360° × Δt / T = 360° × 0,125 / 1 = 45°")
    px, py = d.graph(60, 30, 360, 180, (0, 2), (-12, 12),
                     [(sine(10, 2, 1), SOFT, "ve", (0.05, 10.5)), (sine(7.07, 2, 1, -45), ACCENT, "vs", (0.55, 8))],
                     "t (ms)", "v (V)", xticks=[(0.5, "0,5"), (1, "1"), (1.5, "1,5"), (2, "2")])
    d.add(f'<line x1="{fmt(px(1.25))}" y1="{fmt(py(10))}" x2="{fmt(px(1.25))}" y2="{fmt(py(-11))}" stroke="{SOFT}" stroke-dasharray="4 3"/>')
    d.add(f'<line x1="{fmt(px(1.375))}" y1="{fmt(py(7.07))}" x2="{fmt(px(1.375))}" y2="{fmt(py(-11))}" stroke="{ACCENT}" stroke-dasharray="4 3"/>')
    d.text(px(1.31), py(-11.6) + 14, "Δt", color=ACCENT, weight="700")
    return d


def m6_triangle_phi():
    d = Drawing(520, 240, "Déphasage d'un RC série : R = 1 kΩ et Xc = 577 Ω donnent φ = 30°")
    bx = right_triangle(d, 1, 0.577, 200, ("R = 1 kΩ", "Xc = 577 Ω", "Z ≈ 1,15 kΩ"), "φ")
    d.text(bx + 110, 120, "tan φ = Xc / R = 0,577", anchor="start", size=12, weight="600")
    d.text(bx + 110, 148, "φ = arctan 0,577 ≈ 30°", anchor="start", size=12, weight="600", color=ACCENT)
    d.w = 600
    return d


def m6_rl_passe_bas():
    d = Drawing(480, 230, "Filtre passe-bas RL : bobine en série, sortie aux bornes de la résistance")
    rc_or_rl(d, lambda a, b: d.inductor(a, b, "L", "10 mH"), lambda a, b: d.resistor(a, b, "R", "100 Ω", side=-1), "Vs")
    return d


def m6_rl_courbe():
    d = Drawing(480, 260, "Passe-bas RL 100 Ω, 10 mH : fc = R / (2π × L) ≈ 1,6 kHz")
    d.graph(60, 30, 360, 180, (1, 5), (0, 1.1), [(log_curve(lowpass, 1, 5), ACCENT, "Vs / Ve", (3.6, 0.45))], "f (Hz)", "Vs / Ve",
            marks=[((math.log10(FC), 0.707), "fc ≈ 1,6 kHz")], xticks=DECADES, yticks=[(1, "1"), (0.707, "0,707")])
    return d


# --- Module 7 : la résonance ------------------------------------------------------------------------------------------

def m7_rlc_serie():
    d = Drawing(500, 230, "Circuit RLC série : 50 Ω, 10 mH et 100 nF")
    d.ac_source((60, 165), (60, 65), "~", "1 V", side=1)
    d.wire((60, 65), (60, 40), (100, 40))
    d.resistor((100, 40), (190, 40), "R", "50 Ω")
    d.inductor((190, 40), (300, 40), "L", "10 mH")
    d.wire((300, 40), (400, 40), (400, 85))
    d.capacitor((400, 85), (400, 145), "C", "100 nF")
    d.wire((400, 145), (400, 190), (60, 190), (60, 165))
    return d


def m7_xl_xc():
    d = Drawing(480, 260, "XL monte et XC descend avec la fréquence : elles sont égales à f0")
    xl = log_curve(lambda f: 2 * math.pi * f * 10e-3, 3, 4)
    xc = log_curve(lambda f: min(1600, 1 / (2 * math.pi * f * 100e-9)), 3, 4)
    px, py = d.graph(60, 30, 360, 180, (3, 4), (0, 1700), [(xl, ACCENT, "XL", (3.85, 560)), (xc, SOFT, "XC", (3.06, 1350))], "f (Hz)", "(Ω)",
                     marks=[((math.log10(F0), 316), "f0")], xticks=[(3, "1 k"), (math.log10(5000), "5 k"), (4, "10 k")])
    d.text(px(3.45), py(1100), "f0 ≈ 5 kHz : XL = XC ≈ 316 Ω", anchor="start", size=12, color=ACCENT, weight="600")
    return d


def m7_courbe_i():
    d = Drawing(480, 260, "Courant dans le RLC série sous 1 V : maximum Imax = U / R = 20 mA à f0")
    d.graph(60, 30, 360, 180, (3, 4.4), (0, 22), [(log_curve(lambda f: rlc_current(f, 50), 3, 4.4, 240), ACCENT, "")],
            "f (Hz)", "I (mA)", marks=[((math.log10(F0), 20), "f0 ≈ 5 kHz")], xticks=[(3, "1 k"), (4, "10 k")], yticks=[(20, "20")])
    return d


def m7_courbe_r():
    d = Drawing(480, 260, "Plus la résistance est grande, plus le pic de résonance est bas et large")
    d.graph(60, 30, 360, 180, (3, 4.4), (0, 22),
            [(log_curve(lambda f: rlc_current(f, 50), 3, 4.4, 240), ACCENT, "R = 50 Ω", (3.78, 18)),
             (log_curve(lambda f: rlc_current(f, 200), 3, 4.4, 240), SOFT, "R = 200 Ω", (3.95, 6))],
            "f (Hz)", "I (mA)", xticks=[(3, "1 k"), (4, "10 k")], yticks=[(5, "5"), (20, "20")])
    return d


def m7_bande():
    d = Drawing(500, 260, "Bande passante : de f1 à f2, le courant reste au-dessus de 0,707 × Imax")
    q = 2 * math.pi * F0 * 10e-3 / 50
    f1 = F0 * (math.sqrt(1 + 1 / (4 * q * q)) - 1 / (2 * q))
    f2 = F0 * (math.sqrt(1 + 1 / (4 * q * q)) + 1 / (2 * q))
    pts = [(f, rlc_current(f, 50) / 20) for f in range(3000, 7001, 20)]
    px, py = d.graph(60, 30, 380, 180, (3000, 7000), (0, 1.1), [(pts, ACCENT, ""), ([(3000, 0.707), (7000, 0.707)], SOFT, "")],
                     "f (Hz)", "I / Imax", marks=[((f1, 0.707), "f1"), ((f2, 0.707), "f2")],
                     xticks=[(4000, "4 k"), (5000, "5 k"), (6000, "6 k")], yticks=[(1, "1"), (0.707, "0,707")])
    d.arrow((px(f1), py(0.3)), (px(f2), py(0.3)), color=ACCENT)
    d.arrow((px(f2), py(0.3)), (px(f1), py(0.3)), color=ACCENT)
    d.text((px(f1) + px(f2)) / 2, py(0.3) + 20, "BP ≈ 796 Hz", color=ACCENT, weight="600")
    return d


def m7_q():
    d = Drawing(480, 260, "Facteur de qualité Q = f0 / BP : plus Q est élevé, plus le circuit est sélectif")
    d.graph(60, 30, 360, 180, (3, 4.4), (0, 1.1),
            [(log_curve(lambda f: rlc_current(f, 50) / 20, 3, 4.4, 240), ACCENT, "Q ≈ 6,3", (3.76, 0.95)),
             (log_curve(lambda f: rlc_current(f, 200) / 5, 3, 4.4, 240), SOFT, "Q ≈ 1,6", (4.02, 0.62))],
            "f (Hz)", "I / Imax", xticks=[(3, "1 k"), (4, "10 k")], yticks=[(1, "1"), (0.707, "0,707")])
    return d


def m7_lc_parallele():
    d = Drawing(480, 240, "Circuit LC parallèle (bouchon) alimenté à travers une résistance")
    d.ac_source((60, 170), (60, 70), "~", "")
    d.wire((60, 70), (60, 40), (100, 40))
    d.resistor((100, 40), (200, 40), "R", "10 kΩ")
    d.wire((200, 40), (380, 40)); d.dot((280, 40))
    d.wire((280, 40), (280, 80)); d.inductor((280, 80), (280, 160), "L", "10 mH", side=-1); d.wire((280, 160), (280, 200))
    d.wire((380, 40), (380, 95)); d.capacitor((380, 95), (380, 150), "C", "100 nF"); d.wire((380, 150), (380, 200))
    d.wire((380, 200), (60, 200), (60, 170)); d.dot((280, 200))
    return d


def m7_z_parallele():
    d = Drawing(480, 260, "Impédance du bouchon (10 mH avec 10 Ω de pertes, 100 nF) : maximale à f0")

    def z(f):
        w = 2 * math.pi * f
        zl, zc = complex(10, w * 10e-3), complex(0, -1 / (w * 100e-9))
        return abs(zl * zc / (zl + zc)) / 1000

    d.graph(60, 30, 360, 180, (3, 4.4), (0, 11), [(log_curve(z, 3, 4.4, 300), ACCENT, "")], "f (Hz)", "Z (kΩ)",
            marks=[((math.log10(F0), 10), "f0 ≈ 5 kHz")], xticks=[(3, "1 k"), (4, "10 k")], yticks=[(10, "10")])
    return d


def m7_accord():
    d = Drawing(500, 240, "Circuit d'accord d'un récepteur : le condensateur variable choisit la station")
    d.antenna((80, 100))
    d.wire((80, 100), (80, 130), (200, 130)); d.dot((200, 130))
    d.wire((200, 130), (200, 145)); d.inductor((200, 145), (200, 205), "L", "100 µH", side=-1)
    d.wire((200, 130), (300, 130), (300, 150)); d.variable_capacitor((300, 150), (300, 200), "C", "≈ 253 pF")
    d.wire((200, 205), (200, 220), (300, 220), (300, 200)); d.ground((250, 220))
    d.wire((300, 130), (390, 130))
    d.add(f'<polygon points="390,105 390,155 440,130" fill="#fcfefe" stroke="{INK}" stroke-width="2"/>')
    d.text(415, 95, "amplificateur", size=12, color=SOFT)
    d.h = 260
    return d


def m7_stations():
    d = Drawing(480, 260, "Accordé sur 1 MHz, le circuit laisse passer cette station et atténue ses voisines")
    q = 40

    def g(f):
        return 1 / math.sqrt(1 + (q * (f / 1.0 - 1.0 / f)) ** 2)

    px, py = d.graph(60, 30, 360, 180, (0.85, 1.15), (0, 1.1), [([(0.85 + k * 0.3 / 200, g(0.85 + k * 0.3 / 200)) for k in range(201)], ACCENT, "")],
                     "f (MHz)", "", xticks=[(0.9, "0,9"), (1.0, "1"), (1.1, "1,1")])
    for f in (0.9, 1.0, 1.1):
        d.add(f'<rect x="{fmt(px(f) - 5)}" y="{fmt(py(0.9))}" width="10" height="{fmt(py(0) - py(0.9))}" fill="{SOFT}" opacity="0.35"/>')
    d.text(px(1.0) + 40, py(0.5), "station reçue", anchor="start", size=12, color=ACCENT, weight="600")
    return d


def m7_echange():
    d = Drawing(520, 230, "Dans un circuit LC, l'énergie passe du condensateur à la bobine et revient")
    for dx, cap, coil in ((0, "C chargé : énergie électrique", "I = 0"), (260, "C déchargé", "I maximal : énergie magnétique")):
        d.wire((70 + dx, 50), (170 + dx, 50))
        d.wire((70 + dx, 50), (70 + dx, 85)); d.capacitor((70 + dx, 85), (70 + dx, 135), "C", side=-1); d.wire((70 + dx, 135), (70 + dx, 170))
        d.wire((170 + dx, 50), (170 + dx, 80)); d.inductor((170 + dx, 80), (170 + dx, 140), "L"); d.wire((170 + dx, 140), (170 + dx, 170))
        d.wire((70 + dx, 170), (170 + dx, 170))
        d.text(120 + dx, 195, cap, size=11, color=ACCENT, weight="600")
        d.text(120 + dx, 213, coil, size=11, color=SOFT)
    d.arrow((225, 110), (285, 110), color=ACCENT)
    return d


def m7_amortie():
    d = Drawing(480, 260, "Oscillation amortie : sans apport d'énergie, les pertes éteignent l'oscillation")
    pts = [(t / 40, 10 * math.exp(-t / 40 / 2.5) * math.cos(2 * math.pi * t / 40)) for t in range(0, 401)]
    env = [(t / 40, 10 * math.exp(-t / 40 / 2.5)) for t in range(0, 401, 4)]
    d.graph(60, 30, 360, 180, (0, 10), (-11, 11), [(pts, ACCENT, ""), (env, SOFT, "enveloppe", (5.2, 7))], "t", "u (V)")
    return d


# --- Schémas des questions sur zone cliquable -------------------------------------------------------------------------

def q_m1_circuit():
    d = Drawing(420, 220, "Circuit à identifier")
    d.battery((60, 170), (60, 70), "", "")
    d.wire((60, 70), (60, 40), (120, 40))
    d.switch((120, 40), (180, 40))
    d.resistor((180, 40), (300, 40))
    d.wire((300, 40), (350, 40), (350, 80)); d.lamp((350, 80), (350, 150)); d.wire((350, 150), (350, 190), (60, 190), (60, 170))
    d.zone("generateur", 30, 80, 60, 80); d.zone("interrupteur", 115, 15, 70, 40)
    d.zone("resistance", 215, 25, 50, 30); d.zone("lampe", 325, 95, 50, 50)
    return d


def q_m2_circuit():
    d = Drawing(420, 220, "Circuit à diode et LED")
    d.battery((60, 170), (60, 70))
    d.wire((60, 70), (60, 40), (100, 40))
    d.diode((100, 40), (180, 40))
    d.resistor((180, 40), (290, 40))
    d.wire((290, 40), (350, 40), (350, 80)); d.diode((350, 80), (350, 150), kind="led"); d.wire((350, 150), (350, 190), (60, 190), (60, 170))
    d.zone("diode", 115, 20, 55, 40); d.zone("resistance", 205, 25, 60, 30); d.zone("led", 320, 90, 60, 55)
    return d


def q_m3_npn():
    d = Drawing(260, 180, "Transistor NPN sans légendes")
    d.bjt(140, 90, labels=False)
    d.zone("base", 80, 72, 60, 36); d.zone("collecteur", 132, 20, 50, 40); d.zone("emetteur", 132, 116, 50, 40)
    return d


def q_m4_switch():
    d = Drawing(440, 240, "Montage de commutation")
    b, c, e = d.bjt(270, 150, labels=False)
    d.wire(c, (c[0], 100)); d.lamp((c[0], 100), (c[0], 40)); d.wire((c[0], 40), (c[0], 20), (400, 20))
    d.battery((400, 225), (400, 20))
    d.resistor((130, 150), b)
    d.wire((130, 150), (80, 150))
    d.wire(e, (e[0], 225), (400, 225))
    d.zone("rb", 160, 135, 60, 30); d.zone("transistor", 240, 120, 60, 60); d.zone("lampe", 260, 50, 50, 45)
    return d


def q_m5_sinus():
    d = Drawing(440, 240, "Sinusoïde à repérer")
    px, py = d.graph(50, 30, 340, 170, (0, 25), (-12, 12), [(sine(10, 25, 20), ACCENT, "")], "t", "u")
    d.zone("crete", px(5) - 25, py(10) - 22, 50, 36)
    d.zone("zero", px(10) - 25, py(0) - 18, 50, 36)
    d.zone("creux", px(15) - 25, py(-10) - 14, 50, 36)
    return d


def q_m6_passe_haut():
    d = Drawing(460, 230, "Filtre RC à identifier")
    rc_or_rl(d, lambda a, b: d.capacitor(a, b), lambda a, b: d.resistor(a, b), "")
    d.zone("source", 30, 85, 60, 60); d.zone("condensateur", 145, 18, 50, 44); d.zone("resistance", 280, 92, 40, 46)
    return d


def q_m7_courbe():
    d = Drawing(460, 250, "Courbe de réponse à lire")
    px, py = d.graph(50, 30, 360, 180, (3, 4.4), (0, 22), [(log_curve(lambda f: rlc_current(f, 50), 3, 4.4, 240), ACCENT, "")], "f", "I")
    lf = math.log10(F0)
    d.zone("pic", px(lf) - 25, py(20) - 18, 50, 40)
    d.zone("basses", px(3.15) - 25, py(rlc_current(10 ** 3.15, 50)) - 25, 50, 40)
    d.zone("hautes", px(4.25) - 25, py(rlc_current(10 ** 4.25, 50)) - 25, 50, 40)
    return d


SECTION_DIAGRAMS = {
    1: [m1_circuit_simple, m1_mesures, m1_ohm_circuit, m1_ohm_graph, m1_serie, m1_parallele, m1_puissance,
        m1_puissance_graph, m1_diviseur, m1_diviseur_charge, m1_diviseur_courant, m1_trois_branches, m1_rc_circuit, m1_rc_courbe],
    2: [m2_jonction, m2_symbole, m2_directe, m2_inverse, m2_caracteristique, m2_mesure, m2_led_circuit, m2_led_symbole,
        m2_simple_alternance, m2_redresse_courbe, m2_zener_regulateur, m2_zener_courbe],
    3: [m3_npn, m3_pnp, m3_courants, m3_gain, m3_polarisation, m3_polarisation_mesures, m3_regimes, m3_droite_charge,
        m3_modele_diodes, m3_test_be, m3_jfet, m3_jfet_courbe],
    4: [m4_interrupteur, m4_bloque_sature, m4_calcul_rb, m4_saturation_courbe, m4_relais, m4_led_transistor, m4_ldr,
        m4_ldr_courbe, m4_darlington, m4_cascade, m4_jfet_interrupteur, m4_jfet_blocage],
    5: [m5_sinusoide, m5_frequences, m5_valeurs, m5_efficace, m5_r_circuit, m5_r_phase, m5_c_circuit, m5_xc_courbe, m5_c_phase,
        m5_l_circuit, m5_xl_courbe, m5_l_phase, m5_ecran, m5_banc],
    6: [m6_triangle, m6_arctan, m6_rc_serie, m6_triangle_z, m6_passe_bas, m6_passe_bas_courbe, m6_passe_haut, m6_passe_haut_courbe,
        m6_coupure, m6_attenuation, m6_dephasage, m6_triangle_phi, m6_rl_passe_bas, m6_rl_courbe],
    7: [m7_rlc_serie, m7_xl_xc, m7_courbe_i, m7_courbe_r, m7_bande, m7_q, m7_lc_parallele, m7_z_parallele, m7_accord, m7_stations,
        m7_echange, m7_amortie],
}
QUESTION_DIAGRAMS = {1: q_m1_circuit, 2: q_m2_circuit, 3: q_m3_npn, 4: q_m4_switch, 5: q_m5_sinus, 6: q_m6_passe_haut, 7: q_m7_courbe}


def file_name(func):
    return func.__name__.split("_", 1)[1].replace("_", "-") + ".svg"


def main():
    global LANG
    for LANG, folder in (("fr", ""), ("en", "en")):
        for module, funcs in SECTION_DIAGRAMS.items():
            out = ROOT / "static" / "content" / "electro" / folder / f"m{module}"
            out.mkdir(parents=True, exist_ok=True)
            for func in funcs:
                (out / file_name(func)).write_text(func().svg(), encoding="utf-8")
    LANG = "fr"
    for module, func in QUESTION_DIAGRAMS.items():
        out = ROOT / "content" / "electro" / ("p1" if module <= 4 else "p2") / f"m{module}" / "schemas"
        out.mkdir(parents=True, exist_ok=True)
        drawing = func()
        (out / file_name(func)).write_text(drawing.svg(), encoding="utf-8")
        print(f"m{module}/schemas/{file_name(func)} zones : {drawing.zones}")


if __name__ == "__main__":
    main()
