// Figure « schéma de puissance et schéma de commande » (section 03-puissance-commande de M2, formation moteurs) : platine d'un démarrage direct.
// node tools/figures/power_control/build.mjs [--out <dossier>]
// écrit templates/figures/power_control.svg (dessin sans texte) et static/acad/js/figures/power_control.js (animation).
// Fichiers générés : ne jamais les retoucher à la main, modifier ce script puis le relancer.
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "../kit/iso-kit.mjs";
import { POWER, CONTROL, SHARED } from "./model.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(HERE, "../../..");
const outAt = process.argv.indexOf("--out");
const OUT = outAt > 0 ? resolve(process.argv[outAt + 1]) : null;

const WIDTH = 640;
const HEIGHT = 360;

// Plan (unités monde, z vers le haut ; x vers la droite, y vers l'observateur). Les schémas se lisent de haut en bas : ici, du fond vers l'avant.
// Platine partagée par un trait gravé (x = DIV) : à gauche la puissance (L1 L2 L3, Q1, pôles de KM1, F1, M1), à droite la commande 24 V
// (alimentation, F2, boîte à boutons S1 et S2). KM1 et F1 sont chacun un seul appareil à cheval sur le trait : pôles et relais côté puissance,
// bobine A1-A2, contacts 13-14 et 95-96 côté commande. Conducteurs de puissance : traits épais sur la platine ; fils de commande : aériens, borne à borne.
const PLATE = { x: -112, y: -76, w: 224, d: 158, r: 8 };
const PLATE_H = 6;
const DIV = 14;
const PHASES = [-56, -46, -36];
const DEV = {
  Q1: { plan: { x: -70, y: -62, w: 48, d: 18, r: 2 }, h: 16 },
  KM1p: { plan: { x: -70, y: -32, w: 84, d: 22, r: 2 }, h: 18 },
  KM1c: { plan: { x: DIV, y: -32, w: 40, d: 22, r: 2 }, h: 18 },
  F1p: { plan: { x: -70, y: -2, w: 84, d: 16, r: 2 }, h: 14 },
  F1c: { plan: { x: DIV, y: -2, w: 24, d: 16, r: 2 }, h: 14 },
  SUP: { plan: { x: 62, y: -66, w: 38, d: 18, r: 2 }, h: 14 },
  F2: { plan: { x: 66, y: -38, w: 16, d: 12, r: 2 }, h: 10 },
  STN: { plan: { x: 60, y: 24, w: 44, d: 22, r: 3 }, h: 10 },
  BOX: { plan: { x: -60, y: 20, w: 28, d: 10, r: 1 }, h: 12 },
};
const MOTOR = { x: -46, y: 52, r: 18, h: 22 };
const SHAFT = { r: 3, h: 6 };
const KEY_R = 2.6;
const BUTTONS = { s1: [72, 35], s2: [92, 35] };
const PRESS_DZ = 2.5;
const KM_SLIDE = 10;
const TRIP_DZ = 3;
// Bornes (dessus des appareils) : alimentation + et 0 V, fusible, 95-96, A1-A2, 13-14, bornes de la boîte à boutons.
const top = (key) => DEV[key].h;
const PIN = {
  plus: [72, -57, top("SUP")], zero: [90, -57, top("SUP")],
  f2in: [74, -36, top("F2")], f2out: [74, -28, top("F2")],
  p95: [30, 2, top("F1c")], p96: [30, 10, top("F1c")],
  a1: [24, -27, top("KM1c")], a2: [24, -13, top("KM1c")], p13: [44, -27, top("KM1c")], p14: [44, -13, top("KM1c")],
  s1in: [66, 28, top("STN")], node: [82, 28, top("STN")], s2out: [98, 28, top("STN")],
};
// Fils de commande dans l'ordre du chemin : + → F2 → 95-96 → S1 → (S2 ∥ 13-14) → A1-A2 → 0 V, chacun à sa hauteur.
const WIRES = [["plus", "f2in", 22], ["f2out", "p95", 27], ["p96", "s1in", 25], ["node", "p13", 31], ["s2out", "p14", 29], ["p14", "a1", 21], ["a2", "zero", 33]];

const P = k.fitProjection(k.boxCorners(PLATE, -PLATE_H - 4, 34), WIDTH, HEIGHT, { pad: 14, azimuth: 50 });

