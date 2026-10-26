// Figure « circuit d'accord » (section 05-accord de M7) : poste à condensateur variable, cadran des fréquences, trois stations.
// node tools/figures/lc_tuning/build.mjs [--out <dossier>]
// écrit templates/figures/lc_tuning.svg (dessin sans texte) et static/acad/js/figures/lc_tuning.js (animation).
// Fichiers générés : ne jamais les retoucher à la main, modifier ce script puis le relancer.
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "../kit/iso-kit.mjs";
import { STATIONS, f0, cTune, response, overlapDeg } from "./model.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(HERE, "../../..");
const outAt = process.argv.indexOf("--out");
const OUT = outAt > 0 ? resolve(process.argv[outAt + 1]) : null;

const WIDTH = 640;
const HEIGHT = 360;

// Plan (unités monde, z vers le haut ; x et y croissants vers l'observateur).
// À gauche, le condensateur variable : lames fixes à l'arrière (demi-anneaux), lames mobiles (teal) qui tournent avec l'arbre
// et entrent entre elles ; plus elles sont rentrées, plus C est grand. Au centre, la bobine d'accord (100 µH) ;
// à l'arrière droit, l'antenne et trois galvanomètres, un par station ; devant, le cadran des fréquences et son index.
const PLATE = { x: -150, y: -64, w: 300, d: 120, r: 8 };
const PLATE_H = 10;
const FOOT_H = 5;
const CAP = [-92, -10];
const CAP_BASE = { x: CAP[0] - 30, y: CAP[1] - 30, w: 60, d: 52, r: 3 };
const R_PLATE = 24;
const R_HOLE = 4;
const STATOR_Z = [8, 16, 24, 32, 40];
const ROTOR_Z = [12, 20, 28, 36];
const SHAFT_TOP = 48;
const KNOB_R = 7;
const COIL = [-38, -18];
const COIL_R = 7;
const COIL_H = 30;
const METERS = [[18, -30], [56, -30], [94, -30]];
const METER_H = 12;
const DIAL_R = 10;
const METER_SPAN = (60 * Math.PI) / 180; // 0 à 1 → −60° à +60°
const MAST = [128, -48];
const SCALE = { x: -44, y: 26, w: 176, d: 20, r: 2 };
const SCALE_H = 10;
const FX0 = -36; // abscisse de 0,8 MHz sur l'échelle
const FSX = 160 / 0.4e6; // unités par hertz : 0,8 à 1,2 MHz sur 160 unités
const ARC = 16; // pas des demi-disques

const P = k.fitProjection(
  [...k.boxCorners(PLATE, -PLATE_H - FOOT_H, 0), [MAST[0], MAST[1], 64], [CAP[0], CAP[1], SHAFT_TOP + 6]],
  WIDTH,
  HEIGHT,
  { pad: 18, azimuth: 40 },
);

const at = (point) => k.iso(point, P);
const S = (paths, style) => k.solidSvg(paths, style);
const L = (d, style) => k.lineSvg(d, style);
const D = (points, style) => k.dotsSvg(points, style);
const depth = (x, y, z = 0) => k.depthOf([x, y, z], P);
const poly = (points, closed = false) => k.pathOf(points.map(at), closed);
const xOf = (f) => FX0 + FSX * (f - 0.8e6);

// Demi-disque (r0 = 0) ou demi-anneau (r0 > 0) dans le plan z, de l'angle a0 à a0 + 180°.
function sector(z, r0, a0deg) {
  const pts = [];
  for (let i = 0; i <= ARC; i++) {
    const a = ((a0deg + (180 * i) / ARC) * Math.PI) / 180;
    pts.push([CAP[0] + R_PLATE * Math.cos(a), CAP[1] + R_PLATE * Math.sin(a), z]);
  }
  if (r0 > 0) {
    for (let i = ARC; i >= 0; i--) {
      const a = ((a0deg + (180 * i) / ARC) * Math.PI) / 180;
      pts.push([CAP[0] + r0 * Math.cos(a), CAP[1] + r0 * Math.sin(a), z]);
    }
  } else pts.push([CAP[0], CAP[1], z]);
  return poly(pts, true);
}
const plateSvg = (d, lit, part) =>
  `<g class="iso-solid"${lit ? " data-lit" : ""}${part ? ` data-part="${part}"` : ""}><path class="iso-top" d="${d}"/><path class="iso-line iso-edge" data-tone="${lit ? "lit" : "hi"}" d="${d}"/></g>`;

