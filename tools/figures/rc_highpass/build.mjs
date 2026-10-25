// Figure « passe-haut RC » : banc hydraulique isométrique dessiné avec le kit anatomy, pendant du passe-bas.
// node tools/figures/rc_highpass/build.mjs [--out <dossier>]
// écrit templates/figures/rc_highpass.svg (dessin sans texte) et static/acad/js/figures/rc_highpass.js (animation).
// Fichiers générés : ne jamais les retoucher à la main, modifier ce script puis le relancer.
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "../kit/iso-kit.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(HERE, "../../..");
const outAt = process.argv.indexOf("--out");
const OUT = outAt > 0 ? resolve(process.argv[outAt + 1]) : null;

const WIDTH = 640;
const HEIGHT = 360;

// Plan du banc (unités monde, z vers le haut). La ligne court le long de x, à y = 0 :
// piston (Ve) → cloche à membrane en série (C) → nœud et manomètre (Vs) → vanne étranglée (R) → bac (masse).
const PLATE = { x: -164, y: -52, w: 316, d: 104, r: 8 };
const PLATE_H = 10;
const FOOT_H = 5;
const PIPE_Z = 8;
const PIPE_H = 6;
const DRIVE = { x: -154, y: -14, w: 30, d: 28, r: 3 };
const DRIVE_H = 22;
const KNOB = [-139, 0];
const KNOB_R = 8;
const PUMP = [-100, 0];
const PUMP_R = 14;
const PUMP_H = 50;
const ROD_R = 3;
const ROD_LEN = 26;
const STROKE = 9; // course du piston pour Ve = ±1
// Cloche : deux demi-corps serrant la membrane ; entrée sous la membrane, sortie au-dessus.
const BELL = [-50, 0];
const BELL_R = 15;
const BELL_SEAM = 18; // plan de la membrane
const BELL_TOP = 34;
const OUTLET_Z = 24;
const GLAND_TOP = BELL_TOP + 4 + 3;
const STEM_LEN = 22;
const STEM_LIFT = 8; // course de la tige de membrane pour Vc = ±1
const NODE = { x: 3, y: -9, w: 18, d: 18, r: 2 };
const NODE_H = 32;
const GAUGE = [12, 0];
const GAUGE_Z = 44;
const DIAL_R = 17;
const DIAL_H = 6;
const DIAL_TOP = GAUGE_Z + DIAL_H;
const VALVE = { x: 38, y: -9, w: 22, d: 18, r: 2 };
const VALVE_H = 22;
const WHEEL = [49, 0];
const TRAY = { x: 80, y: -30, w: 64, d: 60, r: 4 };
const TRAY_H = 7;
const WALL = 2.2;
const SPOUT = [102, 0];
const NEEDLE_SPAN = (120 * Math.PI) / 180; // Vs = ±1 → ±120°
const KNOB_SPAN = (270 * Math.PI) / 180; // 10 Hz à 100 kHz sur 270°

const P = k.fitProjection(
  [
    ...k.boxCorners(PLATE, -PLATE_H - FOOT_H, 0),
    [PUMP[0], PUMP[1], PUMP_H + ROD_LEN + STROKE + 6],
    [BELL[0], 0, GLAND_TOP + STEM_LEN - STEM_LIFT + STEM_LIFT * 2 + 4],
    [GAUGE[0] + DIAL_R, 0, DIAL_TOP],
  ],
  WIDTH,
  HEIGHT,
  { pad: 18, azimuth: 40 },
);

const at = (point) => k.iso(point, P);
const S = (paths, style) => k.solidSvg(paths, style);
const L = (d, style) => k.lineSvg(d, style);
const D = (points, style) => k.dotsSvg(points, style);
const depth = (x, y, z = 0) => k.depthOf([x, y, z], P);