const at = (point) => k.iso(point, P);
const S = (paths, style) => k.solidSvg(paths, style);
const L = (d, style) => k.lineSvg(d, style);
const D = (points, style) => k.dotsSvg(points, style);
const depth = (x, y, z = 0) => k.depthOf([x, y, z], P);
const poly = (points) => k.pathOf(points.map(at));
const shift = ([dx, dy, dz]) => { const o = at([0, 0, 0]), e = at([dx, dy, dz]); return `translate(${(e[0] - o[0]).toFixed(3)} ${(e[1] - o[1]).toFixed(3)})`; };

// Sans JavaScript : vue du schéma de puissance, moteur arrêté.
const VIEW0 = "power";
const VIEWS = {
  power: ["Q1", "KM1p", "F1p", "M1"],
  control: ["SUP", "F2", "F1c", "STN", "KM1c"],
  link: ["KM1p", "KM1c", "F1p", "F1c"],
};
const litAt = (key) => VIEWS[VIEW0].includes(key);

// Repères gravés en traits (pas de texte dans le dessin, F11).
const CW = 3.2;
const CH = 5.5;
const GLYPHS = {
  1: [[[0.2, 0.25], [0.6, 0], [0.6, 1]]],
  2: [[[0, 0.2], [0.2, 0], [0.8, 0], [1, 0.2], [1, 0.38], [0, 1], [1, 1]]],
  Q: [[[0.5, 0], [0.15, 0.1], [0, 0.5], [0.15, 0.9], [0.5, 1], [0.85, 0.9], [1, 0.5], [0.85, 0.1], [0.5, 0]], [[0.6, 0.7], [1, 1]]],
  K: [[[0, 0], [0, 1]], [[1, 0], [0, 0.6]], [[0.35, 0.4], [1, 1]]],
  M: [[[0, 1], [0, 0], [0.5, 0.6], [1, 0], [1, 1]]],
  F: [[[1, 0], [0, 0], [0, 1]], [[0, 0.5], [0.75, 0.5]]],
  S: [[[1, 0.12], [0.8, 0], [0.2, 0], [0, 0.15], [0, 0.38], [0.2, 0.5], [0.8, 0.5], [1, 0.62], [1, 0.85], [0.8, 1], [0.2, 1], [0, 0.88]]],
};
const ADVANCE = CW + 1.2;
function engrave(text, x0, yc, z) {
  return [...text].map((ch, i) => GLYPHS[ch].map((line) => k.onTop(line.map(([u, v]) => [x0 + i * ADVANCE + u * CW, yc - CH / 2 + v * CH]), z, P)).join("")).join("");
}
const tag = (text, x0, yc, z) => `<path class="iso-line" data-tone="hi" data-free="" style="stroke-width:1" d="${engrave(text, x0, yc, z)}"/>`;

function plate() {
  const out = [`<path class="iso-halo" d="${k.haloOf(PLATE, -PLATE_H - 4, PLATE_H, P)}"/>`];
  const feet = [...k.corners(PLATE, 22)].sort((a, b) => depth(...a) - depth(...b));
  for (const [x, y] of feet) out.push(S(k.cylinder(x, y, 6, -PLATE_H - 4, 4, P, 8), { tone: "mid" }));
  out.push(S(k.slabOf(PLATE, -PLATE_H, PLATE_H, P, 6, 1.4), { tone: "mid" }));
  const screws = k.corners(PLATE, 9);
  out.push(L(screws.map(([x, y]) => k.ring(x, y, 2.2, 0, P, 12)).join(""), { tone: "lo" }));
  out.push(D(screws.map(([x, y]) => at([x, y, 0])), { size: 0.5 }));
  // Trait gravé entre la zone de puissance et la zone de commande, du bord du fond au bord de devant.
  out.push(L(k.lineOnTop([DIV, PLATE.y], [DIV, PLATE.y + PLATE.d], 0, P), { tone: "lo", dashed: true }));
  return out.join("");
}

// L1 L2 L3 : arrivée par le bord du fond, puis Q1 → KM1 → F1 → boîte à bornes du moteur ; [y départ, z départ, y arrivée, z arrivée, hauteur].
const RUNS = {
  Q1: [PLATE.y, 0, -58, top("Q1"), 22],
  KM1p: [-48, top("Q1"), -27, top("KM1p"), 25],
  F1p: [-13, top("KM1p"), 2, top("F1p"), 24],
  BOX: [10, top("F1p"), 25, top("BOX"), 20],
};
function powerRun(key) {
  const [y0, z0, y1, z1, lane] = RUNS[key];
  const d = PHASES.map((x) => poly([[x, y0, z0], [x, y0, lane], [x, y1, lane], [x, y1, z1]])).join("");
  const ends = PHASES.flatMap((x) => (z0 ? [at([x, y0, z0])] : []).concat([at([x, y1, z1])]));
  return `<g data-wire="power"><path class="iso-line" data-tone="lo" style="stroke-width:1.6" d="${d}"/></g>` + D(ends, { size: 0.9, tone: "hi" });
}

