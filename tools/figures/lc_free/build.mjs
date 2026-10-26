// Figure « oscillation libre d'un LC » (section 06-oscillateurs de M7) : la balançoire de la section, réglée sur un LC réel.
// node tools/figures/lc_free/build.mjs [--out <dossier>]
// écrit templates/figures/lc_free.svg (dessin sans texte) et static/acad/js/figures/lc_free.js (animation).
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

// Plan (unités monde, z vers le haut ; x et y croissants vers l'observateur).
// Portique de balançoire : deux montants et une poutre ; le siège pend à deux cordes et oscille d'avant en arrière (le long de y).
// L'angle des cordes suit la tension du condensateur (θ = 35° pour Vc = 1 V) : hauteur du siège = énergie du condensateur,
// vitesse du siège = courant, donc énergie de la bobine. Devant à droite, un pupitre montre les deux énergies en barres.
const PLATE = { x: -80, y: -42, w: 198, d: 100, r: 8 };
const PLATE_H = 10;
const FOOT_H = 5;
const POST_X = 50;
const TOP = 72;
const ROPE = 50;
const ROPE_X = 16;
const SEAT = { w: 36, d: 10, h: 2.5 };
const THMAX = (35 * Math.PI) / 180; // angle des cordes pour Vc = 1 V
const PANEL = { x: 64, y: 16, w: 46, d: 34, r: 2 };
const PANEL_H = 6;
const BAR_X0 = PANEL.x + 5;
const BAR_LEN = 36;
const BARS = [PANEL.y + 11, PANEL.y + 23]; // énergie du condensateur, puis de la bobine

