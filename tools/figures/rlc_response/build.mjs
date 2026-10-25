// Figure « courbe de réponse » (section 02-courbe-reponse de M7) : table traçante X-Y branchée sur deux RLC série.
// node tools/figures/rlc_response/build.mjs [--out <dossier>]
// écrit templates/figures/rlc_response.svg (dessin sans texte) et static/acad/js/figures/rlc_response.js (animation).
// Fichiers générés : ne jamais les retoucher à la main, modifier ce script puis le relancer.
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "../kit/iso-kit.mjs";
import { F0, R1, R2, F_LO, F_HI, current } from "./model.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(HERE, "../../..");
const outAt = process.argv.indexOf("--out");
const OUT = outAt > 0 ? resolve(process.argv[outAt + 1]) : null;

const WIDTH = 640;
const HEIGHT = 360;

// Plan (unités monde, z vers le haut ; x et y croissants vers l'observateur).
// Pupitre (générateur et deux RLC série, R = 50 Ω et 200 Ω) → câbles → table traçante.
// Sur le papier, x suit la fréquence (0 à 11 kHz, linéaire) et y le courant (0 à 20 mA) ; un portique porte les deux plumes.
const PLATE = { x: -150, y: -64, w: 280, d: 122, r: 8 };
const PLATE_H = 10;
const FOOT_H = 5;
const BED = { x: -110, y: -52, w: 220, d: 96, r: 4 };
const BED_H = 14;
const PAPER = { x: -96, y: -42, w: 192, d: 76, r: 0.5 };
const PAPER_Z = BED_H + 0.6;
const X0 = -88; // abscisse de 0 Hz
const SX = 16 / 1000; // unités par hertz : 1 kHz = 16 unités
const Y0 = 26; // ordonnée de 0 mA
const SY = 3000; // unités par ampère : 20 mA = 60 unités
const RAIL_Z = BED_H + 3;
const RAILS = [{ x: -104, y: -49, w: 208, d: 3, r: 0.6 }, { x: -104, y: 37.5, w: 208, d: 3, r: 0.6 }];
const BRIDGE_Z = 26;
const PEN_Z = 22; // dessous des chariots et des bras
const PUP = { x: -142, y: 46, w: 84, d: 10, r: 1.5 };
const PUP_H = 9;
const KNOB = [-131, 51];
const KNOB_R = 3.6;
const KNOB_SPAN = (270 * Math.PI) / 180; // 500 Hz à 10,5 kHz sur 270°
const ROWS = [48.5, 53.5]; // circuits R = 50 Ω (teal) et R = 200 Ω
const SOCKETS = [-30, -14];
const FRONT = BED.y + BED.d;

const xOf = (f) => X0 + SX * f;
const yOf = (i) => Y0 - SY * i;
// Sans JavaScript : chariot posé au repère « f0 / 2 ».
const FS = F0 / 2;
const GX = xOf(FS);

const P = k.fitProjection(
  [...k.boxCorners(PLATE, -PLATE_H - FOOT_H, 0), [GX, -50, BRIDGE_Z + 3], [GX, 42, BRIDGE_Z + 3]],
  WIDTH,
  HEIGHT,
  { pad: 18, azimuth: 65 },
);

const at = (point) => k.iso(point, P);
const S = (paths, style) => k.solidSvg(paths, style);
const L = (d, style) => k.lineSvg(d, style);
const D = (points, style) => k.dotsSvg(points, style);
const depth = (x, y, z = 0) => k.depthOf([x, y, z], P);
const poly = (points) => k.pathOf(points.map(at));
const rect = (x0, x1, y0, y1, z) => k.planOutline({ x: x0, y: y0, w: x1 - x0, d: y1 - y0, r: 0 }, z, P, 1);

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
  return out.join("");
}

function bed() {
  const out = [S(k.slabOf(BED, 0, BED_H, P, 6, 1), { tone: "mid" })];
  // Douilles des deux voies sur la face avant.
  for (const x of SOCKETS) {
    out.push(L(k.sideRing([x, FRONT, 7], 2.2, "y", P, 16), { tone: "mid" }));
    out.push(L(k.sideRing([x, FRONT, 7], 1, "y", P, 12), { tone: "lo" }));
  }
  return out.join("");
}

