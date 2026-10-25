// Généré par tools/figures/lc_tank/build.mjs : ne pas modifier à la main.
(() => {
const U = 1; // V crête
const RS = 10000; // Ω, résistance en série
const RL = 10; // Ω, pertes de la bobine (courbe de la section)
const L = 0.01; // H
const C = 100e-9; // F
const F0 = 1 / (2 * Math.PI * Math.sqrt(L * C)); // ≈ 5 033 Hz
const F_MIN = 10;
const F_MAX = 100000;

const cx = (re, im) => ({ re, im });
const add = (a, b) => cx(a.re + b.re, a.im + b.im);
const mul = (a, b) => cx(a.re * b.re - a.im * b.im, a.re * b.im + a.im * b.re);
const div = (a, b) => { const d = b.re ** 2 + b.im ** 2; return cx((a.re * b.re + a.im * b.im) / d, (a.im * b.re - a.re * b.im) / d); };
const polar = (a) => ({ amp: Math.hypot(a.re, a.im), deg: Math.atan2(a.im, a.re) * 180 / Math.PI });
const zl = (f) => cx(RL, 2 * Math.PI * f * L);
const zc = (f) => cx(0, -1 / (2 * Math.PI * f * C));
const zt = (f) => div(mul(zl(f), zc(f)), add(zl(f), zc(f)));
const i0 = (f) => div(cx(U, 0), add(cx(RS, 0), zt(f)));
const v0 = (f) => mul(i0(f), zt(f));

const zTank = (f) => polar(zt(f)).amp;
const line = (f) => polar(i0(f));
const tankV = (f) => polar(v0(f));
const coil = (f) => polar(div(v0(f), zl(f)));
const cap = (f) => polar(div(v0(f), zc(f)));
const periodS = (f) => 2 * 0.125 ** (Math.log10(f / F_MIN) / 4);
const O = [326.0945,203.0622], EX = [1.01576,0.60527], EY = [-1.21053,0.50788], EZ = [0,-1.36852];
const scr = (x, y, z) => [O[0] + x * EX[0] + y * EY[0] + z * EZ[0], O[1] + x * EX[1] + y * EY[1] + z * EZ[1]];
const seg = (cx, cy, z, a, r0, r1) => { const p = scr(cx - Math.sin(a) * r0, cy + Math.cos(a) * r0, z), q = scr(cx + Math.sin(a) * r1, cy - Math.cos(a) * r1, z); return "M" + p[0].toFixed(2) + " " + p[1].toFixed(2) + "L" + q[0].toFixed(2) + " " + q[1].toFixed(2); };
const up = (dz) => "translate(" + (EZ[0] * dz).toFixed(3) + " " + (EZ[1] * dz).toFixed(3) + ")";
const PRESETS = { low: F0 / 2, f0: F0, high: F0 * 2 }, CUR_FS = 0.002;
const SPAN = 2.0944, KSPAN = 4.7124, STROKE = 9;
const toF = (v) => F_MIN * 10 ** (v / 100), toV = (f) => Math.round(100 * Math.log10(f / F_MIN));
document.querySelectorAll('.fig[data-fig="lc_tank"]').forEach((card) => {
  const q = (s) => card.querySelector(s), qa = (s) => card.querySelectorAll(s);
  const svg = q("svg"), rod = q('[data-part="rod"]'), fly = q('[data-part="fly"]'), needle = q('[data-part="needle"]'), vt = q('[data-part="vt"]'), knob = q('[data-part="knob"]');
  const range = q("[data-fig-freq]"), play = q("[data-fig-play]"), out = {};
  qa("[data-fig-out]").forEach((el) => { out[el.dataset.figOut] = el; });
  const lang = document.documentElement.lang || "fr", still = matchMedia("(prefers-reduced-motion: reduce)");
  const fmt = (v, d) => new Intl.NumberFormat(lang, { maximumFractionDigits: d, minimumFractionDigits: d }).format(v);
  const sig = (v) => new Intl.NumberFormat(lang, { maximumSignificantDigits: 3, minimumSignificantDigits: 3 }).format(v);
  const qty = (x, u) => { const v = +x.toPrecision(6); return v >= 1000 ? fmt(v / 1000, v >= 1e4 ? 1 : 2) + " k" + u : fmt(v, v >= 100 ? 0 : 1) + " " + u; };
  let f = PRESETS.f0, phase = Math.PI / 2, last = 0, frame = 0, running = false, visible = true;
  function pose() {
    const ve = Math.sin(phase), rad = Math.PI / 180;
    const w = (ph, d) => ph.amp * Math.sin(phase + ph.deg * rad + (d || 0));
    rod.setAttribute("transform", up(STROKE * ve));
    fly.setAttribute("d", seg(4, -17, 44.2, SPAN * w(coil(f), -Math.PI / 2) / CUR_FS, -4, 15.1));
    needle.setAttribute("d", seg(-70, 0, 45.2, SPAN * w(line(f)) / CUR_FS, 3.4, 10));
    vt.setAttribute("d", seg(-36, 0, 45.2, SPAN * w(tankV(f)) / U, 3.4, 10));
    knob.setAttribute("d", seg(-139, 0, 27.2, -KSPAN / 2 + KSPAN * Math.log10(f / F_MIN) / 4, 0, 6.5));
  }
  function report() {
    const text = qty(f, "Hz");
    range.value = toV(f);
    range.setAttribute("aria-valuetext", text);
    if (out.f) out.f.textContent = text;
    if (out.z) out.z.textContent = qty(zTank(f), "Ω");
    if (out.i) out.i.textContent = sig(line(f).amp * 1e6) + " µA";
    if (out.ilc) out.ilc.textContent = sig(coil(f).amp * 1e3) + " / " + sig(cap(f).amp * 1e3) + " mA";
    if (out.vt) out.vt.textContent = sig(tankV(f).amp / U);
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
