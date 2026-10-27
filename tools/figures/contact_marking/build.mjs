// Figure « repères des bornes et des contacts » (section 02-reperage de M2, formation moteurs) : contacteur KM1 et son bloc auxiliaire.
// node tools/figures/contact_marking/build.mjs [--out <dossier>]
// écrit templates/figures/contact_marking.svg (dessin sans texte) et static/acad/js/figures/contact_marking.js (animation).
// Fichiers générés : ne jamais les retoucher à la main, modifier ce script puis le relancer.
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "../kit/iso-kit.mjs";
import { STROKE, marking, pole, offset } from "./model.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(HERE, "../../..");
const outAt = process.argv.indexOf("--out");
const OUT = outAt > 0 ? resolve(process.argv[outAt + 1]) : null;

const WIDTH = 640;
const HEIGHT = 360;

// Plan (unités monde, z vers le haut ; x vers la droite, y vers l'observateur).
// Sur une platine : une alimentation 24 V, le contacteur (bobine A1-A2, pôles 1-2, 3-4, 5-6) et son bloc auxiliaire
// (13-14, 21-22, 31-32, 43-44). Les repères sont gravés sur le dessus, entrées impaires au fond, sorties paires devant.
// Une fenêtre montre l'intérieur : deux plots par contact, reliés à leurs bornes, et un pont porté par l'équipage mobile,
// qui coulisse vers la droite de STROKE quand la bobine est alimentée. Un contact est fermé quand son pont recouvre ses plots.
const PLATE = { x: -150, y: -50, w: 258, d: 100, r: 8 };
const PLATE_H = 8;
const FOOT_H = 4;
const RAIL = { x: -146, y: -9, w: 250, d: 18, r: 1 };
const RAIL_H = 3;
const BASE = RAIL_H; // dessous des appareils
const SUP = { x: -142, y: -26, w: 40, d: 52, r: 3 };
const SUP_H = 18;
const BODY = { x: -88, y: -42, w: 106, d: 84, r: 3 };
const AUX = { x: 20, y: -42, w: 80, d: 84, r: 3 };
const H = 28;
const T = BASE + H; // dessus du contacteur et du bloc
const ROW = 30; // bornes : y = −ROW (entrées impaires), y = +ROW (sorties paires)
const SCREW_R = 3.2;
const STUD = 7; // plots : de y = ±5 à ±9
const COIL_X = -76;
// Contacts : clé, colonne, fonction, repères (tirés du modèle).
const CONTACTS = [
  ...[1, 2, 3].map((n) => ({ key: `p${n}`, x: -54 + (n - 1) * 22, kind: "make", marks: pole(n).map(String) })),
  ...[[1, "make"], [2, "break"], [3, "break"], [4, "make"]].map(([n, kind], i) => ({ key: `c${n}`, x: 34 + i * 18, kind, marks: marking(n, kind) })),
];
const WIN_BODY = { x: -84, y: -14, w: 96, d: 28, r: 2 };
const WIN_AUX = { x: 25, y: -14, w: 70, d: 28, r: 2 };
const CAR_BODY = { x: -68, y: -2.5, w: 66, d: 5, r: 1 };
const CAR_AUX = { x: 26, y: -2.5, w: 66, d: 5, r: 1 };

const P = k.fitProjection(k.boxCorners(PLATE, -PLATE_H - FOOT_H, T + 4), WIDTH, HEIGHT, { pad: 16, azimuth: 60 });

const at = (point) => k.iso(point, P);
const S = (paths, style) => k.solidSvg(paths, style);
const L = (d, style) => k.lineSvg(d, style);
const D = (points, style) => k.dotsSvg(points, style);
const depth = (x, y, z = 0) => k.depthOf([x, y, z], P);
const poly = (points) => k.pathOf(points.map(at));
const top = (from, to) => k.lineOnTop(from, to, T, P);

