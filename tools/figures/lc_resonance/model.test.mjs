// Résonance RLC série (R = 50 Ω, L = 10 mH, C = 100 nF, sous 1 V), littéraux calculés à la main.
// Lancer : node --test "tools/figures/**/*.test.mjs"
import { test } from "node:test";
import assert from "node:assert/strict";

import { F0, xl, xc, z, current, leadDeg, vc, vl, periodS } from "./model.mjs";

const near = (actual, expected, tol) => assert.ok(Math.abs(actual - expected) <= tol, `${actual} ≠ ${expected} ± ${tol}`);

test("f0 = 1 / (2π√(LC)) vaut 5 033 Hz ; à f0, XL = XC ≈ 316 Ω", () => {
  near(F0, 5032.9, 0.1);
  near(xl(F0), 316.23, 0.01);
  near(xc(F0), 316.23, 0.01);
});

test("XL et XC valent 158 Ω et 632 Ω à f0 / 2, l'inverse à 2 × f0", () => {
  near(xl(F0 / 2), 158.11, 0.01);
  near(xc(F0 / 2), 632.46, 0.01);
  near(xl(F0 * 2), 632.46, 0.01);
  near(xc(F0 * 2), 158.11, 0.01);
});

test("Z = √(R² + (XL − XC)²) vaut 50 Ω à f0 (Z = R) et 477 Ω à f0 / 2 et 2 × f0", () => {
  near(z(F0), 50, 1e-9);
  near(z(F0 / 2), 476.97, 0.01);
  near(z(F0 * 2), 476.97, 0.01);
});

test("I = U / Z vaut 20,0 mA à f0 et 2,10 mA de part et d'autre", () => {
  near(current(F0), 0.02, 1e-12);
  near(current(F0 / 2), 0.0020966, 0.0000005);
  near(current(F0 * 2), 0.0020966, 0.0000005);
});

test("le courant avance de 84,0° à f0 / 2 (capacitif), est en phase à f0, retarde de 84,0° à 2 × f0 (inductif)", () => {
  near(leadDeg(F0 / 2), 83.98, 0.005);
  near(leadDeg(F0), 0, 1e-9);
  near(leadDeg(F0 * 2), -83.98, 0.005);
});

test("Vc vaut 6,32 V à f0 pour 1 V d'entrée, 1,33 V à f0 / 2 ; VL vaut 0,332 V à f0 / 2", () => {
  near(vc(F0), 6.325, 0.001);
  near(vl(F0), 6.325, 0.001);
  near(vc(F0 / 2), 1.3260, 0.0005);
  near(vl(F0 / 2), 0.3315, 0.0005);
});

test("loi des mailles : VR(t) + VL(t) + VC(t) = Ve(t) à f0 / 2, f0 et 2 × f0", () => {
  const rad = Math.PI / 180;
  for (const f of [F0 / 2, F0, F0 * 2]) {
    const i = current(f), p = leadDeg(f) * rad;
    for (const wt of [0, 0.7, 2.1, 4]) {
      const sum = 50 * i * Math.sin(wt + p) + xl(f) * i * Math.sin(wt + p + Math.PI / 2) + xc(f) * i * Math.sin(wt + p - Math.PI / 2);
      near(sum, Math.sin(wt), 1e-12);
    }
  }
});

test("la période affichée va de 2 s à 10 Hz à 0,25 s à 100 kHz", () => {
  near(periodS(10), 2, 1e-9);
  near(periodS(100000), 0.25, 1e-9);
});
