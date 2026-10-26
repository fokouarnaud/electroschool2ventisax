// Figure « rôle de l'amplificateur et gain » (section 01-role-gain de M8) : micro → amplificateur alimenté → haut-parleur.
// node tools/figures/amp_gain/build.mjs [--out <dossier>]
// écrit templates/figures/amp_gain.svg (dessin sans texte) et static/acad/js/figures/amp_gain.js (animation).
// Fichiers générés : ne jamais les retoucher à la main, modifier ce script puis le relancer.
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "../kit/iso-kit.mjs";
import { VE, ve, vs } from "./model.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(HERE, "../../..");
const outAt = process.argv.indexOf("--out");
const OUT = outAt > 0 ? resolve(process.argv[outAt + 1]) : null;

const WIDTH = 640;
const HEIGHT = 360;

// Plan (unités monde, z vers le haut ; x et y croissants vers l'observateur).
// À gauche le micro (membrane = ve), au centre l'amplificateur et sa batterie, à droite le haut-parleur (membrane teal = vs).
// Les deux membranes ont la même échelle de déplacement (KZ unités par volt) : celle du micro bouge quarante fois moins.
// Sur le capot de l'amplificateur, deux galvanomètres dont les échelles sont dans le rapport 40 (±60 mV et ±2,4 V)
// et le bouton de gain (−40 à +40).
const PLATE = { x: -128, y: -70, w: 240, d: 112, r: 8 };
const PLATE_H = 10;
const FOOT_H = 5;
const KZ = 4; // unités de déplacement par volt, pour les deux membranes
const MIC = [-108, 8];
const MIC_TOP = 34;
const AMP = { x: -84, y: -26, w: 78, d: 50, r: 3 };
const AMP_H = 16;
const METERS = [[-66, -8, 0.06], [-30, -8, 2.4]]; // galvanomètre d'entrée (±60 mV) et de sortie (±2,4 V)
const DIAL_R = 10;
const SPAN = (100 * Math.PI) / 180; // pleine échelle → ±100°
const KNOB = [-20, 12];
const KNOB_R = 5;
const KSPAN = (135 * Math.PI) / 180; // Av = ±40 → ±135°
const BAT = { x: -76, y: -62, w: 60, d: 20, r: 2 };
const BAT_H = 12;
const SPK = { x: 22, y: -28, w: 56, d: 56, r: 3 };
const SPK_H = 26;
const CONE = [50, 0];
const PLEATS = 3;
const PLEAT_H = 3;
const CONE_Z = SPK_H + PLEATS * PLEAT_H; // dessous de la membrane au repos

const P = k.fitProjection(
  [...k.boxCorners(PLATE, -PLATE_H - FOOT_H, 0), [CONE[0], CONE[1], CONE_Z + 14], [MIC[0], MIC[1], MIC_TOP + 4]],
  WIDTH,
  HEIGHT,
  { pad: 18, azimuth: 40 },
);

const at = (point) => k.iso(point, P);
const S = (paths, style) => k.solidSvg(paths, style);
const L = (d, style) => k.lineSvg(d, style);
const D = (points, style) => k.dotsSvg(points, style);
const depth = (x, y, z = 0) => k.depthOf([x, y, z], P);
const poly = (points) => k.pathOf(points.map(at));

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

function battery() {
  // Batterie : boîtier et deux bornes ; deux câbles l'amènent à l'arrière de l'amplificateur.
  const out = [S(k.slabOf(BAT, 0, BAT_H, P, 3, 0.6), { tone: "mid" })];
  out.push(L(k.planOutline(k.insetPlan(BAT, 3), BAT_H, P), { tone: "faint" }));
  for (const x of [BAT.x + 14, BAT.x + BAT.w - 14]) {
    out.push(S(k.cylinder(x, BAT.y + BAT.d / 2, 2.4, BAT_H, 3, P, 10), { tone: "hi", crease: "lo" }));
  }
  return out.join("");
}

