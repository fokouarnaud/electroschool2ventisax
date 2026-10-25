// US-85 : valeurs du passe-bas RC (R = 1 kΩ, C = 100 nF), littéraux calculés à la main.
// Lancer : node --test "tools/figures/**/*.test.mjs"
import { test } from "node:test";
import assert from "node:assert/strict";

import { FC, xc, ratio, phaseDeg, periodS } from "./model.mjs";

const near = (actual, expected, tol) => assert.ok(Math.abs(actual - expected) <= tol, `${actual} ≠ ${expected} ± ${tol}`);

test("la fréquence de coupure vaut 1 591,5 Hz", () => {
  near(FC, 1591.5, 0.1);
});

test("Xc vaut 15 915 Ω à 100 Hz et 1 000 Ω à fc", () => {
  near(xc(100), 15915, 1);
  near(xc(FC), 1000, 0.01);
});

test("Vs/Ve vaut 0,998 à 100 Hz, 0,707 à fc, 0,0990 à 16 kHz", () => {
  near(ratio(100), 0.998, 0.0005);
  near(ratio(FC), 0.7071, 0.0001);
  near(ratio(16000), 0.0990, 0.00005);
});

test("le déphasage vaut −3,60° à 100 Hz, −45° à fc, −84,3° à 16 kHz", () => {
  near(phaseDeg(100), -3.60, 0.005);
  near(phaseDeg(FC), -45, 0.001);
  near(phaseDeg(16000), -84.32, 0.005);
});

test("la période affichée va de 2 s à 10 Hz à 0,25 s à 100 kHz", () => {
  near(periodS(10), 2, 1e-9);
  near(periodS(100000), 0.25, 1e-9);
});
