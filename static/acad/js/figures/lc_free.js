// Généré par tools/figures/lc_free/build.mjs : ne pas modifier à la main.
(() => {
const L = 0.01; // H
const C = 100e-9; // F
const V0 = 1; // V, charge initiale du condensateur
const W0 = 1 / Math.sqrt(L * C); // rad/s
const F0 = W0 / (2 * Math.PI); // ≈ 5 033 Hz
const SLOW = 2; // s affichées par période réelle (cadence ralentie, F5)

const q = (r) => Math.sqrt(L / C) / r;
const alpha = (r) => r / (2 * L);
const omegaD = (r) => Math.sqrt(W0 ** 2 - alpha(r) ** 2);
const period = (r) => 2 * Math.PI / omegaD(r);
const vc = (t, r) => V0 * Math.exp(-alpha(r) * t) * (Math.cos(omegaD(r) * t) + alpha(r) / omegaD(r) * Math.sin(omegaD(r) * t));
const current = (t, r) => -C * V0 * W0 ** 2 / omegaD(r) * Math.exp(-alpha(r) * t) * Math.sin(omegaD(r) * t);
const energyC = (t, r) => 0.5 * C * vc(t, r) ** 2;
const energyL = (t, r) => 0.5 * L * current(t, r) ** 2;
const O = [307.9298,189.5946], EX = [1.27511,0.75981], EY = [-1.51962,0.63756], EZ = [0,-1.71796];
const scr = (x, y, z) => [O[0] + x * EX[0] + y * EY[0] + z * EZ[0], O[1] + x * EX[1] + y * EY[1] + z * EZ[1]];
const pth = (pts) => pts.map((p, i) => { const s = scr(p[0], p[1], p[2]); return (i ? "L" : "M") + s[0].toFixed(2) + " " + s[1].toFixed(2); }).join("");
const move = (dy, dz) => "translate(" + (EY[0] * dy + EZ[0] * dz).toFixed(3) + " " + (EY[1] * dy + EZ[1] * dz).toFixed(3) + ")";
const TOP = 72, ROPE = 50, RX = 16, THMAX = 0.6109, BX = 69, BLEN = 36, BARS = [27,39], PZ = 6.2;
const E0 = 0.5 * C * V0 ** 2, PRESETS = { r10: 10, r40: 40, r100: 100 };
const seatAt = (th) => [ROPE * Math.sin(th), TOP - 1.5 - ROPE * Math.cos(th)];
const [Y0, Z0] = seatAt(THMAX);
document.querySelectorAll('.fig[data-fig="lc_free"]').forEach((card) => {
  const q2 = (s) => card.querySelector(s), qa = (s) => card.querySelectorAll(s);
  const svg = q2("svg"), seat = q2('[data-part="seat"]'), ropes = q2('[data-part="ropes"]'), barC = q2('[data-part="bar-c"]'), barL = q2('[data-part="bar-l"]');
  const range = q2("[data-fig-r]"), play = q2("[data-fig-play]"), readout = q2(".fig-readout"), out = {};
  qa("[data-fig-out]").forEach((el) => { out[el.dataset.figOut] = el; });
  const lang = document.documentElement.lang || "fr", still = matchMedia("(prefers-reduced-motion: reduce)");
  const nf = (v, d) => new Intl.NumberFormat(lang, { maximumFractionDigits: d, minimumFractionDigits: d }).format(v);
  const sig = (v) => new Intl.NumberFormat(lang, { maximumSignificantDigits: 3, minimumSignificantDigits: 3 }).format(v);
  let r = 40, t = 0, last = 0, frame = 0, running = false, visible = true;
  function report() {
    const v = vc(t, r), i = current(t, r), ec = energyC(t, r) / E0, el = energyL(t, r) / E0, th = THMAX * v, [y, z] = seatAt(th);
    range.value = r;
    range.setAttribute("aria-valuetext", r + " Ω");
    if (out.q) out.q.textContent = sig(q(r));
    if (out.t) out.t.textContent = nf(t / period(r), 2);
    if (out.v) out.v.textContent = sig(v) + " V";
    if (out.i) out.i.textContent = sig(i * 1e3 || 0) + " mA";
    if (out.e) out.e.textContent = nf(100 * (ec + el), 1) + " %";
    seat.setAttribute("transform", move(y - Y0, z - Z0));
    ropes.setAttribute("d", pth([[-RX, 0, TOP - 1.5], [-RX, y, z]]) + pth([[RX, 0, TOP - 1.5], [RX, y, z]]));
    barC.setAttribute("d", pth([[BX, BARS[0], PZ], [BX + BLEN * Math.max(ec, 0.004), BARS[0], PZ]]));
    barL.setAttribute("d", pth([[BX, BARS[1], PZ], [BX + BLEN * Math.max(el, 0.004), BARS[1], PZ]]));
  }
  function tick(now) {
    if (last) t += Math.min(now - last, 100) / 1000 * period(r) / SLOW;
    last = now;
    // L'oscillation s'éteint : à moins de 0,1 % de l'énergie, la balançoire s'arrête et se laisse relancer.
    if ((energyC(t, r) + energyL(t, r)) / E0 < 0.001) { setPlaying(false); report(); return; }
    report();
    frame = running && visible && !still.matches ? requestAnimationFrame(tick) : 0;
  }
  const run = () => { if (!frame && running && visible && !still.matches) { last = 0; frame = requestAnimationFrame(tick); } };
  function setPlaying(on) {
    if (on && (energyC(t, r) + energyL(t, r)) / E0 < 0.001) t = 0;
    running = on;
    if (!on && frame) { cancelAnimationFrame(frame); frame = 0; }
    play.setAttribute("aria-pressed", on ? "true" : "false");
    play.textContent = on ? play.dataset.pause : play.dataset.play;
    readout.setAttribute("aria-live", on ? "off" : "polite");
    if (on) run();
  }
  const recharge = (value) => { setPlaying(false); r = value; t = 0; report(); };
  range.addEventListener("input", () => recharge(+range.value));
  qa("[data-fig-preset]").forEach((b) => b.addEventListener("click", () => recharge(PRESETS[b.dataset.figPreset])));
  play.addEventListener("click", () => setPlaying(!running));
  new IntersectionObserver((e) => { visible = e[e.length - 1].isIntersecting; run(); }).observe(svg);
  q2("[data-fig-controls]").hidden = false;
  report();
});
})();