function supplyCables() {
  // Chaque câble aboutit au bord d'une douille gravée sur le capot (anneau de 1,2 de rayon).
  const routes = [BAT.x + 14, BAT.x + BAT.w - 14].map((x) => [[x, BAT.y + BAT.d / 2, BAT_H + 3], [x, BAT.y + BAT.d + 3, BAT_H + 3], [x, AMP.y + 3, AMP_H]]);
  return routes.map((r) => {
    const [x] = r[0];
    return L(poly(r), { tone: "hi" }) + L(k.ring(x, AMP.y + 4.2, 1.2, AMP_H, P, 10), { tone: "hi" }) + D([at(r[0])], { size: 0.8, tone: "hi" });
  }).join("");
}

function mic() {
  const [x, y] = MIC;
  return (
    S(k.cylinder(x, y, 8, 0, 2, P, 14, 0.4), { tone: "mid" }) +
    S(k.cylinder(x, y, 1.6, 2, MIC_TOP - 10 - 2, P, 8), { tone: "hi", crease: "none" }) +
    S(k.cylinder(x, y, 5.5, MIC_TOP - 10, 9, P, 14), { tone: "mid" }) +
    L(k.ring(x, y, 5.5, MIC_TOP - 1, P, 14), { tone: "lo" })
  );
}
const micMembrane = () => S(k.cylinder(MIC[0], MIC[1], 4.6, MIC_TOP - 1, 1, P, 14), { tone: "hi", crease: "none" });

function amplifier() {
  const out = [S(k.slabOf(AMP, 0, AMP_H, P, 4, 0.8), { tone: "mid" })];
  const z = AMP_H;
  // Triangle de l'amplificateur gravé sur le capot, pointe vers la sortie.
  out.push(L(poly([[-76, 6, z], [-76, 20, z], [-52, 13, z], [-76, 6, z]]), { tone: "hi" }));
  out.push(L(k.lineOnTop([AMP.x, 13], [-76, 13], z, P) + k.lineOnTop([-52, 13], [-42, 13], z, P), { tone: "hi" }));
  out.push(D([at([-42, 13, z])], { size: 0.6, tone: "hi" }));
  for (const [x, y] of METERS) {
    out.push(S(k.cylinder(x, y, DIAL_R, z, 2.5, P, 18, 0.5), { tone: "hi", crease: "lo" }));
    out.push(L(k.ring(x, y, DIAL_R - 2, z + 2.5, P, 24), { tone: "lo" }));
    const ticks = k.radialTicks(x, y, DIAL_R - 2, 8, 4, z + 2.5, [1.2, 2.2], P, -SPAN, SPAN * 2);
    out.push(L(ticks.minor, { tone: "lo" }), L(ticks.major, { tone: "mid" }));
    out.push(L(k.ring(x, y, 1.2, z + 2.5, P, 10), { tone: "mid" }));
  }
  const [kx, ky] = KNOB;
  out.push(L(k.ring(kx, ky, KNOB_R + 2.6, z, P, 18), { tone: "faint" }));
  const kt = k.radialTicks(kx, ky, KNOB_R + 2.6, 8, 4, z, [1, 1.8], P, -KSPAN, KSPAN * 2);
  out.push(L(kt.minor, { tone: "lo" }), L(kt.major, { tone: "mid" }));
  out.push(S(k.cylinder(kx, ky, KNOB_R, z, 3, P, 16), { tone: "hi", crease: "lo" }));
  out.push(L(k.knurl(kx, ky, KNOB_R, z, z + 3, 16, P), { tone: "lo" }));
  return out.join("");
}

function signalCables() {
  // Micro → entrée de l'amplificateur ; sortie → haut-parleur.
  const routes = [
    [[MIC[0] + 8, MIC[1], 1], [MIC[0] + 12, MIC[1], 0.4], [AMP.x - 3, MIC[1], 0.4], [AMP.x, MIC[1], 6]],
    [[AMP.x + AMP.w, 13, 6], [SPK.x, 13, 6]],
  ];
  return routes.map((r) => L(poly(r), { tone: "hi" }) + D([at(r[0]), at(r[r.length - 1])], { size: 0.8, tone: "hi" })).join("");
}

