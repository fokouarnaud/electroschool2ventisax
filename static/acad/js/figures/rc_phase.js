// Généré par tools/figures/rc_phase/build.mjs : ne pas modifier à la main.
(() => {
const R = 1000; // Ω
const C = 100e-9; // F
const FC = 1 / (2 * Math.PI * R * C); // ≈ 1 591,5 Hz
const F_MIN = 10;
const F_MAX = 100000;

const xc = (f) => 1 / (2 * Math.PI * f * C);
const ratio = (f) => 1 / Math.sqrt(1 + (f / FC) ** 2);
const leadDeg = (f) => Math.atan(xc(f) / R) * 180 / Math.PI;
const lagDeg = (f) => 90 - leadDeg(f);
const shift = (f) => lagDeg(f) / 360;
const periodS = (f) => 2 * 0.125 ** (Math.log10(f / F_MIN) / 4);
const O = [333.7247,181.504], EX = [1.31655,0.7845], EY = [-1.569,0.65828], EZ = [0,-1.77378];
const scr = (x, y, z) => [O[0] + x * EX[0] + y * EY[0] + z * EZ[0], O[1] + x * EX[1] + y * EY[1] + z * EZ[1]];
const pth = (pts) => pts.map((p, i) => { const s = scr(p[0], p[1], p[2]); return (i ? "L" : "M") + s[0].toFixed(2) + " " + s[1].toFixed(2); }).join("");
const seg = (cx, cy, z, a, r0, r1) => { const p = scr(cx - Math.sin(a) * r0, cy + Math.cos(a) * r0, z), q = scr(cx + Math.sin(a) * r1, cy - Math.cos(a) * r1, z); return "M" + p[0].toFixed(2) + " " + p[1].toFixed(2) + "L" + q[0].toFixed(2) + " " + q[1].toFixed(2); };
const move = (dx, dy) => "translate(" + (EX[0] * dx + EY[0] * dy).toFixed(3) + " " + (EX[1] * dx + EY[1] * dy).toFixed(3) + ")";
const PRESETS = { low: FC / 10, fc: FC, x577: 1 / (2 * Math.PI * 577 * C), high: FC * 10 };
const KSPAN = 4.7124, PEN_X = -84, PERIOD = 64, TRACE = 164, CH = [-21,13], AMP = 13, GAP = -4, Z = 20.6;
const toF = (v) => F_MIN * 10 ** (v / 100), toV = (f) => Math.round(100 * Math.log10(f / F_MIN));
document.querySelectorAll('.fig[data-fig="rc_phase"]').forEach((card) => {
  const q = (s) => card.querySelector(s), qa = (s) => card.querySelectorAll(s);
  const svg = q("svg"), t1 = q('[data-part="trace-1"]'), t2 = q('[data-part="trace-2"]'), br = q('[data-part="bracket"]'), holes = q('[data-part="holes"]'), knob = q('[data-part="knob"]');
  const pens = [q('[data-part="pen"][data-ch="1"]'), q('[data-part="pen"][data-ch="2"]')], range = q("[data-fig-freq]"), play = q("[data-fig-play]"), out = {};
  qa("[data-fig-out]").forEach((el) => { out[el.dataset.figOut] = el; });
  const lang = document.documentElement.lang || "fr", still = matchMedia("(prefers-reduced-motion: reduce)");
  const fmt = (v, d) => new Intl.NumberFormat(lang, { maximumFractionDigits: d, minimumFractionDigits: d }).format(v);
  const sig = (v, sign) => new Intl.NumberFormat(lang, { maximumSignificantDigits: 3, minimumSignificantDigits: 3, signDisplay: sign || "auto" }).format(v);
  const qty = (v, u) => v >= 1000 ? fmt(v / 1000, v >= 1e4 ? 1 : 2) + " k" + u : fmt(v, v >= 100 ? 0 : 1) + " " + u;
  let f = PRESETS.low, phase = Math.PI / 2, last = 0, frame = 0, running = false, visible = true;
  function pose() {
    const lag = lagDeg(f) * Math.PI / 180, amp = [1, ratio(f)], lags = [0, lag];
    [t1, t2].forEach((t, c) => {
      const pts = [];
      for (let u = 0; u <= TRACE; u += 2) pts.push([PEN_X + u, CH[c] - AMP * amp[c] * Math.sin(phase - 2 * Math.PI * u / PERIOD - lags[c]), Z]);
      t.setAttribute("d", pth(pts));
      pens[c].setAttribute("transform", move(0, -AMP * amp[c] * Math.sin(phase - lags[c])));
    });
    const lagU = PERIOD * lag / (2 * Math.PI), turn = (((phase - Math.PI / 2) / (2 * Math.PI)) % 1 + 1) % 1;
    let ue = PERIOD * turn;
    while (ue < lagU) ue += PERIOD;
    const xe = PEN_X + ue, xs = xe - lagU;
    br.setAttribute("d", pth([[xe, GAP - 2, Z], [xe, GAP + 2, Z]]) + pth([[xe, GAP, Z], [xs, GAP, Z]]) + pth([[xs, GAP - 2, Z], [xs, GAP + 2, Z]]));
    holes.setAttribute("transform", move(8 * ((((phase - Math.PI / 2) / (2 * Math.PI)) * PERIOD / 8) % 1 + 1) % 8, 0));
    knob.setAttribute("d", seg(-127, 47.5, 15.7, -KSPAN / 2 + KSPAN * Math.log10(f / F_MIN) / 4, 0, 3.5));
  }
  function report() {
    const text = qty(f, "Hz");
    range.value = toV(f);
    range.setAttribute("aria-valuetext", text);
    if (out.f) out.f.textContent = text;
    if (out.xc) out.xc.textContent = qty(xc(f), "Ω");
    if (out.lead) out.lead.textContent = sig(leadDeg(f), "always") + "°";
    if (out.shift) out.shift.textContent = sig(shift(f));
    if (out.lag) out.lag.textContent = sig(lagDeg(f)) + "°";
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
