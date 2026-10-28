// Figure « plaque à bornes du moteur » (section 02-reperage de M2, formation moteurs) : couplages étoile et triangle par barrettes droites.
// node tools/figures/terminal_plate/build.mjs [--out <dossier>]
// écrit templates/figures/terminal_plate.svg (dessin sans texte) et static/acad/js/figures/terminal_plate.js (animation).
// Fichiers générés : ne jamais les retoucher à la main, modifier ce script puis le relancer.
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "../kit/iso-kit.mjs";
import { TOP, BOTTOM, LIFT, place, winding, links } from "./model.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(HERE, "../../..");
const outAt = process.argv.indexOf("--out");
const OUT = outAt > 0 ? resolve(process.argv[outAt + 1]) : null;

const WIDTH = 640;
const HEIGHT = 360;

// Plan (unités monde, z vers le haut ; x vers la droite, y vers l'observateur).
// Fond de la boîte à bornes, plaque isolante, six goujons : entrées U1 V1 W1 au fond (y = −ROW), sorties W2 U2 V2 devant (y = +ROW).
// Devant la plaque, les trois enroulements (rangés dans le moteur, ramenés ici pour qu'on les voie) : W, U, V, chacun sous sa sortie ;
// leurs fils sont des pistes sur la plaque, de chaque bout de bobine à sa borne, sans se croiser. Le réseau L1 L2 L3 arrive par un presse-étoupe.
const BOX = { x: -72, y: -66, w: 144, d: 136, r: 8 };
const BOX_H = 10;
const BOARD = { x: -60, y: -40, w: 120, d: 98, r: 4 };
const BOARD_H = 4;
const T = BOARD_H; // dessus de la plaque
const COL = [-30, 0, 30];
const ROW = 14;
const NUT_R = 4.5;
const NUT_H = 2.5;
const PAD = 3.8; // rayon où les pistes rejoignent une borne (sous l'écrou)
const BAR_Z = T + NUT_H; // dessous des barrettes posées
const BAR_H = 1.6;
const STUD_R = 1.6;
const STUD_TOP = T + 8.5;
const COIL_Y = 44;
const COIL_D = 8;
const COIL_W = 20;
const COIL_H = 7;
const GLAND = [0, -54];

const P = k.fitProjection(k.boxCorners(BOX, -BOX_H, STUD_TOP + LIFT + 6), WIDTH, HEIGHT, { pad: 16, azimuth: 60 });

const at = (point) => k.iso(point, P);
const S = (paths, style) => k.solidSvg(paths, style);
const L = (d, style) => k.lineSvg(d, style);
const D = (points, style) => k.dotsSvg(points, style);
const depth = (x, y, z = 0) => k.depthOf([x, y, z], P);
const poly = (points) => k.pathOf(points.map(at));
const xy = (mark) => { const [c, r] = place(mark); return [COL[c], r ? ROW : -ROW]; };

// Sans JavaScript : couplage étoile, enroulement U en teal.
const COUPLING0 = "star";
const LIT0 = "U";

// Repères gravés : lettres et chiffres en traits (pas de texte dans le dessin, F11). Cellule de CW × CH, y vers l'observateur.
const CW = 3;
const CH = 5;
const GLYPHS = {
  1: [[[0.2, 0.25], [0.6, 0], [0.6, 1]]],
  2: [[[0, 0.2], [0.2, 0], [0.8, 0], [1, 0.2], [1, 0.38], [0, 1], [1, 1]]],
  U: [[[0, 0], [0, 0.8], [0.2, 1], [0.8, 1], [1, 0.8], [1, 0]]],
  V: [[[0, 0], [0.5, 1], [1, 0]]],
  W: [[[0, 0], [0.2, 1], [0.5, 0.45], [0.8, 1], [1, 0]]],
};
const ADVANCE = CW + 1.2;
// Repère centré en (xc, yc).
function engrave(text, xc, yc) {
  const x0 = xc - (text.length * ADVANCE - 1.2) / 2;
  return [...text].map((ch, i) => GLYPHS[ch].map((line) => k.onTop(line.map(([u, v]) => [x0 + i * ADVANCE + u * CW, yc - CH / 2 + v * CH]), T, P)).join("")).join("");
}

