// Généré par tools/figures/terminal_plate/build.mjs : ne pas modifier à la main.
(() => {
const TOP = ["U1", "V1", "W1"];
const BOTTOM = TOP.map((_, c) => `${TOP[(c + 2) % 3][0]}2`);
const place = (mark) => (mark[1] === "1" ? [TOP.indexOf(mark), 0] : [BOTTOM.indexOf(mark), 1]);
const winding = (letter) => [`${letter}1`, `${letter}2`];
const links = (coupling) => (coupling === "star" ? [BOTTOM.slice()] : TOP.map((m, c) => [m, BOTTOM[c]]));
const NETWORK = { star: 400, delta: 230 };
const windingVoltage = (coupling, network) => (coupling === "star" ? network / Math.sqrt(3) : network);
const LIFT = 10; // hauteur dont les barrettes se lèvent pendant le changement (unités du dessin)
const SWAP_S = 0.8; // s affichées pour changer les barrettes (mouvement illustratif)
const EZ = [0,-2.21518];
const lift = (dz) => "translate(" + (EZ[0] * dz).toFixed(3) + " " + (EZ[1] * dz).toFixed(3) + ")";
document.querySelectorAll('.fig[data-fig="terminal_plate"]').forEach((card) => {
  const q = (s) => card.querySelector(s), qa = (s) => [...card.querySelectorAll(s)];
  const svg = q("svg"), groups = { star: q('[data-part="star"]'), delta: q('[data-part="delta"]') };
  const couplings = qa("[data-fig-coupling]"), presets = qa("[data-fig-preset]"), out = {};
  qa("[data-fig-out]").forEach((el) => { out[el.dataset.figOut] = el; });
  const lang = document.documentElement.lang || "fr", still = matchMedia("(prefers-reduced-motion: reduce)");
  const volts = (v) => new Intl.NumberFormat(lang, { maximumSignificantDigits: 2 }).format(v) + "\u00a0V";
  let sel = "U", from = "star", to = "star", u = 1, last = 0, frame = 0, visible = true;
  function light() {
    qa(".iso-solid[data-lit]").forEach((el) => el.removeAttribute("data-lit"));
    qa('[data-coil="' + sel + '"] .iso-solid, [data-nut="' + sel + '"] .iso-solid').forEach((el) => el.setAttribute("data-lit", ""));
    qa("[data-trace]").forEach((g) => g.firstElementChild.setAttribute("data-tone", g.dataset.trace === sel ? "lit" : "lo"));
    presets.forEach((b) => b.setAttribute("aria-pressed", b.dataset.figPreset === sel ? "true" : "false"));
  }
  function report() {
    const set = (k, v) => { if (out[k] && out[k].textContent !== v) out[k].textContent = v; };
    set("coupling", out.coupling.dataset[to]);
    set("links", links(to).map((b) => b.join("-")).join(", "));
    set("winding", winding(sel).join("-"));
    set("network", volts(NETWORK[to]));
    set("volts", volts(windingVoltage(to, NETWORK[to])));
    couplings.forEach((b) => b.setAttribute("aria-pressed", b.dataset.figCoupling === to ? "true" : "false"));
  }
  function pose() {
    const old = u < 0.5, z = old ? LIFT * 2 * u : LIFT * (2 - 2 * u);
    for (const c of ["star", "delta"]) {
      const on = c === (old ? from : to);
      groups[c].setAttribute("visibility", on ? "visible" : "hidden");
      groups[c].setAttribute("transform", lift(on ? z : LIFT));
    }
  }
  function tick(now) {
    u = Math.min(1, u + (last ? Math.min(now - last, 100) / 1000 / SWAP_S : 0));
    last = now;
    pose();
    frame = u < 1 && visible && !still.matches ? requestAnimationFrame(tick) : 0;
  }
  const run = () => { if (!frame && u < 1) { if (still.matches) { u = 1; pose(); } else if (visible) { last = 0; frame = requestAnimationFrame(tick); } } };
  couplings.forEach((b) => b.addEventListener("click", () => {
    const next = b.dataset.figCoupling;
    if (next === to) return;
    from = u < 0.5 ? from : to;
    to = next;
    u = from === to ? 1 : 0;
    pose();
    report();
    run();
  }));
  presets.forEach((b) => b.addEventListener("click", () => { sel = b.dataset.figPreset; light(); report(); }));
  new IntersectionObserver((e) => { visible = e[e.length - 1].isIntersecting; if (!visible) { u = 1; pose(); } run(); }).observe(svg);
  q("[data-fig-controls]").hidden = false;
  light();
  report();
});
})();
