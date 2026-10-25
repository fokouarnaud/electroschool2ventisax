// Déphasage du passe-bas RC (R = 1 kΩ, C = 100 nF), littéraux calculés à la main.
// Lancer : node --test "tools/figures/**/*.test.mjs"
import { test } from "node:test";
import assert from "node:assert/strict";

import { FC, xc, ratio, lagDeg, leadDeg, shift, periodS } from "./model.mjs";

const near = (actual, expected, tol) => assert.ok(Math.abs(actual - expected) <= tol, `${actual} ≠ ${expected} ± ${tol}`);
// Xc = 577 Ω, l'exemple de la section : f = 1 / (2π × 577 Ω × 100 nF) ≈ 2 758 Hz.
const F577 = 1 / (2 * Math.PI * 577 * 100e-9);

test("la fréquence de coupure vaut 1 591,5 Hz ; Xc = 577 Ω vers 2 758 Hz", () => {
  near(FC, 1591.5, 0.1);
  near(F577, 2758.3, 0.5);
  near(xc(F577), 577, 1e-9);
});

test("l'avance du courant arctan(Xc / R) vaut 84,3°, 45°, 30,0° et 5,71°", () => {
  near(leadDeg(FC / 10), 84.29, 0.005);
  near(leadDeg(FC), 45, 0.001);
  near(leadDeg(F577), 29.98, 0.005);
  near(leadDeg(FC * 10), 5.71, 0.005);
});

test("le retard de Vs vaut 5,71°, 45°, 60,0° et 84,3° : 90° moins l'avance du courant", () => {
  near(lagDeg(FC / 10), 5.71, 0.005);
  near(lagDeg(FC), 45, 0.001);
  near(lagDeg(F577), 60.02, 0.005);
  near(lagDeg(FC * 10), 84.29, 0.005);
  for (const f of [10, FC / 10, FC, F577, FC * 10, 100000]) near(lagDeg(f) + leadDeg(f), 90, 1e-9);
});

test("Δt / T = φ / 360° vaut 0,0159, 0,125, 0,167 et 0,234", () => {
  near(shift(FC / 10), 0.01586, 0.00005);
  near(shift(FC), 0.125, 1e-9);
  near(shift(F577), 0.1667, 0.00005);
  near(shift(FC * 10), 0.2341, 0.00005);
});

test("Vs/Ve vaut 0,995 à fc / 10, 0,707 à fc, 0,500 à Xc = 577 Ω, 0,0995 à 10 × fc", () => {
  near(ratio(FC / 10), 0.995, 0.0005);
  near(ratio(FC), 0.7071, 0.0001);
  near(ratio(F577), 0.4998, 0.0005);
  near(ratio(FC * 10), 0.0995, 0.00005);
});

test("la période affichée va de 2 s à 10 Hz à 0,25 s à 100 kHz", () => {
  near(periodS(10), 2, 1e-9);
  near(periodS(100000), 0.25, 1e-9);
});