function plate() {
  const out = [`<path class="iso-halo" d="${k.haloOf(PLATE, -PLATE_H - FOOT_H, PLATE_H, P)}"/>`];
  const feet = [...k.corners(PLATE, 22)].sort((a, b) => depth(...a) - depth(...b));
  for (const [x, y] of feet) {
    out.push(S(k.cylinder(x, y, 7, -PLATE_H - FOOT_H, 1.6, P, 8), { tone: "lo" }));
    out.push(S(k.cylinder(x, y, 5.4, -PLATE_H - FOOT_H + 1.6, FOOT_H - 1.6, P, 8), { tone: "mid" }));
  }
  out.push(S(k.slabOf(PLATE, -PLATE_H, PLATE_H, P, 5, 1.6), { tone: "mid" }));
  out.push(L(k.planOutline(k.insetPlan(PLATE, 5), 0, P), { tone: "lo" }));
  const screws = k.corners(PLATE, 10);
  out.push(L(screws.map(([x, y]) => k.ring(x, y, 2.2, 0, P, 16)).join(""), { tone: "lo" }));
  out.push(D(screws.map(([x, y]) => at([x, y, 0])), { size: 0.5 }));
  // Réglette des fréquences le long du bord avant : quatre décades, de 10 Hz à 100 kHz.
  const strip = { x: -140, y: PLATE.y + PLATE.d - 14, w: 200, d: 7, r: 1 };
  out.push(S(k.slabOf(strip, 0, 0.6, P, 3), { tone: "lo", crease: "none" }));
  const ticks = k.topTicks(strip.x + 4, strip.x + strip.w - 4, 4, 12, strip.y + 0.8, 0.6, [2, 3.8], P);
  out.push(L(ticks.minor, { tone: "lo" }), L(ticks.major, { tone: "mid" }));
  out.push(D([at([strip.x + 2, strip.y + 3.5, 0.6]), at([strip.x + strip.w - 2, strip.y + 3.5, 0.6])], { size: 0.45 }));
  // Plaque signalétique gravée de trois lignes.
  const label = { x: 92, y: PLATE.y + PLATE.d - 16, w: 40, d: 10, r: 1 };
  out.push(S(k.slabOf(label, 0, 0.5, P, 3), { tone: "lo", crease: "none" }));
  out.push(L([2.6, 5, 7.4].map((dy, i) => k.lineOnTop([label.x + 4, label.y + dy], [label.x + label.w - 4 - i * 8, label.y + dy], 0.5, P)).join(""), { tone: "faint", free: "both" }));
  return out.join("");
}

const pipe = (plan, z = PIPE_Z, h = PIPE_H) => S(k.slabOf({ d: PIPE_H, r: 1.2, ...plan }, z, h, P, 2), { tone: "mid" });
const collar = (x, z = PIPE_Z) => S(k.slabOf({ x: x - 1.5, y: -4.5, w: 3, d: 9, r: 0.8 }, z - 1.5, PIPE_H + 3, P, 2), { tone: "mid" });

function returnLine() {
  // Retour au bac (la masse) : conduite basse à l'arrière, du bac à l'aspiration de la pompe.
  const out = [];
  out.push(pipe({ x: PUMP[0] - 3, y: -24, w: 6, d: 12 }, 1, 5));
  out.push(pipe({ x: PUMP[0] - 3, y: -24, w: TRAY.x - PUMP[0] + 3, d: 6 }, 1, 5));
  out.push(D([at([-20, -21, 6]), at([60, -21, 6])], { size: 0.4, tone: "lo" }));
  return out.join("");
}

function drive() {
  const out = [];
  out.push(S(k.slabOf(DRIVE, 0, DRIVE_H, P, 6, 0.8), { tone: "mid" }));
  out.push(L(k.planOutline(k.insetPlan(DRIVE, 3), DRIVE_H, P), { tone: "faint" }));
  // Fentes d'aération, chacune arrêtée par deux points (aucun trait ne finit dans le vide).
  for (const z of [6, 10, 14]) out.push(L(k.segment([DRIVE.x + DRIVE.w, DRIVE.y + 5, z], [DRIVE.x + DRIVE.w, DRIVE.y + DRIVE.d - 5, z], P), { tone: "lo" }));
  out.push(D([6, 10, 14].flatMap((z) => [at([DRIVE.x + DRIVE.w, DRIVE.y + 5, z]), at([DRIVE.x + DRIVE.w, DRIVE.y + DRIVE.d - 5, z])]), { size: 0.4, tone: "lo" }));
  out.push(D(k.corners(DRIVE, 3).map(([x, y]) => at([x, y, DRIVE_H])), { size: 0.45 }));
  const [x, y] = KNOB;
  const ticks = k.radialTicks(x, y, KNOB_R + 4.5, 12, 3, DRIVE_H, [1.4, 2.8], P, -KNOB_SPAN / 2, KNOB_SPAN);
  out.push(L(k.ring(x, y, KNOB_R + 4.5, DRIVE_H, P, 28), { tone: "faint" }));
  out.push(L(ticks.minor, { tone: "lo" }), L(ticks.major, { tone: "mid" }));
  out.push(S(k.cylinder(x, y, KNOB_R, DRIVE_H, 5, P, 24), { tone: "hi", crease: "lo" }));
  out.push(L(k.knurl(x, y, KNOB_R, DRIVE_H, DRIVE_H + 5, 28, P), { tone: "lo" }));
  out.push(L(k.ring(x, y, KNOB_R - 2, DRIVE_H + 5, P, 20), { tone: "faint" }));
  return out.join("");
}