function paper() {
  const out = [S(k.slabOf(PAPER, BED_H, 0.6, P, 2), { tone: "lo", crease: "none" })];
  // Quadrillage tiré d'un bord à l'autre : une ligne par kilohertz, une par 5 mA.
  const verticals = Array.from({ length: 12 }, (_, n) => k.lineOnTop([xOf(n * 1000), PAPER.y], [xOf(n * 1000), PAPER.y + PAPER.d], PAPER_Z, P));
  out.push(L(verticals.join(""), { tone: "faint" }));
  const horizontals = [0.005, 0.01, 0.015, 0.02].map((i) => k.lineOnTop([PAPER.x, yOf(i)], [PAPER.x + PAPER.w, yOf(i)], PAPER_Z, P));
  out.push(L(horizontals.join(""), { tone: "faint" }));
  out.push(L(k.lineOnTop([PAPER.x - 0.3, Y0], [PAPER.x + PAPER.w + 0.3, Y0], PAPER_Z, P), { tone: "lo" }));
  // Repère de f0, commun aux deux courbes.
  out.push(L(k.lineOnTop([xOf(F0), PAPER.y], [xOf(F0), PAPER.y + PAPER.d], PAPER_Z, P), { tone: "mid", dashed: true }));
  return out.join("");
}

function curve(r) {
  // Courbe déjà tracée par un balayage complet, de 100 Hz à 11 kHz.
  const points = [];
  for (let f = 100; f <= 11000; f += 25) points.push([xOf(f), yOf(current(f, r)), PAPER_Z]);
  return poly(points);
}

function rail(plan) {
  return S(k.slabOf(plan, BED_H, RAIL_Z - BED_H, P, 2), { tone: "hi", crease: "lo" });
}

function pen(r, side, lit) {
  // Chariot pincé sur le flanc du portique, bras horizontal et stylet posé sur le papier à l'abscisse du portique.
  const y = yOf(current(FS, r));
  const cx = side > 0 ? GX + 3 : GX - 8;
  const ax = side > 0 ? GX : GX - 3.5;
  return (
    S(k.cylinder(GX, y, 0.6, PAPER_Z, PEN_Z - PAPER_Z + 1, P, 8), { tone: "hi", crease: "none", lit }) +
    S(k.slabOf({ x: ax, y: y - 0.6, w: 3.5, d: 1.2, r: 0.2 }, PEN_Z, 1, P, 1), { tone: "hi", crease: "none", lit }) +
    S(k.slabOf({ x: cx, y: y - 2.5, w: 5, d: 5, r: 0.8 }, PEN_Z, BRIDGE_Z + 3 - PEN_Z, P, 2), { tone: "hi", crease: "lo", lit })
  );
}

function gantry() {
  // Portique : deux sabots posés sur les rails, poutre transversale, deux plumes (R = 200 Ω côté arrière, R = 50 Ω côté avant).
  const ends = [{ x: GX - 4, y: -50, w: 8, d: 6, r: 1 }, { x: GX - 4, y: 36, w: 8, d: 6, r: 1 }];
  return (
    S(k.slabOf(ends[0], RAIL_Z, BRIDGE_Z - RAIL_Z, P, 2, 0.4), { tone: "mid" }) +
    `<g data-part="pen" data-r="${R2}">${pen(R2, -1, false)}</g>` +
    `<g data-part="pen" data-r="${R1}">${pen(R1, 1, true)}</g>` +
    S(k.slabOf({ x: GX - 3, y: -49, w: 6, d: 90, r: 1 }, BRIDGE_Z, 3, P, 2, 0.4), { tone: "hi", crease: "lo" }) +
    S(k.slabOf(ends[1], RAIL_Z, BRIDGE_Z - RAIL_Z, P, 2, 0.4), { tone: "mid" })
  );
}

