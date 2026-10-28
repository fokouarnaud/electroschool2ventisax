// Plaque à bornes d'un moteur triphasé (M2 de moteurs, section 02-reperage), littéraux écrits à la main.
// Lancer : node --test "tools/figures/**/*.test.mjs"
import { test } from "node:test";
import assert from "node:assert/strict";

import { TOP, BOTTOM, place, winding, links, windingVoltage, NETWORK } from "./model.mjs";

test("la plaque : entrées U1 V1 W1 au fond, sorties W2 U2 V2 devant, décalées d'un cran", () => {
  assert.deepEqual(TOP, ["U1", "V1", "W1"]);
  assert.deepEqual(BOTTOM, ["W2", "U2", "V2"]);
  assert.deepEqual(place("U1"), [0, 0]);
  assert.deepEqual(place("U2"), [1, 1]);
  assert.deepEqual(place("V1"), [1, 0]);
  assert.deepEqual(place("V2"), [2, 1]);
  assert.deepEqual(place("W1"), [2, 0]);
  assert.deepEqual(place("W2"), [0, 1]);
});

test("un enroulement relie ses deux bornes : U1-U2, V1-V2, W1-W2", () => {
  assert.deepEqual(winding("U"), ["U1", "U2"]);
  assert.deepEqual(winding("V"), ["V1", "V2"]);
  assert.deepEqual(winding("W"), ["W1", "W2"]);
});

test("étoile : une barrette horizontale relie W2, U2 et V2 ; triangle : trois barrettes verticales", () => {
  assert.deepEqual(links("star"), [["W2", "U2", "V2"]]);
  assert.deepEqual(links("delta"), [["U1", "W2"], ["V1", "U2"], ["W1", "V2"]]);
});

test("grâce au décalage, chaque barrette est droite : une rangée en étoile, une colonne en triangle", () => {
  for (const bar of links("star")) assert.ok(bar.every((m) => place(m)[1] === place(bar[0])[1]));
  for (const bar of links("delta")) assert.ok(bar.every((m) => place(m)[0] === place(bar[0])[0]));
});

test("en triangle, chaque barrette relie le début d'un enroulement à la fin d'un autre, jamais les deux bouts d'un même enroulement", () => {
  for (const [a, b] of links("delta")) {
    assert.equal(a[1], "1");
    assert.equal(b[1], "2");
    assert.notEqual(a[0], b[0]);
  }
  // Sorties non décalées (U2 V2 W2) : la barrette verticale U1-U2 court-circuiterait l'enroulement U.
  const aligned = ["U2", "V2", "W2"];
  assert.ok(TOP.every((m, c) => aligned[c][0] === m[0]));
});

test("tension par enroulement d'un moteur 230/400 V : étoile sur 400 V, U / √3 ≈ 230,9 V ; triangle sur 230 V, 230 V", () => {
  assert.equal(NETWORK.star, 400);
  assert.equal(NETWORK.delta, 230);
  assert.ok(Math.abs(windingVoltage("star", 400) - 230.94) < 0.01);
  assert.equal(windingVoltage("delta", 230), 230);
  assert.ok(Math.abs(windingVoltage("star", 230) - 132.79) < 0.01);
  assert.equal(windingVoltage("delta", 400), 400);
});
