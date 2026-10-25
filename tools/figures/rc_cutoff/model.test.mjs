// Fréquence de coupure du passe-bas RC (R = 1 kΩ, C = 100 nF), littéraux calculés à la main.
// Lancer : node --test "tools/figures/**/*.test.mjs"
import { test } from "node:test";
import assert from "node:assert/strict";

import { FC, xc, ratio, ratioR, phaseDeg, phaseRDeg, periodS } from "./model.mjs";

const near = (actual, expected, tol) => assert.ok(Math.abs(actual - expected) <= tol, `${actual} ≠ ${expected} ± ${tol}`);

test("la fréquence de coupure vaut 1 591,5 Hz", () => {
  near(FC, 1591.5, 0.1);
});

test("Xc vaut 10 000 Ω à fc / 10, 1 000 Ω à fc (Xc = R) et 100 Ω à 10 × fc", () => {
  near(xc(FC / 10), 10000, 0.01);
  near(xc(FC), 1000, 0.01);
  near(xc(FC * 10), 100, 0.01);
});

test("Vs/Ve vaut 0,995 à fc / 10, 0,707 à fc, 0,0995 à 10 × fc", () => {
  near(ratio(FC / 10), 0.995, 0.0005);
  near(ratio(FC), 0.7071, 0.0001);
  near(ratio(FC * 10), 0.0995, 0.00005);
});

test("la tension aux bornes de R vaut 0,0995, 0,707 puis 0,995 de Ve : égale à Vs à fc seulement", () => {
  near(ratioR(FC / 10), 0.0995, 0.00005);
  near(ratioR(FC), 0.7071, 0.0001);
  near(ratioR(FC * 10), 0.995, 0.0005);
  near(ratio(FC) - ratioR(FC), 0, 1e-12);
});

test("VR avance de +84,3° à fc / 10, +45° à fc, +5,71° à 10 × fc ; Vs retarde de −5,71°, −45°, −84,3°", () => {
  near(phaseRDeg(FC / 10), 84.29, 0.005);
  near(phaseRDeg(FC), 45, 0.001);
  near(phaseRDeg(FC * 10), 5.71, 0.005);
  near(phaseDeg(FC / 10), -5.71, 0.005);
  near(phaseDeg(FC * 10), -84.29, 0.005);
});

test("loi des mailles : VR(t) + Vs(t) = Ve(t) à fc / 10, fc et 10 × fc", () => {
  const rad = Math.PI / 180;
  for (const f of [FC / 10, FC, FC * 10]) {
    for (const wt of [0, 0.7, 2.1, 4]) {
      near(ratioR(f) * Math.sin(wt + phaseRDeg(f) * rad) + ratio(f) * Math.sin(wt + phaseDeg(f) * rad), Math.sin(wt), 1e-12);
    }
  }
});

test("la période affichée va de 2 s à 10 Hz à 0,25 s à 100 kHz", () => {
  near(periodS(10), 2, 1e-9);
  near(periodS(100000), 0.25, 1e-9);
});
