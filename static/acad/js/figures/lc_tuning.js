// Généré par tools/figures/lc_tuning/build.mjs : ne pas modifier à la main.
(() => {
const L = 100e-6; // H
const Q = 40; // facteur de qualité de la courbe « stations » de la section
const CMIN = 180e-12; // F, lames sorties
const CMAX = 360e-12; // F, lames rentrées
const STATIONS = [0.9e6, 1e6, 1.1e6]; // Hz
const SWEEP_S = 8; // durée d'un aller du balayage

const f0 = (c, l = L) => 1 / (2 * Math.PI * Math.sqrt(l * c));
const cTune = (f, l = L) => 1 / (4 * Math.PI ** 2 * f ** 2 * l);
const response = (f, fr) => 1 / Math.sqrt(1 + (Q * (f / fr - fr / f)) ** 2);
const overlapDeg = (c) => 180 * (c - CMIN) / (CMAX - CMIN);
const sweepC = (t) => { const u = ((t / SWEEP_S) % 2 + 2) % 2; return CMIN + (CMAX - CMIN) * (u <= 1 ? u : 2 - u); };
const O = [314.2831,176.9921], EX = [1.19926,0.71461], EY = [-1.42923,0.59963], EZ = [0,-1.61576];
const scr = (x, y, z) => [O[0] + x * EX[0] + y * EY[0] + z * EZ[0], O[1] + x * EX[1] + y * EY[1] + z * EZ[1]];
const pth = (pts, closed) => pts.map((p, i) => { const s = scr(p[0], p[1], p[2]); return (i ? "L" : "M") + s[0].toFixed(2) + " " + s[1].toFixed(2); }).join("") + (closed ? "Z" : "");
const seg = (cx, cy, z, a, r0, r1) => pth([[cx - Math.sin(a) * r0, cy + Math.cos(a) * r0, z], [cx + Math.sin(a) * r1, cy - Math.cos(a) * r1, z]]);
const CX = -92, CY = -10, RP = 24, ARC = 16, ROTOR_Z = [12,20,28,36], METERS = [[18,-30],[56,-30],[94,-30]], MSPAN = 1.0472;
const PRESETS = { s0: cTune(STATIONS[0]), s1: cTune(STATIONS[1]), s2: cTune(STATIONS[2]) };
const half = (z, a0) => { const pts = []; for (let i = 0; i <= ARC; i++) { const a = (a0 + 180 * i / ARC) * Math.PI / 180; pts.push([CX + RP * Math.cos(a), CY + RP * Math.sin(a), z]); } pts.push([CX, CY, z]); return pth(pts, true); };
const xOf = (f) => -36 + 0.0004 * (f - 0.8e6);
document.querySelectorAll('.fig[data-fig="lc_tuning"]').forEach((card) => {
  const q = (s) => card.querySelector(s), qa = (s) => card.querySelectorAll(s);
  const svg = q("svg"), knob = q('[data-part="knob"]'), idx = q('[data-part="index"]'), rotors = [...qa('[data-part="rotor"]')], meters = [...qa('[data-part="meter"]')];
  const range = q("[data-fig-c]"), play = q("[data-fig-play]"), readout = q(".fig-readout"), out = {};
  qa("[data-fig-out]").forEach((el) => { out[el.dataset.figOut] = el; });
  const lang = document.documentElement.lang || "fr", still = matchMedia("(prefers-reduced-motion: reduce)");
  const sig = (v) => new Intl.NumberFormat(lang, { maximumSignificantDigits: 3, minimumSignificantDigits: 3 }).format(v);
  const mhz = (v) => new Intl.NumberFormat(lang, { maximumFractionDigits: 3, minimumFractionDigits: 3 }).format(v / 1e6) + " MHz";
  let c = PRESETS.s1, t = 0, last = 0, frame = 0, running = false, visible = true;
  function report() {
    const f = f0(c), th = overlapDeg(c), pf = sig(c * 1e12) + " pF";
    range.value = Math.round(c * 2e12) / 2;
    range.setAttribute("aria-valuetext", pf);
    if (out.c) out.c.textContent = pf;
    if (out.f) out.f.textContent = mhz(f);
    STATIONS.forEach((s, n) => { if (out["g" + n]) out["g" + n].textContent = sig(response(s, f)); });
    rotors.forEach((g, n) => { const d = half(ROTOR_Z[n], th); g.querySelectorAll("path").forEach((p) => p.setAttribute("d", d)); });
    knob.setAttribute("d", seg(CX, CY, 53.2, (th - 90) * Math.PI / 180, 0, 6));
    idx.setAttribute("d", pth([[xOf(f), 26.8, 10.3], [xOf(f), 45.2, 10.3]]));
    meters.forEach((m) => { const n = +m.dataset.n, [mx, my] = METERS[n]; m.setAttribute("d", seg(mx, my, 14.2, -MSPAN + 2 * MSPAN * response(STATIONS[n], f), 1.2, 7)); });
  }
  function tick(now) {
    if (last) t += Math.min(now - last, 100) / 1000;
    last = now;
    c = sweepC(t);
    report();
    frame = running && visible && !still.matches ? requestAnimationFrame(tick) : 0;
  }
  const run = () => { if (!frame && running && visible && !still.matches) { last = 0; frame = requestAnimationFrame(tick); } };
  function setPlaying(on) {
    running = on;
    play.setAttribute("aria-pressed", on ? "true" : "false");
    play.textContent = on ? play.dataset.pause : play.dataset.play;
    readout.setAttribute("aria-live", on ? "off" : "polite");
    if (on) { t = SWEEP_S * (c - CMIN) / (CMAX - CMIN); run(); }
  }
  range.addEventListener("input", () => { setPlaying(false); c = +range.value * 1e-12; report(); });
  qa("[data-fig-preset]").forEach((b) => b.addEventListener("click", () => { setPlaying(false); c = PRESETS[b.dataset.figPreset]; report(); }));
  play.addEventListener("click", () => setPlaying(!running));
  new IntersectionObserver((e) => { visible = e[e.length - 1].isIntersecting; run(); }).observe(svg);
  q("[data-fig-controls]").hidden = false;
  report();
});
})();
