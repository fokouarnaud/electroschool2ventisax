// Figure « déphasage » (section 06-dephasage de M6) : traceur à deux voies branché sur le passe-bas RC du cours.
// node tools/figures/rc_phase/build.mjs [--out <dossier>]
// écrit templates/figures/rc_phase.svg (dessin sans texte) et static/acad/js/figures/rc_phase.js (animation).
// Fichiers générés : ne jamais les retoucher à la main, modifier ce script puis le relancer.
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "../kit/iso-kit.mjs";
import { FC, ratio, lagDeg } from "./model.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(HERE, "../../..");
const outAt = process.argv.indexOf("--out");
const OUT = outAt > 0 ? resolve(process.argv[outAt + 1]) : null;

const WIDTH = 640;
const HEIGHT = 360;

// Plan (unités monde, z vers le haut ; x et y croissants vers l'observateur).
// Générateur (Ve, bouton de fréquence) → boîtier du filtre RC → traceur : voie 1 = Ve, voie 2 = Vs aux bornes de C.
// Le papier défile vers l'avant à une vitesse qui suit la fréquence : une période occupe toujours PERIOD unités,
// soit huit graduations de la réglette du châssis (45° par graduation).
const PLATE = { x: -150, y: -64, w: 272, d: 122, r: 8 };
const PLATE_H = 10;
const FOOT_H = 5;
const BODY = { x: -130, y: -46, w: 240, d: 84, r: 4 };
const BODY_H = 20;
const PAPER = { x: -100, y: -38, w: 180, d: 68, r: 0.5 };
const PAPER_Z = BODY_H + 0.6;
const SUPPLY = { x: -128, y: -44, w: 26, d: 80, r: 3 };
const TAKEUP = { x: 82, y: -44, w: 26, d: 80, r: 3 };
const HOUSING_H = 9;
const PEN_X = -84;
const PERIOD = 64;
const TRACE = 164; // longueur tracée, de la plume au carter avant
const CH = [-21, 13]; // axes des voies 1 et 2
const AMP = 13; // déviation pour une tension égale à Ve crête
const GAP = -4; // séparation des voies, porte l'accolade Δt
const BRIDGE = { x: PEN_X - 3, y: -45, w: 6, d: 82, r: 1 };
const BRIDGE_Z = 34;
const GEN = { x: -144, y: 40, w: 34, d: 15, r: 2 };
const GEN_H = 12;
const KNOB = [-127, 47.5];
const KNOB_R = 4.5;
const KNOB_SPAN = (270 * Math.PI) / 180; // 10 Hz à 100 kHz sur 270°
const FILTER = { x: -92, y: 42, w: 26, d: 11, r: 1.5 };
const FILTER_H = 7;
const SOCKETS = [-46, -26]; // entrées des voies 1 et 2, sur la face avant du châssis