function box() {
  const out = [`<path class="iso-halo" d="${k.haloOf(BOX, -BOX_H, BOX_H, P)}"/>`];
  out.push(S(k.slabOf(BOX, -BOX_H, BOX_H, P, 6, 1.2), { tone: "mid" }));
  const screws = k.corners(BOX, 7);
  out.push(L(screws.map(([x, y]) => k.ring(x, y, 2.2, 0, P, 12)).join(""), { tone: "lo" }));
  out.push(D(screws.map(([x, y]) => at([x, y, 0])), { size: 0.5 }));
  out.push(S(k.cylinder(...GLAND, 7, 0, 5, P, 18), { tone: "mid", crease: "lo" }));
  out.push(S(k.slabOf(BOARD, 0, BOARD_H, P, 4, 0.6), { tone: "mid" }));
  return out.join("");
}

// Pistes d'un enroulement : chaque bout de bobine rejoint sa borne ; le dernier point se pose sur le bord de la borne.
function pad(points, mark) {
  const [cx, cy] = xy(mark);
  const [px, py] = points[points.length - 1];
  const len = Math.hypot(px - cx, py - cy);
  return [...points, [cx + ((px - cx) / len) * PAD, cy + ((py - cy) / len) * PAD]];
}
function routes(letter) {
  const [start, end] = winding(letter);
  const xc = xy(end)[0]; // la bobine est rangée sous sa sortie
  const back = COIL_Y;
  const [sx, sy] = xy(start);
  const out = [pad([[xc + COIL_W / 2 - 1, back], [xc + COIL_W / 2 - 1, ROW + 12]], end)];
  if (sx < xc) out.push(pad([[xc - COIL_W / 2 + 1, back], [xc - 15, back - 6], [xc - 15, sy]], start));
  else out.push(pad([[xc - COIL_W / 2 + 1, back], [-48, back - 8], [-48, sy - 21], [sx, sy - 21]], start));
  return out;
}

function traces() {
  return ["U", "V", "W"]
    .map((letter) => `<g data-trace="${letter}">${L(routes(letter).map((r) => k.onTop(r, T, P)).join(""), { tone: letter === LIT0 ? "lit" : "lo" })}</g>`)
    .join("");
}

function labels() {
  const marks = [...TOP.map((m) => [m, -ROW - 14]), ...BOTTOM.map((m) => [m, ROW + 9])];
  return `<path class="iso-line" data-tone="hi" data-free="" style="stroke-width:1" d="${marks.map(([m, y]) => engrave(m, xy(m)[0], y)).join("")}"/>`;
}

function nuts() {
  // Écrou de pied et goujon de chaque borne, peints du fond vers l'avant.
  const marks = [...TOP, ...BOTTOM].sort((a, b) => depth(...xy(a)) - depth(...xy(b)));
  return marks.map((m) => {
    const [x, y] = xy(m);
    const nut = S(k.cylinder(x, y, NUT_R, T, NUT_H, P, 6), { tone: "hi", crease: "lo", lit: m[0] === LIT0 });
    const stud = S(k.cylinder(x, y, STUD_R, BAR_Z, STUD_TOP - BAR_Z, P, 10), { tone: "hi", crease: "none" });
    return `<g data-nut="${m[0]}">${nut}</g>${stud}`;
  }).join("");
}