function desk() {
  // Pupitre : bouton du générateur, puis les deux circuits gravés, branchés en parallèle sur la même barre de sortie.
  const out = [S(k.slabOf(PUP, 0, PUP_H, P, 4, 0.8), { tone: "mid" })];
  const z = PUP_H;
  const [x, y] = KNOB;
  out.push(L(k.ring(x, y, KNOB_R + 2.4, z, P, 20), { tone: "faint" }));
  const ticks = k.radialTicks(x, y, KNOB_R + 2.4, 10, 5, z, [0.8, 1.6], P, -KNOB_SPAN / 2, KNOB_SPAN);
  out.push(L(ticks.minor, { tone: "lo" }), L(ticks.major, { tone: "mid" }));
  out.push(S(k.cylinder(x, y, KNOB_R, z, 3, P, 16), { tone: "hi", crease: "lo" }));
  out.push(L(k.knurl(x, y, KNOB_R, z, z + 3, 20, P), { tone: "lo" }));
  const bus = rect(-122, -121.2, 47, 55, z);
  const row = (yy, rLen) => {
    const xr = -118 + rLen;
    const coil = [xr + 3, xr + 5, xr + 7];
    const c1 = xr + 11;
    return (
      k.lineOnTop([-121.2, yy], [-118, yy], z, P) + rect(-118, xr, yy - 1.2, yy + 1.2, z) +
      k.lineOnTop([xr, yy], [xr + 2, yy], z, P) + coil.map((cx) => k.ring(cx, yy, 1, z, P, 12)).join("") +
      k.lineOnTop([xr + 8, yy], [c1, yy], z, P) + rect(c1, c1 + 0.6, yy - 1.8, yy + 1.8, z) + rect(c1 + 1.6, c1 + 2.2, yy - 1.8, yy + 1.8, z) +
      k.lineOnTop([c1 + 2.2, yy], [PUP.x + PUP.w - 0.6, yy], z, P)
    );
  };
  out.push(L(bus, { tone: "hi" }));
  out.push(L(row(ROWS[0], 5), { tone: "lit" }));
  out.push(L(row(ROWS[1], 12), { tone: "hi" }));
  return out.join("");
}

function cables() {
  const routes = ROWS.map((yy, n) => [[PUP.x + PUP.w, yy, 4], [PUP.x + PUP.w + 4, yy, 0.4], [SOCKETS[n], yy, 0.4], [SOCKETS[n], FRONT + 1, 0.4], [SOCKETS[n], FRONT, 7]]);
  return routes.map((r, n) => L(poly(r), { tone: n ? "hi" : "lit" }) + D([at(r[0]), at(r[r.length - 1])], { size: 0.8, tone: "hi" })).join("");
}

// Aiguille du bouton (même tracé que seg() du script).
function pointer([x, y], z, a, r0, r1) {
  const p = at([x - Math.sin(a) * r0, y + Math.cos(a) * r0, z]);
  const q = at([x + Math.sin(a) * r1, y - Math.cos(a) * r1, z]);
  return "M" + p[0].toFixed(2) + " " + p[1].toFixed(2) + "L" + q[0].toFixed(2) + " " + q[1].toFixed(2);
}
const knobAngle = (f) => -KNOB_SPAN / 2 + (KNOB_SPAN * (f - F_LO)) / (F_HI - F_LO);

const body = [
  plate(),
  bed(),
  rail(RAILS[0]),
  paper(),
  `<path class="iso-line" data-tone="mid" d="${curve(R2)}" style="stroke-width:1.2"/>`,
  `<path class="iso-line" data-tone="lit" d="${curve(R1)}" style="stroke-width:1.3"/>`,
  rail(RAILS[1]),
  `<g data-part="gantry">${gantry()}</g>`,
  cables(),
  desk(),
  `<path data-part="knob" class="iso-line" data-tone="hi" d="${pointer(KNOB, PUP_H + 3.2, knobAngle(FS), 0, KNOB_R - 0.8)}" style="stroke-width:1.1"/>`,
];

const svg = k
  .figureSvg({ width: WIDTH, height: HEIGHT, label: "", body })
  .replace(' role="img" aria-label=""', ' aria-hidden="true" focusable="false"');

// Projection linéaire : écran = o + x·ex + y·ey + z·ez (exacte en isométrie).
const o = at([0, 0, 0]);
const axis = (v) => at(v).map((c, i) => +(c - o[i]).toFixed(5));
const num = (v) => +v.toFixed(4);
const model = readFileSync(join(HERE, "model.mjs"), "utf8").replace(/^export /gm, "").replace(/^\/\/.*\n/gm, "");

