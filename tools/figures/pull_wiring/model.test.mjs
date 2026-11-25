// Quatre câblages d'un bouton sur une entrée (esp32, M3, section 02-tirage), valeurs vérifiées à la main.
// Lancer : node --test "tools/figures/**/*.test.mjs"
import { test } from "node:test";
import assert from "node:assert/strict";

import { WIRINGS, reading, parts } from "./model.mjs";

const near = (a, b, tol) => assert.ok(Math.abs(a - b) <= tol, `${a} ≠ ${b}`);

test("les quatre câblages de la section, dans son ordre", () => {
  assert.deepEqual(WIRINGS, ["ext-down", "ext-up", "int-up", "int-down"]);
});

test("pull-down externe : relâché 0 V, LOW, aucun courant ; appuyé 3,3 V, HIGH, 3,3 V / 10 kΩ = 0,33 mA", () => {
  assert.deepEqual(reading("ext-down", false), { volts: 0, level: "LOW", amps: 0 });
  const r = reading("ext-down", true);
  assert.equal(r.volts, 3.3); assert.equal(r.level, "HIGH"); near(r.amps, 0.00033, 1e-9);
});

test("pull-up externe : relâché 3,3 V, HIGH ; appuyé 0 V, LOW, 0,33 mA", () => {
  assert.deepEqual(reading("ext-up", false), { volts: 3.3, level: "HIGH", amps: 0 });
  const r = reading("ext-up", true);
  assert.equal(r.volts, 0); assert.equal(r.level, "LOW"); near(r.amps, 0.00033, 1e-9);
});

test("pull-up interne : relâché HIGH ; appuyé LOW, 3,3 V / 45 kΩ = 0,0733 mA", () => {
  assert.deepEqual(reading("int-up", false), { volts: 3.3, level: "HIGH", amps: 0 });
  const r = reading("int-up", true);
  assert.equal(r.level, "LOW"); near(r.amps, 0.0000733, 1e-7);
});

test("pull-down interne : relâché LOW ; appuyé HIGH, 0,0733 mA", () => {
  assert.deepEqual(reading("int-down", false), { volts: 0, level: "LOW", amps: 0 });
  const r = reading("int-down", true);
  assert.equal(r.volts, 3.3); assert.equal(r.level, "HIGH"); near(r.amps, 0.0000733, 1e-7);
});

test("pièces présentes : interrupteurs internes, résistance externe et côté du bouton", () => {
  assert.deepEqual(parts("ext-down"), { pullUp: false, pullDown: false, resistor: "gnd", button: "3v3" });
  assert.deepEqual(parts("ext-up"), { pullUp: false, pullDown: false, resistor: "3v3", button: "gnd" });
  assert.deepEqual(parts("int-up"), { pullUp: true, pullDown: false, resistor: null, button: "gnd" });
  assert.deepEqual(parts("int-down"), { pullUp: false, pullDown: true, resistor: null, button: "3v3" });
});

test("le tirage impose le niveau relâché, le bouton l'inverse : jamais deux fois le même niveau", () => {
  for (const w of WIRINGS) assert.notEqual(reading(w, false).level, reading(w, true).level);
});
