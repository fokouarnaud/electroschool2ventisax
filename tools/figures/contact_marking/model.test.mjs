// Repères des contacts d'un contacteur (M2 de moteurs, section 02-reperage), littéraux écrits à la main.
// Lancer : node --test "tools/figures/**/*.test.mjs"
import { test } from "node:test";
import assert from "node:assert/strict";

import { marking, decode, pole, offset, closed, STROKE, TOUCH } from "./model.mjs";

test("contacts auxiliaires : numéro d'ordre puis fonction (3-4 à fermeture, 1-2 à ouverture)", () => {
  assert.deepEqual(marking(1, "make"), ["13", "14"]);
  assert.deepEqual(marking(2, "break"), ["21", "22"]);
  assert.deepEqual(marking(3, "break"), ["31", "32"]);
  assert.deepEqual(marking(4, "make"), ["43", "44"]);
});

test("lire un repère : le premier chiffre numérote, le second dit la fonction ; une paire incohérente n'est pas un contact", () => {
  assert.deepEqual(decode("21", "22"), { order: 2, kind: "break" });
  assert.deepEqual(decode("43", "44"), { order: 4, kind: "make" });
  assert.deepEqual(decode("13", "14"), { order: 1, kind: "make" });
  assert.equal(decode("13", "12"), null);
  assert.equal(decode("13", "24"), null);
});

test("pôles de puissance : entrée impaire, sortie paire", () => {
  assert.deepEqual(pole(1), [1, 2]);
  assert.deepEqual(pole(2), [3, 4]);
  assert.deepEqual(pole(3), [5, 6]);
});

test("au repos (bobine non alimentée) le contact à fermeture est ouvert, celui à ouverture fermé ; alimentée, l'inverse", () => {
  assert.equal(closed("make", 0), false);
  assert.equal(closed("break", 0), true);
  assert.equal(closed("make", 1), true);
  assert.equal(closed("break", 1), false);
});

test("le pont coulisse de la course entière ; fermé tant qu'il recouvre les plots (décalage ≤ 2)", () => {
  assert.equal(STROKE, 5);
  assert.equal(TOUCH, 2);
  assert.equal(offset("make", 0), -5);
  assert.equal(offset("make", 1), 0);
  assert.equal(offset("break", 0), 0);
  assert.equal(offset("break", 1), 5);
  assert.equal(closed("make", 0.6), true);
  assert.equal(closed("make", 0.59), false);
  assert.equal(closed("break", 0.4), true);
  assert.equal(closed("break", 0.41), false);
});

test("à mi-course, le contact à ouverture s'est déjà ouvert et celui à fermeture pas encore fermé", () => {
  assert.equal(closed("break", 0.5), false);
  assert.equal(closed("make", 0.5), false);
});