const js = `// Généré par tools/figures/rlc_response/build.mjs : ne pas modifier à la main.
(() => {
${model}const O = ${JSON.stringify(o.map(num))}, EX = ${JSON.stringify(axis([1, 0, 0]))}, EY = ${JSON.stringify(axis([0, 1, 0]))};
const scr = (x, y, z) => [O[0] + x * EX[0] + y * EY[0] + z * ${axis([0, 0, 1])[0]}, O[1] + x * EX[1] + y * EY[1] + z * ${axis([0, 0, 1])[1]}];
const seg = (cx, cy, z, a, r1) => { const q = scr(cx + Math.sin(a) * r1, cy - Math.cos(a) * r1, z), p = scr(cx, cy, z); return "M" + p[0].toFixed(2) + " " + p[1].toFixed(2) + "L" + q[0].toFixed(2) + " " + q[1].toFixed(2); };
const move = (dx, dy) => "translate(" + (EX[0] * dx + EY[0] * dy).toFixed(3) + " " + (EX[1] * dx + EY[1] * dy).toFixed(3) + ")";
const FS = F0 / 2, SX = ${SX}, SY = ${SY}, KSPAN = ${num(KNOB_SPAN)};
const PRESETS = { low: FS, f0: F0, high: F0 * 2 };
document.querySelectorAll('.fig[data-fig="rlc_response"]').forEach((card) => {
  const q = (s) => card.querySelector(s), qa = (s) => card.querySelectorAll(s);
  const svg = q("svg"), gantry = q('[data-part="gantry"]'), knob = q('[data-part="knob"]'), pens = [...qa('[data-part="pen"]')];
  const range = q("[data-fig-freq]"), play = q("[data-fig-play]"), readout = q(".fig-readout"), out = {};
  qa("[data-fig-out]").forEach((el) => { out[el.dataset.figOut] = el; });
  const lang = document.documentElement.lang || "fr", still = matchMedia("(prefers-reduced-motion: reduce)");
  const fmt = (v, d) => new Intl.NumberFormat(lang, { maximumFractionDigits: d, minimumFractionDigits: d }).format(v);
  const sig = (v) => new Intl.NumberFormat(lang, { maximumSignificantDigits: 3, minimumSignificantDigits: 3 }).format(v);
  const hz = (v) => v >= 1000 ? fmt(v / 1000, 2) + " kHz" : fmt(v, 0) + " Hz";
  let f = FS, t = 0, last = 0, frame = 0, running = false, visible = true;
  function report() {
    range.value = Math.round(f / 50) * 50;
    range.setAttribute("aria-valuetext", hz(f));
    if (out.f) out.f.textContent = hz(f);
    if (out.i1) out.i1.textContent = sig(current(f, R1) * 1000) + " mA";
    if (out.i2) out.i2.textContent = sig(current(f, R2) * 1000) + " mA";
    gantry.setAttribute("transform", move(SX * (f - FS), 0));
    pens.forEach((g) => { const r = +g.dataset.r; g.setAttribute("transform", move(0, -SY * (current(f, r) - current(FS, r)))); });
    knob.setAttribute("d", seg(${KNOB[0]}, ${KNOB[1]}, ${PUP_H + 3.2}, -KSPAN / 2 + KSPAN * (f - F_LO) / (F_HI - F_LO), ${KNOB_R - 0.8}));
  }
  function tick(now) {
    if (last) t += Math.min(now - last, 100) / 1000;
    last = now;
    f = sweepF(t);
    report();
    frame = running && visible && !still.matches ? requestAnimationFrame(tick) : 0;
  }
  const run = () => { if (!frame && running && visible && !still.matches) { last = 0; frame = requestAnimationFrame(tick); } };
  function setPlaying(on) {
    running = on;
    play.setAttribute("aria-pressed", on ? "true" : "false");
    play.textContent = on ? play.dataset.pause : play.dataset.play;
    readout.setAttribute("aria-live", on ? "off" : "polite");
    if (on) { t = SWEEP_S * (Math.min(Math.max(f, F_LO), F_HI) - F_LO) / (F_HI - F_LO); run(); }
  }
  range.addEventListener("input", () => { setPlaying(false); f = +range.value; report(); });
  qa("[data-fig-preset]").forEach((b) => b.addEventListener("click", () => { setPlaying(false); f = PRESETS[b.dataset.figPreset]; report(); }));
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
const svgPath = OUT ? join(OUT, "rlc_response.svg") : join(ROOT, "templates", "figures", "rlc_response.svg");
const jsPath = OUT ? join(OUT, "rlc_response.js") : join(ROOT, "static", "acad", "js", "figures", "rlc_response.js");
write(svgPath, svg + "\n");
write(jsPath, js);
console.log(`wrote ${svgPath} (${Buffer.byteLength(svg)} o), ${jsPath} (${Buffer.byteLength(js)} o)`);
