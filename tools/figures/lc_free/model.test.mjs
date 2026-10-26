// Oscillation libre d'un LC avec pertes (L = 10 mH, C = 100 nF, chargé à 1 V), littéraux calculés à la main.
// Lancer : node --test "tools/figures/**/*.test.mjs"
import { test } from "node:test";
import assert from "node:assert/strict";

import { F0, q, alpha, omegaD, vc, current, energyC, energyL, period } from "./model.mjs";

const near = (actual, expected, tol) => assert.ok(Math.abs(actual - expected) <= tol, `${actual} ≠ ${expected} ± ${tol}`);

test("Q = √(L/C) / R : 31,6 avec 10 Ω, 7,91 avec 40 Ω (la courbe de la section), 3,16 avec 100 Ω", () => {
  near(F0, 5032.9, 0.1);
  near(q(10), 31.623, 0.001);
  near(q(40), 7.9057, 0.0001);
  near(q(100), 3.1623, 0.0001);
});

test("avec 40 Ω : α = 2 000 s⁻¹, ωd = 31 559,5 rad/s, période 199,09 µs, enveloppe τ = 2,5 périodes", () => {
  near(alpha(40), 2000, 1e-9);
  near(omegaD(40), 31559.5, 0.1);
  near(period(40), 199.09e-6, 0.01e-6);
  near(1 / alpha(40) / (1 / F0), 2.516, 0.001);
});

test("à t = 0 : Vc = 1 V, i = 0, toute l'énergie (50 nJ) est dans le condensateur", () => {
  near(vc(0, 40), 1, 1e-12);
  near(current(0, 40), 0, 1e-12);
  near(energyC(0, 40), 50e-9, 1e-15);
  near(energyL(0, 40), 0, 1e-15);
});

test("premier pic de courant à t = π / 2ωd : 2,868 mA", () => {
  near(Math.abs(current(Math.PI / (2 * omegaD(40)), 40)), 2.8684e-3, 0.0002e-3);
});

test("après une période, Vc = 0,6716 V et il reste 45,1 % de l'énergie ; après cinq, Vc = 0,1366 V", () => {
  const T = period(40);
  near(vc(T, 40), 0.67155, 0.00005);
  near((energyC(T, 40) + energyL(T, 40)) / 50e-9, 0.45098, 0.00005);
  near(vc(5 * T, 40), 0.13657, 0.00005);
});

test("l'énergie totale ne fait que décroître, et vaut ½CVc² + ½Li²", () => {
  let prev = Infinity;
  for (let n = 0; n <= 40; n++) {
    const t = (n * period(40)) / 8, e = energyC(t, 40) + energyL(t, 40);
    assert.ok(e <= prev + 1e-18, `t = ${t}`);
    prev = e;
  }
});

test("i = dq/dt : la dérivée numérique de C × Vc donne le courant", () => {
  for (const t of [10e-6, 73e-6, 151e-6]) {
    const h = 1e-10, dq = (100e-9 * vc(t + h, 40) - 100e-9 * vc(t - h, 40)) / (2 * h);
    near(current(t, 40), dq, 1e-7);
  }
});
