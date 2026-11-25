// Figure « quatre câblages d'un bouton » (section 02-tirage de M3, formation esp32) : la puce ouverte et ce qu'on câble autour.
// node tools/figures/pull_wiring/build.mjs [--out <dossier>]
// écrit templates/figures/pull_wiring.svg (dessin sans texte) et static/acad/js/figures/pull_wiring.js (animation).
// Fichiers générés : ne jamais les retoucher à la main, modifier ce script puis le relancer.
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "../kit/iso-kit.mjs";
import { parts } from "./model.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(HERE, "../../..");
const outAt = process.argv.indexOf("--out");
const OUT = outAt > 0 ? resolve(process.argv[outAt + 1]) : null;

const WIDTH = 640;
const HEIGHT = 360;

// Plan (unités monde, z vers le haut ; x vers la droite, y vers l'observateur ; au fond le 3,3 V, devant la masse).
// À gauche, la puce ouverte : rail 3,3 V et rail GND internes, tirage interne vers 3,3 V (au fond) et vers GND (devant),
// chacun derrière un interrupteur relié à la piste de la broche ; la piste mène au tampon d'entrée, puis au drapeau GPIO_IN,
// levé quand le niveau lu vaut 1. À droite, hors de la puce : rail 3,3 V, rail GND, la piste de la broche, la résistance
// externe de 10 kΩ et le bouton, chacun du côté que le câblage choisi impose.
const PLATE = { x: -112, y: -58, w: 224, d: 116, r: 8 };
const PLATE_H = 8;
const CHIP = { x: -106, y: -50, w: 102, d: 100, r: 4 };
const CT = 6; // dessus de la puce
const LX = -38; // colonne des tirages internes
const EX = 40; // colonne de la résistance externe
const BX = 80; // colonne du bouton
const CAP_Z = 4;
const PRESS = 2; // course du bouton
const FLAG = { low: CT + 3, high: CT + 9 };

const P = k.fitProjection(k.boxCorners(PLATE, -PLATE_H - 4, 22), WIDTH, HEIGHT, { pad: 16, azimuth: 58 });
const at = (point) => k.iso(point, P);
const S = (paths, style) => k.solidSvg(paths, style);
const L = (d, style) => k.lineSvg(d, style);
const D = (points, style) => k.dotsSvg(points, style);
const top = (from, to, z) => k.lineOnTop(from, to, z, P);
const shiftZ = (dz) => { const o = at([0, 0, 0]), e = at([0, 0, dz]); return `translate(${(e[0] - o[0]).toFixed(3)} ${(e[1] - o[1]).toFixed(3)})`; };

// Sans JavaScript : pull-down externe, bouton relâché.
const W0 = "ext-down";
const P0 = parts(W0);
const hide = (on) => (on ? "" : ' visibility="hidden"');
const wire = (key, d, width = 1.6) => `<g data-wire="${key}"><path class="iso-line" data-tone="lo" style="stroke-width:${width}" d="${d}"/></g>`;

function plate() {
  const out = [`<path class="iso-halo" d="${k.haloOf(PLATE, -PLATE_H - 4, PLATE_H, P)}"/>`];
  for (const [x, y] of k.corners(PLATE, 20)) out.push(S(k.cylinder(x, y, 6, -PLATE_H - 4, 4, P, 8), { tone: "mid" }));
  out.push(S(k.slabOf(PLATE, -PLATE_H, PLATE_H, P, 5, 1.4), { tone: "mid" }));
  return out.join("");
}

// Signes gravés sur les rails : « + » pour le 3,3 V (au fond), « − » pour la masse (devant), dessinés en traits.
function signs(x, yBack, yFront, z) {
  const plus = top([x - 2, yBack + 2], [x + 2, yBack + 2], z) + top([x, yBack + 0.4], [x, yBack + 3.6], z);
  const minus = top([x - 2, yFront + 2], [x + 2, yFront + 2], z);
  return `<path class="iso-line" data-tone="hi" data-free="" style="stroke-width:1.2" d="${plus + minus}"/>`;
}