const P = k.fitProjection(
  [...k.boxCorners(PLATE, -PLATE_H - FOOT_H, 0), [0, 0, TOP + 6], [-POST_X - 4, 0, TOP + 4], [POST_X + 4, 0, TOP + 4]],
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

function post(x) {
  // Montant : patin au sol, poteau, deux jambes de force arrêtées sur le patin et sur le poteau.
  const out = [S(k.slabOf({ x: x - 3, y: -30, w: 6, d: 60, r: 1 }, 0, 3, P, 2, 0.4), { tone: "mid" })];
  out.push(L(poly([[x, -24, 3], [x, -1.5, 30]]) + poly([[x, 24, 3], [x, 1.5, 30]]), { tone: "mid" }));
  out.push(D([at([x, -24, 3]), at([x, 24, 3])], { size: 0.8, tone: "hi" }));
  out.push(S(k.slabOf({ x: x - 2, y: -2, w: 4, d: 4, r: 0.5 }, 3, TOP - 3, P, 2), { tone: "hi", crease: "lo" }));
  return out.join("");
}

function beam() {
  const out = [S(k.slabOf({ x: -POST_X - 4, y: -2.5, w: 2 * POST_X + 8, d: 5, r: 1 }, TOP, 4, P, 2, 0.5), { tone: "hi", crease: "lo" })];
  // Crochets des cordes, sous la poutre.
  out.push(S(k.cylinder(-ROPE_X, 0, 1.4, TOP - 1.5, 1.5, P, 8), { tone: "mid", crease: "none" }));
  out.push(S(k.cylinder(ROPE_X, 0, 1.4, TOP - 1.5, 1.5, P, 8), { tone: "mid", crease: "none" }));
  return out.join("");
}

// Position du siège pour un angle de cordes θ : le siège reste horizontal, ses coins hauts accrochés aux cordes.
const seatAt = (th) => [ROPE * Math.sin(th), TOP - 1.5 - ROPE * Math.cos(th)];
function seat(th) {
  const [y, z] = seatAt(th);
  return S(k.slabOf({ x: -SEAT.w / 2, y: y - SEAT.d / 2, w: SEAT.w, d: SEAT.d, r: 1 }, z - SEAT.h, SEAT.h, P, 2, 0.4), { tone: "hi", crease: "lo", lit: true });
}
function ropes(th) {
  const [y, z] = seatAt(th);
  return poly([[-ROPE_X, 0, TOP - 1.5], [-ROPE_X, y, z]]) + poly([[ROPE_X, 0, TOP - 1.5], [ROPE_X, y, z]]);
}

function panel() {
  // Pupitre des énergies : deux gorges graduées en quarts, où courent les barres.
  const out = [S(k.slabOf(PANEL, 0, PANEL_H, P, 3, 0.6), { tone: "mid" })];
  for (const y of BARS) {
    out.push(L(k.planOutline({ x: BAR_X0, y: y - 2.5, w: BAR_LEN, d: 5, r: 0 }, PANEL_H, P, 1), { tone: "lo" }));
    out.push(L([0.25, 0.5, 0.75].map((f) => k.lineOnTop([BAR_X0 + BAR_LEN * f, y - 2.5], [BAR_X0 + BAR_LEN * f, y - 4], PANEL_H, P)).join(""), { tone: "lo" }));
  }
  return out.join("");
}
const bar = (n, share) => poly([[BAR_X0, BARS[n], PANEL_H + 0.2], [BAR_X0 + BAR_LEN * Math.max(share, 0.004), BARS[n], PANEL_H + 0.2]]);

// Sans JavaScript : balançoire tenue en haut, condensateur chargé à 1 V, toute l'énergie dans le condensateur.
const body = [
  plate(),
  post(-POST_X),
  post(POST_X),
  beam(),
  `<path data-part="ropes" class="iso-line" data-tone="mid" d="${ropes(THMAX)}" style="stroke-width:1.2"/>`,
  `<g data-part="seat">${seat(THMAX)}</g>`,
  D([at([-ROPE_X, 0, TOP - 1.5]), at([ROPE_X, 0, TOP - 1.5])], { size: 0.9, tone: "hi" }),
  panel(),
  `<path data-part="bar-c" class="iso-line" data-tone="hi" data-free="end" d="${bar(0, 1)}" style="stroke-width:4"/>`,
  `<path data-part="bar-l" class="iso-line" data-tone="mid" data-free="end" d="${bar(1, 0)}" style="stroke-width:4"/>`,
];

const svg = k
  .figureSvg({ width: WIDTH, height: HEIGHT, label: "", body })
  .replace(' role="img" aria-label=""', ' aria-hidden="true" focusable="false"');

// Projection linéaire : écran = o + x·ex + y·ey + z·ez (exacte en isométrie).
const o = at([0, 0, 0]);
const axis = (v) => at(v).map((c, i) => +(c - o[i]).toFixed(5));
const num = (v) => +v.toFixed(4);
const model = readFileSync(join(HERE, "model.mjs"), "utf8").replace(/^export /gm, "").replace(/^\/\/.*\n/gm, "");

const js = `// Généré par tools/figures/lc_free/build.mjs : ne pas modifier à la main.
(() => {
${model}const O = ${JSON.stringify(o.map(num))}, EX = ${JSON.stringify(axis([1, 0, 0]))}, EY = ${JSON.stringify(axis([0, 1, 0]))}, EZ = ${JSON.stringify(axis([0, 0, 1]))};
const scr = (x, y, z) => [O[0] + x * EX[0] + y * EY[0] + z * EZ[0], O[1] + x * EX[1] + y * EY[1] + z * EZ[1]];
const pth = (pts) => pts.map((p, i) => { const s = scr(p[0], p[1], p[2]); return (i ? "L" : "M") + s[0].toFixed(2) + " " + s[1].toFixed(2); }).join("");
const move = (dy, dz) => "translate(" + (EY[0] * dy + EZ[0] * dz).toFixed(3) + " " + (EY[1] * dy + EZ[1] * dz).toFixed(3) + ")";
const TOP = ${TOP}, ROPE = ${ROPE}, RX = ${ROPE_X}, THMAX = ${num(THMAX)}, BX = ${BAR_X0}, BLEN = ${BAR_LEN}, BARS = ${JSON.stringify(BARS)}, PZ = ${PANEL_H + 0.2};
const E0 = 0.5 * C * V0 ** 2, PRESETS = { r10: 10, r40: 40, r100: 100 };
const seatAt = (th) => [ROPE * Math.sin(th), TOP - 1.5 - ROPE * Math.cos(th)];
const [Y0, Z0] = seatAt(THMAX);
document.querySelectorAll('.fig[data-fig="lc_free"]').forEach((card) => {
  const q2 = (s) => card.querySelector(s), qa = (s) => card.querySelectorAll(s);
  const svg = q2("svg"), seat = q2('[data-part="seat"]'), ropes = q2('[data-part="ropes"]'), barC = q2('[data-part="bar-c"]'), barL = q2('[data-part="bar-l"]');
  const range = q2("[data-fig-r]"), play = q2("[data-fig-play]"), readout = q2(".fig-readout"), out = {};
  qa("[data-fig-out]").forEach((el) => { out[el.dataset.figOut] = el; });
  const lang = document.documentElement.lang || "fr", still = matchMedia("(prefers-reduced-motion: reduce)");
  const nf = (v, d) => new Intl.NumberFormat(lang, { maximumFractionDigits: d, minimumFractionDigits: d }).format(v);
  const sig = (v) => new Intl.NumberFormat(lang, { maximumSignificantDigits: 3, minimumSignificantDigits: 3 }).format(v);
  let r = 40, t = 0, last = 0, frame = 0, running = false, visible = true;
  function report() {
    const v = vc(t, r), i = current(t, r), ec = energyC(t, r) / E0, el = energyL(t, r) / E0, th = THMAX * v, [y, z] = seatAt(th);
    range.value = r;
    range.setAttribute("aria-valuetext", r + " Ω");
    if (out.q) out.q.textContent = sig(q(r));
    if (out.t) out.t.textContent = nf(t / period(r), 2);
    if (out.v) out.v.textContent = sig(v) + " V";
    if (out.i) out.i.textContent = sig(i * 1e3 || 0) + " mA";
    if (out.e) out.e.textContent = nf(100 * (ec + el), 1) + " %";
    seat.setAttribute("transform", move(y - Y0, z - Z0));
    ropes.setAttribute("d", pth([[-RX, 0, TOP - 1.5], [-RX, y, z]]) + pth([[RX, 0, TOP - 1.5], [RX, y, z]]));
    barC.setAttribute("d", pth([[BX, BARS[0], PZ], [BX + BLEN * Math.max(ec, 0.004), BARS[0], PZ]]));
    barL.setAttribute("d", pth([[BX, BARS[1], PZ], [BX + BLEN * Math.max(el, 0.004), BARS[1], PZ]]));
  }
  function tick(now) {
    if (last) t += Math.min(now - last, 100) / 1000 * period(r) / SLOW;
    last = now;
    // L'oscillation s'éteint : à moins de 0,1 % de l'énergie, la balançoire s'arrête et se laisse relancer.
    if ((energyC(t, r) + energyL(t, r)) / E0 < 0.001) { setPlaying(false); report(); return; }
    report();
    frame = running && visible && !still.matches ? requestAnimationFrame(tick) : 0;
  }
  const run = () => { if (!frame && running && visible && !still.matches) { last = 0; frame = requestAnimationFrame(tick); } };
  function setPlaying(on) {
    if (on && (energyC(t, r) + energyL(t, r)) / E0 < 0.001) t = 0;
    running = on;
    if (!on && frame) { cancelAnimationFrame(frame); frame = 0; }
    play.setAttribute("aria-pressed", on ? "true" : "false");
    play.textContent = on ? play.dataset.pause : play.dataset.play;
    readout.setAttribute("aria-live", on ? "off" : "polite");
    if (on) run();
  }
  const recharge = (value) => { setPlaying(false); r = value; t = 0; report(); };
  range.addEventListener("input", () => recharge(+range.value));
  qa("[data-fig-preset]").forEach((b) => b.addEventListener("click", () => recharge(PRESETS[b.dataset.figPreset])));
  play.addEventListener("click", () => setPlaying(!running));
  new IntersectionObserver((e) => { visible = e[e.length - 1].isIntersecting; run(); }).observe(svg);
  q2("[data-fig-controls]").hidden = false;
  report();
});
})();
`;

const write = (path, text) => {
  mkdirSync(dirname(path), { recursive: true });
  writeFileSync(path, text.replace(/\r\n/g, "\n"));
};
const svgPath = OUT ? join(OUT, "lc_free.svg") : join(ROOT, "templates", "figures", "lc_free.svg");
const jsPath = OUT ? join(OUT, "lc_free.js") : join(ROOT, "static", "acad", "js", "figures", "lc_free.js");
write(svgPath, svg + "\n");
write(jsPath, js);
console.log(`wrote ${svgPath} (${Buffer.byteLength(svg)} o), ${jsPath} (${Buffer.byteLength(js)} o)`);
