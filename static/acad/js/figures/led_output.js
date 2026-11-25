// Généré par tools/figures/led_output/build.mjs : ne pas modifier à la main.
(() => {
const VCC = 3.3;
const VF = 2.0;
const R = 330;
const WIRINGS = ["source", "sink"];
function output(w, high) {
  const lit = w === "source" ? high : !high;
  const amps = lit ? (VCC - VF) / R : 0;
  return { volts: high ? VCC : 0, closed: high ? "P" : "N", lit, amps, flow: lit ? (w === "source" ? "out" : "in") : null, vr: lit ? VCC - VF : 0, vled: lit ? VF : 0 };
}
const MOVE_S = 0.25; // s de course du drapeau GPIO_OUT (illustratif)
const EZ = [0,-2.05864], RISE = 6;
const shift = (dz) => "translate(" + (EZ[0] * dz).toFixed(3) + " " + (EZ[1] * dz).toFixed(3) + ")";
document.querySelectorAll('.fig[data-fig="led_output"]').forEach((card) => {
  const q = (s) => card.querySelector(s), qa = (s) => [...card.querySelectorAll(s)];
  const svg = q("svg"), level = q("[data-fig-level]"), presets = qa("[data-fig-preset]"), out = {};
  qa("[data-fig-out]").forEach((el) => { out[el.dataset.figOut] = el; });
  const lang = document.documentElement.lang || "fr", still = matchMedia("(prefers-reduced-motion: reduce)");
  const num = (v, d) => new Intl.NumberFormat(lang, { maximumSignificantDigits: d }).format(v);
  let wiring = "source", high = true, flag = 1, last = 0, frame = 0, visible = true;
  const show = (key, on) => { const g = q('[data-part="' + key + '"]'); if (on) g.removeAttribute("visibility"); else g.setAttribute("visibility", "hidden"); };
  function draw() {
    const o = output(wiring, high), src = wiring === "source";
    show("src", src); show("snk", !src);
    show("p-open", o.closed !== "P"); show("p-closed", o.closed === "P"); show("n-open", o.closed !== "N"); show("n-closed", o.closed === "N");
    qa(".iso-solid[data-lit]").forEach((el) => el.removeAttribute("data-lit"));
    if (o.lit) qa('[data-part="' + (src ? "led-src" : "led-snk") + '"] .iso-solid').forEach((el) => el.setAttribute("data-lit", ""));
    // fils parcourus par un courant : seulement quand la LED est allumée
    const live = o.lit ? (src ? ["p", "tin", "trunk", "src"] : ["snk", "trunk", "tin", "n"]) : [];
    qa("[data-wire]").forEach((g) => g.querySelector("path").setAttribute("data-tone", live.includes(g.dataset.wire) ? "hi" : "lo"));
    presets.forEach((b) => b.setAttribute("aria-pressed", b.dataset.figPreset === wiring ? "true" : "false"));
    const set = (key, v) => { if (out[key] && out[key].textContent !== v) out[key].textContent = v; };
    set("wiring", q('[data-fig-preset="' + wiring + '"]').textContent.trim());
    set("level", high ? "HIGH" : "LOW");
    set("volts", num(o.volts, 2) + " V");
    set("closed", o.closed === "P" ? out.closed.dataset.p : out.closed.dataset.n);
    set("led", o.lit ? out.led.dataset.on : out.led.dataset.off);
    set("amps", o.lit ? num(o.amps * 1000, 3) + " mA" : "0 mA");
    set("flow", o.flow ? out.flow.dataset[o.flow] : out.flow.dataset.none);
    level.textContent = high ? level.dataset.low : level.dataset.high;
  }
  const pose = () => q('[data-part="flag"]').setAttribute("transform", shift(RISE * flag));
  function tick(now) {
    const step = last ? Math.min(now - last, 100) / 1000 / MOVE_S : 0, goal = high ? 1 : 0;
    last = now;
    flag = goal > flag ? Math.min(goal, flag + step) : Math.max(goal, flag - step);
    pose();
    frame = flag !== goal && visible && !still.matches ? requestAnimationFrame(tick) : 0;
  }
  function run() {
    const goal = high ? 1 : 0;
    if (still.matches) { flag = goal; pose(); return; }
    if (!frame && visible && flag !== goal) { last = 0; frame = requestAnimationFrame(tick); }
  }
  level.addEventListener("click", () => { high = !high; draw(); run(); });
  presets.forEach((b) => b.addEventListener("click", () => { wiring = b.dataset.figPreset; draw(); run(); }));
  new IntersectionObserver((e) => { visible = e[e.length - 1].isIntersecting; run(); }).observe(svg);
  q("[data-fig-controls]").hidden = false;
  draw();
  run();
});
})();
