// Rôle de l'amplificateur et gain (entrée 50 mV crête, gain de −40 à +40), littéraux calculés à la main.
// Lancer : node --test "tools/figures/**/*.test.mjs"
import { test } from "node:test";
import assert from "node:assert/strict";

import { VE, ve, vs, peakOut, gainOf, inverted, GAIN_MIN, GAIN_MAX } from "./model.mjs";

const near = (actual, expected, tol) => assert.ok(Math.abs(actual - expected) <= tol, `${actual} ≠ ${expected} ± ${tol}`);

test("l'exemple de la section : 50 mV crête à l'entrée, 2 V crête à la sortie, Av = 2 / 0,05 = 40", () => {
  near(VE, 0.05, 1e-12);
  near(peakOut(40), 2, 1e-12);
  near(gainOf(2, 0.05), 40, 1e-12);
});

test("Av = −39 : 1,95 V crête, sortie inversée ; Av = 1 : 50 mV, en phase", () => {
  near(peakOut(-39), 1.95, 1e-12);
  assert.equal(inverted(-39), true);
  near(peakOut(1), 0.05, 1e-12);
  assert.equal(inverted(1), false);
  assert.equal(GAIN_MIN, -40);
  assert.equal(GAIN_MAX, 40);
});

test("à chaque instant vs(t) = Av × ve(t) : en phase pour Av > 0, en opposition pour Av < 0", () => {
  for (const ph of [0.3, 1.2, 2.5, 4]) {
    near(vs(ph, 40), 40 * ve(ph), 1e-12);
    near(vs(ph, -39), -39 * ve(ph), 1e-12);
    assert.ok(Math.sign(vs(ph, -39)) === -Math.sign(ve(ph)));
  }
  near(ve(Math.PI / 2), 0.05, 1e-12);
  near(vs(Math.PI / 2, 40), 2, 1e-12);
  near(vs(Math.PI / 2, -39), -1.95, 1e-12);
});