const solid = (key, extra = "") => {
  const { plan, h } = DEV[key];
  return `<g data-dev="${key}">${S(k.slabOf(plan, 0, h, P, 3, 0.6), { tone: "mid", lit: litAt(key) })}</g>${extra}`;
};
const pins = (keys) => L(keys.map((p) => k.ring(PIN[p][0], PIN[p][1], 2.2, PIN[p][2], P, 12)).join(""), { tone: "lo" });

const parts = {
  Q1: () => {
    const { plan, h } = DEV.Q1;
    const cx = plan.x + plan.w / 2, cy = plan.y + plan.d / 2;
    return solid("Q1") + S(k.cylinder(cx, cy, 6, h, 2.5, P, 16), { tone: "hi", crease: "lo" })
      + S(k.slabOf({ x: cx - 2, y: plan.y + 1, w: 4, d: plan.d - 2, r: 1 }, h + 2.5, 2, P, 2), { tone: "hi", crease: "none" })
      + L(PHASES.map((x) => k.ring(x, -58, 2.2, h, P, 12) + k.ring(x, -48, 2.2, h, P, 12)).join(""), { tone: "lo" })
      + tag("Q1", -32, -53, h);
  },
  KM1p: () => {
    const { plan, h } = DEV.KM1p;
    const rings = L(PHASES.map((x) => k.ring(x, -27, 2.2, h, P, 12) + k.ring(x, -13, 2.2, h, P, 12)).join(""), { tone: "lo" });
    // Fenêtre de l'indicateur de position et indicateur (coulisse quand KM1 se ferme).
    const win = { x: -20, y: -22, w: 30, d: 6, r: 1 };
    return solid("KM1p", rings + L(k.planOutline(win, h, P), { tone: "lo" })
      + `<g data-part="km">${S(k.slabOf({ x: win.x + 1, y: win.y + 1, w: 6, d: 4, r: 0.5 }, h, 1.2, P, 1), { tone: "hi", crease: "none" })}</g>`
      + tag("KM1", -31, -12, h));
  },
  KM1c: () => solid("KM1c", pins(["a1", "a2", "p13", "p14"])),
  F1p: () => {
    const { plan, h } = DEV.F1p;
    return solid("F1p", L(PHASES.map((x) => k.ring(x, 2, 2.2, h, P, 12) + k.ring(x, 10, 2.2, h, P, 12)).join(""), { tone: "lo" })
      + `<g data-part="f1">${S(k.cylinder(-14, 6, 3, h, 2, P, 12), { tone: "hi", crease: "lo" })}</g>`
      + tag("F1", -30, 6, h));
  },
  F1c: () => solid("F1c", pins(["p95", "p96"])),
  SUP: () => solid("SUP", ["plus", "zero"].map((p) => S(k.cylinder(PIN[p][0], PIN[p][1], 2.6, PIN[p][2], 2, P, 10), { tone: "hi", crease: "lo" })).join("")
    + L(k.planOutline(k.insetPlan(DEV.SUP.plan, 3), top("SUP"), P), { tone: "faint" })),
  F2: () => solid("F2", S(k.cylinder(74, -32, 3, top("F2"), 2.5, P, 12), { tone: "hi", crease: "lo" }) + tag("F2", 66.5, -26 + 4, 0)),
  STN: () => {
    const z = top("STN");
    const caps = Object.entries(BUTTONS).map(([key, [x, y]]) =>
      L(k.ring(x, y, 7.5, z, P, 18), { tone: "lo" }) + `<g data-part="${key}">${S(k.cylinder(x, y, 6, z, 4, P, 16), { tone: "hi", crease: "lo" })}</g>`).join("");
    return solid("STN", pins(["s1in", "node", "s2out"]) + caps + tag("S1", 68, 43, z) + tag("S2", 88, 43, z));
  },
  BOX: () => solid("BOX", L(PHASES.map((x) => k.ring(x, 25, 2.2, top("BOX"), P, 12)).join(""), { tone: "lo" })),
  M1: () => {
    const { x, y, r, h } = MOTOR;
    const body = S(k.cylinder(x, y, r, 0, h, P, 24, 1), { tone: "mid", lit: litAt("M1") });
    const fins = L([6, 11, 16].map((z) => k.sideArc(x, y, r, z, P, 24)).join(""), { tone: "lo" });
    const shaft = S(k.cylinder(x, y, SHAFT.r, h, SHAFT.h, P, 12), { tone: "hi", crease: "lo" });
    const key = L(k.lineOnTop([x, y], [x + KEY_R, y], h + SHAFT.h, P), { tone: "lit", free: true });
    return `<g data-dev="M1">${body}</g>${fins}${L(k.ring(x, y, r - 5, h, P, 24), { tone: "lo" })}${shaft}<g data-part="key">${key}</g>` + tag("M1", x - 4, y + r + 6, 0);
  },
};