// Barrette : de la première à la dernière borne qu'elle relie, percée sur chaque goujon.
function bar(marks) {
  const pts = marks.map(xy);
  const xs = pts.map((p) => p[0]), ys = pts.map((p) => p[1]);
  const plan = { x: Math.min(...xs) - 4, y: Math.min(...ys) - 3, w: Math.max(...xs) - Math.min(...xs) + 8, d: Math.max(...ys) - Math.min(...ys) + 6, r: 2 };
  if (plan.w < plan.d) Object.assign(plan, { x: xs[0] - 3, w: 6, y: Math.min(...ys) - 4, d: Math.max(...ys) - Math.min(...ys) + 8 });
  return S(k.slabOf(plan, BAR_Z, BAR_H, P, 3), { tone: "hi", crease: "lo" }) + L(pts.map(([x, y]) => k.ring(x, y, STUD_R + 0.6, BAR_Z + BAR_H, P, 10)).join(""), { tone: "lo" });
}
const lift = (dz) => { const o = at([0, 0, 0]), e = at([0, 0, dz]); return `translate(${(e[0] - o[0]).toFixed(3)} ${(e[1] - o[1]).toFixed(3)})`; };
function bars(coupling) {
  const shown = coupling === COUPLING0;
  const sorted = links(coupling).slice().sort((a, b) => depth(...xy(a[0])) - depth(...xy(b[0])));
  return `<g data-part="${coupling}"${shown ? "" : ` visibility="hidden" transform="${lift(LIFT)}"`}>${sorted.map(bar).join("")}</g>`;
}

// Bouts des goujons, au-dessus des barrettes posées.
function tips() {
  return [...TOP, ...BOTTOM].sort((a, b) => depth(...xy(a)) - depth(...xy(b)))
    .map((m) => S(k.cylinder(...xy(m), STUD_R, BAR_Z + BAR_H, STUD_TOP - BAR_Z - BAR_H, P, 10), { tone: "hi", crease: "none" })).join("");
}

function coils() {
  // Bobines W, U, V devant la plaque, chacune sous sa sortie ; spires gravées sur le dessus.
  return BOTTOM.map((m) => {
    const letter = m[0], xc = xy(m)[0];
    const plan = { x: xc - COIL_W / 2, y: COIL_Y, w: COIL_W, d: COIL_D, r: 1.5 };
    const turns = Array.from({ length: 8 }, (_, i) => k.lineOnTop([plan.x + 2 + i * 2.3, plan.y], [plan.x + 2 + i * 2.3, plan.y + COIL_D], T + COIL_H, P)).join("");
    return `<g data-coil="${letter}">${S(k.slabOf(plan, T, COIL_H, P, 3, 0.5), { tone: "hi", crease: "lo", lit: letter === LIT0 })}</g>` + L(turns, { tone: "lo" });
  }).join("");
}

function cables() {
  // Réseau L1 L2 L3 : du presse-étoupe au bout du goujon de U1, V1, W1.
  return TOP.map((m, c) => {
    const [x, y] = xy(m);
    const r = [[GLAND[0] + (c - 1) * 3, GLAND[1], 5], [GLAND[0] + (c - 1) * 3, GLAND[1], STUD_TOP + 6], [x, y - 10, STUD_TOP + 6], [x, y, STUD_TOP]];
    return L(poly(r), { tone: "hi" }) + D([at(r[0]), at(r[r.length - 1])], { size: 0.8, tone: "hi" });
  }).join("");
}

const body = [box(), traces(), labels(), coils(), nuts(), bars("star"), bars("delta"), tips(), cables()];

const svg = k
  .figureSvg({ width: WIDTH, height: HEIGHT, label: "", body })
  .replace(' role="img" aria-label=""', ' aria-hidden="true" focusable="false"');

// Projection linéaire : écran = o + z·ez (exacte en isométrie).
const o = at([0, 0, 0]);
const ez = at([0, 0, 1]).map((c, i) => +(c - o[i]).toFixed(5));
const model = readFileSync(join(HERE, "model.mjs"), "utf8").replace(/^export /gm, "").replace(/^\/\/.*\n/gm, "");