function chip() {
  const out = [S(k.slabOf(CHIP, 0, CT, P, 3, 0.8), { tone: "mid" })];
  out.push(L(k.planOutline(k.insetPlan(CHIP, 5), CT, P), { tone: "faint", dashed: true }));
  // rails internes : 3,3 V au fond, GND devant
  for (const y of [-42, 38]) out.push(S(k.slabOf({ x: -98, y, w: 88, d: 4, r: 1 }, CT, 1.2, P, 2), { tone: "hi", crease: "none" }));
  out.push(signs(-94, -42, 38, CT + 1.2));
  return out.join("");
}

// Un tirage interne : résistance sur son rail, interrupteur (levier ouvert ou fermé) vers la piste de la broche.
function internal(key, s) {
  const rail = s < 0 ? -38 : 38;
  const res = s < 0 ? { x: LX - 3, y: -36, w: 6, d: 14, r: 1 } : { x: LX - 3, y: 22, w: 6, d: 14, r: 1 };
  const near = s * 6, far = s * 16, end = s < 0 ? -22 : 22;
  const closed = (s < 0 ? P0.pullUp : P0.pullDown);
  const out = [wire(key, k.segment([LX, rail, CT + 1.2], [LX, s * 30, CT + 1.5], P) + top([LX, end - s * 4], [LX, far], CT) + top([LX, near], [LX, 0], CT))];
  out.push(`<g data-part="r-${key}">${S(k.slabOf(res, CT, 3, P, 2), { tone: "hi", crease: "lo" })}</g>`);
  for (const y of [near, far]) out.push(S(k.cylinder(LX, y, 2, CT, 1, P, 10), { tone: "hi", crease: "none" }));
  out.push(`<g data-part="${key}-open"${hide(!closed)}>${L(top([LX, near], [LX + 7, far + -s * 2], CT + 1), { tone: "hi", free: true })}</g>`);
  out.push(`<g data-part="${key}-closed"${hide(closed)}>${L(top([LX, near], [LX, far], CT + 1), { tone: "hi" })}</g>`);
  return out.join("");
}

function inside() {
  const out = [internal("iu", -1)];
  // piste de la broche, tampon d'entrée (triangle gravé, pointe vers GPIO_IN) et drapeau GPIO_IN
  out.push(wire("tin", top([-66, 0], [-4, 0], CT), 1.8));
  out.push(L(top([-72, 0], [-90, 0], CT), { tone: "lo" }));
  out.push(S(k.slabOf({ x: -78, y: -6, w: 12, d: 12, r: 1 }, CT, 3, P, 2), { tone: "mid" }));
  out.push(L(k.onTop([[-68, -4], [-68, 4], [-76, 0]], CT + 3, P, true), { tone: "hi" }));
  out.push(S(k.cylinder(-90, 0, 1.2, CT, 11, P, 10), { tone: "hi", crease: "none" }));
  out.push(`<g data-part="flag" transform="${shiftZ(0)}">${S(k.slabOf({ x: -101, y: -4, w: 10, d: 8, r: 1 }, FLAG.low, 1.5, P, 2), { tone: "hi", crease: "lo" })}</g>`);
  out.push(internal("id", 1));
  return out.join("");
}

