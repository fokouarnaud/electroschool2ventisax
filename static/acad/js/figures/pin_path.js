// Généré par tools/figures/pin_path/build.mjs : ne pas modifier à la main.
(() => {
const PIN = 25;
const STAGES = ["cpu", "bus", "reg", "mux", "pad", "board"];
const hex = (n) => "0x" + n.toString(16).toUpperCase().padStart(8, "0");
function write(high) {
  const mask = 2 ** PIN;
  const address = high ? 0x3ff44008 : 0x3ff4400c;
  return {
    mask, maskHex: hex(mask), register: high ? "GPIO_OUT_W1TS_REG" : "GPIO_OUT_W1TC_REG", address, addressHex: hex(address),
    bit: high ? 1 : 0, closed: high ? "P" : "N", volts: high ? 3.3 : 0, led: high,
  };
}
const reached = (step, stage) => STAGES.indexOf(stage) < step - 1;
const STEP_S = 1.6; // s par étape en lecture automatique (illustratif)
const EZ = [0,-1.88333], RISE = 4;
const shift = (dz) => "translate(" + (EZ[0] * dz).toFixed(3) + " " + (EZ[1] * dz).toFixed(3) + ")";
// fils franchis après chaque étape
const WIRES = { cpu: "cpu", bus: "bus", reg: "reg", mux: ["route", "mux"], pad: "pad", board: "pin" };
document.querySelectorAll('.fig[data-fig="pin_path"]').forEach((card) => {
  const q = (s) => card.querySelector(s), qa = (s) => [...card.querySelectorAll(s)];
  const svg = q("svg"), prev = q("[data-fig-prev]"), next = q("[data-fig-next]"), play = q("[data-fig-play]"), level = q("[data-fig-level]");
  const items = qa("[data-fig-step]"), out = {};
  qa("[data-fig-out]").forEach((el) => { out[el.dataset.figOut] = el; });
  const lang = document.documentElement.lang || "fr", still = matchMedia("(prefers-reduced-motion: reduce)");
  const num = (v) => new Intl.NumberFormat(lang, { maximumSignificantDigits: 2 }).format(v);
  let step = 1, high = true, timer = 0, visible = true;
  const show = (key, on) => { const g = q('[data-part="' + key + '"]'); if (on) g.removeAttribute("visibility"); else g.setAttribute("visibility", "hidden"); };
  function draw() {
    const now = write(high), before = write(!high);
    // chaque pièce garde l'état précédent tant que le signal ne l'a pas atteinte
    const bit = step >= 3 ? now.bit : before.bit, sw = step >= 5 ? now.closed : before.closed, pin = step >= 6 ? now : before;
    q('[data-part="bit"]').setAttribute("transform", shift(RISE * bit));
    show("lever-p", sw === "P"); show("lever-n", sw === "N");
    qa(".iso-solid[data-lit]").forEach((el) => el.removeAttribute("data-lit"));
    qa('[data-stage="' + STAGES[step - 1] + '"] .iso-solid').forEach((el) => el.setAttribute("data-lit", ""));
    if (pin.led) qa('[data-part="led"] .iso-solid').forEach((el) => el.setAttribute("data-lit", ""));
    const crossed = STAGES.filter((s) => reached(step, s)).flatMap((s) => [].concat(WIRES[s]));
    if (pin.led) crossed.push("led");
    qa("[data-wire]").forEach((g) => g.querySelector("path").setAttribute("data-tone", crossed.includes(g.dataset.wire) ? "hi" : "lo"));
    items.forEach((li) => { if (+li.dataset.figStep === step) li.setAttribute("aria-current", "step"); else li.removeAttribute("aria-current"); });
    const set = (key, v) => { if (out[key] && out[key].textContent !== v) out[key].textContent = v; };
    set("step", step + " / " + STAGES.length);
    set("code", "digitalWrite(25, " + (high ? "HIGH" : "LOW") + ");");
    set("mask", now.maskHex);
    set("register", now.register.replace("GPIO_OUT_", "").replace("_REG", "") + " (GPIO_OUT)");
    set("address", now.addressHex);
    set("bit", String(bit));
    set("switch", sw === "P" ? out.switch.dataset.p : out.switch.dataset.n);
    set("volts", num(pin.volts) + " V");
    set("led", pin.led ? out.led.dataset.on : out.led.dataset.off);
    prev.disabled = step === 1; next.disabled = step === STAGES.length;
    level.textContent = high ? level.dataset.low : level.dataset.high;
    play.textContent = timer ? play.dataset.pause : play.dataset.play;
  }
  function stop() { clearInterval(timer); timer = 0; }
  function tick() { if (!visible) return; if (step < STAGES.length) { step++; draw(); } else { stop(); draw(); } }
  prev.addEventListener("click", () => { stop(); step = Math.max(1, step - 1); draw(); });
  next.addEventListener("click", () => { stop(); step = Math.min(STAGES.length, step + 1); draw(); });
  level.addEventListener("click", () => { stop(); high = !high; step = 1; draw(); });
  play.addEventListener("click", () => {
    if (timer) { stop(); draw(); return; }
    if (step === STAGES.length) step = 1;
    if (still.matches) { step = STAGES.length; draw(); return; }
    timer = setInterval(tick, STEP_S * 1000);
    draw();
  });
  new IntersectionObserver((e) => { visible = e[e.length - 1].isIntersecting; }).observe(svg);
  q("[data-fig-controls]").hidden = false;
  draw();
});
})();