function plate() {
  const out = [`<path class="iso-halo" d="${k.haloOf(PLATE, -PLATE_H - FOOT_H, PLATE_H, P)}"/>`];
  const feet = [...k.corners(PLATE, 22)].sort((a, b) => depth(...a) - depth(...b));
  for (const [x, y] of feet) out.push(S(k.cylinder(x, y, 6, -PLATE_H - FOOT_H, FOOT_H, P, 8), { tone: "mid" }));
  out.push(S(k.slabOf(PLATE, -PLATE_H, PLATE_H, P, 5, 1.6), { tone: "mid" }));
  out.push(L(k.planOutline(k.insetPlan(PLATE, 5), 0, P), { tone: "lo" }));
  const screws = k.corners(PLATE, 10);
  out.push(L(screws.map(([x, y]) => k.ring(x, y, 2.2, 0, P, 16)).join(""), { tone: "lo" }));
  out.push(D(screws.map(([x, y]) => at([x, y, 0])), { size: 0.5 }));
  return out.join("");
}

function capacitorBack() {
  // Socle, arbre et deux colonnettes qui portent les lames fixes.
  const out = [S(k.slabOf(CAP_BASE, 0, 4, P, 3, 0.6), { tone: "mid" })];
  for (const a of [225, 315]) {
    const r = (R_PLATE + R_HOLE) / 2 + 4;
    const x = CAP[0] + r * Math.cos((a * Math.PI) / 180), y = CAP[1] + r * Math.sin((a * Math.PI) / 180);
    out.push(S(k.cylinder(x, y, 1.6, 4, STATOR_Z[STATOR_Z.length - 1] - 4, P, 8), { tone: "mid", crease: "none" }));
  }
  out.push(S(k.cylinder(CAP[0], CAP[1], 2.2, 4, SHAFT_TOP - 4, P, 10), { tone: "hi", crease: "none" }));
  return out.join("");
}

function plates(theta) {
  // Lames empilées par hauteur croissante : fixes (arrière, demi-anneaux) et mobiles (teal), en alternance.
  const levels = [...STATOR_Z.map((z) => [z, false]), ...ROTOR_Z.map((z) => [z, true])].sort((a, b) => a[0] - b[0]);
  return levels.map(([z, rotor]) => (rotor ? plateSvg(sector(z, 0, theta), true, "rotor") : plateSvg(sector(z, R_HOLE, 180), false))).join("");
}

function knob() {
  const [x, y] = CAP;
  return (
    S(k.cylinder(x, y, KNOB_R, SHAFT_TOP, 5, P, 18), { tone: "hi", crease: "lo" }) +
    L(k.knurl(x, y, KNOB_R, SHAFT_TOP, SHAFT_TOP + 5, 20, P), { tone: "lo" }) +
    L(k.ring(x, y, KNOB_R - 2, SHAFT_TOP + 5, P, 16), { tone: "faint" })
  );
}

function coil() {
  // Bobine d'accord : mandrin isolant et spires.
  const [x, y] = COIL;
  const out = [S(k.cylinder(x, y, COIL_R + 3, 0, 3, P, 14, 0.4), { tone: "mid" })];
  out.push(S(k.cylinder(x, y, COIL_R, 3, COIL_H, P, 14), { tone: "hi", crease: "none" }));
  out.push(L(Array.from({ length: 9 }, (_, i) => k.sideArc(x, y, COIL_R, 7 + i * 3, P, 14)).join(""), { tone: "mid" }));
  out.push(S(k.cylinder(x, y, COIL_R + 1.5, COIL_H + 3, 2, P, 14, 0.3), { tone: "mid" }));
  return out.join("");
}

function mast() {
  const [x, y] = MAST;
  return (
    S(k.cylinder(x, y, 5, 0, 4, P, 12, 0.4), { tone: "mid" }) +
    S(k.cylinder(x, y, 1.2, 4, 56, P, 8), { tone: "hi", crease: "none" }) +
    S(k.cylinder(x, y, 2.2, 60, 2, P, 10), { tone: "hi", crease: "lo" })
  );
}

function meter([x, y]) {
  // Galvanomètre d'une station : boîtier, cadran, échelle de 0 à 1 sur ±60°, axe de l'aiguille.
  const box = { x: x - 13, y: y - 11, w: 26, d: 22, r: 2 };
  const out = [S(k.slabOf(box, 0, METER_H, P, 3, 0.6), { tone: "mid" })];
  out.push(S(k.cylinder(x, y, DIAL_R, METER_H, 2, P, 16, 0.4), { tone: "hi", crease: "lo" }));
  const top = METER_H + 2;
  out.push(L(k.ring(x, y, DIAL_R - 2, top, P, 20), { tone: "lo" }));
  const ticks = k.radialTicks(x, y, DIAL_R - 2, 4, 2, top, [1.2, 2.2], P, -METER_SPAN, METER_SPAN * 2);
  out.push(L(ticks.minor, { tone: "lo" }), L(ticks.major, { tone: "mid" }));
  out.push(L(k.ring(x, y, 1.2, top, P, 10), { tone: "mid" }));
  return out.join("");
}

