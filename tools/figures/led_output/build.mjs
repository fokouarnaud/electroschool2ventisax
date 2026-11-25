// Figure « sortie LED, source et puits » (section 03-source-puits de M2, formation esp32) : l'étage de sortie et la LED.
// node tools/figures/led_output/build.mjs [--out <dossier>]
// écrit templates/figures/led_output.svg (dessin sans texte) et static/acad/js/figures/led_output.js (animation).
// Fichiers générés : ne jamais les retoucher à la main, modifier ce script puis le relancer.
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "../kit/iso-kit.mjs";
import { output } from "./model.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(HERE, "../../..");
const outAt = process.argv.indexOf("--out");
const OUT = outAt > 0 ? resolve(process.argv[outAt + 1]) : null;

const WIDTH = 640;
const HEIGHT = 360;

// Plan (unités monde, z vers le haut ; x vers la droite, y vers l'observateur ; au fond le 3,3 V, devant la masse).
// À gauche, la puce ouverte : le drapeau GPIO_OUT (levé = 1) commande l'étage de sortie, deux interrupteurs en colonne,
// P du rail 3,3 V vers la piste de la broche, N de la piste vers le rail GND, jamais fermés ensemble. À droite, hors de
// la puce : la broche, la résistance de 330 Ω et la LED, vers le rail GND (source) ou depuis le rail 3,3 V (puits).
const PLATE = { x: -112, y: -58, w: 224, d: 116, r: 8 };
const PLATE_H = 8;
const CHIP = { x: -106, y: -50, w: 102, d: 100, r: 4 };
const CT = 6; // dessus de la puce
const LX = -38; // colonne de l'étage de sortie
const EX = 50; // colonne de la résistance et de la LED
const FLAG = { low: CT + 3, high: CT + 9 };

const P = k.fitProjection(k.boxCorners(PLATE, -PLATE_H - 4, 22), WIDTH, HEIGHT, { pad: 16, azimuth: 58 });
const at = (point) => k.iso(point, P);
const S = (paths, style) => k.solidSvg(paths, style);
const L = (d, style) => k.lineSvg(d, style);
const top = (from, to, z) => k.lineOnTop(from, to, z, P);
const shiftZ = (dz) => { const o = at([0, 0, 0]), e = at([0, 0, dz]); return `translate(${(e[0] - o[0]).toFixed(3)} ${(e[1] - o[1]).toFixed(3)})`; };

// Sans JavaScript : source, niveau haut, LED allumée.
const W0 = "source";
const O0 = output(W0, true);
const LIVE0 = ["p", "tin", "trunk", "src"];
const hide = (on) => (on ? "" : ' visibility="hidden"');
const wire = (key, d, width = 1.6) => `<g data-wire="${key}"><path class="iso-line" data-tone="${LIVE0.includes(key) ? "hi" : "lo"}" style="stroke-width:${width}" d="${d}"/></g>`;

function signs(x, yBack, yFront, z) {
  const plus = top([x - 2, yBack + 2], [x + 2, yBack + 2], z) + top([x, yBack + 0.4], [x, yBack + 3.6], z);
  const minus = top([x - 2, yFront + 2], [x + 2, yFront + 2], z);
  return `<path class="iso-line" data-tone="hi" data-free="" style="stroke-width:1.2" d="${plus + minus}"/>`;
}

function plate() {
  const out = [`<path class="iso-halo" d="${k.haloOf(PLATE, -PLATE_H - 4, PLATE_H, P)}"/>`];
  for (const [x, y] of k.corners(PLATE, 20)) out.push(S(k.cylinder(x, y, 6, -PLATE_H - 4, 4, P, 8), { tone: "mid" }));
  out.push(S(k.slabOf(PLATE, -PLATE_H, PLATE_H, P, 5, 1.4), { tone: "mid" }));
  return out.join("");
}

function chip() {
  const out = [S(k.slabOf(CHIP, 0, CT, P, 3, 0.8), { tone: "mid" })];
  out.push(L(k.planOutline(k.insetPlan(CHIP, 5), CT, P), { tone: "faint", dashed: true }));
  for (const y of [-42, 38]) out.push(S(k.slabOf({ x: -98, y, w: 88, d: 4, r: 1 }, CT, 1.2, P, 2), { tone: "hi", crease: "none" }));
  out.push(signs(-94, -42, 38, CT + 1.2));
  return out.join("");
}

