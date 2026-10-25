// Généré par tools/figures/rlc_bandwidth/build.mjs : ne pas modifier à la main.
(() => {
const L = 0.01; // H
const C = 100e-9; // F
const R1 = 50; // Ω, Q ≈ 6,3
const R2 = 200; // Ω, Q ≈ 1,6
const F0 = 1 / (2 * Math.PI * Math.sqrt(L * C)); // ≈ 5 033 Hz
const F_LO = 2000;
const F_HI = 8000;
const SWEEP_S = 8; // durée d'un aller du balayage

const xl = (f) => 2 * Math.PI * f * L;
const xc = (f) => 1 / (2 * Math.PI * f * C);
const ratio = (f, r) => r / Math.sqrt(r ** 2 + (xl(f) - xc(f)) ** 2);
const q = (r) => xl(F0) / r;
const f1 = (r) => (Math.sqrt((r / (2 * L)) ** 2 + 1 / (L * C)) - r / (2 * L)) / (2 * Math.PI);
const f2 = (r) => (Math.sqrt((r / (2 * L)) ** 2 + 1 / (L * C)) + r / (2 * L)) / (2 * Math.PI);
const band = (r) => f2(r) - f1(r);
const sweepF = (t) => { const u = ((t / SWEEP_S) % 2 + 2) % 2; return F_LO + (F_HI - F_LO) * (u <= 1 ? u : 2 - u); };
const O = [335.4206,174.0206], EX = [1.79287,0.41802], EY = [-0.83603,0.89644];
const scr = (x, y, z) => [O[0] + x * EX[0] + y * EY[0] + z * 0, O[1] + x * EX[1] + y * EY[1] + z * -1.71319];
const seg = (cx, cy, z, a, r1) => { const q = scr(cx + Math.sin(a) * r1, cy - Math.cos(a) * r1, z), p = scr(cx, cy, z); return "M" + p[0].toFixed(2) + " " + p[1].toFixed(2) + "L" + q[0].toFixed(2) + " " + q[1].toFixed(2); };
const move = (dx, dy) => "translate(" + (EX[0] * dx + EY[0] * dy).toFixed(3) + " " + (EX[1] * dx + EY[1] * dy).toFixed(3) + ")";
const FS = f1(R1), SX = 0.0293, SY = 60, KSPAN = 4.7124;
const PRESETS = { f1: f1(R1), f0: F0, f2: f2(R1) };
document.querySelectorAll('.fig[data-fig="rlc_bandwidth"]').forEach((card) => {
  const q = (s) => card.querySelector(s), qa = (s) => card.querySelectorAll(s);
  const svg = q("svg"), gantry = q('[data-part="gantry"]'), knob = q('[data-part="knob"]'), pens = [...qa('[data-part="pen"]')];
  const range = q("[data-fig-freq]"), play = q("[data-fig-play]"), readout = q(".fig-readout"), out = {};
  qa("[data-fig-out]").forEach((el) => { out[el.dataset.figOut] = el; });
  const lang = document.documentElement.lang || "fr", still = matchMedia("(prefers-reduced-motion: reduce)");
  const fmt = (v, d) => new Intl.NumberFormat(lang, { maximumFractionDigits: d, minimumFractionDigits: d }).format(v);
  const sig = (v) => new Intl.NumberFormat(lang, { maximumSignificantDigits: 3, minimumSignificantDigits: 3 }).format(v);
  const hz = (v) => v >= 1000 ? fmt(v / 1000, 2) + " kHz" : fmt(v, 0) + " Hz";
  let f = FS, t = 0, last = 0, frame = 0, running = false, visible = true;
  function report() {
    range.value = Math.round(f / 10) * 10;
    range.setAttribute("aria-valuetext", hz(f));
    if (out.f) out.f.textContent = hz(f);
    if (out.r1) out.r1.textContent = sig(ratio(f, R1));
    if (out.r2) out.r2.textContent = sig(ratio(f, R2));
    gantry.setAttribute("transform", move(SX * (f - FS), 0));
    pens.forEach((g) => { const r = +g.dataset.r; g.setAttribute("transform", move(0, -SY * (ratio(f, r) - ratio(FS, r)))); });
    knob.setAttribute("d", seg(-131, 51, 12.2, -KSPAN / 2 + KSPAN * (f - F_LO) / (F_HI - F_LO), 2.8));
  }
  function tick(now) {
    if (last) t += Math.min(now - last, 100) / 1000;
    last = now;
    f = sweepF(t);
    report();
    frame = running && visible && !still.matches ? requestAnimationFrame(tick) : 0;
  }
  const run = () => { if (!frame && running && visible && !still.matches) { last = 0; frame = requestAnimationFrame(tick); } };
  function setPlaying(on) {
    running = on;
    play.setAttribute("aria-pressed", on ? "true" : "false");
    play.textContent = on ? play.dataset.pause : play.dataset.play;
    readout.setAttribute("aria-live", on ? "off" : "polite");
    if (on) { t = SWEEP_S * (Math.min(Math.max(f, F_LO), F_HI) - F_LO) / (F_HI - F_LO); run(); }
  }
  range.addEventListener("input", () => { setPlaying(false); f = +range.value; report(); });
  qa("[data-fig-preset]").forEach((b) => b.addEventListener("click", () => { setPlaying(false); f = PRESETS[b.dataset.figPreset]; report(); }));
  play.addEventListener("click", () => setPlaying(!running));
  new IntersectionObserver((e) => { visible = e[e.length - 1].isIntersecting; run(); }).observe(svg);
  q("[data-fig-controls]").hidden = false;
  report();
});
})();
