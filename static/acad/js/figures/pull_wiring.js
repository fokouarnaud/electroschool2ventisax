// Généré par tools/figures/pull_wiring/build.mjs : ne pas modifier à la main.
(() => {
const VCC = 3.3;
const R_EXT = 10000;
const R_INT = 45000;
const WIRINGS = ["ext-down", "ext-up", "int-up", "int-down"];
const PULL = { "ext-down": ["gnd", false], "ext-up": ["3v3", false], "int-up": ["3v3", true], "int-down": ["gnd", true] };
function parts(w) {
  const [side, inside] = PULL[w];
  return { pullUp: inside && side === "3v3", pullDown: inside && side === "gnd", resistor: inside ? null : side, button: side === "3v3" ? "gnd" : "3v3" };
}
function reading(w, pressed) {
  const [side, inside] = PULL[w];
  const high = (side === "3v3") !== pressed;
  return { volts: high ? VCC : 0, level: high ? "HIGH" : "LOW", amps: pressed ? VCC / (inside ? R_INT : R_EXT) : 0 };
}
const PRESS_S = 0.25; // s de course du bouton (illustratif)
const EZ = [0,-2.05864], PRESS = 2, RISE = 6;
const shift = (dz) => "translate(" + (EZ[0] * dz).toFixed(3) + " " + (EZ[1] * dz).toFixed(3) + ")";
document.querySelectorAll('.fig[data-fig="pull_wiring"]').forEach((card) => {
  const q = (s) => card.querySelector(s), qa = (s) => [...card.querySelectorAll(s)];
  const svg = q("svg"), push = q("[data-fig-push]"), presets = qa("[data-fig-preset]"), out = {};
  qa("[data-fig-out]").forEach((el) => { out[el.dataset.figOut] = el; });
  const lang = document.documentElement.lang || "fr", still = matchMedia("(prefers-reduced-motion: reduce)");
  const num = (v, d) => new Intl.NumberFormat(lang, { maximumSignificantDigits: d }).format(v);
  let wiring = "ext-down", pressed = false, t = 0, flag = 0, last = 0, frame = 0, visible = true;
  const show = (key, on) => { const g = q('[data-part="' + key + '"]'); if (on) g.removeAttribute("visibility"); else g.setAttribute("visibility", "hidden"); };
  function draw() {
    const p = parts(wiring), r = reading(wiring, pressed), side = (s) => (s === "3v3" ? "up" : "down");
    show("iu-open", !p.pullUp); show("iu-closed", p.pullUp); show("id-open", !p.pullDown); show("id-closed", p.pullDown);
    ["up", "down"].forEach((s) => { show("er-" + s, p.resistor && side(p.resistor) === s); show("bt-" + s, side(p.button) === s); });
    const pull = p.pullUp ? "iu" : p.pullDown ? "id" : "e" + side(p.resistor)[0];
    qa(".iso-solid[data-lit]").forEach((el) => el.removeAttribute("data-lit"));
    qa('[data-part="r-' + pull + '"] .iso-solid').forEach((el) => el.setAttribute("data-lit", ""));
    // fils parcourus par un courant : le tirage, la piste et le bouton, seulement bouton appuyé
    const live = r.amps ? [pull, "trunk", "b" + side(p.button)[0]].concat(p.pullUp || p.pullDown ? ["tin"] : []) : [];
    qa("[data-wire]").forEach((g) => g.querySelector("path").setAttribute("data-tone", live.includes(g.dataset.wire) ? "hi" : "lo"));
    presets.forEach((b) => b.setAttribute("aria-pressed", b.dataset.figPreset === wiring ? "true" : "false"));
    const set = (key, v) => { if (out[key] && out[key].textContent !== v) out[key].textContent = v; };
    set("wiring", q('[data-fig-preset="' + wiring + '"]').textContent.trim());
    set("button", pressed ? out.button.dataset.pressed : out.button.dataset.released);
    set("volts", num(r.volts, 2) + " V");
    set("level", r.level);
    set("amps", r.amps ? num(r.amps * 1000, 3) + " mA" : "0 mA");
    push.textContent = pressed ? push.dataset.release : push.dataset.press;
    push.setAttribute("aria-pressed", pressed ? "true" : "false");
  }
  function pose() {
    ["up", "down"].forEach((s) => q('[data-part="cap-' + s + '"]').setAttribute("transform", shift(-PRESS * t)));
    q('[data-part="flag"]').setAttribute("transform", shift(RISE * flag));
  }
  const goal = () => [pressed ? 1 : 0, reading(wiring, pressed).level === "HIGH" ? 1 : 0];
  function tick(now) {
    const step = last ? Math.min(now - last, 100) / 1000 / PRESS_S : 0, [gt, gf] = goal();
    last = now;
    t = gt > t ? Math.min(gt, t + step) : Math.max(gt, t - step);
    flag = gf > flag ? Math.min(gf, flag + step) : Math.max(gf, flag - step);
    pose();
    frame = (t !== gt || flag !== gf) && visible && !still.matches ? requestAnimationFrame(tick) : 0;
  }
  function run() {
    const [gt, gf] = goal();
    if (still.matches) { t = gt; flag = gf; pose(); return; }
    if (!frame && visible && (t !== gt || flag !== gf)) { last = 0; frame = requestAnimationFrame(tick); }
  }
  push.addEventListener("click", () => { pressed = !pressed; draw(); run(); });
  presets.forEach((b) => b.addEventListener("click", () => { wiring = b.dataset.figPreset; pressed = false; draw(); run(); }));
  new IntersectionObserver((e) => { visible = e[e.length - 1].isIntersecting; run(); }).observe(svg);
  q("[data-fig-controls]").hidden = false;
  draw();
  run();
});
})();