function outside() {
  const out = [];
  // broche : patte au bord de la puce, puis piste jusqu'au nœud
  out.push(S(k.slabOf({ x: -4, y: -2.5, w: 16, d: 5, r: 0.5 }, 0, CT - 1, P, 1), { tone: "hi", crease: "lo" }));
  out.push(S(k.slabOf({ x: 18, y: -50, w: 88, d: 6, r: 1 }, 0, 2, P, 2), { tone: "mid" }));
  for (const s of [-1, 1]) {
    const key = s < 0 ? "up" : "down";
    // résistance externe de 10 kΩ, rayée de trois bagues
    const body = s < 0 ? { x: EX - 4, y: -34, w: 8, d: 20, r: 3 } : { x: EX - 4, y: 14, w: 8, d: 20, r: 3 };
    const bands = [0.25, 0.45, 0.65].map((f) => top([EX - 4, body.y + f * body.d], [EX + 4, body.y + f * body.d], 6)).join("");
    out.push(`<g data-part="er-${key}"${hide(P0.resistor === (s < 0 ? "3v3" : "gnd"))}>`
      + wire(`e${key[0]}`, top([EX, s * 44], [EX, s * 34], 0.2) + k.segment([EX, s * 14, 0.2], [EX, 0, 0.5], P))
      + `<g data-part="r-e${key[0]}">${S(k.slabOf(body, 0, 6, P, 3), { tone: "hi", crease: "lo", lit: s > 0 })}</g>` + L(bands, { tone: "lo" }) + "</g>");
    // bouton-poussoir : socle et capuchon, qui descend de PRESS quand on appuie
    const base = s < 0 ? { x: BX - 8, y: -30, w: 16, d: 16, r: 1 } : { x: BX - 8, y: 14, w: 16, d: 16, r: 1 };
    const cy = base.y + 8;
    out.push(`<g data-part="bt-${key}"${hide(P0.button === (s < 0 ? "3v3" : "gnd"))}>`
      + wire(`b${key[0]}`, top([BX, s * 44], [BX, s * 30], 0.2) + k.segment([BX, s * 14, 0.2], [BX, 0, 0.5], P))
      + S(k.slabOf(base, 0, CAP_Z, P, 2), { tone: "mid" }) + L(k.ring(BX, cy, 6, CAP_Z, P, 16), { tone: "lo" })
      + `<g data-part="cap-${key}">${S(k.cylinder(BX, cy, 5, CAP_Z, 3, P, 16), { tone: "hi", crease: "lo" })}</g></g>`);
    if (s < 0) out.push(wire("trunk", top([12, 0], [BX, 0], 0.5), 1.8) + D([at([BX, 0, 0.5]), at([EX, 0, 0.5])], { size: 0.9, tone: "hi" }));
  }
  out.push(S(k.slabOf({ x: 18, y: 44, w: 88, d: 6, r: 1 }, 0, 2, P, 2), { tone: "mid" }));
  out.push(signs(23, -49, 45, 2));
  return out.join("");
}

const body = [plate(), chip(), inside(), outside()];
const svg = k.figureSvg({ width: WIDTH, height: HEIGHT, label: "", body }).replace(' role="img" aria-label=""', ' aria-hidden="true" focusable="false"');

const o = at([0, 0, 0]);
const ez = at([0, 0, 1]).map((c, i) => +(c - o[i]).toFixed(5));
const model = readFileSync(join(HERE, "model.mjs"), "utf8").replace(/^export /gm, "").replace(/^\/\/.*\n/gm, "");

