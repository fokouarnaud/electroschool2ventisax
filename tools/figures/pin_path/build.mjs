// Figure « du programme à la broche de la carte » (section 02-architecture de M1, formation esp32) : le chemin d'un digitalWrite.
// node tools/figures/pin_path/build.mjs [--out <dossier>]
// écrit templates/figures/pin_path.svg (dessin sans texte) et static/acad/js/figures/pin_path.js (animation).
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
const HEIGHT = 380;

// Plan (unités monde, z vers le haut ; x vers la droite, y vers l'observateur). Le chemin suit y = 0, de gauche à droite :
// dans la puce ouverte, le CPU, le bus interne, le registre GPIO_OUT (bloc du bit 25, levé = 1), la matrice GPIO et l'IO MUX,
// le plot 25 (levier vers le contact P, 3,3 V, au fond, ou N, GND, devant) ; hors de la puce, la patte du module, la broche G25
// de la carte, la résistance de 330 Ω, la LED et le rail GND.
const PLATE = { x: -132, y: -46, w: 264, d: 92, r: 8 };
const PLATE_H = 8;
const CHIP = { x: -126, y: -40, w: 170, d: 80, r: 4 };
const CT = 6;
const BIT = { low: CT + 4, rise: 4 };

const P = k.fitProjection(k.boxCorners(PLATE, -PLATE_H - 4, 24), WIDTH, HEIGHT, { pad: 14, azimuth: 40 });
const at = (point) => k.iso(point, P);
const S = (paths, style) => k.solidSvg(paths, style);
const L = (d, style) => k.lineSvg(d, style);
const top = (from, to, z) => k.lineOnTop(from, to, z, P);
const shiftZ = (dz) => { const o = at([0, 0, 0]), e = at([0, 0, dz]); return `translate(${(e[0] - o[0]).toFixed(3)} ${(e[1] - o[1]).toFixed(3)})`; };

// Sans JavaScript : dernière étape de digitalWrite(25, HIGH) ; tout le chemin est franchi, la LED est allumée.
const hide = (on) => (on ? "" : ' visibility="hidden"');
const wire = (key, d, width = 1.6) => `<g data-wire="${key}"><path class="iso-line" data-tone="hi" style="stroke-width:${width}" d="${d}"/></g>`;
const stage = (key, inner) => `<g data-stage="${key}">${inner}</g>`;

function plate() {
  const out = [`<path class="iso-halo" d="${k.haloOf(PLATE, -PLATE_H - 4, PLATE_H, P)}"/>`];
  for (const [x, y] of k.corners(PLATE, 18)) out.push(S(k.cylinder(x, y, 6, -PLATE_H - 4, 4, P, 8), { tone: "mid" }));
  out.push(S(k.slabOf(PLATE, -PLATE_H, PLATE_H, P, 5, 1.4), { tone: "mid" }));
  return out.join("");
}

function chip() {
  return S(k.slabOf(CHIP, 0, CT, P, 3, 0.8), { tone: "mid" }) + L(k.planOutline(k.insetPlan(CHIP, 4), CT, P), { tone: "faint", dashed: true });
}

