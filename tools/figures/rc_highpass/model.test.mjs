// Valeurs du passe-haut RC (R = 1 kΩ, C = 100 nF), littéraux calculés à la main.
// Lancer : node --test "tools/figures/**/*.test.mjs"
import { test } from "node:test";
import assert from "node:assert/strict";

import { FC, xc, ratio, phaseDeg, capRatio, capPhaseDeg, periodS } from "./model.mjs";

const near = (actual, expected, tol) => assert.ok(Math.abs(actual - expected) <= tol, `${actual} ≠ ${expected} ± ${tol}`);

test("la fréquence de coupure vaut 1 591,5 Hz", () => {
  near(FC, 1591.5, 0.1);
});

test("Xc vaut 15 915 Ω à 100 Hz, 1 000 Ω à fc et 99,47 Ω à 16 kHz", () => {
  near(xc(100), 15915, 1);
  near(xc(FC), 1000, 0.01);
  near(xc(16000), 99.47, 0.01);
});

test("Vs/Ve (aux bornes de R) vaut 0,0627 à 100 Hz, 0,707 à fc, 0,995 à 16 kHz", () => {
  near(ratio(100), 0.0627, 0.00005);
  near(ratio(FC), 0.7071, 0.0001);
  near(ratio(16000), 0.9951, 0.00005);
});

test("Vs est en avance : +86,4° à 100 Hz, +45° à fc, +5,68° à 16 kHz", () => {
  near(phaseDeg(100), 86.40, 0.005);
  near(phaseDeg(FC), 45, 0.001);
  near(phaseDeg(16000), 5.68, 0.005);
});

test("la tension du condensateur vaut 0,998 à 100 Hz, 0,707 à fc, 0,0990 à 16 kHz, en retard", () => {
  near(capRatio(100), 0.998, 0.0005);
  near(capRatio(FC), 0.7071, 0.0001);
  near(capRatio(16000), 0.0990, 0.00005);
  near(capPhaseDeg(100), -3.60, 0.005);
  near(capPhaseDeg(16000), -84.32, 0.005);
});

test("Vc + Vs redonne Ve à chaque instant (loi des mailles)", () => {
  for (const f of [100, FC, 16000]) {
    for (const t of [0, 0.4, 1.3, 2.9]) {
      const vs = ratio(f) * Math.sin(t + phaseDeg(f) * Math.PI / 180);
      const vc = capRatio(f) * Math.sin(t + capPhaseDeg(f) * Math.PI / 180);
      near(vs + vc, Math.sin(t), 1e-12);
    }
  }
});

test("la période affichée va de 2 s à 10 Hz à 0,25 s à 100 kHz", () => {
  near(periodS(10), 2, 1e-9);
  near(periodS(100000), 0.25, 1e-9);
});
