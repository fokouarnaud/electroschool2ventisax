// Sortie LED en source et en puits (esp32, M2, section 03-source-puits), valeurs vérifiées à la main.
// Lancer : node --test "tools/figures/**/*.test.mjs"
import { test } from "node:test";
import assert from "node:assert/strict";

import { WIRINGS, output } from "./model.mjs";

const near = (a, b, tol) => assert.ok(Math.abs(a - b) <= tol, `${a} ≠ ${b}`);

test("deux câblages, dans l'ordre de la section", () => {
  assert.deepEqual(WIRINGS, ["source", "sink"]);
});

test("source, HIGH : interrupteur vers 3,3 V fermé, LED allumée, (3,3 − 2,0) / 330 = 3,94 mA qui sortent de la broche", () => {
  const o = output("source", true);
  assert.equal(o.volts, 3.3); assert.equal(o.closed, "P"); assert.equal(o.lit, true); assert.equal(o.flow, "out");
  near(o.amps, 0.0039394, 1e-6); near(o.vr, 1.3, 1e-9); assert.equal(o.vled, 2.0);
});

test("source, LOW : interrupteur vers GND fermé, 0 V des deux côtés de la LED, éteinte", () => {
  assert.deepEqual(output("source", false), { volts: 0, closed: "N", lit: false, amps: 0, flow: null, vr: 0, vled: 0 });
});

test("puits, HIGH : 3,3 V des deux côtés de la LED, aucun courant, éteinte", () => {
  assert.deepEqual(output("sink", true), { volts: 3.3, closed: "P", lit: false, amps: 0, flow: null, vr: 0, vled: 0 });
});

test("puits, LOW : interrupteur vers GND fermé, LED allumée, 3,94 mA qui entrent dans la broche", () => {
  const o = output("sink", false);
  assert.equal(o.volts, 0); assert.equal(o.closed, "N"); assert.equal(o.lit, true); assert.equal(o.flow, "in");
  near(o.amps, 0.0039394, 1e-6);
});

test("loi des mailles quand la LED est allumée : VR + VLED = 3,3 V", () => {
  for (const [w, high] of [["source", true], ["sink", false]]) {
    const o = output(w, high);
    near(o.vr + o.vled, 3.3, 1e-12);
  }
});