// Un interrupteur de l'étage de sortie : P (s = −1, vers le rail 3,3 V) ou N (s = 1, vers le rail GND).
function stage(key, s) {
  const near = s * 6, far = s * 16, rail = s < 0 ? -38 : 38;
  const closed = O0.closed === key.toUpperCase();
  const out = [wire(key, k.segment([LX, rail, s < 0 ? CT : CT + 1.2], [LX, far, CT], P) + top([LX, near], [LX, 0], CT))];
  for (const y of [near, far]) out.push(S(k.cylinder(LX, y, 2, CT, 1, P, 10), { tone: "hi", crease: "none" }));
  out.push(`<g data-part="${key}-open"${hide(!closed)}>${L(top([LX, near], [LX + 7, far - s * 2], CT + 1), { tone: "hi", free: true })}</g>`);
  out.push(`<g data-part="${key}-closed"${hide(closed)}>${L(top([LX, near], [LX, far], CT + 1), { tone: "hi", free: true })}</g>`);
  return out.join("");
}

function inside() {
  const out = [stage("p", -1)];
  // GPIO_OUT : registre et son drapeau ; la ligne de commande pointillée mène au bloc de commande de l'étage
  out.push(L(top([-84, 0], [-52, 0], CT), { tone: "lo", dashed: true }));
  out.push(S(k.slabOf({ x: -52, y: -4, w: 10, d: 8, r: 1 }, CT, 3, P, 2), { tone: "mid" }));
  out.push(S(k.slabOf({ x: -96, y: -6, w: 12, d: 12, r: 1 }, CT, 2, P, 2), { tone: "mid" }));
  out.push(S(k.cylinder(-90, 0, 1.2, CT + 2, 9, P, 10), { tone: "hi", crease: "none" }));
  out.push(`<g data-part="flag" transform="${shiftZ(FLAG.high - FLAG.low)}">${S(k.slabOf({ x: -101, y: -4, w: 10, d: 8, r: 1 }, FLAG.low, 1.5, P, 2), { tone: "hi", crease: "lo" })}</g>`);
  out.push(wire("tin", top([LX, 0], [-4, 0], CT), 1.8));
  out.push(stage("n", 1));
  return out.join("");
}

// Résistance de 330 Ω (trois bagues) et LED (boîtier et dôme), le long d'une colonne, de y0 à y1.
function resistor(y0) {
  const body = { x: EX - 4, y: y0, w: 8, d: 16, r: 3 };
  const bands = [0.25, 0.45, 0.65].map((f) => top([EX - 4, y0 + f * 16], [EX + 4, y0 + f * 16], 6)).join("");
  return S(k.slabOf(body, 0, 6, P, 3), { tone: "hi", crease: "lo" }) + L(bands, { tone: "lo" });
}
function led(key, cy, lit) {
  return `<g data-part="${key}">${S(k.cylinder(EX, cy, 4.5, 0, 5, P, 16), { tone: "hi", crease: "lo", lit })}${S(k.cylinder(EX, cy, 3.2, 5, 2.5, P, 14), { tone: "hi", crease: "lo", lit })}</g>`;
}

function outside() {
  const out = [];
  out.push(S(k.slabOf({ x: -4, y: -2.5, w: 16, d: 5, r: 0.5 }, 0, CT - 1, P, 1), { tone: "hi", crease: "lo" }));
  out.push(S(k.slabOf({ x: 18, y: -50, w: 88, d: 6, r: 1 }, 0, 2, P, 2), { tone: "mid" }));
  // puits : 3,3 V (au fond), LED, résistance, broche
  out.push(`<g data-part="snk"${hide(W0 === "sink")}>`
    + wire("snk", top([EX, -44], [EX, -38], 0.2) + top([EX, -30], [EX, -24], 0.2) + k.segment([EX, -8, 0.2], [EX, 0, 0.5], P))
    + led("led-snk", -34, false) + resistor(-24) + "</g>");
  out.push(wire("trunk", top([12, 0], [EX, 0], 0.5), 1.8));
  // source : broche, résistance, LED, GND (devant)
  out.push(`<g data-part="src"${hide(W0 === "source")}>`
    + wire("src", k.segment([EX, 0, 0.5], [EX, 8, 0.2], P) + top([EX, 24], [EX, 30], 0.2) + top([EX, 38], [EX, 44], 0.2))
    + resistor(8) + led("led-src", 34, O0.lit) + "</g>");
  out.push(S(k.slabOf({ x: 18, y: 44, w: 88, d: 6, r: 1 }, 0, 2, P, 2), { tone: "mid" }));
  out.push(signs(23, -49, 45, 2));
  return out.join("");
}

const body = [plate(), chip(), inside(), outside()];
const svg = k.figureSvg({ width: WIDTH, height: HEIGHT, label: "", body }).replace(' role="img" aria-label=""', ' aria-hidden="true" focusable="false"');

