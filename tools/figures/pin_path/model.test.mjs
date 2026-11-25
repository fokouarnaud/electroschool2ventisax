// Du programme à la broche de la carte (esp32, M1, section 02-architecture), valeurs vérifiées à la main.
// Lancer : node --test "tools/figures/**/*.test.mjs"
import { test } from "node:test";
import assert from "node:assert/strict";

import { STAGES, PIN, write, reached } from "./model.mjs";

test("six étapes, du processeur à la broche de la carte", () => {
  assert.deepEqual(STAGES, ["cpu", "bus", "reg", "mux", "pad", "board"]);
  assert.equal(PIN, 25);
});

test("digitalWrite(25, HIGH) : masque 1 << 25 = 0x02000000 écrit dans GPIO_OUT_W1TS (0x3FF44008)", () => {
  const w = write(true);
  assert.equal(w.mask, 33554432);
  assert.equal(w.maskHex, "0x02000000");
  assert.equal(w.register, "GPIO_OUT_W1TS_REG");
  assert.equal(w.addressHex, "0x3FF44008");
  assert.equal(w.bit, 1);
  assert.equal(w.closed, "P");
  assert.equal(w.volts, 3.3);
  assert.equal(w.led, true);
});

test("digitalWrite(25, LOW) : même masque, écrit dans GPIO_OUT_W1TC (0x3FF4400C) ; bit 0, N fermé, 0 V, LED éteinte", () => {
  const w = write(false);
  assert.equal(w.maskHex, "0x02000000");
  assert.equal(w.register, "GPIO_OUT_W1TC_REG");
  assert.equal(w.addressHex, "0x3FF4400C");
  assert.deepEqual([w.bit, w.closed, w.volts, w.led], [0, "N", 0, false]);
});

test("le signal a franchi une étape quand on l'a dépassée : à l'étape 3 (registre), cpu et bus sont franchis, pas le registre", () => {
  assert.deepEqual(STAGES.map((s) => reached(3, s)), [true, true, false, false, false, false]);
  assert.deepEqual(STAGES.map((s) => reached(1, s)), [false, false, false, false, false, false]);
  assert.deepEqual(STAGES.map((s) => reached(6, s)), [true, true, true, true, true, false]);
});
