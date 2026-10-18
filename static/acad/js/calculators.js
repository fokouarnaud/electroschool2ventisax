// Calculateurs du cours (US-13), non notés. Le serveur place des emplacements inertes
// <div class="calc" data-calc="ohm|divider|resistor|bias"> ; les libellés traduits viennent de #calc-labels.
(function () {
  "use strict";
  var slots = document.querySelectorAll(".calc[data-calc]");
  var L = (document.getElementById("calc-labels") || { dataset: {} }).dataset;
  if (!slots.length) return;

  var PREFIX = { p: 1e-12, n: 1e-9, u: 1e-6, "µ": 1e-6, "μ": 1e-6, m: 1e-3, k: 1e3, M: 1e6, G: 1e9 };
  var SHOW = [[1e9, "G"], [1e6, "M"], [1e3, "k"], [1, ""], [1e-3, "m"], [1e-6, "µ"], [1e-9, "n"], [1e-12, "p"]];

  // « 4,7k » ou « 2.2 mA » -> nombre en unité de base ; NaN si la saisie n'est pas une grandeur.
  function parse(text) {
    var m = String(text).trim().match(/^([+-]?\d+(?:[.,]\d+)?)\s*([pnuµμmkMG]?)/);
    return m ? parseFloat(m[1].replace(",", ".")) * (m[2] ? PREFIX[m[2]] : 1) : NaN;
  }
  function show(value, unit) {
    if (!isFinite(value)) return "-";
    if (value === 0) return "0 " + unit;
    var abs = Math.abs(value);
    for (var i = 0; i < SHOW.length; i++) {
      if (abs >= SHOW[i][0] * 0.9995 || i === SHOW.length - 1) {
        var n = (value / SHOW[i][0]).toPrecision(3);
        if (n.indexOf(".") >= 0) n = n.replace(/0+$/, "").replace(/\.$/, ""); // « 100 » garde ses zéros
        return n.replace(".", L.decimal || ",") + " " + SHOW[i][1] + unit;
      }
    }
  }
  function el(tag, attrs, text) {
    var e = document.createElement(tag);
    Object.keys(attrs || {}).forEach(function (k) { e.setAttribute(k, attrs[k]); });
    if (text) e.textContent = text;
    return e;
  }
  var uid = 0;
  function field(box, label, unit, placeholder) {
    var id = "calc-" + (++uid);
    var wrap = el("div", { "class": "field" });
    wrap.appendChild(el("label", { "for": id }, label));
    var row = el("div", { "class": "unit-input" });
    var input = el("input", { id: id, type: "text", inputmode: "decimal", autocomplete: "off", spellcheck: "false", placeholder: placeholder || "" });
    row.appendChild(input);
    if (unit) row.appendChild(el("span", { "class": "unit" }, unit));
    wrap.appendChild(row);
    box.appendChild(wrap);
    return input;
  }
  function frame(slot, title, hint) {
    slot.setAttribute("role", "group");
    slot.setAttribute("aria-label", title);
    var head = el("p", { "class": "calc-title" }, title);
    slot.appendChild(head);
    if (hint) slot.appendChild(el("p", { "class": "calc-hint" }, hint));
    var grid = el("div", { "class": "calc-grid" });
    slot.appendChild(grid);
    var out = el("output", { "class": "calc-out", "aria-live": "polite" });
    slot.appendChild(out);
    return { grid: grid, out: out };
  }

  var builders = {
    ohm: function (slot) {
      var f = frame(slot, L.ohmTitle, L.ohmHint);
      var u = field(f.grid, L.voltage, "V", "12"), i = field(f.grid, L.current, "A", "2,5m"), r = field(f.grid, L.resistance, "Ω", "4,7k");
      function run() {
        var U = parse(u.value), I = parse(i.value), R = parse(r.value);
        if (!isNaN(U) && !isNaN(R) && isNaN(I)) f.out.textContent = "I = U / R = " + show(U / R, "A");
        else if (!isNaN(U) && !isNaN(I) && isNaN(R)) f.out.textContent = "R = U / I = " + show(U / I, "Ω");
        else if (!isNaN(I) && !isNaN(R) && isNaN(U)) f.out.textContent = "U = R × I = " + show(R * I, "V");
        else f.out.textContent = L.ohmHint;
      }
      slot.addEventListener("input", run);
      run();
    },
    divider: function (slot) {
      var f = frame(slot, L.dividerTitle, null);
      var vin = field(f.grid, L.vin, "V", "12"), r1 = field(f.grid, "R1", "Ω", "10k"), r2 = field(f.grid, "R2", "Ω", "4,7k");
      function run() {
        var V = parse(vin.value), a = parse(r1.value), b = parse(r2.value);
        f.out.textContent = (isNaN(V) || isNaN(a) || isNaN(b) || a + b === 0) ? L.fillAll : "Vs = Ve × R2 / (R1 + R2) = " + show(V * b / (a + b), "V");
      }
      slot.addEventListener("input", run);
      run();
    },
    resistor: function (slot) {
      var f = frame(slot, L.resistorTitle, null);
      var colors = (L.colors || "").split(",");
      function band(label, values) {
        var id = "calc-" + (++uid);
        var wrap = el("div", { "class": "field" });
        wrap.appendChild(el("label", { "for": id }, label));
        var select = el("select", { id: id });
        values.forEach(function (v) { select.appendChild(el("option", { value: v[0] }, v[1])); });
        wrap.appendChild(select);
        f.grid.appendChild(wrap);
        return select;
      }
      var digits = colors.slice(0, 10).map(function (c, n) { return [n, n + " " + c]; });
      var multipliers = colors.slice(0, 7).map(function (c, n) { return [n, "×" + show(Math.pow(10, n), "").trim() + " " + c]; });
      var b1 = band(L.band1, digits), b2 = band(L.band2, digits), b3 = band(L.multiplier, multipliers);
      b1.value = "4"; b2.value = "7"; b3.value = "2";
      function run() {
        var value = (parseInt(b1.value, 10) * 10 + parseInt(b2.value, 10)) * Math.pow(10, parseInt(b3.value, 10));
        f.out.textContent = "R = " + show(value, "Ω");
      }
      slot.addEventListener("change", run);
      run();
    },
    bias: function (slot) {
      var f = frame(slot, L.biasTitle, L.biasHint);
      var vbb = field(f.grid, "VBB", "V", "5"), rb = field(f.grid, "RB", "Ω", "100k"), beta = field(f.grid, "β", "", "100");
      function run() {
        var V = parse(vbb.value), R = parse(rb.value), B = parse(beta.value);
        if (isNaN(V) || isNaN(R) || isNaN(B) || R === 0) { f.out.textContent = L.fillAll; return; }
        var ib = Math.max(0, (V - 0.7) / R);
        f.out.textContent = "IB = (VBB − 0" + (L.decimal || ",") + "7 V) / RB = " + show(ib, "A") + " ; IC = β × IB = " + show(B * ib, "A");
      }
      slot.addEventListener("input", run);
      run();
    }
  };
  slots.forEach(function (slot) {
    var build = builders[slot.dataset.calc];
    if (build) { slot.classList.add("is-live"); build(slot); }
  });
})();