function pump() {
  const out = [];
  const [x, y] = PUMP;
  out.push(S(k.cylinder(x, y, PUMP_R + 3, 0, 4, P, 24, 0.6), { tone: "mid" }));
  out.push(S(k.cylinder(x, y, PUMP_R, 4, PUMP_H - 8, P, 24), { tone: "mid" }));
  out.push(L([16, 28, 38].map((z) => k.sideArc(x, y, PUMP_R, z, P, 20)).join(""), { tone: "faint" }));
  out.push(S(k.cylinder(x, y, PUMP_R + 2, PUMP_H - 4, 4, P, 24, 0.6), { tone: "mid" }));
  const bolts = Array.from({ length: 8 }, (_, i) => (i / 8) * Math.PI * 2);
  out.push(D(bolts.map((a) => at([x + Math.sin(a) * (PUMP_R + 0.6), y - Math.cos(a) * (PUMP_R + 0.6), PUMP_H])), { size: 0.45 }));
  out.push(S(k.cylinder(x, y, 5, PUMP_H, 3, P, 12), { tone: "mid" }));
  return out.join("");
}

function rod() {
  // Tige de piston : monte et descend avec Ve (pièce mobile, déplacée par le script).
  const [x, y] = PUMP;
  return (
    S(k.cylinder(x, y, ROD_R, PUMP_H + 3 - STROKE, ROD_LEN, P, 12), { tone: "hi", crease: "none" }) +
    S(k.cylinder(x, y, 6, PUMP_H + 3 - STROKE + ROD_LEN, 5, P, 16, 0.6), { tone: "hi", crease: "lo" }) +
    L(k.knurl(x, y, 6, PUMP_H - STROKE + ROD_LEN + 4, PUMP_H - STROKE + ROD_LEN + 8, 20, P), { tone: "lo" })
  );
}

function bell() {
  // Cloche à membrane (le condensateur en série) : l'eau ne la traverse pas, la membrane pousse le même volume devant elle.
  const out = [];
  const [x, y] = BELL;
  out.push(S(k.cylinder(x, y, BELL_R, 0, BELL_SEAM - 1.5, P, 18), { tone: "mid" }));
  // Brides serrant la membrane, boulonnées.
  out.push(S(k.cylinder(x, y, BELL_R + 3, BELL_SEAM - 1.5, 3, P, 18, 0.5), { tone: "mid" }));
  const bolts = Array.from({ length: 10 }, (_, i) => (i / 10) * Math.PI * 2);
  out.push(D(bolts.map((a) => at([x + Math.sin(a) * (BELL_R + 1.6), y - Math.cos(a) * (BELL_R + 1.6), BELL_SEAM + 1.5])), { size: 0.45 }));
  out.push(S(k.cylinder(x, y, BELL_R, BELL_SEAM + 1.5, BELL_TOP - BELL_SEAM - 1.5, P, 18), { tone: "mid" }));
  out.push(S(k.cylinder(x, y, BELL_R + 1.5, BELL_TOP, 4, P, 18, 0.6), { tone: "mid" }));
  // Presse-étoupe de la tige.
  out.push(S(k.cylinder(x, y, 4.2, BELL_TOP + 4, 3, P, 12), { tone: "mid" }));
  return out.join("");
}

function stem() {
  // Tige de membrane : monte avec la charge du condensateur, Vc (pièce mobile).
  const [x, y] = BELL;
  const z0 = GLAND_TOP - STEM_LIFT;
  return (
    S(k.cylinder(x, y, 2.2, z0, STEM_LEN, P, 12), { tone: "hi", crease: "none" }) +
    S(k.cylinder(x, y, 5, z0 + STEM_LEN, 2.4, P, 16, 0.5), { tone: "hi", crease: "lo" }) +
    L(k.ring(x, y, 3, z0 + STEM_LEN + 2.4, P, 16), { tone: "lo" })
  );
}

