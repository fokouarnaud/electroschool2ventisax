// Généré par tools/figures/contact_marking/build.mjs : ne pas modifier à la main.
(() => {
const STROKE = 5; // course de l'équipage mobile (unités du dessin)
const TOUCH = 2; // décalage maximal du pont sur ses plots pour que le contact soit fermé
const TRAVEL_S = 0.6; // s affichées pour la course entière (cadence ralentie, F5)

const marking = (order, kind) => (kind === "make" ? [`${order}3`, `${order}4`] : [`${order}1`, `${order}2`]);
function decode(a, b) {
  const order = Math.floor(+a / 10);
  if (order < 1 || Math.floor(+b / 10) !== order) return null;
  const pair = `${+a % 10}${+b % 10}`;
  return pair === "34" ? { order, kind: "make" } : pair === "12" ? { order, kind: "break" } : null;
}
const pole = (n) => [2 * n - 1, 2 * n];
const offset = (kind, t) => (kind === "make" ? (t - 1) * STROKE : t * STROKE);
const closed = (kind, t) => Math.abs(offset(kind, t)) <= TOUCH + 1e-9;
const EX = [1.91278,0.55217], CONTACTS = [["p1","make","1-2"],["p2","make","3-4"],["p3","make","5-6"],["c1","make","13-14"],["c2","break","21-22"],["c3","break","31-32"],["c4","make","43-44"]];
const shift = (dx) => "translate(" + (EX[0] * dx).toFixed(3) + " " + (EX[1] * dx).toFixed(3) + ")";
document.querySelectorAll('.fig[data-fig="contact_marking"]').forEach((card) => {
  const q = (s) => card.querySelector(s), qa = (s) => [...card.querySelectorAll(s)];
  const svg = q("svg"), cars = qa('[data-part="carriage"]'), power = q("[data-fig-power]"), presets = qa("[data-fig-preset]"), out = {};
  qa("[data-fig-out]").forEach((el) => { out[el.dataset.figOut] = el; });
  const lang = document.documentElement.lang || "fr", still = matchMedia("(prefers-reduced-motion: reduce)");
  let sel = "c1", t = 0, target = 0, last = 0, frame = 0, visible = true;
  const solids = (key) => qa('[data-contact="' + key + '"] .iso-solid, [data-screw="' + key + '"] .iso-solid' + (key === "coil" ? ", [data-coil] .iso-solid" : ""));
  function light() {
    qa(".iso-solid[data-lit]").forEach((el) => el.removeAttribute("data-lit"));
    solids(sel).forEach((el) => el.setAttribute("data-lit", ""));
    presets.forEach((b) => b.setAttribute("aria-pressed", b.dataset.figPreset === sel ? "true" : "false"));
  }
  function report() {
    const row = sel === "coil" ? null : CONTACTS.find((c) => c[0] === sel);
    const set = (k, v) => { if (out[k] && out[k].textContent !== v) out[k].textContent = v; };
    set("mark", row ? row[2] : "A1-A2");
    const first = row && row[0][0] === "c" ? decode(...row[2].split("-")) : null;
    set("order", first ? new Intl.NumberFormat(lang).format(first.order) : out.order.dataset.none);
    set("kind", row ? (row[0][0] === "p" ? out.kind.dataset.pole : out.kind.dataset[row[1]]) : out.kind.dataset.coil);
    set("state", row ? (closed(row[1], t) ? out.state.dataset.closed : out.state.dataset.open) : (target ? out.state.dataset.on : out.state.dataset.off));
  }
  function pose() { cars.forEach((g) => g.setAttribute("transform", shift(STROKE * t))); }
  function tick(now) {
    const step = last ? Math.min(now - last, 100) / 1000 / TRAVEL_S : 0;
    last = now;
    t = target ? Math.min(1, t + step) : Math.max(0, t - step);
    pose();
    report();
    frame = t !== target && visible && !still.matches ? requestAnimationFrame(tick) : 0;
  }
  const run = () => { if (!frame && t !== target) { if (still.matches) { t = target; pose(); report(); } else if (visible) { last = 0; frame = requestAnimationFrame(tick); } } };
  power.addEventListener("click", () => {
    target = target ? 0 : 1;
    power.setAttribute("aria-pressed", target ? "true" : "false");
    power.textContent = target ? power.dataset.off : power.dataset.on;
    report();
    run();
  });
  presets.forEach((b) => b.addEventListener("click", () => { sel = b.dataset.figPreset; light(); report(); }));
  new IntersectionObserver((e) => { visible = e[e.length - 1].isIntersecting; run(); }).observe(svg);
  q("[data-fig-controls]").hidden = false;
  light();
  report();
});
})();