function inside() {
  const out = [];
  // CPU
  out.push(wire("cpu", top([-90, 0], [-84, 0], CT)));
  out.push(stage("cpu", S(k.slabOf({ x: -118, y: -18, w: 28, d: 36, r: 2 }, CT, 8, P, 3, 0.6), { tone: "hi", crease: "lo" })));
  // bus interne : barre le long de y
  out.push(stage("bus", S(k.slabOf({ x: -84, y: -32, w: 4, d: 64, r: 1 }, CT, 2, P, 2), { tone: "hi", crease: "none" })));
  out.push(wire("bus", top([-80, 0], [-72, 0], CT)));
  // registre GPIO_OUT et son bloc du bit 25
  out.push(stage("reg", S(k.slabOf({ x: -72, y: -14, w: 30, d: 28, r: 2 }, CT, 4, P, 2), { tone: "hi", crease: "lo" })
    + L([-66, -60, -54, -48].map((x) => top([x, -14], [x, 14], CT + 4)).join(""), { tone: "lo" })));
  out.push(`<g data-part="bit" transform="${shiftZ(BIT.rise)}">${S(k.slabOf({ x: -60, y: -5, w: 6, d: 10, r: 1 }, BIT.low, 3, P, 2), { tone: "hi", crease: "lo" })}</g>`);
  out.push(wire("reg", top([-42, 0], [-34, 0], CT)));
  // matrice GPIO et IO MUX : grille de croisements, route du bit 25 vers le plot 25 sur y = 0
  out.push(stage("mux", S(k.slabOf({ x: -34, y: -24, w: 24, d: 48, r: 2 }, CT, 6, P, 2), { tone: "hi", crease: "lo" })
    + L([-12, 12].map((y) => top([-34, y], [-10, y], CT + 6)).join("") + [-26, -18].map((x) => top([x, -24], [x, 24], CT + 6)).join(""), { tone: "faint" })));
  out.push(wire("route", top([-34, 0], [-10, 0], CT + 6)));
  out.push(wire("mux", top([-10, 0], [-2, 0], CT)));
  // plot 25 : pivot, contact P (au fond) et contact N (devant)
  const z = CT + 3;
  out.push(stage("pad", S(k.slabOf({ x: -2, y: -14, w: 20, d: 28, r: 2 }, CT, 3, P, 2), { tone: "hi", crease: "lo" })));
  for (const [x, y] of [[4, 0], [12, -8], [12, 8]]) out.push(S(k.cylinder(x, y, 1.8, z, 1, P, 10), { tone: "hi", crease: "none" }));
  out.push(L(top([12, -9.8], [12, -14], z) + top([12, 9.8], [12, 14], z), { tone: "lo" }));
  out.push(`<g data-part="lever-p">${L(top([4, 0], [12, -8], z + 1), { tone: "hi", free: true })}</g>`);
  out.push(`<g data-part="lever-n"${hide(false)}>${L(top([4, 0], [12, 8], z + 1), { tone: "hi", free: true })}</g>`);
  out.push(wire("pad", top([18, 0], [44, 0], CT)));
  return out.join("");
}

function outside() {
  const out = [];
  out.push(wire("pin", top([56, 0], [70, 0], 0.5)));
  out.push(stage("board", S(k.slabOf({ x: 44, y: -2.5, w: 12, d: 5, r: 0.5 }, 0, CT - 1, P, 1), { tone: "hi", crease: "lo" })
    + S(k.slabOf({ x: 64, y: -6, w: 12, d: 12, r: 1 }, 0, 4, P, 2), { tone: "mid" })
    + S(k.slabOf({ x: 68, y: -2, w: 4, d: 4, r: 0.5 }, 4, 8, P, 1), { tone: "hi", crease: "lo" })));
  out.push(wire("led", top([76, 0], [84, 0], 0.5) + top([100, 0], [106, 0], 0.5) + top([114, 0], [120, 0], 0.5)));
  out.push(S(k.slabOf({ x: 84, y: -3, w: 16, d: 6, r: 2.5 }, 0, 5, P, 3), { tone: "hi", crease: "lo" })
    + L([88, 92, 96].map((x) => top([x, -3], [x, 3], 5)).join(""), { tone: "lo" }));
  out.push(`<g data-part="led">${S(k.cylinder(110, 0, 4.5, 0, 5, P, 16), { tone: "hi", crease: "lo", lit: true })}${S(k.cylinder(110, 0, 3.2, 5, 2.5, P, 14), { tone: "hi", crease: "lo", lit: true })}</g>`);
  out.push(S(k.slabOf({ x: 120, y: -34, w: 5, d: 68, r: 1 }, 0, 2, P, 2), { tone: "mid" }));
  out.push(`<path class="iso-line" data-tone="hi" data-free="" style="stroke-width:1.2" d="${top([121, 28], [124, 28], 2)}"/>`);
  return out.join("");
}

const body = [plate(), chip(), inside(), outside()];
const svg = k.figureSvg({ width: WIDTH, height: HEIGHT, label: "", body }).replace(' role="img" aria-label=""', ' aria-hidden="true" focusable="false"');

const o = at([0, 0, 0]);
const ez = at([0, 0, 1]).map((c, i) => +(c - o[i]).toFixed(5));
const model = readFileSync(join(HERE, "model.mjs"), "utf8").replace(/^export /gm, "").replace(/^\/\/.*\n/gm, "");