function cabinet() {
  const out = [S(k.slabOf(SPK, 0, SPK_H, P, 4, 0.8), { tone: "mid" })];
  out.push(L(k.ring(CONE[0], CONE[1], 23, SPK_H, P, 24), { tone: "lo" }));
  return out.join("");
}
const pleat = (n) => S(k.cylinder(CONE[0], CONE[1], n % 2 ? 19 : 20.5, SPK_H + n * PLEAT_H, PLEAT_H, P, 20), { tone: "hi", crease: "none" });
const cone = () =>
  S(k.cylinder(CONE[0], CONE[1], 20, CONE_Z, 1.6, P, 20, 0.4), { tone: "hi", crease: "lo", lit: true }) +
  L(k.ring(CONE[0], CONE[1], 13, CONE_Z + 1.6, P, 20), { tone: "lo" }) +
  S(k.cylinder(CONE[0], CONE[1], 6, CONE_Z + 1.6, 2.5, P, 14), { tone: "hi", crease: "lo" });

// Aiguilles (même tracé que seg() du script).
function pointer([x, y], z, a, r0, r1) {
  const p = at([x - Math.sin(a) * r0, y + Math.cos(a) * r0, z]);
  const q = at([x + Math.sin(a) * r1, y - Math.cos(a) * r1, z]);
  return "M" + p[0].toFixed(2) + " " + p[1].toFixed(2) + "L" + q[0].toFixed(2) + " " + q[1].toFixed(2);
}
// Sans JavaScript : Av = 40, entrée à sa crête (+50 mV), sortie à +2 V.
const A0 = 40;
const PH0 = Math.PI / 2;
const up = (dz) => { const o = at([0, 0, 0]), e = at([0, 0, dz]); return `translate(${(e[0] - o[0]).toFixed(3)} ${(e[1] - o[1]).toFixed(3)})`; };

const body = [
  plate(),
  battery(),
  mic(),
  `<g data-part="mic" transform="${up(KZ * ve(PH0))}">${micMembrane()}</g>`,
  signalCables(),
  amplifier(),
  supplyCables(),
  ...METERS.map(([x, y, fs], n) => `<path data-part="meter" data-n="${n}" class="iso-line" data-tone="hi" data-free="end" d="${pointer([x, y], AMP_H + 2.7, (SPAN * (n ? vs(PH0, A0) : ve(PH0))) / fs, 1.2, DIAL_R - 3)}" style="stroke-width:1.2"/>`),
  `<path data-part="knob" class="iso-line" data-tone="hi" d="${pointer(KNOB, AMP_H + 3.2, (KSPAN * A0) / 40, 0, KNOB_R - 1)}" style="stroke-width:1.1"/>`,
  cabinet(),
  ...Array.from({ length: PLEATS }, (_, n) => `<g data-part="pleat" data-step="${n + 1}" transform="${up((KZ * vs(PH0, A0) * (n + 1)) / PLEATS)}">${pleat(n)}</g>`),
  `<g data-part="pleat" data-step="${PLEATS}" transform="${up(KZ * vs(PH0, A0))}">${cone()}</g>`,
];

const svg = k
  .figureSvg({ width: WIDTH, height: HEIGHT, label: "", body })
  .replace(' role="img" aria-label=""', ' aria-hidden="true" focusable="false"');

// Projection linéaire : écran = o + x·ex + y·ey + z·ez (exacte en isométrie).
const o = at([0, 0, 0]);
const axis = (v) => at(v).map((c, i) => +(c - o[i]).toFixed(5));
const num = (v) => +v.toFixed(4);
const model = readFileSync(join(HERE, "model.mjs"), "utf8").replace(/^export /gm, "").replace(/^\/\/.*\n/gm, "");