function node() {
  // Nœud entre membrane et vanne : bloc à deux piquages, manomètre au-dessus.
  const out = [];
  out.push(S(k.slabOf(NODE, 0, NODE_H, P, 4, 0.6), { tone: "mid" }));
  out.push(L(k.planOutline(k.insetPlan(NODE, 3), NODE_H, P), { tone: "faint" }));
  out.push(D(k.corners(NODE, 2.6).map(([px, py]) => at([px, py, NODE_H])), { size: 0.45 }));
  return out.join("");
}

function gauge() {
  const out = [];
  const [x, y] = GAUGE;
  out.push(S(k.cylinder(x, y, 3.4, NODE_H, GAUGE_Z - NODE_H, P, 12), { tone: "mid", crease: "none" }));
  out.push(S(k.cylinder(x, y, DIAL_R, GAUGE_Z, DIAL_H, P, 28, 0.8), { tone: "hi", crease: "lo" }));
  out.push(L(k.ring(x, y, DIAL_R - 2, DIAL_TOP, P, 36), { tone: "lo" }));
  const ticks = k.radialTicks(x, y, DIAL_R - 3, 24, 6, DIAL_TOP, [1.3, 2.8], P, -NEEDLE_SPAN, NEEDLE_SPAN * 2);
  out.push(L(ticks.minor, { tone: "lo" }), L(ticks.major, { tone: "mid" }));
  // Repères ±0,707 de la coupure (−3 dB), plus fins que les graduations.
  out.push(L([-1, 1].map((s) => {
    const a = s * 0.7071 * NEEDLE_SPAN;
    return k.lineOnTop([x + Math.sin(a) * (DIAL_R - 7), y - Math.cos(a) * (DIAL_R - 7)], [x + Math.sin(a) * (DIAL_R - 5.6), y - Math.cos(a) * (DIAL_R - 5.6)], DIAL_TOP, P);
  }).join(""), { tone: "hi" }));
  out.push(L(k.ring(x, y, 1.6, DIAL_TOP, P, 16), { tone: "mid" }));
  return out.join("");
}

function valve() {
  const out = [];
  out.push(S(k.slabOf(VALVE, PIPE_Z - 4, VALVE_H - PIPE_Z + 4, P, 4, 0.6), { tone: "mid" }));
  out.push(L(k.planOutline(k.insetPlan(VALVE, 3), VALVE_H, P), { tone: "faint" }));
  out.push(D(k.corners(VALVE, 2.6).map(([x, y]) => at([x, y, VALVE_H])), { size: 0.45 }));
  const [x, y] = WHEEL;
  out.push(S(k.cylinder(x, y, 2.2, VALVE_H, 10, P, 10), { tone: "mid", crease: "none" }));
  out.push(S(k.cylinder(x, y, 10, VALVE_H + 10, 2.6, P, 20, 0.4), { tone: "mid" }));
  out.push(L(k.knurl(x, y, 10, VALVE_H + 10, VALVE_H + 12.6, 20, P), { tone: "lo" }));
  out.push(L([0, 1, 2].map((i) => k.lineOnTop([x, y], [x + Math.sin((i * 2 * Math.PI) / 3) * 10, y - Math.cos((i * 2 * Math.PI) / 3) * 10], VALVE_H + 12.6, P)).join(""), { tone: "lo" }));
  out.push(D([at([x, y, VALVE_H + 12.6])], { size: 0.5, tone: "hi" }));
  return out.join("");
}

function trayWall(plan) {
  return S(k.slabOf(plan, 0, TRAY_H, P, 2), { tone: "mid" });
}

function trayBack() {
  const out = [S(k.slabOf(TRAY, 0, 0.8, P, 4), { tone: "lo", crease: "none" })];
  out.push(trayWall({ x: TRAY.x, y: TRAY.y, w: TRAY.w, d: WALL, r: 0.6 }));
  out.push(trayWall({ x: TRAY.x, y: TRAY.y, w: WALL, d: TRAY.d, r: 0.6 }));
  return out.join("");
}

