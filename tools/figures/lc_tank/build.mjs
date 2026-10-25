// Figure « circuit bouchon » (section 04-lc-parallele de M7) : vanne (R) en série, puis roue à volant (L) et cloche (C) en parallèle.
// node tools/figures/lc_tank/build.mjs [--out <dossier>]
// écrit templates/figures/lc_tank.svg (dessin sans texte) et static/acad/js/figures/lc_tank.js (animation).
// Fichiers générés : ne jamais les retoucher à la main, modifier ce script puis le relancer.
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "../kit/iso-kit.mjs";
import { F0, U, line, tankV, coil } from "./model.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(HERE, "../../..");
const outAt = process.argv.indexOf("--out");
const OUT = outAt > 0 ? resolve(process.argv[outAt + 1]) : null;

const WIDTH = 640;
const HEIGHT = 360;

// Plan du banc (unités monde, z vers le haut) : piston (Ve) → vanne étranglée coiffée d'un débitmètre (Rs, courant de ligne)
// → nœud coiffé d'un manomètre (tension du bouchon Vt) → deux branches en parallèle vers le bac (la masse) :
// à l'arrière la roue à volant (L), à l'avant la cloche à membrane (C).
// Le débitmètre et le repère du volant partagent la même échelle (±2 mA) : à f0, le courant de ligne est minimal
// tandis qu'un courant trente fois plus grand va et vient entre L et C.
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
// Carter de la roue à aubes : entrée en bas, sortie en haut ; l'arbre porte le volant au-dessus du couvercle.
const TURB = [4, -17];
const TURB_R = 14;
const CASE_TOP = 30;
const FLY_Z = 38;
const FLY_R = 18;
const FLY_H = 4;
const FLY_TOP = FLY_Z + FLY_H;
const HUB_R = 4;
// Cloche : deux demi-corps serrant la membrane ; entrée sous la membrane, sortie au-dessus, vers le bac.
const BELL = [40, 17];
const BELL_R = 15;
const BELL_SEAM = 18;
const BELL_TOP = 34;
const OUTLET_Z = 24;
// Vanne (R) coiffée du débitmètre : aiguille à ±120° pour i = ±Imax.
const VALVE = { x: -80, y: -9, w: 20, d: 18, r: 2 };
const VALVE_H = 22;
const GAUGE = [-70, 0];
const GAUGE_Z = 40;
const DIAL_R = 14;
const DIAL_H = 5;
const DIAL_TOP = GAUGE_Z + DIAL_H;
const NODE = { x: -44, y: -24, w: 16, d: 48, r: 2 };
const NODE_H = 30;
const NGAUGE = [-36, 0];
const BRANCH = [-17, 17]; // axes des branches L (arrière) et C (avant)
const TRAY = { x: 80, y: -30, w: 64, d: 60, r: 4 };
const TRAY_H = 7;
const WALL = 2.2;
const NEEDLE_SPAN = (120 * Math.PI) / 180; // ±120° pour ±2 mA (débitmètre, volant) ou ±Ve (manomètre)
const CUR_FS = 2e-3; // A, pleine échelle commune du débitmètre et du volant
const KNOB_SPAN = (270 * Math.PI) / 180; // 10 Hz à 100 kHz sur 270°

const P = k.fitProjection(
  [
    ...k.boxCorners(PLATE, -PLATE_H - FOOT_H, 0),
    [PUMP[0], PUMP[1], PUMP_H + ROD_LEN + STROKE + 6],
    [TURB[0], TURB[1], FLY_TOP + 4],
    [TURB[0] - FLY_R, TURB[1], FLY_TOP],
    [GAUGE[0] - DIAL_R, 0, DIAL_TOP],
    [BELL[0], BELL[1], BELL_TOP + 8],
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
    out.push(S(k.cylinder(x, y, 6, -PLATE_H - FOOT_H, FOOT_H, P, 8), { tone: "mid" }));
  }
  out.push(S(k.slabOf(PLATE, -PLATE_H, PLATE_H, P, 5, 1.6), { tone: "mid" }));
  out.push(L(k.planOutline(k.insetPlan(PLATE, 5), 0, P), { tone: "lo" }));
  const screws = k.corners(PLATE, 10);
  out.push(L(screws.map(([x, y]) => k.ring(x, y, 2.2, 0, P, 16)).join(""), { tone: "lo" }));
  out.push(D(screws.map(([x, y]) => at([x, y, 0])), { size: 0.5 }));
  return out.join("");
}