const P = k.fitProjection(
  [...k.boxCorners(PLATE, -PLATE_H - FOOT_H, 0), [BRIDGE.x, BRIDGE.y, BRIDGE_Z + 3], [BRIDGE.x, BRIDGE.y + BRIDGE.d, BRIDGE_Z + 3]],
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

function body() {
  const out = [S(k.slabOf(BODY, 0, BODY_H, P, 6, 1), { tone: "mid" })];
  // Entrées des deux voies sur la face avant : douilles arrêtées par leur point de contact.
  for (const x of SOCKETS) {
    out.push(L(k.sideRing([x, BODY.y + BODY.d, 10], 2.2, "y", P, 16), { tone: "mid" }));
    out.push(L(k.sideRing([x, BODY.y + BODY.d, 10], 1, "y", P, 12), { tone: "lo" }));
  }
  // Réglette fixe du châssis devant le papier : une graduation par huitième de période (45°), une grande par période.
  const ticks = k.topTicks(PEN_X, PEN_X + TRACE - 4, PERIOD / 8, 8, PAPER.y + PAPER.d + 1.5, BODY_H, [2, 4], P);
  out.push(L(k.lineOnTop([PEN_X, PAPER.y + PAPER.d + 1.5], [TAKEUP.x, PAPER.y + PAPER.d + 1.5], BODY_H, P), { tone: "lo" }));
  out.push(L(ticks.minor, { tone: "lo" }), L(ticks.major, { tone: "hi" }));
  return out.join("");
}

function paper() {
  const out = [S(k.slabOf(PAPER, BODY_H, 0.6, P, 2), { tone: "lo", crease: "none" })];
  // Lignes imprimées le long du défilement (invariantes quand le papier avance) : axes des voies et séparation.
  out.push(L(CH.map((y) => k.lineOnTop([PAPER.x, y], [PAPER.x + PAPER.w, y], PAPER_Z, P)).join(""), { tone: "faint" }));
  out.push(L([CH[0] - AMP, CH[0] + AMP, CH[1] - AMP, CH[1] + AMP].map((y) => k.lineOnTop([PAPER.x, y], [PAPER.x + PAPER.w, y], PAPER_Z, P)).join(""), { tone: "faint" }));
  out.push(L(k.lineOnTop([PAPER.x, GAP], [PAPER.x + PAPER.w, GAP], PAPER_Z, P), { tone: "lo" }));
  return out.join("");
}

function holes() {
  // Perforations d'entraînement : elles avancent avec le papier (pièce mobile, décalée modulo leur pas).
  const xs = Array.from({ length: 21 }, (_, i) => PAPER.x + 6 + i * 8);
  return D(xs.flatMap((x) => [at([x, PAPER.y + 3, PAPER_Z]), at([x, PAPER.y + PAPER.d - 3, PAPER_Z])]), { size: 0.7, tone: "mid" });
}

function housing(plan) {
  const out = [S(k.slabOf(plan, BODY_H, HOUSING_H, P, 4, 0.8), { tone: "mid" })];
  out.push(L(k.planOutline(k.insetPlan(plan, 3), BODY_H + HOUSING_H, P), { tone: "faint" }));
  out.push(D(k.corners(plan, 2.4).map(([x, y]) => at([x, y, BODY_H + HOUSING_H])), { size: 0.45 }));
  return out.join("");
}

function bridge() {
  const out = [];
  for (const y of [BRIDGE.y + 1, BRIDGE.y + BRIDGE.d - 5]) {
    out.push(S(k.slabOf({ x: BRIDGE.x + 1, y, w: 4, d: 4, r: 0.5 }, BODY_H, BRIDGE_Z - BODY_H, P, 2), { tone: "mid" }));
  }
  out.push(S(k.slabOf(BRIDGE, BRIDGE_Z, 3, P, 2, 0.4), { tone: "hi" }));
  // Rainure de guidage des chariots, arrêtée par deux butées.
  out.push(L(k.lineOnTop([BRIDGE.x + 3, BRIDGE.y + 6], [BRIDGE.x + 3, BRIDGE.y + BRIDGE.d - 6], BRIDGE_Z + 3, P), { tone: "lo" }));
  out.push(D([at([BRIDGE.x + 3, BRIDGE.y + 6, BRIDGE_Z + 3]), at([BRIDGE.x + 3, BRIDGE.y + BRIDGE.d - 6, BRIDGE_Z + 3])], { size: 0.6, tone: "hi" }));
  return out.join("");
}

function pen(y, lit) {
  // Chariot pendu sous le pont et sa plume posée sur le papier ; le script le déplace le long du pont.
  return (
    S(k.cylinder(PEN_X, y, 0.9, PAPER_Z, 7, P, 8), { tone: "hi", crease: "none", lit }) +
    S(k.slabOf({ x: PEN_X - 2.5, y: y - 2.5, w: 5, d: 5, r: 0.8 }, PAPER_Z + 7, BRIDGE_Z - PAPER_Z - 7, P, 2), { tone: "hi", crease: "lo", lit })
  );
}

function generator() {
  const out = [S(k.slabOf(GEN, 0, GEN_H, P, 4, 0.8), { tone: "mid" })];
  out.push(L(k.planOutline(k.insetPlan(GEN, 2.5), GEN_H, P), { tone: "faint" }));
  const [x, y] = KNOB;
  const ticks = k.radialTicks(x, y, KNOB_R + 3, 12, 3, GEN_H, [1, 2], P, -KNOB_SPAN / 2, KNOB_SPAN);
  out.push(L(k.ring(x, y, KNOB_R + 3, GEN_H, P, 24), { tone: "faint" }));
  out.push(L(ticks.minor, { tone: "lo" }), L(ticks.major, { tone: "mid" }));
  out.push(S(k.cylinder(x, y, KNOB_R, GEN_H, 3.5, P, 20), { tone: "hi", crease: "lo" }));
  out.push(L(k.knurl(x, y, KNOB_R, GEN_H, GEN_H + 3.5, 24, P), { tone: "lo" }));
  out.push(D([at([GEN.x + GEN.w - 5, GEN.y + 4, GEN_H]), at([GEN.x + GEN.w - 5, GEN.y + GEN.d - 4, GEN_H])], { size: 0.8, tone: "hi" }));
  return out.join("");
}

function filter() {
  // Boîtier du filtre : résistance en série (rectangle) puis condensateur vers la masse (deux plaques), gravés sur le capot.
  const out = [S(k.slabOf(FILTER, 0, FILTER_H, P, 3, 0.5), { tone: "mid" })];
  const z = FILTER_H;
  const y = FILTER.y + FILTER.d / 2;
  const x0 = FILTER.x + 3;
  // Chaque trait part d'un bord du capot ou finit sur un symbole fermé (aucun bout dans le vide).
  out.push(L(
    k.lineOnTop([FILTER.x + 0.6, y], [x0 + 4, y], z, P) + k.planOutline({ x: x0 + 4, y: y - 1.5, w: 7, d: 3, r: 0 }, z, P, 1) +
    k.lineOnTop([x0 + 11, y], [x0 + 16.6, y], z, P) +
    k.planOutline({ x: x0 + 16.6, y: y - 2.5, w: 0.8, d: 5, r: 0 }, z, P, 1) + k.planOutline({ x: x0 + 18.4, y: y - 2.5, w: 0.8, d: 5, r: 0 }, z, P, 1) +
    k.lineOnTop([x0 + 19.2, y], [FILTER.x + FILTER.w - 0.6, y], z, P),
    { tone: "hi" },
  ));
  out.push(D([at([x0 + 14, y, z])], { size: 0.6, tone: "hi" }));
  return out.join("");
}

function cables() {
  // Câbles posés sur le socle : générateur → filtre, générateur → voie 1 (Ve), filtre → voie 2 (Vs).
  const front = BODY.y + BODY.d;
  const routes = [
    [[GEN.x + GEN.w, 47.5, 4], [FILTER.x, 47.5, 3]],
    [[GEN.x + GEN.w - 4, GEN.y, 5], [GEN.x + GEN.w - 4, 39.5, 0.4], [SOCKETS[0], 39.5, 0.4], [SOCKETS[0], front, 8]],
    [[FILTER.x + FILTER.w, 47.5, 3], [FILTER.x + FILTER.w + 4, 47.5, 0.4], [SOCKETS[1], 47.5, 0.4], [SOCKETS[1], front + 2, 0.4], [SOCKETS[1], front, 8]],
  ];
  return routes.map((r) => L(poly(r), { tone: "hi" }) + D([at(r[0]), at(r[r.length - 1])], { size: 0.8, tone: "hi" })).join("");
}

// Tracés, chariots et accolade à une fréquence et une phase données (mêmes formules que le script).
const deviation = (amp, phase, u, lag) => amp * Math.sin(phase - (2 * Math.PI * u) / PERIOD - lag);
function trace(ch, amp, phase, lag) {
  const points = [];
  for (let u = 0; u <= TRACE; u += 2) points.push([PEN_X + u, CH[ch] - AMP * deviation(amp, phase, u, lag), PAPER_Z]);
  return poly(points);
}
function bracket(phase, lag) {
  const lagU = (PERIOD * lag) / (2 * Math.PI);
  const turn = (((phase - Math.PI / 2) / (2 * Math.PI)) % 1 + 1) % 1;
  let ue = PERIOD * turn;
  while (ue < lagU) ue += PERIOD;
  const xe = PEN_X + ue, xs = PEN_X + ue - lagU;
  return poly([[xe, GAP - 2, PAPER_Z], [xe, GAP + 2, PAPER_Z]]) + poly([[xe, GAP, PAPER_Z], [xs, GAP, PAPER_Z]]) + poly([[xs, GAP - 2, PAPER_Z], [xs, GAP + 2, PAPER_Z]]);
}

// Sans JavaScript : figé au repère « fc / 10 », Ve à sa crête sous la plume.
const F0 = FC / 10;
const PHASE0 = Math.PI / 2;
const LAG0 = (lagDeg(F0) * Math.PI) / 180;

const body_ = [
  plate(),
  body(),
  paper(),
  `<g data-part="holes">${holes()}</g>`,
  `<path data-part="trace-1" class="iso-line" data-tone="hi" d="${trace(0, 1, PHASE0, 0)}" style="stroke-width:1.1"/>`,
  `<path data-part="trace-2" class="iso-line" data-tone="lit" d="${trace(1, ratio(F0), PHASE0, LAG0)}" style="stroke-width:1.3"/>`,
  `<path data-part="bracket" class="iso-line" data-tone="lit" d="${bracket(PHASE0, LAG0)}" style="stroke-width:1.4"/>`,
  housing(SUPPLY),
  bridge(),
  `<g data-part="pen" data-ch="1">${pen(CH[0], false)}</g>`,
  `<g data-part="pen" data-ch="2">${pen(CH[1], true)}</g>`,
  housing(TAKEUP),
  cables(),
  generator(),
  `<path data-part="knob" class="iso-line" data-tone="hi" data-free="start" d="" style="stroke-width:1.1"/>`,
  filter(),
];

const svg = k
  .figureSvg({ width: WIDTH, height: HEIGHT, label: "", body: body_ })
  .replace(' role="img" aria-label=""', ' aria-hidden="true" focusable="false"');

// Projection linéaire : écran = o + x·ex + y·ey + z·ez (exacte en isométrie).
const o = at([0, 0, 0]);
const axis = (v) => at(v).map((c, i) => +(c - o[i]).toFixed(5));
const num = (v) => +v.toFixed(4);
const model = readFileSync(join(HERE, "model.mjs"), "utf8").replace(/^export /gm, "").replace(/^\/\/.*\n/gm, "");

const js = `// Généré par tools/figures/rc_phase/build.mjs : ne pas modifier à la main.
(() => {
${model}const O = ${JSON.stringify(o.map(num))}, EX = ${JSON.stringify(axis([1, 0, 0]))}, EY = ${JSON.stringify(axis([0, 1, 0]))}, EZ = ${JSON.stringify(axis([0, 0, 1]))};
const scr = (x, y, z) => [O[0] + x * EX[0] + y * EY[0] + z * EZ[0], O[1] + x * EX[1] + y * EY[1] + z * EZ[1]];
const pth = (pts) => pts.map((p, i) => { const s = scr(p[0], p[1], p[2]); return (i ? "L" : "M") + s[0].toFixed(2) + " " + s[1].toFixed(2); }).join("");
const seg = (cx, cy, z, a, r0, r1) => { const p = scr(cx - Math.sin(a) * r0, cy + Math.cos(a) * r0, z), q = scr(cx + Math.sin(a) * r1, cy - Math.cos(a) * r1, z); return "M" + p[0].toFixed(2) + " " + p[1].toFixed(2) + "L" + q[0].toFixed(2) + " " + q[1].toFixed(2); };
const move = (dx, dy) => "translate(" + (EX[0] * dx + EY[0] * dy).toFixed(3) + " " + (EX[1] * dx + EY[1] * dy).toFixed(3) + ")";
const PRESETS = { low: FC / 10, fc: FC, x577: 1 / (2 * Math.PI * 577 * C), high: FC * 10 };
const KSPAN = ${num(KNOB_SPAN)}, PEN_X = ${PEN_X}, PERIOD = ${PERIOD}, TRACE = ${TRACE}, CH = ${JSON.stringify(CH)}, AMP = ${AMP}, GAP = ${GAP}, Z = ${PAPER_Z};
const toF = (v) => F_MIN * 10 ** (v / 100), toV = (f) => Math.round(100 * Math.log10(f / F_MIN));
document.querySelectorAll('.fig[data-fig="rc_phase"]').forEach((card) => {
  const q = (s) => card.querySelector(s), qa = (s) => card.querySelectorAll(s);
  const svg = q("svg"), t1 = q('[data-part="trace-1"]'), t2 = q('[data-part="trace-2"]'), br = q('[data-part="bracket"]'), holes = q('[data-part="holes"]'), knob = q('[data-part="knob"]');
  const pens = [q('[data-part="pen"][data-ch="1"]'), q('[data-part="pen"][data-ch="2"]')], range = q("[data-fig-freq]"), play = q("[data-fig-play]"), out = {};
  qa("[data-fig-out]").forEach((el) => { out[el.dataset.figOut] = el; });
  const lang = document.documentElement.lang || "fr", still = matchMedia("(prefers-reduced-motion: reduce)");
  const fmt = (v, d) => new Intl.NumberFormat(lang, { maximumFractionDigits: d, minimumFractionDigits: d }).format(v);
  const sig = (v, sign) => new Intl.NumberFormat(lang, { maximumSignificantDigits: 3, minimumSignificantDigits: 3, signDisplay: sign || "auto" }).format(v);
  const qty = (v, u) => v >= 1000 ? fmt(v / 1000, v >= 1e4 ? 1 : 2) + " k" + u : fmt(v, v >= 100 ? 0 : 1) + " " + u;
  let f = PRESETS.low, phase = Math.PI / 2, last = 0, frame = 0, running = false, visible = true;
  function pose() {
    const lag = lagDeg(f) * Math.PI / 180, amp = [1, ratio(f)], lags = [0, lag];
    [t1, t2].forEach((t, c) => {
      const pts = [];
      for (let u = 0; u <= TRACE; u += 2) pts.push([PEN_X + u, CH[c] - AMP * amp[c] * Math.sin(phase - 2 * Math.PI * u / PERIOD - lags[c]), Z]);
      t.setAttribute("d", pth(pts));
      pens[c].setAttribute("transform", move(0, -AMP * amp[c] * Math.sin(phase - lags[c])));
    });
    const lagU = PERIOD * lag / (2 * Math.PI), turn = (((phase - Math.PI / 2) / (2 * Math.PI)) % 1 + 1) % 1;
    let ue = PERIOD * turn;
    while (ue < lagU) ue += PERIOD;
    const xe = PEN_X + ue, xs = xe - lagU;
    br.setAttribute("d", pth([[xe, GAP - 2, Z], [xe, GAP + 2, Z]]) + pth([[xe, GAP, Z], [xs, GAP, Z]]) + pth([[xs, GAP - 2, Z], [xs, GAP + 2, Z]]));
    holes.setAttribute("transform", move(8 * ((((phase - Math.PI / 2) / (2 * Math.PI)) * PERIOD / 8) % 1 + 1) % 8, 0));
    knob.setAttribute("d", seg(${KNOB[0]}, ${KNOB[1]}, ${GEN_H + 3.7}, -KSPAN / 2 + KSPAN * Math.log10(f / F_MIN) / 4, 0, ${KNOB_R - 1}));
  }
  function report() {
    const text = qty(f, "Hz");
    range.value = toV(f);
    range.setAttribute("aria-valuetext", text);
    if (out.f) out.f.textContent = text;
    if (out.xc) out.xc.textContent = qty(xc(f), "Ω");
    if (out.lead) out.lead.textContent = sig(leadDeg(f), "always") + "°";
    if (out.shift) out.shift.textContent = sig(shift(f));
    if (out.lag) out.lag.textContent = sig(lagDeg(f)) + "°";
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
const svgPath = OUT ? join(OUT, "rc_phase.svg") : join(ROOT, "templates", "figures", "rc_phase.svg");
const jsPath = OUT ? join(OUT, "rc_phase.js") : join(ROOT, "static", "acad", "js", "figures", "rc_phase.js");
write(svgPath, svg + "\n");
write(jsPath, js);
console.log(`wrote ${svgPath} (${Buffer.byteLength(svg)} o), ${jsPath} (${Buffer.byteLength(js)} o)`);
