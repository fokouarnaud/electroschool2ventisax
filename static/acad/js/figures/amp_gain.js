// Généré par tools/figures/amp_gain/build.mjs : ne pas modifier à la main.
(() => {
const VE = 0.05; // V crête à l'entrée, l'exemple de la section
const GAIN_MIN = -40;
const GAIN_MAX = 40;
const PERIOD_S = 2; // s affichées par période du signal (cadence ralentie, F5)

const ve = (ph) => VE * Math.sin(ph);
const vs = (ph, a) => a * ve(ph);
const peakOut = (a) => Math.abs(a) * VE;
const gainOf = (out, inp) => out / inp;
const inverted = (a) => a < 0;
const O = [307.1809,182.6601], EX = [1.47608,0.87956], EY = [-1.75913,0.73804], EZ = [0,-1.98872];
const scr = (x, y, z) => [O[0] + x * EX[0] + y * EY[0] + z * EZ[0], O[1] + x * EX[1] + y * EY[1] + z * EZ[1]];
const seg = (cx, cy, z, a, r0, r1) => { const p = scr(cx - Math.sin(a) * r0, cy + Math.cos(a) * r0, z), q = scr(cx + Math.sin(a) * r1, cy - Math.cos(a) * r1, z); return "M" + p[0].toFixed(2) + " " + p[1].toFixed(2) + "L" + q[0].toFixed(2) + " " + q[1].toFixed(2); };
const up = (dz) => "translate(" + (EZ[0] * dz).toFixed(3) + " " + (EZ[1] * dz).toFixed(3) + ")";
const KZ = 4, SPAN = 1.7453, KSPAN = 2.3562, METERS = [[-66,-8,0.06],[-30,-8,2.4]], PLEATS = 3;
const PRESETS = { a40: 40, am39: -39 };
document.querySelectorAll('.fig[data-fig="amp_gain"]').forEach((card) => {
  const q = (s) => card.querySelector(s), qa = (s) => card.querySelectorAll(s);
  const svg = q("svg"), mic = q('[data-part="mic"]'), knob = q('[data-part="knob"]'), meters = [...qa('[data-part="meter"]')], pleats = [...qa('[data-part="pleat"]')];
  const range = q("[data-fig-gain]"), play = q("[data-fig-play]"), out = {};
  qa("[data-fig-out]").forEach((el) => { out[el.dataset.figOut] = el; });
  const lang = document.documentElement.lang || "fr", still = matchMedia("(prefers-reduced-motion: reduce)");
  const nf = (v, d, sign) => new Intl.NumberFormat(lang, { maximumFractionDigits: d, minimumFractionDigits: d, signDisplay: sign || "auto" }).format(v);
  let a = 40, phase = Math.PI / 2, last = 0, frame = 0, running = false, visible = true;
  function pose() {
    const vi = ve(phase), vo = vs(phase, a);
    mic.setAttribute("transform", up(KZ * vi));
    pleats.forEach((g) => g.setAttribute("transform", up(KZ * vo * g.dataset.step / PLEATS)));
    meters.forEach((m) => { const n = +m.dataset.n, [x, y, fs] = METERS[n]; m.setAttribute("d", seg(x, y, 18.7, SPAN * (n ? vo : vi) / fs, 1.2, 7)); });
    knob.setAttribute("d", seg(-20, 12, 19.2, KSPAN * a / 40, 0, 4));
  }
  function report() {
    range.value = a;
    range.setAttribute("aria-valuetext", nf(a, 0, "exceptZero"));
    if (out.a) out.a.textContent = nf(a, 0, "exceptZero");
    if (out.ve) out.ve.textContent = nf(VE * 1000, 1) + " mV";
    if (out.vs) out.vs.textContent = nf(peakOut(a), 2) + " V";
    if (out.ph) out.ph.textContent = inverted(a) ? out.ph.dataset.inverted : out.ph.dataset.inPhase;
    pose();
  }
  function tick(now) {
    if (last) phase += 2 * Math.PI * Math.min(now - last, 100) / 1000 / PERIOD_S;
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
  range.addEventListener("input", () => { a = +range.value; report(); setPlaying(true); });
  qa("[data-fig-preset]").forEach((b) => b.addEventListener("click", () => { a = PRESETS[b.dataset.figPreset]; report(); setPlaying(true); }));
  play.addEventListener("click", () => setPlaying(!running));
  new IntersectionObserver((e) => { visible = e[e.length - 1].isIntersecting; run(); }).observe(svg);
  q("[data-fig-controls]").hidden = false;
  report();
});
})();