const pipe = (plan, z = PIPE_Z, h = PIPE_H) => S(k.slabOf({ d: PIPE_H, r: 1.2, ...plan }, z, h, P, 2), { tone: "mid" });
const collar = (x, z = PIPE_Z, y = 0) => S(k.slabOf({ x: x - 1.5, y: y - 4.5, w: 3, d: 9, r: 0.8 }, z - 1.5, PIPE_H + 3, P, 2), { tone: "mid" });

function returnLine() {
  // Retour au bac (la masse) : conduite basse à l'arrière, du bac à l'aspiration de la pompe.
  const out = [];
  out.push(pipe({ x: PUMP[0] - 3, y: -44, w: 6, d: 32 }, 1, 5));
  out.push(pipe({ x: PUMP[0] - 3, y: -44, w: TRAY.x + 14 - PUMP[0] + 3, d: 6 }, 1, 5));
  out.push(pipe({ x: TRAY.x + 8, y: -44, w: 6, d: 16 }, 1, 5));
  out.push(D([at([-20, -41, 6]), at([60, -41, 6])], { size: 0.4, tone: "lo" }));
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
  out.push(L(k.ring(x, y, KNOB_R + 4.5, DRIVE_H, P, 20), { tone: "faint" }));
  out.push(L(ticks.minor, { tone: "lo" }), L(ticks.major, { tone: "mid" }));
  out.push(S(k.cylinder(x, y, KNOB_R, DRIVE_H, 5, P, 18), { tone: "hi", crease: "lo" }));
  out.push(L(k.knurl(x, y, KNOB_R, DRIVE_H, DRIVE_H + 5, 20, P), { tone: "lo" }));
  out.push(L(k.ring(x, y, KNOB_R - 2, DRIVE_H + 5, P, 20), { tone: "faint" }));
  return out.join("");
}

