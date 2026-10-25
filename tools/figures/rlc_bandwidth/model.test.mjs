// Bande passante du RLC série (L = 10 mH, C = 100 nF ; R = 50 Ω ou 200 Ω), littéraux calculés à la main.
// Lancer : node --test "tools/figures/**/*.test.mjs"
import { test } from "node:test";
import assert from "node:assert/strict";

import { F0, R1, R2, xl, ratio, f1, f2, band, q, F_LO, F_HI, sweepF } from "./model.mjs";

const near = (actual, expected, tol) => assert.ok(Math.abs(actual - expected) <= tol, `${actual} ≠ ${expected} ± ${tol}`);

test("Q = XL(f0) / R vaut 6,32 avec 50 Ω et 1,58 avec 200 Ω", () => {
  near(xl(F0), 316.23, 0.01);
  near(q(R1), 6.3246, 0.0005);
  near(q(R2), 1.5811, 0.0005);
});

test("f1 et f2 valent 4 650,7 Hz et 5 446,5 Hz avec 50 Ω ; 3 687,0 Hz et 6 870,2 Hz avec 200 Ω", () => {
  near(f1(R1), 4650.7, 0.1);
  near(f2(R1), 5446.5, 0.1);
  near(f1(R2), 3687.0, 0.1);
  near(f2(R2), 6870.2, 0.1);
});

test("BP = f2 − f1 vaut 795,8 Hz et 3 183,1 Hz, soit f0 / Q", () => {
  near(band(R1), 795.8, 0.05);
  near(band(R2), 3183.1, 0.05);
  near(band(R1), F0 / q(R1), 1e-9);
  near(band(R2), F0 / q(R2), 1e-9);
});

test("I / Imax vaut 0,707 à f1 et f2, 1 à f0 ; le circuit de 200 Ω est encore à 0,970 aux bornes de l'autre", () => {
  for (const r of [R1, R2]) {
    near(ratio(f1(r), r), Math.SQRT1_2, 1e-12);
    near(ratio(f2(r), r), Math.SQRT1_2, 1e-12);
    near(ratio(F0, r), 1, 1e-12);
  }
  near(ratio(f1(R1), R2), 0.9701, 0.0001);
  near(ratio(f2(R1), R2), 0.9701, 0.0001);
});

test("le balayage va de 2 kHz à 8 kHz en 8 s, puis revient", () => {
  assert.equal(F_LO, 2000);
  assert.equal(F_HI, 8000);
  near(sweepF(0), 2000, 1e-9);
  near(sweepF(8), 8000, 1e-9);
  near(sweepF(12), 5000, 1e-9);
});
