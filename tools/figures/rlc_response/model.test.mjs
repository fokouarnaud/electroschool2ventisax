// Courbe de réponse du RLC série (L = 10 mH, C = 100 nF, sous 1 V ; R = 50 Ω ou 200 Ω), littéraux calculés à la main.
// Lancer : node --test "tools/figures/**/*.test.mjs"
import { test } from "node:test";
import assert from "node:assert/strict";

import { F0, R1, R2, z, current, F_LO, F_HI, sweepF } from "./model.mjs";

const near = (actual, expected, tol) => assert.ok(Math.abs(actual - expected) <= tol, `${actual} ≠ ${expected} ± ${tol}`);

test("f0 vaut 5 033 Hz et ne dépend pas de R", () => {
  near(F0, 5032.9, 0.1);
  assert.equal(R1, 50);
  assert.equal(R2, 200);
});

test("Imax = U / R : 20,0 mA avec 50 Ω, 5,00 mA avec 200 Ω", () => {
  near(current(F0, R1), 0.02, 1e-12);
  near(current(F0, R2), 0.005, 1e-12);
});

test("à f0 / 2 et 2 × f0 : Z = 477 Ω et I = 2,10 mA avec 50 Ω ; Z = 515 Ω et I = 1,94 mA avec 200 Ω", () => {
  for (const f of [F0 / 2, F0 * 2]) {
    near(z(f, R1), 476.97, 0.01);
    near(current(f, R1), 0.0020966, 0.0000005);
    near(z(f, R2), 514.78, 0.01);
    near(current(f, R2), 0.0019426, 0.0000005);
  }
});

test("la cloche est symétrique en échelle logarithmique : I(f0 × k) = I(f0 / k)", () => {
  for (const k of [1.1, 1.5, 3]) {
    near(current(F0 * k, R1), current(F0 / k, R1), 1e-12);
    near(current(F0 * k, R2), current(F0 / k, R2), 1e-12);
  }
});

test("le balayage va de 500 Hz à 10,5 kHz en 8 s, puis revient", () => {
  assert.equal(F_LO, 500);
  assert.equal(F_HI, 10500);
  near(sweepF(0), 500, 1e-9);
  near(sweepF(4), 5500, 1e-9);
  near(sweepF(8), 10500, 1e-9);
  near(sweepF(12), 5500, 1e-9);
  near(sweepF(16), 500, 1e-9);
});