function pump() {
  const out = [];
  const [x, y] = PUMP;
  out.push(S(k.cylinder(x, y, PUMP_R + 3, 0, 4, P, 16, 0.6), { tone: "mid" }));
  out.push(S(k.cylinder(x, y, PUMP_R, 4, PUMP_H - 8, P, 18), { tone: "mid" }));
  out.push(S(k.cylinder(x, y, PUMP_R + 2, PUMP_H - 4, 4, P, 16, 0.6), { tone: "mid" }));
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

function turbine() {
  // Carter de la roue (la bobine en série) : l'eau le traverse et fait tourner la roue à aubes qu'il enferme.
  const out = [];
  const [x, y] = TURB;
  out.push(S(k.cylinder(x, y, TURB_R, 0, CASE_TOP, P, 14), { tone: "mid" }));
  out.push(L([10, 20].map((z) => k.sideArc(x, y, TURB_R, z, P, 16)).join(""), { tone: "faint" }));
  out.push(S(k.cylinder(x, y, TURB_R + 2, CASE_TOP, 3, P, 14, 0.5), { tone: "mid" }));
  // Palier et arbre du volant.
  out.push(S(k.cylinder(x, y, HUB_R, CASE_TOP + 3, 3, P, 12), { tone: "mid" }));
  out.push(S(k.cylinder(x, y, 1.8, CASE_TOP + 6, FLY_Z - CASE_TOP - 6, P, 10), { tone: "hi", crease: "none" }));
  return out.join("");
}

function flywheel() {
  // Volant d'inertie (la pièce à observer) : jante pleine, moyeu et cercle de repère gravé.
  const [x, y] = TURB;
  return (
    S(k.cylinder(x, y, FLY_R, FLY_Z, FLY_H, P, 18, 0.6), { tone: "hi", crease: "lo", lit: true }) +
    L(k.ring(x, y, FLY_R - 3, FLY_TOP, P, 24), { tone: "lo" }) +
    S(k.cylinder(x, y, HUB_R, FLY_TOP, 2, P, 12), { tone: "hi", crease: "lo" })
  );
}

function bell() {
  // Cloche à membrane (le condensateur en série) : l'eau ne la traverse pas, la membrane pousse le même volume devant elle.
  const out = [];
  const [x, y] = BELL;
  out.push(S(k.cylinder(x, y, BELL_R, 0, BELL_SEAM - 1.5, P, 14), { tone: "mid" }));
  // Brides serrant la membrane, boulonnées.
  out.push(S(k.cylinder(x, y, BELL_R + 3, BELL_SEAM - 1.5, 3, P, 14, 0.5), { tone: "mid" }));
  const bolts = Array.from({ length: 10 }, (_, i) => (i / 10) * Math.PI * 2);
  out.push(D(bolts.map((a) => at([x + Math.sin(a) * (BELL_R + 1.6), y - Math.cos(a) * (BELL_R + 1.6), BELL_SEAM + 1.5])), { size: 0.45 }));
  out.push(S(k.cylinder(x, y, BELL_R, BELL_SEAM + 1.5, BELL_TOP - BELL_SEAM - 1.5, P, 14), { tone: "mid" }));
  out.push(S(k.cylinder(x, y, BELL_R + 1.5, BELL_TOP, 4, P, 14, 0.6), { tone: "mid" }));
  // Bouchon de purge du demi-corps supérieur.
  out.push(S(k.cylinder(x, y, 4.2, BELL_TOP + 4, 3, P, 12), { tone: "mid" }));
  out.push(L(k.ring(x, y, 2.4, BELL_TOP + 7, P, 12), { tone: "lo" }));
  return out.join("");
}

function gauge([x, y], base) {
  const out = [];
  out.push(S(k.cylinder(x, y, 3.4, base, GAUGE_Z - base, P, 12), { tone: "mid", crease: "none" }));
  out.push(S(k.cylinder(x, y, DIAL_R, GAUGE_Z, DIAL_H, P, 18, 0.8), { tone: "hi", crease: "lo" }));
  out.push(L(k.ring(x, y, DIAL_R - 2, DIAL_TOP, P, 24), { tone: "lo" }));
  const ticks = k.radialTicks(x, y, DIAL_R - 3, 16, 4, DIAL_TOP, [1.3, 2.8], P, -NEEDLE_SPAN, NEEDLE_SPAN * 2);
  out.push(L(ticks.minor, { tone: "lo" }), L(ticks.major, { tone: "mid" }));
  out.push(L(k.ring(x, y, 1.6, DIAL_TOP, P, 16), { tone: "mid" }));
  return out.join("");
}

function valve() {
  const out = [];
  out.push(S(k.slabOf(VALVE, PIPE_Z - 4, VALVE_H - PIPE_Z + 4, P, 4, 0.6), { tone: "mid" }));
  out.push(L(k.planOutline(k.insetPlan(VALVE, 3), VALVE_H, P), { tone: "faint" }));
  out.push(D(k.corners(VALVE, 2.6).map(([x, y]) => at([x, y, VALVE_H])), { size: 0.45 }));
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

function node() {
  // Nœud : une entrée (la ligne), deux départs (L à l'arrière, C à l'avant) ; le manomètre lit la tension du bouchon.
  return (
    S(k.slabOf(NODE, 0, NODE_H, P, 4, 0.6), { tone: "mid" }) +
    L(k.planOutline(k.insetPlan(NODE, 3), NODE_H, P), { tone: "faint" })
  );
}

function spout(x, y, top) {
  // Bec de branche : l'eau retombe dans le bac, à la pression de la masse.
  return (
    S(k.cylinder(x, y, 3.6, 3, top - 3, P, 12), { tone: "mid", crease: "none" }) +
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
// Aiguille ou repère tracé sur une face du dessus (même tracé que seg() du script).
function pointer([x, y], z, a, r0, r1) {
  const p = at([x - Math.sin(a) * r0, y + Math.cos(a) * r0, z]);
  const q = at([x + Math.sin(a) * r1, y - Math.cos(a) * r1, z]);
  return "M" + p[0].toFixed(2) + " " + p[1].toFixed(2) + "L" + q[0].toFixed(2) + " " + q[1].toFixed(2);
}
const RAD = Math.PI / 180;
const at0 = (ph, wt) => ph.amp * Math.sin(wt + ph.deg * RAD);
// Le volant suit l'eau qui traverse la bobine : quart de période derrière iL, à l'échelle du débitmètre.
const flyAngle = (f, wt) => (NEEDLE_SPAN * coil(f).amp * Math.sin(wt + coil(f).deg * RAD - Math.PI / 2)) / CUR_FS;
// Sans JavaScript : figé à f0, Ve à sa crête.
const FS = F0;
const PHASE0 = Math.PI / 2;

const body = [
  plate(),
  returnLine(),
  drive(),
  `<path data-part="knob" class="iso-line" data-tone="hi" data-free="start" d="" style="stroke-width:1.1"/>`,
  pump(),
  `<g data-part="rod">${rod()}</g>`,
  pipe({ x: PUMP[0] + PUMP_R - 1, y: -3, w: VALVE.x - PUMP[0] - PUMP_R + 2 }),
  valve(),
  gauge(GAUGE, VALVE_H),
  `<path data-part="needle" class="iso-line" data-tone="lit" data-free="start" d="${pointer(GAUGE, DIAL_TOP + 0.2, (at0(line(FS), PHASE0) * NEEDLE_SPAN) / CUR_FS, 3.4, DIAL_R - 4)}" style="stroke-width:1.2"/>`,
  pipe({ x: VALVE.x + VALVE.w - 1, y: -3, w: NODE.x - VALVE.x - VALVE.w + 2 }),
  node(),
  gauge(NGAUGE, NODE_H),
  `<path data-part="vt" class="iso-line" data-tone="hi" data-free="start" d="${pointer(NGAUGE, DIAL_TOP + 0.2, (at0(tankV(FS), PHASE0) * NEEDLE_SPAN) / U, 3.4, DIAL_R - 4)}" style="stroke-width:1.2"/>`,
  pipe({ x: NODE.x + NODE.w - 1, y: BRANCH[0] - 3, w: TURB[0] - TURB_R - NODE.x - NODE.w + 2 }),
  collar(NODE.x + NODE.w + 3, PIPE_Z, BRANCH[0]),
  turbine(),
  flywheel(),
  `<path data-part="fly" class="iso-line" data-tone="hi" d="${pointer(TURB, FLY_TOP + 2.2, flyAngle(FS, PHASE0), -HUB_R, FLY_R - 2.9)}" style="stroke-width:1.6"/>`,
  trayBack(),
  pipe({ x: TURB[0] + TURB_R - 1, y: BRANCH[0] - 3, w: 102 - TURB[0] - TURB_R + 4 }),
  spout(102, BRANCH[0], PIPE_Z + PIPE_H),
  pipe({ x: NODE.x + NODE.w - 1, y: BRANCH[1] - 3, w: BELL[0] - BELL_R - NODE.x - NODE.w + 2 }),
  bell(),
  pipe({ x: BELL[0] + BELL_R - 1, y: BRANCH[1] - 3, w: 102 - BELL[0] - BELL_R + 4 }, OUTLET_Z),
  collar(BELL[0] + BELL_R + 3, OUTLET_Z, BRANCH[1]),
  spout(102, BRANCH[1], OUTLET_Z + PIPE_H),
  trayFront(),
];

const svg = k
  .figureSvg({ width: WIDTH, height: HEIGHT, label: "", body })
  .replace(' role="img" aria-label=""', ' aria-hidden="true" focusable="false"');

// Projection linéaire : écran = o + x·ex + y·ey + z·ez (exacte en isométrie).
const o = at([0, 0, 0]);
const axis = (v) => at(v).map((c, i) => +(c - o[i]).toFixed(5));
const num = (v) => +v.toFixed(4);
const model = readFileSync(join(HERE, "model.mjs"), "utf8").replace(/^export /gm, "").replace(/^\/\/.*\n/gm, "");

const js = `// Généré par tools/figures/lc_tank/build.mjs : ne pas modifier à la main.
(() => {
${model}const O = ${JSON.stringify(o.map(num))}, EX = ${JSON.stringify(axis([1, 0, 0]))}, EY = ${JSON.stringify(axis([0, 1, 0]))}, EZ = ${JSON.stringify(axis([0, 0, 1]))};
const scr = (x, y, z) => [O[0] + x * EX[0] + y * EY[0] + z * EZ[0], O[1] + x * EX[1] + y * EY[1] + z * EZ[1]];
const seg = (cx, cy, z, a, r0, r1) => { const p = scr(cx - Math.sin(a) * r0, cy + Math.cos(a) * r0, z), q = scr(cx + Math.sin(a) * r1, cy - Math.cos(a) * r1, z); return "M" + p[0].toFixed(2) + " " + p[1].toFixed(2) + "L" + q[0].toFixed(2) + " " + q[1].toFixed(2); };
const up = (dz) => "translate(" + (EZ[0] * dz).toFixed(3) + " " + (EZ[1] * dz).toFixed(3) + ")";
const PRESETS = { low: F0 / 2, f0: F0, high: F0 * 2 }, CUR_FS = ${CUR_FS};
const SPAN = ${num(NEEDLE_SPAN)}, KSPAN = ${num(KNOB_SPAN)}, STROKE = ${STROKE};
const toF = (v) => F_MIN * 10 ** (v / 100), toV = (f) => Math.round(100 * Math.log10(f / F_MIN));
document.querySelectorAll('.fig[data-fig="lc_tank"]').forEach((card) => {
  const q = (s) => card.querySelector(s), qa = (s) => card.querySelectorAll(s);
  const svg = q("svg"), rod = q('[data-part="rod"]'), fly = q('[data-part="fly"]'), needle = q('[data-part="needle"]'), vt = q('[data-part="vt"]'), knob = q('[data-part="knob"]');
  const range = q("[data-fig-freq]"), play = q("[data-fig-play]"), out = {};
  qa("[data-fig-out]").forEach((el) => { out[el.dataset.figOut] = el; });
  const lang = document.documentElement.lang || "fr", still = matchMedia("(prefers-reduced-motion: reduce)");
  const fmt = (v, d) => new Intl.NumberFormat(lang, { maximumFractionDigits: d, minimumFractionDigits: d }).format(v);
  const sig = (v) => new Intl.NumberFormat(lang, { maximumSignificantDigits: 3, minimumSignificantDigits: 3 }).format(v);
  const qty = (x, u) => { const v = +x.toPrecision(6); return v >= 1000 ? fmt(v / 1000, v >= 1e4 ? 1 : 2) + " k" + u : fmt(v, v >= 100 ? 0 : 1) + " " + u; };
  let f = PRESETS.f0, phase = Math.PI / 2, last = 0, frame = 0, running = false, visible = true;
  function pose() {
    const ve = Math.sin(phase), rad = Math.PI / 180;
    const w = (ph, d) => ph.amp * Math.sin(phase + ph.deg * rad + (d || 0));
    rod.setAttribute("transform", up(STROKE * ve));
    fly.setAttribute("d", seg(${TURB[0]}, ${TURB[1]}, ${FLY_TOP + 2.2}, SPAN * w(coil(f), -Math.PI / 2) / CUR_FS, -${HUB_R}, ${FLY_R - 2.9}));
    needle.setAttribute("d", seg(${GAUGE[0]}, ${GAUGE[1]}, ${DIAL_TOP + 0.2}, SPAN * w(line(f)) / CUR_FS, 3.4, ${DIAL_R - 4}));
    vt.setAttribute("d", seg(${NGAUGE[0]}, ${NGAUGE[1]}, ${DIAL_TOP + 0.2}, SPAN * w(tankV(f)) / U, 3.4, ${DIAL_R - 4}));
    knob.setAttribute("d", seg(${KNOB[0]}, ${KNOB[1]}, ${DRIVE_H + 5.2}, -KSPAN / 2 + KSPAN * Math.log10(f / F_MIN) / 4, 0, ${KNOB_R - 1.5}));
  }
  function report() {
    const text = qty(f, "Hz");
    range.value = toV(f);
    range.setAttribute("aria-valuetext", text);
    if (out.f) out.f.textContent = text;
    if (out.z) out.z.textContent = qty(zTank(f), "Ω");
    if (out.i) out.i.textContent = sig(line(f).amp * 1e6) + " µA";
    if (out.ilc) out.ilc.textContent = sig(coil(f).amp * 1e3) + " / " + sig(cap(f).amp * 1e3) + " mA";
    if (out.vt) out.vt.textContent = sig(tankV(f).amp / U);
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
const svgPath = OUT ? join(OUT, "lc_tank.svg") : join(ROOT, "templates", "figures", "lc_tank.svg");
const jsPath = OUT ? join(OUT, "lc_tank.js") : join(ROOT, "static", "acad", "js", "figures", "lc_tank.js");
write(svgPath, svg + "\n");
write(jsPath, js);
console.log(`wrote ${svgPath} (${Buffer.byteLength(svg)} o), ${jsPath} (${Buffer.byteLength(js)} o)`);