function spout() {
  // Bec de la vanne : l'eau retombe dans le bac, à la pression de la masse.
  const [x, y] = SPOUT;
  return (
    S(k.cylinder(x, y, 3.6, 3, PIPE_Z + PIPE_H - 3, P, 12), { tone: "mid", crease: "none" }) +
    S(k.cylinder(x, y, 4.6, 1.6, 1.6, P, 12, 0.3), { tone: "mid" })
  );
}

function trayFront() {
  const out = [];
  out.push(trayWall({ x: TRAY.x + TRAY.w - WALL, y: TRAY.y, w: WALL, d: TRAY.d, r: 0.6 }));
  out.push(trayWall({ x: TRAY.x, y: TRAY.y + TRAY.d - WALL, w: TRAY.w, d: WALL, r: 0.6 }));
  out.push(D(k.corners(TRAY, 1.1).map(([x, y]) => at([x, y, TRAY_H])), { size: 0.4 }));
  return out.join("");
}

// Pièces mobiles posées à leur repos (Ve = Vc = Vs = 0) ; le script les déplace.
const body = [
  plate(),
  returnLine(),
  drive(),
  `<path data-part="knob" class="iso-line" data-tone="hi" data-free="start" d="" style="stroke-width:1.1"/>`,
  pump(),
  `<g data-part="rod">${rod()}</g>`,
  pipe({ x: PUMP[0] + PUMP_R - 1, y: -3, w: BELL[0] - BELL_R - PUMP[0] - PUMP_R + 2 }),
  collar(PUMP[0] + PUMP_R + 3),
  bell(),
  `<g data-part="stem">${stem()}</g>`,
  pipe({ x: BELL[0] + BELL_R - 1, y: -3, w: NODE.x - BELL[0] - BELL_R + 2 }, OUTLET_Z),
  collar(BELL[0] + BELL_R + 3, OUTLET_Z),
  node(),
  pipe({ x: NODE.x + NODE.w - 1, y: -3, w: VALVE.x - NODE.x - NODE.w + 2 }),
  valve(),
  trayBack(),
  pipe({ x: VALVE.x + VALVE.w - 1, y: -3, w: SPOUT[0] - VALVE.x - VALVE.w + 4 }),
  collar(TRAY.x + 1),
  spout(),
  trayFront(),
  gauge(),
  `<path data-part="needle" class="iso-line" data-tone="lit" data-free="start" d="" style="stroke-width:1.2"/>`,
];

const svg = k
  .figureSvg({ width: WIDTH, height: HEIGHT, label: "", body })
  .replace(' role="img" aria-label=""', ' aria-hidden="true" focusable="false"');

// Projection linéaire : écran = o + x·ex + y·ey + z·ez (exacte en isométrie).
const o = at([0, 0, 0]);
const axis = (v) => at(v).map((c, i) => +(c - o[i]).toFixed(5));
const num = (v) => +v.toFixed(4);
const model = readFileSync(join(HERE, "model.mjs"), "utf8").replace(/^export /gm, "").replace(/^\/\/.*\n/gm, "");