function wires() {
  // Fils de commande aériens : de la borne de départ, montée, traversée à sa hauteur, descente sur la borne d'arrivée.
  const d = WIRES.map(([a, b, lane]) => poly([PIN[a], [PIN[a][0], PIN[a][1], lane], [PIN[b][0], PIN[b][1], lane], PIN[b]])).join("");
  const ends = WIRES.flatMap(([a, b]) => [at(PIN[a]), at(PIN[b])]);
  return `<g data-wire="control"><path class="iso-line" data-tone="lo" style="stroke-width:0.9" d="${d}"/></g>` + D(ends, { size: 0.8, tone: "hi" });
}

// Appareils peints du fond vers l'avant.
const center = (key) => key === "M1" ? [MOTOR.x, MOTOR.y] : [DEV[key].plan.x + DEV[key].plan.w / 2, DEV[key].plan.y + DEV[key].plan.d / 2];
const order = Object.keys(parts).sort((a, b) => depth(...center(a)) - depth(...center(b)));

const body = [plate(), ...order.map((key) => parts[key]() + (RUNS[key] ? powerRun(key) : "")), wires()];

const svg = k
  .figureSvg({ width: WIDTH, height: HEIGHT, label: "", body })
  .replace(' role="img" aria-label=""', ' aria-hidden="true" focusable="false"');

// Projection linéaire : écran = o + x·ex + y·ey + z·ez (exacte en isométrie).
const o = at([0, 0, 0]);
const vec = (v) => at(v).map((c, i) => +(c - o[i]).toFixed(5));
const model = readFileSync(join(HERE, "model.mjs"), "utf8").replace(/^export /gm, "").replace(/^\/\/.*\n/gm, "");
const keyTop = [MOTOR.x, MOTOR.y, MOTOR.h + SHAFT.h];