const js = `// Généré par tools/figures/amp_gain/build.mjs : ne pas modifier à la main.
(() => {
${model}const O = ${JSON.stringify(o.map(num))}, EX = ${JSON.stringify(axis([1, 0, 0]))}, EY = ${JSON.stringify(axis([0, 1, 0]))}, EZ = ${JSON.stringify(axis([0, 0, 1]))};
const scr = (x, y, z) => [O[0] + x * EX[0] + y * EY[0] + z * EZ[0], O[1] + x * EX[1] + y * EY[1] + z * EZ[1]];
const seg = (cx, cy, z, a, r0, r1) => { const p = scr(cx - Math.sin(a) * r0, cy + Math.cos(a) * r0, z), q = scr(cx + Math.sin(a) * r1, cy - Math.cos(a) * r1, z); return "M" + p[0].toFixed(2) + " " + p[1].toFixed(2) + "L" + q[0].toFixed(2) + " " + q[1].toFixed(2); };
const up = (dz) => "translate(" + (EZ[0] * dz).toFixed(3) + " " + (EZ[1] * dz).toFixed(3) + ")";
const KZ = ${KZ}, SPAN = ${num(SPAN)}, KSPAN = ${num(KSPAN)}, METERS = ${JSON.stringify(METERS)}, PLEATS = ${PLEATS};
const PRESETS = { a40: 40, am39: -39 };
document.querySelectorAll('.fig[data-fig="amp_gain"]').forEach((card) => {
  const q = (s) => card.querySelector(s), qa = (s) => card.querySelectorAll(s);
  const svg = q("svg"), mic = q('[data-part="mic"]'), knob = q('[data-part="knob"]'), meters = [...qa('[data-part="meter"]')], pleats = [...qa('[data-part="pleat"]')];
  const range = q("[data-fig-gain]"), play = q("[data-fig-play]"), out = {};
  qa("[data-fig-out]").forEach((el) => { out[el.dataset.figOut] = el; });
  const lang = document.documentElement.lang || "fr", still = matchMedia("(prefers-reduced-motion: reduce)");
  const nf = (v, d, sign) => new Intl.NumberFormat(lang, { maximumFractionDigits: d, minimumFractionDigits: d, signDisplay: sign || "auto" }).format(v);
  let a = 40, phase = Math.PI / 2, last = 0, frame = 0, running = false, visible = true;
  function pose() {
    const vi = ve(phase), vo = vs(phase, a);
    mic.setAttribute("transform", up(KZ * vi));
    pleats.forEach((g) => g.setAttribute("transform", up(KZ * vo * g.dataset.step / PLEATS)));
    meters.forEach((m) => { const n = +m.dataset.n, [x, y, fs] = METERS[n]; m.setAttribute("d", seg(x, y, ${AMP_H + 2.7}, SPAN * (n ? vo : vi) / fs, 1.2, ${DIAL_R - 3})); });
    knob.setAttribute("d", seg(${KNOB[0]}, ${KNOB[1]}, ${AMP_H + 3.2}, KSPAN * a / 40, 0, ${KNOB_R - 1}));
  }
  function report() {
    range.value = a;
    range.setAttribute("aria-valuetext", nf(a, 0, "exceptZero"));
    if (out.a) out.a.textContent = nf(a, 0, "exceptZero");
    if (out.ve) out.ve.textContent = nf(VE * 1000, 1) + " mV";
    if (out.vs) out.vs.textContent = nf(peakOut(a), 2) + " V";
    if (out.ph) out.ph.textContent = inverted(a) ? out.ph.dataset.inverted : out.ph.dataset.inPhase;
    pose();
  }
  function tick(now) {
    if (last) phase += 2 * Math.PI * Math.min(now - last, 100) / 1000 / PERIOD_S;
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
  range.addEventListener("input", () => { a = +range.value; report(); setPlaying(true); });
  qa("[data-fig-preset]").forEach((b) => b.addEventListener("click", () => { a = PRESETS[b.dataset.figPreset]; report(); setPlaying(true); }));
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
const svgPath = OUT ? join(OUT, "amp_gain.svg") : join(ROOT, "templates", "figures", "amp_gain.svg");
const jsPath = OUT ? join(OUT, "amp_gain.js") : join(ROOT, "static", "acad", "js", "figures", "amp_gain.js");
write(svgPath, svg + "\n");
write(jsPath, js);
console.log(`wrote ${svgPath} (${Buffer.byteLength(svg)} o), ${jsPath} (${Buffer.byteLength(js)} o)`);