const js = `// Généré par tools/figures/rc_highpass/build.mjs : ne pas modifier à la main.
(() => {
${model}const O = ${JSON.stringify(o.map(num))}, EX = ${JSON.stringify(axis([1, 0, 0]))}, EY = ${JSON.stringify(axis([0, 1, 0]))}, EZ = ${JSON.stringify(axis([0, 0, 1]))};
const scr = (x, y, z) => [O[0] + x * EX[0] + y * EY[0] + z * EZ[0], O[1] + x * EX[1] + y * EY[1] + z * EZ[1]];
const seg = (cx, cy, z, a, r0, r1) => { const p = scr(cx - Math.sin(a) * r0, cy + Math.cos(a) * r0, z), q = scr(cx + Math.sin(a) * r1, cy - Math.cos(a) * r1, z); return "M" + p[0].toFixed(2) + " " + p[1].toFixed(2) + "L" + q[0].toFixed(2) + " " + q[1].toFixed(2); };
const up = (dz) => "translate(" + (EZ[0] * dz).toFixed(3) + " " + (EZ[1] * dz).toFixed(3) + ")";
const PRESETS = { low: 100, fc: FC, high: 16000 };
const SPAN = ${num(NEEDLE_SPAN)}, KSPAN = ${num(KNOB_SPAN)}, STROKE = ${STROKE}, LIFT = ${STEM_LIFT};
const toF = (v) => F_MIN * 10 ** (v / 100), toV = (f) => Math.round(100 * Math.log10(f / F_MIN));
document.querySelectorAll('.fig[data-fig="rc_highpass"]').forEach((card) => {
  const q = (s) => card.querySelector(s), qa = (s) => card.querySelectorAll(s);
  const svg = q("svg"), rod = q('[data-part="rod"]'), stem = q('[data-part="stem"]'), needle = q('[data-part="needle"]'), knob = q('[data-part="knob"]');
  const range = q("[data-fig-freq]"), play = q("[data-fig-play]"), out = {};
  qa("[data-fig-out]").forEach((el) => { out[el.dataset.figOut] = el; });
  const lang = document.documentElement.lang || "fr", still = matchMedia("(prefers-reduced-motion: reduce)");
  const fmt = (v, d, sign) => new Intl.NumberFormat(lang, { maximumFractionDigits: d, minimumFractionDigits: d, signDisplay: sign || "auto" }).format(v);
  const qty = (v, u) => v >= 1000 ? fmt(v / 1000, v >= 1e4 ? 1 : 2) + " k" + u : fmt(v, v >= 100 ? 0 : 1) + " " + u;
  let f = PRESETS.low, phase = Math.PI / 2, last = 0, frame = 0, running = false, visible = true;
  function pose() {
    const ve = Math.sin(phase), rad = Math.PI / 180;
    const vs = ratio(f) * Math.sin(phase + phaseDeg(f) * rad), vc = capRatio(f) * Math.sin(phase + capPhaseDeg(f) * rad);
    rod.setAttribute("transform", up(STROKE * ve));
    stem.setAttribute("transform", up(LIFT * vc));
    needle.setAttribute("d", seg(${GAUGE[0]}, ${GAUGE[1]}, ${DIAL_TOP + 0.2}, vs * SPAN, 3.4, ${DIAL_R - 4}));
    knob.setAttribute("d", seg(${KNOB[0]}, ${KNOB[1]}, ${DRIVE_H + 5.2}, -KSPAN / 2 + KSPAN * Math.log10(f / F_MIN) / 4, 0, ${KNOB_R - 1.5}));
  }
  function report() {
    const text = qty(f, "Hz");
    range.value = toV(f);
    range.setAttribute("aria-valuetext", text);
    if (out.f) out.f.textContent = text;
    if (out.xc) out.xc.textContent = qty(xc(f), "Ω");
    if (out.ratio) out.ratio.textContent = fmt(ratio(f), 3);
    if (out.phase) out.phase.textContent = fmt(phaseDeg(f), 1, "exceptZero") + "°";
    pose();
  }
  function tick(now) {
    if (last) phase += 2 * Math.PI * Math.min(now - last, 100) / 1000 / periodS(f);
    last = now;
    pose();
    frame = running && visible && !still.matches ? requestAnimationFrame(tick) : 0;
  }
  const run = () => { if (!frame && running && visible && !still.matches) { last = 0; frame = requestAnimationFrame(tick); } };
  function setPlaying(on) {
    running = on;
    play.setAttribute("aria-pressed", on ? "true" : "false");
    play.textContent = on ? play.dataset.pause : play.dataset.play;
    if (on) run();
  }
  range.addEventListener("input", () => { f = toF(+range.value); report(); setPlaying(true); });
  qa("[data-fig-preset]").forEach((b) => b.addEventListener("click", () => { f = PRESETS[b.dataset.figPreset]; report(); setPlaying(true); }));
  play.addEventListener("click", () => setPlaying(!running));
  new IntersectionObserver((e) => { visible = e[e.length - 1].isIntersecting; run(); }).observe(svg);
  q("[data-fig-controls]").hidden = false;
  report();
});
})();
`;

const write = (path, text) => {
  mkdirSync(dirname(path), { recursive: true });
  writeFileSync(path, text.replace(/\r\n/g, "\n"));
};
const svgPath = OUT ? join(OUT, "rc_highpass.svg") : join(ROOT, "templates", "figures", "rc_highpass.svg");
const jsPath = OUT ? join(OUT, "rc_highpass.js") : join(ROOT, "static", "acad", "js", "figures", "rc_highpass.js");
write(svgPath, svg + "\n");
write(jsPath, js);
console.log(`wrote ${svgPath} (${Buffer.byteLength(svg)} o), ${jsPath} (${Buffer.byteLength(js)} o)`);