const js = `// Généré par tools/figures/terminal_plate/build.mjs : ne pas modifier à la main.
(() => {
${model}const EZ = ${JSON.stringify(ez)};
const lift = (dz) => "translate(" + (EZ[0] * dz).toFixed(3) + " " + (EZ[1] * dz).toFixed(3) + ")";
document.querySelectorAll('.fig[data-fig="terminal_plate"]').forEach((card) => {
  const q = (s) => card.querySelector(s), qa = (s) => [...card.querySelectorAll(s)];
  const svg = q("svg"), groups = { star: q('[data-part="star"]'), delta: q('[data-part="delta"]') };
  const couplings = qa("[data-fig-coupling]"), presets = qa("[data-fig-preset]"), out = {};
  qa("[data-fig-out]").forEach((el) => { out[el.dataset.figOut] = el; });
  const lang = document.documentElement.lang || "fr", still = matchMedia("(prefers-reduced-motion: reduce)");
  const volts = (v) => new Intl.NumberFormat(lang, { maximumSignificantDigits: 2 }).format(v) + "\\u00a0V";
  let sel = "U", from = "star", to = "star", u = 1, last = 0, frame = 0, visible = true;
  function light() {
    qa(".iso-solid[data-lit]").forEach((el) => el.removeAttribute("data-lit"));
    qa('[data-coil="' + sel + '"] .iso-solid, [data-nut="' + sel + '"] .iso-solid').forEach((el) => el.setAttribute("data-lit", ""));
    qa("[data-trace]").forEach((g) => g.firstElementChild.setAttribute("data-tone", g.dataset.trace === sel ? "lit" : "lo"));
    presets.forEach((b) => b.setAttribute("aria-pressed", b.dataset.figPreset === sel ? "true" : "false"));
  }
  function report() {
    const set = (k, v) => { if (out[k] && out[k].textContent !== v) out[k].textContent = v; };
    set("coupling", out.coupling.dataset[to]);
    set("links", links(to).map((b) => b.join("-")).join(", "));
    set("winding", winding(sel).join("-"));
    set("network", volts(NETWORK[to]));
    set("volts", volts(windingVoltage(to, NETWORK[to])));
    couplings.forEach((b) => b.setAttribute("aria-pressed", b.dataset.figCoupling === to ? "true" : "false"));
  }
  function pose() {
    const old = u < 0.5, z = old ? LIFT * 2 * u : LIFT * (2 - 2 * u);
    for (const c of ["star", "delta"]) {
      const on = c === (old ? from : to);
      groups[c].setAttribute("visibility", on ? "visible" : "hidden");
      groups[c].setAttribute("transform", lift(on ? z : LIFT));
    }
  }
  function tick(now) {
    u = Math.min(1, u + (last ? Math.min(now - last, 100) / 1000 / SWAP_S : 0));
    last = now;
    pose();
    frame = u < 1 && visible && !still.matches ? requestAnimationFrame(tick) : 0;
  }
  const run = () => { if (!frame && u < 1) { if (still.matches) { u = 1; pose(); } else if (visible) { last = 0; frame = requestAnimationFrame(tick); } } };
  couplings.forEach((b) => b.addEventListener("click", () => {
    const next = b.dataset.figCoupling;
    if (next === to) return;
    from = u < 0.5 ? from : to;
    to = next;
    u = from === to ? 1 : 0;
    pose();
    report();
    run();
  }));
  presets.forEach((b) => b.addEventListener("click", () => { sel = b.dataset.figPreset; light(); report(); }));
  new IntersectionObserver((e) => { visible = e[e.length - 1].isIntersecting; if (!visible) { u = 1; pose(); } run(); }).observe(svg);
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
const svgPath = OUT ? join(OUT, "terminal_plate.svg") : join(ROOT, "templates", "figures", "terminal_plate.svg");
const jsPath = OUT ? join(OUT, "terminal_plate.js") : join(ROOT, "static", "acad", "js", "figures", "terminal_plate.js");
write(svgPath, svg + "\n");
write(jsPath, js);
console.log(`wrote ${svgPath} (${Buffer.byteLength(svg)} o), ${jsPath} (${Buffer.byteLength(js)} o)`);