function scale() {
  // Cadran des fréquences : échelle de 0,8 à 1,2 MHz, une graduation par 10 kHz, une grande par 50 kHz, trois stations.
  const out = [S(k.slabOf(SCALE, 0, SCALE_H, P, 4, 0.8), { tone: "mid" })];
  const z = SCALE_H;
  const base = SCALE.y + 6;
  out.push(L(k.lineOnTop([xOf(0.8e6), base], [xOf(1.2e6), base], z, P), { tone: "lo" }));
  const ticks = k.topTicks(xOf(0.8e6), xOf(1.2e6), FSX * 10e3, 5, base, z, [2, 4], P);
  out.push(L(ticks.minor, { tone: "lo" }), L(ticks.major, { tone: "mid" }));
  out.push(L(STATIONS.map((f) => k.planOutline({ x: xOf(f) - 1.5, y: base + 6, w: 3, d: 4, r: 0 }, z, P, 1)).join(""), { tone: "lit" }));
  return out.join("");
}

// Aiguilles et index (même tracé que seg() du script).
function pointer([x, y], z, a, r0, r1) {
  const p = at([x - Math.sin(a) * r0, y + Math.cos(a) * r0, z]);
  const q = at([x + Math.sin(a) * r1, y - Math.cos(a) * r1, z]);
  return "M" + p[0].toFixed(2) + " " + p[1].toFixed(2) + "L" + q[0].toFixed(2) + " " + q[1].toFixed(2);
}
const meterAngle = (g) => -METER_SPAN + 2 * METER_SPAN * g;
// Index tiré d'un bord à l'autre de la face supérieure (biseau de 0,8 compris).
const index = (f) => poly([[xOf(f), SCALE.y + 0.8, SCALE_H + 0.3], [xOf(f), SCALE.y + SCALE.d - 0.8, SCALE_H + 0.3]]);

// Sans JavaScript : accordé sur 1 MHz, l'exemple de la section (C ≈ 253 pF).
const CS = cTune(1e6);
const FS = f0(CS);
const THETA = overlapDeg(CS);

const body = [
  plate(),
  mast(),
  ...METERS.map((m, n) => meter(m) + `<path data-part="meter" data-n="${n}" class="iso-line" data-tone="hi" d="${pointer(m, METER_H + 2.2, meterAngle(response(STATIONS[n], FS)), 1.2, DIAL_R - 3)}" style="stroke-width:1.2"/>`),
  capacitorBack(),
  plates(THETA),
  knob(),
  `<path data-part="knob" class="iso-line" data-tone="hi" d="${pointer(CAP, SHAFT_TOP + 5.2, ((THETA - 90) * Math.PI) / 180, 0, KNOB_R - 1)}" style="stroke-width:1.2"/>`,
  coil(),
  scale(),
  `<path data-part="index" class="iso-line" data-tone="hi" d="${index(FS)}" style="stroke-width:1.6"/>`,
];

const svg = k
  .figureSvg({ width: WIDTH, height: HEIGHT, label: "", body })
  .replace(' role="img" aria-label=""', ' aria-hidden="true" focusable="false"');

// Projection linéaire : écran = o + x·ex + y·ey + z·ez (exacte en isométrie).
const o = at([0, 0, 0]);
const axis = (v) => at(v).map((c, i) => +(c - o[i]).toFixed(5));
const num = (v) => +v.toFixed(4);
const model = readFileSync(join(HERE, "model.mjs"), "utf8").replace(/^export /gm, "").replace(/^\/\/.*\n/gm, "");