// Repères gravés : chiffres et lettre A en traits (pas de texte dans le dessin, F11). Cellule de CW × CH, y vers l'observateur.
const CW = 4;
const CH = 7;
const GLYPHS = {
  1: [[[0.2, 0.25], [0.6, 0], [0.6, 1]]],
  2: [[[0, 0.2], [0.2, 0], [0.8, 0], [1, 0.2], [1, 0.38], [0, 1], [1, 1]]],
  3: [[[0, 0], [1, 0], [0.45, 0.4], [0.8, 0.45], [1, 0.65], [1, 0.85], [0.8, 1], [0.2, 1], [0, 0.85]]],
  4: [[[0.75, 1], [0.75, 0], [0, 0.68], [1, 0.68]]],
  5: [[[1, 0], [0, 0], [0, 0.45], [0.7, 0.42], [1, 0.6], [1, 0.85], [0.8, 1], [0, 1]]],
  6: [[[0.9, 0], [0.35, 0], [0, 0.4], [0, 0.85], [0.2, 1], [0.8, 1], [1, 0.85], [1, 0.6], [0.8, 0.45], [0, 0.5]]],
  A: [[[0, 1], [0.5, 0], [1, 1]], [[0.22, 0.58], [0.78, 0.58]]],
};
const ADVANCE = CW + 1.4;
// Repère aligné à droite sur xr, centré en yc.
function engrave(text, xr, yc) {
  const x0 = xr - text.length * ADVANCE + 1.4;
  return [...text].map((ch, i) => GLYPHS[ch].map((line) => k.onTop(line.map(([u, v]) => [x0 + i * ADVANCE + u * CW, yc - CH / 2 + v * CH]), T, P)).join("")).join("");
}

function plate() {
  const out = [`<path class="iso-halo" d="${k.haloOf(PLATE, -PLATE_H - FOOT_H, PLATE_H, P)}"/>`];
  const feet = [...k.corners(PLATE, 20)].sort((a, b) => depth(...a) - depth(...b));
  for (const [x, y] of feet) out.push(S(k.cylinder(x, y, 6, -PLATE_H - FOOT_H, FOOT_H, P, 8), { tone: "mid" }));
  out.push(S(k.slabOf(PLATE, -PLATE_H, PLATE_H, P, 5, 1.4), { tone: "mid" }));
  const screws = k.corners(PLATE, 9);
  out.push(L(screws.map(([x, y]) => k.ring(x, y, 2.2, 0, P, 12)).join(""), { tone: "lo" }));
  out.push(D(screws.map(([x, y]) => at([x, y, 0])), { size: 0.5 }));
  out.push(S(k.slabOf(RAIL, 0, RAIL_H, P, 2), { tone: "mid" }));
  return out.join("");
}

function supply() {
  // Alimentation 24 V (adaptateur sur rail) : deux bornes sur le dessus.
  const out = [S(k.slabOf(SUP, BASE, SUP_H, P, 3, 0.6), { tone: "mid" })];
  out.push(L(k.planOutline(k.insetPlan(SUP, 4), BASE + SUP_H, P), { tone: "faint" }));
  for (const y of [-14, 14]) out.push(S(k.cylinder(-122, y, 2.6, BASE + SUP_H, 2.5, P, 10), { tone: "hi", crease: "lo" }));
  return out.join("");
}

function screw(x, y, key) {
  const head = S(k.cylinder(x, y, SCREW_R, T, 1.2, P, 12), { tone: "hi", crease: "lo" });
  const slot = L(k.lineOnTop([x - SCREW_R, y], [x + SCREW_R, y], T + 1.2, P), { tone: "lo" });
  return `<g data-screw="${key}">${head}${slot}</g>`;
}

function box(plan) {
  return S(k.slabOf(plan, BASE, H, P, 3, 0.8), { tone: "mid" });
}

function terminals(columns) {
  // Pour chaque colonne : creux des bornes, vis, repères gravés et piste de la borne à son plot (ou à la bobine).
  const out = [];
  for (const { x, key, marks, to } of columns) {
    out.push(L(k.ring(x, -ROW, SCREW_R + 1, T, P, 14) + k.ring(x, ROW, SCREW_R + 1, T, P, 14), { tone: "lo" }));
    out.push(L(top([x, -ROW + SCREW_R + 1], [x, -to]) + top([x, ROW - SCREW_R - 1], [x, to]), { tone: "faint" }));
    out.push(`<path class="iso-line" data-tone="hi" data-free="" style="stroke-width:1" d="${engrave(marks[0], x - 3, -ROW + 10) + engrave(marks[1], x - 3, ROW - 10)}"/>`);
    out.push(screw(x, -ROW, key), screw(x, ROW, key));
  }
  return out.join("");
}