const js = `// Généré par tools/figures/pull_wiring/build.mjs : ne pas modifier à la main.
(() => {
${model}const EZ = ${JSON.stringify(ez)}, PRESS = ${PRESS}, RISE = ${FLAG.high - FLAG.low};
const shift = (dz) => "translate(" + (EZ[0] * dz).toFixed(3) + " " + (EZ[1] * dz).toFixed(3) + ")";
document.querySelectorAll('.fig[data-fig="pull_wiring"]').forEach((card) => {
  const q = (s) => card.querySelector(s), qa = (s) => [...card.querySelectorAll(s)];
  const svg = q("svg"), push = q("[data-fig-push]"), presets = qa("[data-fig-preset]"), out = {};
  qa("[data-fig-out]").forEach((el) => { out[el.dataset.figOut] = el; });
  const lang = document.documentElement.lang || "fr", still = matchMedia("(prefers-reduced-motion: reduce)");
  const num = (v, d) => new Intl.NumberFormat(lang, { maximumSignificantDigits: d }).format(v);
  let wiring = "ext-down", pressed = false, t = 0, flag = 0, last = 0, frame = 0, visible = true;
  const show = (key, on) => { const g = q('[data-part="' + key + '"]'); if (on) g.removeAttribute("visibility"); else g.setAttribute("visibility", "hidden"); };
  function draw() {
    const p = parts(wiring), r = reading(wiring, pressed), side = (s) => (s === "3v3" ? "up" : "down");
    show("iu-open", !p.pullUp); show("iu-closed", p.pullUp); show("id-open", !p.pullDown); show("id-closed", p.pullDown);
    ["up", "down"].forEach((s) => { show("er-" + s, p.resistor && side(p.resistor) === s); show("bt-" + s, side(p.button) === s); });
    const pull = p.pullUp ? "iu" : p.pullDown ? "id" : "e" + side(p.resistor)[0];
    qa(".iso-solid[data-lit]").forEach((el) => el.removeAttribute("data-lit"));
    qa('[data-part="r-' + pull + '"] .iso-solid').forEach((el) => el.setAttribute("data-lit", ""));
    // fils parcourus par un courant : le tirage, la piste et le bouton, seulement bouton appuyé
    const live = r.amps ? [pull, "trunk", "b" + side(p.button)[0]].concat(p.pullUp || p.pullDown ? ["tin"] : []) : [];
    qa("[data-wire]").forEach((g) => g.querySelector("path").setAttribute("data-tone", live.includes(g.dataset.wire) ? "hi" : "lo"));
    presets.forEach((b) => b.setAttribute("aria-pressed", b.dataset.figPreset === wiring ? "true" : "false"));
    const set = (key, v) => { if (out[key] && out[key].textContent !== v) out[key].textContent = v; };
    set("wiring", q('[data-fig-preset="' + wiring + '"]').textContent.trim());
    set("button", pressed ? out.button.dataset.pressed : out.button.dataset.released);
    set("volts", num(r.volts, 2) + " V");
    set("level", r.level);
    set("amps", r.amps ? num(r.amps * 1000, 3) + " mA" : "0 mA");
    push.textContent = pressed ? push.dataset.release : push.dataset.press;
    push.setAttribute("aria-pressed", pressed ? "true" : "false");
  }
  function pose() {
    ["up", "down"].forEach((s) => q('[data-part="cap-' + s + '"]').setAttribute("transform", shift(-PRESS * t)));
    q('[data-part="flag"]').setAttribute("transform", shift(RISE * flag));
  }
  const goal = () => [pressed ? 1 : 0, reading(wiring, pressed).level === "HIGH" ? 1 : 0];
  function tick(now) {
    const step = last ? Math.min(now - last, 100) / 1000 / PRESS_S : 0, [gt, gf] = goal();
    last = now;
    t = gt > t ? Math.min(gt, t + step) : Math.max(gt, t - step);
    flag = gf > flag ? Math.min(gf, flag + step) : Math.max(gf, flag - step);
    pose();
    frame = (t !== gt || flag !== gf) && visible && !still.matches ? requestAnimationFrame(tick) : 0;
  }
  function run() {
    const [gt, gf] = goal();
    if (still.matches) { t = gt; flag = gf; pose(); return; }
    if (!frame && visible && (t !== gt || flag !== gf)) { last = 0; frame = requestAnimationFrame(tick); }
  }
  push.addEventListener("click", () => { pressed = !pressed; draw(); run(); });
  presets.forEach((b) => b.addEventListener("click", () => { wiring = b.dataset.figPreset; pressed = false; draw(); run(); }));
  new IntersectionObserver((e) => { visible = e[e.length - 1].isIntersecting; run(); }).observe(svg);
  q("[data-fig-controls]").hidden = false;
  draw();
  run();
});
})();
`;

const write = (path, text) => {
  mkdirSync(dirname(path), { recursive: true });
  writeFileSync(path, text.replace(/\r\n/g, "\n"));
};
const svgPath = OUT ? join(OUT, "pull_wiring.svg") : join(ROOT, "templates", "figures", "pull_wiring.svg");
const jsPath = OUT ? join(OUT, "pull_wiring.js") : join(ROOT, "static", "acad", "js", "figures", "pull_wiring.js");
write(svgPath, svg + "\n");
write(jsPath, js);
console.log(`wrote ${svgPath} (${Buffer.byteLength(svg)} o), ${jsPath} (${Buffer.byteLength(js)} o)`);
