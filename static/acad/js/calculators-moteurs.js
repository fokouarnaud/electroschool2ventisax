// Calculateurs de la formation « Moteurs électriques et commande » (US-68, US-69), non notés.
// Chargé avant calculators.js, qui les remplit avec ses outils (champs, saisie avec préfixes, affichage).
(function () {
  "use strict";
  var SQRT3 = Math.sqrt(3);

  function number(h, value) {
    return String(Number(value.toPrecision(3))).replace(".", h.L.decimal || ",");
  }

  window.acadMotorCalculators = {
    // I = P / (√3 × U × cos φ × η) en triphasé, P / (U × cos φ × η) en monophasé.
    motor_current: function (slot, h) {
      var L = h.L, f = h.frame(slot, L.motorCurrentTitle, L.motorCurrentHint);
      var mode = h.choice(f.grid, L.supply, (L.supplies || "").split(","));
      var p = h.field(f.grid, L.power, "W", "4k"), u = h.field(f.grid, L.voltage, "V", "400");
      var cos = h.field(f.grid, L.powerFactor, "", "0,85"), eta = h.field(f.grid, L.efficiency, "", "0,88");
      function run() {
        var P = h.parse(p.value), U = h.parse(u.value), C = h.parse(cos.value), E = h.parse(eta.value);
        if (!(P > 0 && U > 0 && C > 0 && C <= 1 && E > 0 && E <= 1)) { f.out.textContent = L.motorCurrentHint; return; }
        f.out.textContent = mode.value === "0"
          ? "I = P / (√3 × U × cos φ × η) = " + h.show(P / (SQRT3 * U * C * E), "A")
          : "I = P / (U × cos φ × η) = " + h.show(P / (U * C * E), "A");
      }
      slot.addEventListener("input", run);
      slot.addEventListener("change", run);
      run();
    },
    // ns = 60 × f / p ; g = (ns − n) / ns.
    speed: function (slot, h) {
      var L = h.L, f = h.frame(slot, L.speedTitle, L.speedHint);
      var hz = h.field(f.grid, L.frequency, "Hz", "50"), pairs = h.field(f.grid, L.polePairs, "", "2");
      var n = h.field(f.grid, L.realSpeed, L.rpm, "1450");
      function run() {
        var F = h.parse(hz.value), P = h.parse(pairs.value), N = h.parse(n.value);
        if (!(F > 0 && P >= 1 && Math.round(P) === P)) { f.out.textContent = L.speedHint; return; }
        var ns = 60 * F / P, parts = ["ns = 60 × f / p = " + number(h, ns) + " " + L.rpm];
        if (N > 0 && N <= ns) parts.push("g = (ns − n) / ns = " + number(h, (ns - N) / ns * 100) + L.percent);
        f.out.textContent = parts.join(" ; ");
      }
      slot.addEventListener("input", run);
      run();
    },
    // C = P / ω, ω = 2π × n / 60.
    torque: function (slot, h) {
      var L = h.L, f = h.frame(slot, L.torqueTitle, null);
      var p = h.field(f.grid, L.power, "W", "4k"), n = h.field(f.grid, L.realSpeed, L.rpm, "1450");
      function run() {
        var P = h.parse(p.value), N = h.parse(n.value);
        if (!(P > 0 && N > 0)) { f.out.textContent = L.fillAll; return; }
        f.out.textContent = "C = P / (2π × n / 60) = " + h.show(P / (2 * Math.PI * N / 60), "N·m");
      }
      slot.addEventListener("input", run);
      run();
    },
    // En étoile, chaque enroulement reçoit U / √3 ; courant et couple de démarrage sont divisés par 3.
    stardelta: function (slot, h) {
      var L = h.L, f = h.frame(slot, L.starDeltaTitle, L.starDeltaHint);
      var u = h.field(f.grid, L.lineVoltage, "V", "400"), i = h.field(f.grid, L.directCurrent, "A", "60");
      var c = h.field(f.grid, L.directTorque, "N·m", "50");
      function run() {
        var U = h.parse(u.value), I = h.parse(i.value), C = h.parse(c.value), parts = [];
        if (U > 0) parts.push(L.windingStar + " = U / √3 = " + h.show(U / SQRT3, "V"));
        if (I > 0) parts.push(L.currentStar + " = " + h.show(I / 3, "A"));
        if (C > 0) parts.push(L.torqueStar + " = " + h.show(C / 3, "N·m"));
        f.out.textContent = parts.length ? parts.join(" ; ") : L.starDeltaHint;
      }
      slot.addEventListener("input", run);
      run();
    }
  };
})();