function studs(columns) {
  return columns.map(({ x }) => [-1, 1].map((s) => S(k.slabOf({ x: x - 1, y: s > 0 ? 5 : -9, w: 2, d: 4, r: 0 }, T, 0.8, P, 1), { tone: "mid", crease: "none" })).join("")).join("");
}

const bridge = ({ key, x, kind }) =>
  `<g data-contact="${key}">${S(k.slabOf({ x: x - 1 + offset(kind, 0), y: -9, w: 2, d: 18, r: 0 }, T + 0.8, 1, P, 1), { tone: "hi", crease: "none", lit: key === LIT0 })}</g>`;
const carriage = (plan, columns) =>
  `<g data-part="carriage" transform="${shift(STROKE * T0)}">${S(k.slabOf(plan, T, 0.8, P, 2), { tone: "mid", crease: "none" })}${columns.map(bridge).join("")}</g>`;

function coil() {
  // Bobine visible dans la fenêtre : noyau et spires, reliée à A1 et A2.
  const plan = { x: COIL_X - 6, y: -8, w: 12, d: 16, r: 1 };
  const turns = [-5, -3, -1, 1, 3, 5].map((y) => k.lineOnTop([plan.x, y], [plan.x + plan.w, y], T + 2.5, P)).join("");
  return `<g data-coil="">${S(k.slabOf(plan, T, 2.5, P, 2), { tone: "hi", crease: "lo", lit: LIT0 === "coil" })}</g>` + L(turns, { tone: "lo" });
}

function cables() {
  // Alimentation → A1 (au fond) et A2 (devant) ; chaque câble se pose sur la vis.
  return [-1, 1].map((s) => {
    const r = [[-122, 14 * s, BASE + SUP_H + 2.5], [-122, 14 * s, T + 5], [-96, ROW * s, T + 5], [COIL_X - SCREW_R, ROW * s, T + 1.2]];
    return L(poly(r), { tone: "hi" }) + D([at(r[0]), at(r[r.length - 1])], { size: 0.8, tone: "hi" });
  }).join("");
}

// Sans JavaScript : bobine non alimentée, contact 13-14 en teal.
const T0 = 0;
const LIT0 = "c1";
const shift = (dx) => { const o = at([0, 0, 0]), e = at([dx, 0, 0]); return `translate(${(e[0] - o[0]).toFixed(3)} ${(e[1] - o[1]).toFixed(3)})`; };

const powerCols = CONTACTS.filter((c) => c.key[0] === "p").map((c) => ({ ...c, to: 9 }));
const auxCols = CONTACTS.filter((c) => c.key[0] === "c").map((c) => ({ ...c, to: 9 }));
const coilCol = { x: COIL_X, key: "coil", marks: ["A1", "A2"], to: 8 };

const body = [
  plate(),
  supply(),
  box(BODY),
  L(k.planOutline(WIN_BODY, T, P), { tone: "lo" }),
  terminals([coilCol, ...powerCols]),
  coil(),
  studs(powerCols),
  carriage(CAR_BODY, powerCols),
  box(AUX),
  L(k.planOutline(WIN_AUX, T, P), { tone: "lo" }),
  terminals(auxCols),
  studs(auxCols),
  carriage(CAR_AUX, auxCols),
  cables(),
];

const svg = k
  .figureSvg({ width: WIDTH, height: HEIGHT, label: "", body })
  .replace(' role="img" aria-label=""', ' aria-hidden="true" focusable="false"');

// Projection linéaire : écran = o + x·ex + y·ey + z·ez (exacte en isométrie).
const o = at([0, 0, 0]);
const ex = at([1, 0, 0]).map((c, i) => +(c - o[i]).toFixed(5));
const model = readFileSync(join(HERE, "model.mjs"), "utf8").replace(/^export /gm, "").replace(/^\/\/.*\n/gm, "");
const table = CONTACTS.map(({ key, kind, marks }) => [key, kind, marks.join("-")]);

