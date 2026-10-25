// Circuit bouchon (source 1 V crête, Rs = 10 kΩ en série, L = 10 mH avec 10 Ω de pertes, C = 100 nF), littéraux calculés à la main.
// Lancer : node --test "tools/figures/**/*.test.mjs"
import { test } from "node:test";
import assert from "node:assert/strict";

import { F0, zTank, line, tankV, coil, cap, periodS } from "./model.mjs";

const near = (actual, expected, tol) => assert.ok(Math.abs(actual - expected) <= tol, `${actual} ≠ ${expected} ± ${tol}`);
const wave = ({ amp, deg }, wt) => amp * Math.sin(wt + (deg * Math.PI) / 180);

test("f0 vaut 5 033 Hz, comme pour le circuit série", () => {
  near(F0, 5032.9, 0.1);
});

test("Z du bouchon : 10 005 Ω à f0, 211,2 Ω à f0 / 2, 210,8 Ω à 2 × f0", () => {
  near(zTank(F0), 10005, 1);
  near(zTank(F0 / 2), 211.19, 0.05);
  near(zTank(F0 * 2), 210.80, 0.05);
});

test("le courant de ligne est minimal à f0 : 50,0 µA, contre 99,8 µA et 100,0 µA de part et d'autre", () => {
  near(line(F0).amp, 49.99e-6, 0.01e-6);
  near(line(F0 / 2).amp, 99.80e-6, 0.01e-6);
  near(line(F0 * 2).amp, 99.97e-6, 0.01e-6);
});

test("la tension du bouchon vaut 0,500 Ve à f0 et 0,0211 Ve de part et d'autre", () => {
  near(tankV(F0).amp, 0.5002, 0.0002);
  near(tankV(F0 / 2).amp, 0.02108, 0.00002);
  near(tankV(F0 * 2).amp, 0.02107, 0.00002);
});

test("à f0, 1,58 mA circulent entre L et C, 32 fois le courant de ligne", () => {
  near(coil(F0).amp, 1.581e-3, 0.001e-3);
  near(cap(F0).amp, 1.582e-3, 0.001e-3);
  near(coil(F0 / 2).amp, 0.1331e-3, 0.0002e-3);
  near(cap(F0 / 2).amp, 0.03333e-3, 0.0001e-3);
});

test("loi des nœuds : i(t) = iL(t) + iC(t) à f0 / 2, f0 et 2 × f0", () => {
  for (const f of [F0 / 2, F0, F0 * 2]) {
    for (const wt of [0, 0.7, 2.1, 4]) near(wave(line(f), wt), wave(coil(f), wt) + wave(cap(f), wt), 1e-12);
  }
});

test("la période affichée va de 2 s à 10 Hz à 0,25 s à 100 kHz", () => {
  near(periodS(10), 2, 1e-9);
  near(periodS(100000), 0.25, 1e-9);
});
