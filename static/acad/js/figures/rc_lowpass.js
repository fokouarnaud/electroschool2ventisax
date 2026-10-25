// Généré par tools/figures/rc_lowpass/build.mjs : ne pas modifier à la main.
(() => {
const R = 1000; // Ω
const C = 100e-9; // F
const FC = 1 / (2 * Math.PI * R * C); // ≈ 1 591,5 Hz
const F_MIN = 10;
const F_MAX = 100000;

const xc = (f) => 1 / (2 * Math.PI * f * C);
const ratio = (f) => 1 / Math.sqrt(1 + (f / FC) ** 2);
const phaseDeg = (f) => -Math.atan(f / FC) * 180 / Math.PI;
const periodS = (f) => 2 * 0.125 ** (Math.log10(f / F_MIN) / 4);
const O = [326.0945,203.0622], EX = [1.01576,0.60527], EY = [-1.21053,0.50788], EZ = [0,-1.36852];
const scr = (x, y, z) => [O[0] + x * EX[0] + y * EY[0] + z * EZ[0], O[1] + x * EX[1] + y * EY[1] + z * EZ[1]];
const seg = (cx, cy, z, a, r0, r1) => { const p = scr(cx - Math.sin(a) * r0, cy + Math.cos(a) * r0, z), q = scr(cx + Math.sin(a) * r1, cy - Math.cos(a) * r1, z); return "M" + p[0].toFixed(2) + " " + p[1].toFixed(2) + "L" + q[0].toFixed(2) + " " + q[1].toFixed(2); };
const up = (dz) => "translate(" + (EZ[0] * dz).toFixed(3) + " " + (EZ[1] * dz).toFixed(3) + ")";
const PRESETS = { low: 100, fc: FC, high: 16000 };
const SPAN = 2.0944, KSPAN = 4.7124, STROKE = 9, LIFT = 9, PLEATS = 6;
const toF = (v) => F_MIN * 10 ** (v / 100), toV = (f) => Math.round(100 * Math.log10(f / F_MIN));
document.querySelectorAll('.fig[data-fig="rc_lowpass"]').forEach((card) => {
  const q = (s) => card.querySelector(s), qa = (s) => card.querySelectorAll(s);
  const svg = q("svg"), rod = q('[data-part="rod"]'), needle = q('[data-part="needle"]'), knob = q('[data-part="knob"]');
  const pleats = [...qa('[data-part="pleat"]')], range = q("[data-fig-freq]"), play = q("[data-fig-play]"), out = {};
  qa("[data-fig-out]").forEach((el) => { out[el.dataset.figOut] = el; });
  const lang = document.documentElement.lang || "fr", still = matchMedia("(prefers-reduced-motion: reduce)");
  const fmt = (v, d) => new Intl.NumberFormat(lang, { maximumFractionDigits: d, minimumFractionDigits: d }).format(v);
  const qty = (v, u) => v >= 1000 ? fmt(v / 1000, v >= 1e4 ? 1 : 2) + " k" + u : fmt(v, v >= 100 ? 0 : 1) + " " + u;
  let f = PRESETS.low, phase = Math.PI / 2, last = 0, frame = 0, running = false, visible = true;
  function pose() {
    const ve = Math.sin(phase), vs = ratio(f) * Math.sin(phase + phaseDeg(f) * Math.PI / 180);
    rod.setAttribute("transform", up(STROKE * ve));
    pleats.forEach((g) => g.setAttribute("transform", up(LIFT * vs * g.dataset.step / PLEATS)));
    needle.setAttribute("d", seg(124, 0, 50.2, vs * SPAN, 3.4, 13));
    knob.setAttribute("d", seg(-139, 0, 27.2, -KSPAN / 2 + KSPAN * Math.log10(f / F_MIN) / 4, 0, 6.5));
  }
  function report() {
    const text = qty(f, "Hz");
    range.value = toV(f);
    range.setAttribute("aria-valuetext", text);
    if (out.f) out.f.textContent = text;
    if (out.xc) out.xc.textContent = qty(xc(f), "Ω");
    if (out.ratio) out.ratio.textContent = fmt(ratio(f), 3);
    if (out.phase) out.phase.textContent = fmt(phaseDeg(f), 1) + "°";
    pose();
  }
  function tick(now) {
    if (last) phase += 2 * Math.PI * Math.min(now - last, 100) / 1000 / periodS(f);
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
  range.addEventListener("input", () => { f = toF(+range.value); report(); setPlaying(true); });
  qa("[data-fig-preset]").forEach((b) => b.addEventListener("click", () => { f = PRESETS[b.dataset.figPreset]; report(); setPlaying(true); }));
  play.addEventListener("click", () => setPlaying(!running));
  new IntersectionObserver((e) => { visible = e[e.length - 1].isIntersecting; run(); }).observe(svg);
  q("[data-fig-controls]").hidden = false;
  report();
});
})();
