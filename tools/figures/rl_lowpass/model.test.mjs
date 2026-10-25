// Passe-bas RL (L = 10 mH en série, R = 100 Ω vers la masse), littéraux calculés à la main.
// Lancer : node --test "tools/figures/**/*.test.mjs"
import { test } from "node:test";
import assert from "node:assert/strict";

import { FC, xl, ratio, lagDeg, coilRatio, coilPhaseDeg, periodS } from "./model.mjs";

const near = (actual, expected, tol) => assert.ok(Math.abs(actual - expected) <= tol, `${actual} ≠ ${expected} ± ${tol}`);

test("fc = R / (2π × L) vaut 1 591,5 Hz", () => {
  near(FC, 1591.5, 0.1);
});

test("XL vaut 10,0 Ω à fc / 10, 100 Ω à fc (XL = R) et 1 000 Ω à 10 × fc", () => {
  near(xl(FC / 10), 10, 1e-9);
  near(xl(FC), 100, 1e-9);
  near(xl(FC * 10), 1000, 1e-9);
});

test("Vs/Ve, aux bornes de R, vaut 0,995 à fc / 10, 0,707 à fc, 0,0995 à 10 × fc", () => {
  near(ratio(FC / 10), 0.995, 0.0005);
  near(ratio(FC), 0.7071, 0.0001);
  near(ratio(FC * 10), 0.0995, 0.00005);
});

test("le courant (et Vs) retarde de φ = arctan(XL / R) : 5,71°, 45°, 84,3°", () => {
  near(lagDeg(FC / 10), 5.71, 0.005);
  near(lagDeg(FC), 45, 0.001);
  near(lagDeg(FC * 10), 84.29, 0.005);
});

test("VL/Ve vaut 0,0995, 0,707, 0,995 et avance de 90° − φ", () => {
  near(coilRatio(FC / 10), 0.0995, 0.00005);
  near(coilRatio(FC), 0.7071, 0.0001);
  near(coilRatio(FC * 10), 0.995, 0.0005);
  near(coilPhaseDeg(FC), 45, 0.001);
});

test("loi des mailles : VL(t) + Vs(t) = Ve(t) à fc / 10, fc et 10 × fc", () => {
  const rad = Math.PI / 180;
  for (const f of [FC / 10, FC, FC * 10]) {
    for (const wt of [0, 0.7, 2.1, 4]) {
      near(coilRatio(f) * Math.sin(wt + coilPhaseDeg(f) * rad) + ratio(f) * Math.sin(wt - lagDeg(f) * rad), Math.sin(wt), 1e-12);
    }
  }
});

test("la période affichée va de 2 s à 10 Hz à 0,25 s à 100 kHz", () => {
  near(periodS(10), 2, 1e-9);
  near(periodS(100000), 0.25, 1e-9);
});
