// Circuit d'accord (L = 100 µH, condensateur variable de 180 à 360 pF, Q = 40 comme la courbe de la section), littéraux calculés à la main.
// Lancer : node --test "tools/figures/**/*.test.mjs"
import { test } from "node:test";
import assert from "node:assert/strict";

import { L, CMIN, CMAX, STATIONS, f0, cTune, response, overlapDeg, sweepC } from "./model.mjs";

const near = (actual, expected, tol) => assert.ok(Math.abs(actual - expected) <= tol, `${actual} ≠ ${expected} ± ${tol}`);

test("C = 1 / (4π² × f0² × L) : 253,3 pF pour 1 MHz, 312,7 pF pour 0,9 MHz, 209,3 pF pour 1,1 MHz", () => {
  near(cTune(1e6), 253.3e-12, 0.05e-12);
  near(cTune(0.9e6), 312.7e-12, 0.05e-12);
  near(cTune(1.1e6), 209.3e-12, 0.05e-12);
});

test("l'autre exemple de la section : 100 kHz avec L = 1 mH donne 2,53 nF", () => {
  near(cTune(100e3, 1e-3), 2.533e-9, 0.001e-9);
});

test("le condensateur va de 180 à 360 pF : f0 va de 1,186 MHz à 0,8388 MHz (838 823 Hz) ; diminuer C fait monter f0", () => {
  near(f0(CMIN), 1.18628e6, 10);
  near(f0(CMAX), 0.83882e6, 10);
  assert.ok(f0(CMIN) > f0(CMAX));
  near(f0(cTune(1e6)), 1e6, 1e-6);
  assert.deepEqual(STATIONS, [0.9e6, 1e6, 1.1e6]);
  assert.equal(L, 100e-6);
});

test("accordé sur 1 MHz : 1 pour la station, 0,118 pour 0,9 MHz et 0,130 pour 1,1 MHz", () => {
  near(response(1e6, 1e6), 1, 1e-12);
  near(response(0.9e6, 1e6), 0.1176, 0.0001);
  near(response(1.1e6, 1e6), 0.1298, 0.0001);
});

test("accordé sur 0,9 MHz : 0,118 pour 1 MHz et 0,0618 pour 1,1 MHz", () => {
  near(response(0.9e6, 0.9e6), 1, 1e-12);
  near(response(1e6, 0.9e6), 0.1176, 0.0001);
  near(response(1.1e6, 0.9e6), 0.06176, 0.00005);
});

test("les lames sont rentrées de 73,3° pour 253,3 pF, de 0° à 180 pF, de 180° à 360 pF", () => {
  near(overlapDeg(cTune(1e6)), 73.3, 0.05);
  near(overlapDeg(CMIN), 0, 1e-9);
  near(overlapDeg(CMAX), 180, 1e-9);
});

test("le balayage va de 180 à 360 pF en 8 s, puis revient", () => {
  near(sweepC(0), 180e-12, 1e-21);
  near(sweepC(8), 360e-12, 1e-21);
  near(sweepC(12), 270e-12, 1e-21);
});
