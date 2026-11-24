// Calculateurs de la formation « Microcontrôleurs : l'ESP32 » (US-111, US-112), non notés.
// Chargé avant calculators.js, qui les remplit avec ses outils (champs, saisie avec préfixes, affichage).
(function () {
  "use strict";
  var VCC = 3.3, ADC_MAX = 4095, LEDC_CLOCK = 80e6;

  function whole(value) {
    return String(Math.round(value));
  }
  function vcc(h) {
    return "3" + (h.L.decimal || ",") + "3 V";
  }

  window.acadEsp32Calculators = {
    // R = (3,3 V − Vf) / I ; courant réel avec la résistance choisie.
    led: function (slot, h) {
      var L = h.L, f = h.frame(slot, L.ledTitle, null);
      var vf = h.field(f.grid, L.forwardVoltage, "V", "2"), i = h.field(f.grid, L.ledCurrent, "A", "4m");
      var r = h.field(f.grid, L.chosenResistance, "Ω", "330");
      function run() {
        var VF = h.parse(vf.value), I = h.parse(i.value), R = h.parse(r.value), parts = [];
        if (!(VF > 0 && VF < VCC)) { f.out.textContent = L.ledHint; return; }
        if (I > 0) parts.push("R = (" + vcc(h) + " − Vf) / I = " + h.show((VCC - VF) / I, "Ω"));
        if (R > 0) parts.push(L.realCurrent + " = " + h.show((VCC - VF) / R, "A"));
        f.out.textContent = parts.length ? parts.join(" ; ") : L.ledHint;
      }
      slot.addEventListener("input", run);
      run();
    },
    // Modèle idéal : valeur = U / 3,3 V × 4095, et inversement.
    adc: function (slot, h) {
      var L = h.L, f = h.frame(slot, L.adcTitle, L.adcHint);
      var u = h.field(f.grid, L.voltage, "V", "1,65"), v = h.field(f.grid, L.adcValue, "", "2048");
      function run() {
        var U = h.parse(u.value), V = h.parse(v.value);
        if (U >= 0 && U <= VCC) f.out.textContent = L.adcValue + " = U / " + vcc(h) + " × 4095 = " + whole(U / VCC * ADC_MAX);
        else if (V >= 0 && V <= ADC_MAX) f.out.textContent = "U = " + L.adcValue + " × " + vcc(h) + " / 4095 = " + h.show(V * VCC / ADC_MAX, "V");
        else f.out.textContent = L.adcHint;
      }
      slot.addEventListener("input", run);
      run();
    },
    // valeur = rapport cyclique × (2^bits − 1) ; fréquence maximale = 80 MHz / 2^bits.
    pwm: function (slot, h) {
      var L = h.L, f = h.frame(slot, L.pwmTitle, null);
      var bits = h.field(f.grid, L.resolution, "bits", "8"), duty = h.field(f.grid, L.dutyCycle, "%", "50");
      function run() {
        var B = h.parse(bits.value), D = h.parse(duty.value);
        if (!(B >= 1 && B <= 20 && Math.round(B) === B)) { f.out.textContent = L.pwmHint; return; }
        var steps = Math.pow(2, B), parts = [L.maxFrequency + " = 80 MHz / 2^" + B + " = " + h.show(LEDC_CLOCK / steps, "Hz")];
        if (D >= 0 && D <= 100) parts.push(L.pwmValue + " = " + whole(D / 100 * (steps - 1)));
        f.out.textContent = parts.join(" ; ");
      }
      slot.addEventListener("input", run);
      run();
    },
    // Trame 8N1 : 10 bits par octet ; durée = 10 / débit, octets par seconde = débit / 10.
    uart: function (slot, h) {
      var L = h.L, f = h.frame(slot, L.uartTitle, null);
      var rate = h.field(f.grid, L.bitRate, "bit/s", "115200");
      function run() {
        var R = h.parse(rate.value);
        if (!(R > 0)) { f.out.textContent = L.fillAll; return; }
        f.out.textContent = L.byteTime + " = 10 / " + whole(R) + " = " + h.show(10 / R, "s") +
          " ; " + L.bytesPerSecond + " = " + whole(R / 10);
      }
      slot.addEventListener("input", run);
      run();
    }
  };
})();