const js = `// Généré par tools/figures/lc_tuning/build.mjs : ne pas modifier à la main.
(() => {
${model}const O = ${JSON.stringify(o.map(num))}, EX = ${JSON.stringify(axis([1, 0, 0]))}, EY = ${JSON.stringify(axis([0, 1, 0]))}, EZ = ${JSON.stringify(axis([0, 0, 1]))};
const scr = (x, y, z) => [O[0] + x * EX[0] + y * EY[0] + z * EZ[0], O[1] + x * EX[1] + y * EY[1] + z * EZ[1]];
const pth = (pts, closed) => pts.map((p, i) => { const s = scr(p[0], p[1], p[2]); return (i ? "L" : "M") + s[0].toFixed(2) + " " + s[1].toFixed(2); }).join("") + (closed ? "Z" : "");
const seg = (cx, cy, z, a, r0, r1) => pth([[cx - Math.sin(a) * r0, cy + Math.cos(a) * r0, z], [cx + Math.sin(a) * r1, cy - Math.cos(a) * r1, z]]);
const CX = ${CAP[0]}, CY = ${CAP[1]}, RP = ${R_PLATE}, ARC = ${ARC}, ROTOR_Z = ${JSON.stringify(ROTOR_Z)}, METERS = ${JSON.stringify(METERS)}, MSPAN = ${num(METER_SPAN)};
const PRESETS = { s0: cTune(STATIONS[0]), s1: cTune(STATIONS[1]), s2: cTune(STATIONS[2]) };
const half = (z, a0) => { const pts = []; for (let i = 0; i <= ARC; i++) { const a = (a0 + 180 * i / ARC) * Math.PI / 180; pts.push([CX + RP * Math.cos(a), CY + RP * Math.sin(a), z]); } pts.push([CX, CY, z]); return pth(pts, true); };
const xOf = (f) => ${FX0} + ${FSX} * (f - 0.8e6);
document.querySelectorAll('.fig[data-fig="lc_tuning"]').forEach((card) => {
  const q = (s) => card.querySelector(s), qa = (s) => card.querySelectorAll(s);
  const svg = q("svg"), knob = q('[data-part="knob"]'), idx = q('[data-part="index"]'), rotors = [...qa('[data-part="rotor"]')], meters = [...qa('[data-part="meter"]')];
  const range = q("[data-fig-c]"), play = q("[data-fig-play]"), readout = q(".fig-readout"), out = {};
  qa("[data-fig-out]").forEach((el) => { out[el.dataset.figOut] = el; });
  const lang = document.documentElement.lang || "fr", still = matchMedia("(prefers-reduced-motion: reduce)");
  const sig = (v) => new Intl.NumberFormat(lang, { maximumSignificantDigits: 3, minimumSignificantDigits: 3 }).format(v);
  const mhz = (v) => new Intl.NumberFormat(lang, { maximumFractionDigits: 3, minimumFractionDigits: 3 }).format(v / 1e6) + " MHz";
  let c = PRESETS.s1, t = 0, last = 0, frame = 0, running = false, visible = true;
  function report() {
    const f = f0(c), th = overlapDeg(c), pf = sig(c * 1e12) + " pF";
    range.value = Math.round(c * 2e12) / 2;
    range.setAttribute("aria-valuetext", pf);
    if (out.c) out.c.textContent = pf;
    if (out.f) out.f.textContent = mhz(f);
    STATIONS.forEach((s, n) => { if (out["g" + n]) out["g" + n].textContent = sig(response(s, f)); });
    rotors.forEach((g, n) => { const d = half(ROTOR_Z[n], th); g.querySelectorAll("path").forEach((p) => p.setAttribute("d", d)); });
    knob.setAttribute("d", seg(CX, CY, ${SHAFT_TOP + 5.2}, (th - 90) * Math.PI / 180, 0, ${KNOB_R - 1}));
    idx.setAttribute("d", pth([[xOf(f), ${SCALE.y + 0.8}, ${SCALE_H + 0.3}], [xOf(f), ${SCALE.y + SCALE.d - 0.8}, ${SCALE_H + 0.3}]]));
    meters.forEach((m) => { const n = +m.dataset.n, [mx, my] = METERS[n]; m.setAttribute("d", seg(mx, my, ${METER_H + 2.2}, -MSPAN + 2 * MSPAN * response(STATIONS[n], f), 1.2, ${DIAL_R - 3})); });
  }
  function tick(now) {
    if (last) t += Math.min(now - last, 100) / 1000;
    last = now;
    c = sweepC(t);
    report();
    frame = running && visible && !still.matches ? requestAnimationFrame(tick) : 0;
  }
  const run = () => { if (!frame && running && visible && !still.matches) { last = 0; frame = requestAnimationFrame(tick); } };
  function setPlaying(on) {
    running = on;
    play.setAttribute("aria-pressed", on ? "true" : "false");
    play.textContent = on ? play.dataset.pause : play.dataset.play;
    readout.setAttribute("aria-live", on ? "off" : "polite");
    if (on) { t = SWEEP_S * (c - CMIN) / (CMAX - CMIN); run(); }
  }
  range.addEventListener("input", () => { setPlaying(false); c = +range.value * 1e-12; report(); });
  qa("[data-fig-preset]").forEach((b) => b.addEventListener("click", () => { setPlaying(false); c = PRESETS[b.dataset.figPreset]; report(); }));
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
const svgPath = OUT ? join(OUT, "lc_tuning.svg") : join(ROOT, "templates", "figures", "lc_tuning.svg");
const jsPath = OUT ? join(OUT, "lc_tuning.js") : join(ROOT, "static", "acad", "js", "figures", "lc_tuning.js");
write(svgPath, svg + "\n");
write(jsPath, js);
console.log(`wrote ${svgPath} (${Buffer.byteLength(svg)} o), ${jsPath} (${Buffer.byteLength(js)} o)`);
