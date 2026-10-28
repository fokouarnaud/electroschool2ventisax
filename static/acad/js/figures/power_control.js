// Généré par tools/figures/power_control/build.mjs : ne pas modifier à la main.
(() => {
const REST = { s1: false, s2: false, f1: false, km: false };
const coil = (s) => !s.f1 && !s.s1 && (s.s2 || s.km);
const EVENTS = { "s2-down": { s2: true }, "s2-up": { s2: false }, "s1-down": { s1: true }, "s1-up": { s1: false }, trip: { f1: true }, reset: { f1: false } };
function step(s, event) {
  const next = { ...s, ...EVENTS[event] };
  next.km = coil(next);
  return next;
}
const run = (s, events) => events.reduce(step, s);
const states = (s) => ({ coil: s.km, poles: s.km, c1314: s.km, f9596: !s.f1, motor: s.km });
const POWER = ["Q1", "KM1", "F1", "M1"];
const CONTROL = ["F2", "F1", "S1", "S2", "KM1"];
const SHARED = POWER.filter((d) => CONTROL.includes(d));
const PRESS_S = 0.5; // s pendant lesquelles un bouton reste enfoncé (impulsion)
const TURN_S = 1.2; // s affichées par tour d'arbre (cadence ralentie, F5)
const O = [323.752,197.986], EX = [1.49065,0.6254], EY = [-1.2508,0.74532], EZ = [0,-1.6852];
const VIEWS = {"power":["Q1","KM1p","F1p","M1"],"control":["SUP","F2","F1c","STN","KM1c"],"link":["KM1p","KM1c","F1p","F1c"]}, KEY = [-46,52,28], KEY_R = 2.6;
const scr = (x, y, z) => [O[0] + x * EX[0] + y * EY[0] + z * EZ[0], O[1] + x * EX[1] + y * EY[1] + z * EZ[1]];
const move = (dx, dy, dz) => "translate(" + (EX[0] * dx + EY[0] * dy + EZ[0] * dz).toFixed(3) + " " + (EX[1] * dx + EY[1] * dy + EZ[1] * dz).toFixed(3) + ")";
document.querySelectorAll('.fig[data-fig="power_control"]').forEach((card) => {
  const q = (s) => card.querySelector(s), qa = (s) => [...card.querySelectorAll(s)];
  const svg = q("svg"), part = (k) => q('[data-part="' + k + '"]'), key = q('[data-part="key"] path');
  const views = qa("[data-fig-preset]"), trip = q("[data-fig-trip]"), out = {};
  qa("[data-fig-out]").forEach((el) => { out[el.dataset.figOut] = el; });
  const still = matchMedia("(prefers-reduced-motion: reduce)");
  let s = REST, view = "power", angle = 0, last = 0, frame = 0, visible = true;
  const timers = {};
  function light() {
    qa('[data-dev] .iso-solid').forEach((el) => {
      const on = VIEWS[view].includes(el.parentNode.dataset.dev);
      if (on) el.setAttribute("data-lit", ""); else el.removeAttribute("data-lit");
    });
    views.forEach((b) => b.setAttribute("aria-pressed", b.dataset.figPreset === view ? "true" : "false"));
  }
  function pose() {
    const st = states(s);
    part("s1").setAttribute("transform", move(0, 0, s.s1 ? -2.5 : 0));
    part("s2").setAttribute("transform", move(0, 0, s.s2 ? -2.5 : 0));
    part("km").setAttribute("transform", move(st.poles ? 10 : 0, 0, 0));
    part("f1").setAttribute("transform", move(0, 0, s.f1 ? 3 : 0));
    qa('[data-wire="power"] path').forEach((w) => w.setAttribute("data-tone", st.motor ? "hi" : "lo"));
    q('[data-wire="control"] path').setAttribute("data-tone", st.coil ? "hi" : "lo");
    const a = scr(...KEY), b = scr(KEY[0] + KEY_R * Math.cos(angle), KEY[1] + KEY_R * Math.sin(angle), KEY[2]);
    key.setAttribute("d", "M" + a[0].toFixed(2) + " " + a[1].toFixed(2) + "L" + b[0].toFixed(2) + " " + b[1].toFixed(2));
  }
  function report() {
    const st = states(s), set = (k, v) => { if (out[k] && out[k].textContent !== v) out[k].textContent = v; };
    set("view", out.view.dataset[view]);
    set("role", out.role.dataset[view]);
    set("coil", st.coil ? out.coil.dataset.on : out.coil.dataset.off);
    set("c1314", st.c1314 ? out.c1314.dataset.closed : out.c1314.dataset.open);
    set("f9596", st.f9596 ? out.f9596.dataset.closed : out.f9596.dataset.open);
    set("motor", st.motor ? out.motor.dataset.on : out.motor.dataset.off);
    trip.setAttribute("aria-pressed", s.f1 ? "true" : "false");
    trip.textContent = s.f1 ? trip.dataset.reset : trip.dataset.trip;
  }
  function tick(now) {
    angle += (last ? Math.min(now - last, 100) / 1000 : 0) * 2 * Math.PI / TURN_S;
    last = now;
    pose();
    frame = states(s).motor && visible && !still.matches ? requestAnimationFrame(tick) : 0;
  }
  const run = () => { if (!frame && states(s).motor && visible && !still.matches) { last = 0; frame = requestAnimationFrame(tick); } };
  const apply = (event) => { s = step(s, event); pose(); report(); run(); };
  function press(button) {
    clearTimeout(timers[button]);
    apply(button + "-down");
    timers[button] = setTimeout(() => apply(button + "-up"), still.matches ? 0 : PRESS_S * 1000);
  }
  qa("[data-fig-press]").forEach((b) => b.addEventListener("click", () => press(b.dataset.figPress)));
  trip.addEventListener("click", () => apply(s.f1 ? "reset" : "trip"));
  views.forEach((b) => b.addEventListener("click", () => { view = b.dataset.figPreset; light(); report(); }));
  new IntersectionObserver((e) => { visible = e[e.length - 1].isIntersecting; run(); }).observe(svg);
  q("[data-fig-controls]").hidden = false;
  light();
  pose();
  report();
});
})();