const js = `// Généré par tools/figures/contact_marking/build.mjs : ne pas modifier à la main.
(() => {
${model}const EX = ${JSON.stringify(ex)}, CONTACTS = ${JSON.stringify(table)};
const shift = (dx) => "translate(" + (EX[0] * dx).toFixed(3) + " " + (EX[1] * dx).toFixed(3) + ")";
document.querySelectorAll('.fig[data-fig="contact_marking"]').forEach((card) => {
  const q = (s) => card.querySelector(s), qa = (s) => [...card.querySelectorAll(s)];
  const svg = q("svg"), cars = qa('[data-part="carriage"]'), power = q("[data-fig-power]"), presets = qa("[data-fig-preset]"), out = {};
  qa("[data-fig-out]").forEach((el) => { out[el.dataset.figOut] = el; });
  const lang = document.documentElement.lang || "fr", still = matchMedia("(prefers-reduced-motion: reduce)");
  let sel = "c1", t = 0, target = 0, last = 0, frame = 0, visible = true;
  const solids = (key) => qa('[data-contact="' + key + '"] .iso-solid, [data-screw="' + key + '"] .iso-solid' + (key === "coil" ? ", [data-coil] .iso-solid" : ""));
  function light() {
    qa(".iso-solid[data-lit]").forEach((el) => el.removeAttribute("data-lit"));
    solids(sel).forEach((el) => el.setAttribute("data-lit", ""));
    presets.forEach((b) => b.setAttribute("aria-pressed", b.dataset.figPreset === sel ? "true" : "false"));
  }
  function report() {
    const row = sel === "coil" ? null : CONTACTS.find((c) => c[0] === sel);
    const set = (k, v) => { if (out[k] && out[k].textContent !== v) out[k].textContent = v; };
    set("mark", row ? row[2] : "A1-A2");
    const first = row && row[0][0] === "c" ? decode(...row[2].split("-")) : null;
    set("order", first ? new Intl.NumberFormat(lang).format(first.order) : out.order.dataset.none);
    set("kind", row ? (row[0][0] === "p" ? out.kind.dataset.pole : out.kind.dataset[row[1]]) : out.kind.dataset.coil);
    set("state", row ? (closed(row[1], t) ? out.state.dataset.closed : out.state.dataset.open) : (target ? out.state.dataset.on : out.state.dataset.off));
  }
  function pose() { cars.forEach((g) => g.setAttribute("transform", shift(STROKE * t))); }
  function tick(now) {
    const step = last ? Math.min(now - last, 100) / 1000 / TRAVEL_S : 0;
    last = now;
    t = target ? Math.min(1, t + step) : Math.max(0, t - step);
    pose();
    report();
    frame = t !== target && visible && !still.matches ? requestAnimationFrame(tick) : 0;
  }
  const run = () => { if (!frame && t !== target) { if (still.matches) { t = target; pose(); report(); } else if (visible) { last = 0; frame = requestAnimationFrame(tick); } } };
  power.addEventListener("click", () => {
    target = target ? 0 : 1;
    power.setAttribute("aria-pressed", target ? "true" : "false");
    power.textContent = target ? power.dataset.off : power.dataset.on;
    report();
    run();
  });
  presets.forEach((b) => b.addEventListener("click", () => { sel = b.dataset.figPreset; light(); report(); }));
  new IntersectionObserver((e) => { visible = e[e.length - 1].isIntersecting; run(); }).observe(svg);
  q("[data-fig-controls]").hidden = false;
  light();
  report();
});
})();
`;

const write = (path, text) => {
  mkdirSync(dirname(path), { recursive: true });
  writeFileSync(path, text.replace(/\r\n/g, "\n"));
};
const svgPath = OUT ? join(OUT, "contact_marking.svg") : join(ROOT, "templates", "figures", "contact_marking.svg");
const jsPath = OUT ? join(OUT, "contact_marking.js") : join(ROOT, "static", "acad", "js", "figures", "contact_marking.js");
write(svgPath, svg + "\n");
write(jsPath, js);
console.log(`wrote ${svgPath} (${Buffer.byteLength(svg)} o), ${jsPath} (${Buffer.byteLength(js)} o)`);