const js = `// Généré par tools/figures/power_control/build.mjs : ne pas modifier à la main.
(() => {
${model}const O = ${JSON.stringify(o.map((c) => +c.toFixed(3)))}, EX = ${JSON.stringify(vec([1, 0, 0]))}, EY = ${JSON.stringify(vec([0, 1, 0]))}, EZ = ${JSON.stringify(vec([0, 0, 1]))};
const VIEWS = ${JSON.stringify(VIEWS)}, KEY = ${JSON.stringify(keyTop)}, KEY_R = ${KEY_R};
const scr = (x, y, z) => [O[0] + x * EX[0] + y * EY[0] + z * EZ[0], O[1] + x * EX[1] + y * EY[1] + z * EZ[1]];
const move = (dx, dy, dz) => "translate(" + (EX[0] * dx + EY[0] * dy + EZ[0] * dz).toFixed(3) + " " + (EX[1] * dx + EY[1] * dy + EZ[1] * dz).toFixed(3) + ")";
document.querySelectorAll('.fig[data-fig="power_control"]').forEach((card) => {
  const q = (s) => card.querySelector(s), qa = (s) => [...card.querySelectorAll(s)];
  const svg = q("svg"), part = (k) => q('[data-part="' + k + '"]'), key = q('[data-part="key"] path');
  const views = qa("[data-fig-preset]"), trip = q("[data-fig-trip]"), out = {};
  qa("[data-fig-out]").forEach((el) => { out[el.dataset.figOut] = el; });
  const still = matchMedia("(prefers-reduced-motion: reduce)");
  let s = REST, view = "power", angle = 0, last = 0, frame = 0, visible = true;
  const timers = {};
  function light() {
    qa('[data-dev] .iso-solid').forEach((el) => {
      const on = VIEWS[view].includes(el.parentNode.dataset.dev);
      if (on) el.setAttribute("data-lit", ""); else el.removeAttribute("data-lit");
    });
    views.forEach((b) => b.setAttribute("aria-pressed", b.dataset.figPreset === view ? "true" : "false"));
  }
  function pose() {
    const st = states(s);
    part("s1").setAttribute("transform", move(0, 0, s.s1 ? -${PRESS_DZ} : 0));
    part("s2").setAttribute("transform", move(0, 0, s.s2 ? -${PRESS_DZ} : 0));
    part("km").setAttribute("transform", move(st.poles ? ${KM_SLIDE} : 0, 0, 0));
    part("f1").setAttribute("transform", move(0, 0, s.f1 ? ${TRIP_DZ} : 0));
    qa('[data-wire="power"] path').forEach((w) => w.setAttribute("data-tone", st.motor ? "hi" : "lo"));
    q('[data-wire="control"] path').setAttribute("data-tone", st.coil ? "hi" : "lo");
    const a = scr(...KEY), b = scr(KEY[0] + KEY_R * Math.cos(angle), KEY[1] + KEY_R * Math.sin(angle), KEY[2]);
    key.setAttribute("d", "M" + a[0].toFixed(2) + " " + a[1].toFixed(2) + "L" + b[0].toFixed(2) + " " + b[1].toFixed(2));
  }
  function report() {
    const st = states(s), set = (k, v) => { if (out[k] && out[k].textContent !== v) out[k].textContent = v; };
    set("view", out.view.dataset[view]);
    set("role", out.role.dataset[view]);
    set("coil", st.coil ? out.coil.dataset.on : out.coil.dataset.off);
    set("c1314", st.c1314 ? out.c1314.dataset.closed : out.c1314.dataset.open);
    set("f9596", st.f9596 ? out.f9596.dataset.closed : out.f9596.dataset.open);
    set("motor", st.motor ? out.motor.dataset.on : out.motor.dataset.off);
    trip.setAttribute("aria-pressed", s.f1 ? "true" : "false");
    trip.textContent = s.f1 ? trip.dataset.reset : trip.dataset.trip;
  }
  function tick(now) {
    angle += (last ? Math.min(now - last, 100) / 1000 : 0) * 2 * Math.PI / TURN_S;
    last = now;
    pose();
    frame = states(s).motor && visible && !still.matches ? requestAnimationFrame(tick) : 0;
  }
  const run = () => { if (!frame && states(s).motor && visible && !still.matches) { last = 0; frame = requestAnimationFrame(tick); } };
  const apply = (event) => { s = step(s, event); pose(); report(); run(); };
  function press(button) {
    clearTimeout(timers[button]);
    apply(button + "-down");
    timers[button] = setTimeout(() => apply(button + "-up"), still.matches ? 0 : PRESS_S * 1000);
  }
  qa("[data-fig-press]").forEach((b) => b.addEventListener("click", () => press(b.dataset.figPress)));
  trip.addEventListener("click", () => apply(s.f1 ? "reset" : "trip"));
  views.forEach((b) => b.addEventListener("click", () => { view = b.dataset.figPreset; light(); report(); }));
  new IntersectionObserver((e) => { visible = e[e.length - 1].isIntersecting; run(); }).observe(svg);
  q("[data-fig-controls]").hidden = false;
  light();
  pose();
  report();
});
})();
`;

const write = (path, text) => {
  mkdirSync(dirname(path), { recursive: true });
  writeFileSync(path, text.replace(/\r\n/g, "\n"));
};
// Les vues reprennent les appareils du modèle : puissance, commande et appareils communs.
const parent = (key) => key.replace(/[pc]$/, "").replace(/^(SUP|STN|BOX)$/, "");
for (const [view, list] of [["power", POWER], ["control", CONTROL], ["link", SHARED]]) {
  const named = [...new Set(VIEWS[view].map(parent).filter(Boolean))];
  if (named.some((d) => !list.includes(d))) throw new Error(`vue ${view} hors du modèle : ${named}`);
}
const svgPath = OUT ? join(OUT, "power_control.svg") : join(ROOT, "templates", "figures", "power_control.svg");
const jsPath = OUT ? join(OUT, "power_control.js") : join(ROOT, "static", "acad", "js", "figures", "power_control.js");
write(svgPath, svg + "\n");
write(jsPath, js);
console.log(`wrote ${svgPath} (${Buffer.byteLength(svg)} o), ${jsPath} (${Buffer.byteLength(js)} o)`);