const o = at([0, 0, 0]);
const ez = at([0, 0, 1]).map((c, i) => +(c - o[i]).toFixed(5));
const model = readFileSync(join(HERE, "model.mjs"), "utf8").replace(/^export /gm, "").replace(/^\/\/.*\n/gm, "");

const js = `// Généré par tools/figures/led_output/build.mjs : ne pas modifier à la main.
(() => {
${model}const EZ = ${JSON.stringify(ez)}, RISE = ${FLAG.high - FLAG.low};
const shift = (dz) => "translate(" + (EZ[0] * dz).toFixed(3) + " " + (EZ[1] * dz).toFixed(3) + ")";
document.querySelectorAll('.fig[data-fig="led_output"]').forEach((card) => {
  const q = (s) => card.querySelector(s), qa = (s) => [...card.querySelectorAll(s)];
  const svg = q("svg"), level = q("[data-fig-level]"), presets = qa("[data-fig-preset]"), out = {};
  qa("[data-fig-out]").forEach((el) => { out[el.dataset.figOut] = el; });
  const lang = document.documentElement.lang || "fr", still = matchMedia("(prefers-reduced-motion: reduce)");
  const num = (v, d) => new Intl.NumberFormat(lang, { maximumSignificantDigits: d }).format(v);
  let wiring = "source", high = true, flag = 1, last = 0, frame = 0, visible = true;
  const show = (key, on) => { const g = q('[data-part="' + key + '"]'); if (on) g.removeAttribute("visibility"); else g.setAttribute("visibility", "hidden"); };
  function draw() {
    const o = output(wiring, high), src = wiring === "source";
    show("src", src); show("snk", !src);
    show("p-open", o.closed !== "P"); show("p-closed", o.closed === "P"); show("n-open", o.closed !== "N"); show("n-closed", o.closed === "N");
    qa(".iso-solid[data-lit]").forEach((el) => el.removeAttribute("data-lit"));
    if (o.lit) qa('[data-part="' + (src ? "led-src" : "led-snk") + '"] .iso-solid').forEach((el) => el.setAttribute("data-lit", ""));
    // fils parcourus par un courant : seulement quand la LED est allumée
    const live = o.lit ? (src ? ["p", "tin", "trunk", "src"] : ["snk", "trunk", "tin", "n"]) : [];
    qa("[data-wire]").forEach((g) => g.querySelector("path").setAttribute("data-tone", live.includes(g.dataset.wire) ? "hi" : "lo"));
    presets.forEach((b) => b.setAttribute("aria-pressed", b.dataset.figPreset === wiring ? "true" : "false"));
    const set = (key, v) => { if (out[key] && out[key].textContent !== v) out[key].textContent = v; };
    set("wiring", q('[data-fig-preset="' + wiring + '"]').textContent.trim());
    set("level", high ? "HIGH" : "LOW");
    set("volts", num(o.volts, 2) + " V");
    set("closed", o.closed === "P" ? out.closed.dataset.p : out.closed.dataset.n);
    set("led", o.lit ? out.led.dataset.on : out.led.dataset.off);
    set("amps", o.lit ? num(o.amps * 1000, 3) + " mA" : "0 mA");
    set("flow", o.flow ? out.flow.dataset[o.flow] : out.flow.dataset.none);
    level.textContent = high ? level.dataset.low : level.dataset.high;
  }
  const pose = () => q('[data-part="flag"]').setAttribute("transform", shift(RISE * flag));
  function tick(now) {
    const step = last ? Math.min(now - last, 100) / 1000 / MOVE_S : 0, goal = high ? 1 : 0;
    last = now;
    flag = goal > flag ? Math.min(goal, flag + step) : Math.max(goal, flag - step);
    pose();
    frame = flag !== goal && visible && !still.matches ? requestAnimationFrame(tick) : 0;
  }
  function run() {
    const goal = high ? 1 : 0;
    if (still.matches) { flag = goal; pose(); return; }
    if (!frame && visible && flag !== goal) { last = 0; frame = requestAnimationFrame(tick); }
  }
  level.addEventListener("click", () => { high = !high; draw(); run(); });
  presets.forEach((b) => b.addEventListener("click", () => { wiring = b.dataset.figPreset; draw(); run(); }));
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
const svgPath = OUT ? join(OUT, "led_output.svg") : join(ROOT, "templates", "figures", "led_output.svg");
const jsPath = OUT ? join(OUT, "led_output.js") : join(ROOT, "static", "acad", "js", "figures", "led_output.js");
write(svgPath, svg + "\n");
write(jsPath, js);
console.log(`wrote ${svgPath} (${Buffer.byteLength(svg)} o), ${jsPath} (${Buffer.byteLength(js)} o)`);