const js = `// Généré par tools/figures/pin_path/build.mjs : ne pas modifier à la main.
(() => {
${model}const EZ = ${JSON.stringify(ez)}, RISE = ${BIT.rise};
const shift = (dz) => "translate(" + (EZ[0] * dz).toFixed(3) + " " + (EZ[1] * dz).toFixed(3) + ")";
// fils franchis après chaque étape
const WIRES = { cpu: "cpu", bus: "bus", reg: "reg", mux: ["route", "mux"], pad: "pad", board: "pin" };
document.querySelectorAll('.fig[data-fig="pin_path"]').forEach((card) => {
  const q = (s) => card.querySelector(s), qa = (s) => [...card.querySelectorAll(s)];
  const svg = q("svg"), prev = q("[data-fig-prev]"), next = q("[data-fig-next]"), play = q("[data-fig-play]"), level = q("[data-fig-level]");
  const items = qa("[data-fig-step]"), out = {};
  qa("[data-fig-out]").forEach((el) => { out[el.dataset.figOut] = el; });
  const lang = document.documentElement.lang || "fr", still = matchMedia("(prefers-reduced-motion: reduce)");
  const num = (v) => new Intl.NumberFormat(lang, { maximumSignificantDigits: 2 }).format(v);
  let step = 1, high = true, timer = 0, visible = true;
  const show = (key, on) => { const g = q('[data-part="' + key + '"]'); if (on) g.removeAttribute("visibility"); else g.setAttribute("visibility", "hidden"); };
  function draw() {
    const now = write(high), before = write(!high);
    // chaque pièce garde l'état précédent tant que le signal ne l'a pas atteinte
    const bit = step >= 3 ? now.bit : before.bit, sw = step >= 5 ? now.closed : before.closed, pin = step >= 6 ? now : before;
    q('[data-part="bit"]').setAttribute("transform", shift(RISE * bit));
    show("lever-p", sw === "P"); show("lever-n", sw === "N");
    qa(".iso-solid[data-lit]").forEach((el) => el.removeAttribute("data-lit"));
    qa('[data-stage="' + STAGES[step - 1] + '"] .iso-solid').forEach((el) => el.setAttribute("data-lit", ""));
    if (pin.led) qa('[data-part="led"] .iso-solid').forEach((el) => el.setAttribute("data-lit", ""));
    const crossed = STAGES.filter((s) => reached(step, s)).flatMap((s) => [].concat(WIRES[s]));
    if (pin.led) crossed.push("led");
    qa("[data-wire]").forEach((g) => g.querySelector("path").setAttribute("data-tone", crossed.includes(g.dataset.wire) ? "hi" : "lo"));
    items.forEach((li) => { if (+li.dataset.figStep === step) li.setAttribute("aria-current", "step"); else li.removeAttribute("aria-current"); });
    const set = (key, v) => { if (out[key] && out[key].textContent !== v) out[key].textContent = v; };
    set("step", step + " / " + STAGES.length);
    set("code", "digitalWrite(25, " + (high ? "HIGH" : "LOW") + ");");
    set("mask", now.maskHex);
    set("register", now.register.replace("GPIO_OUT_", "").replace("_REG", "") + " (GPIO_OUT)");
    set("address", now.addressHex);
    set("bit", String(bit));
    set("switch", sw === "P" ? out.switch.dataset.p : out.switch.dataset.n);
    set("volts", num(pin.volts) + " V");
    set("led", pin.led ? out.led.dataset.on : out.led.dataset.off);
    prev.disabled = step === 1; next.disabled = step === STAGES.length;
    level.textContent = high ? level.dataset.low : level.dataset.high;
    play.textContent = timer ? play.dataset.pause : play.dataset.play;
  }
  function stop() { clearInterval(timer); timer = 0; }
  function tick() { if (!visible) return; if (step < STAGES.length) { step++; draw(); } else { stop(); draw(); } }
  prev.addEventListener("click", () => { stop(); step = Math.max(1, step - 1); draw(); });
  next.addEventListener("click", () => { stop(); step = Math.min(STAGES.length, step + 1); draw(); });
  level.addEventListener("click", () => { stop(); high = !high; step = 1; draw(); });
  play.addEventListener("click", () => {
    if (timer) { stop(); draw(); return; }
    if (step === STAGES.length) step = 1;
    if (still.matches) { step = STAGES.length; draw(); return; }
    timer = setInterval(tick, STEP_S * 1000);
    draw();
  });
  new IntersectionObserver((e) => { visible = e[e.length - 1].isIntersecting; }).observe(svg);
  q("[data-fig-controls]").hidden = false;
  draw();
});
})();
`;

const write = (path, text) => {
  mkdirSync(dirname(path), { recursive: true });
  writeFileSync(path, text.replace(/\r\n/g, "\n"));
};
const svgPath = OUT ? join(OUT, "pin_path.svg") : join(ROOT, "templates", "figures", "pin_path.svg");
const jsPath = OUT ? join(OUT, "pin_path.js") : join(ROOT, "static", "acad", "js", "figures", "pin_path.js");
write(svgPath, svg + "\n");
write(jsPath, js);
console.log(`wrote ${svgPath} (${Buffer.byteLength(svg)} o), ${jsPath} (${Buffer.byteLength(js)} o)`);
