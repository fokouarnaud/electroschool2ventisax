// Schéma de puissance et schéma de commande d'un démarrage direct (M2 de moteurs, section 03-puissance-commande), états écrits à la main.
// Lancer : node --test "tools/figures/**/*.test.mjs"
import { test } from "node:test";
import assert from "node:assert/strict";

import { REST, step, run, coil, states, POWER, CONTROL, SHARED } from "./model.mjs";

test("au repos, S2 ouvert : bobine non alimentée, moteur arrêté", () => {
  assert.equal(coil(REST), false);
  assert.deepEqual(states(REST), { coil: false, poles: false, c1314: false, f9596: true, motor: false });
});

test("on appuie sur S2 : la bobine est alimentée, les pôles et le contact 13-14 se ferment, le moteur démarre", () => {
  const s = step(REST, "s2-down");
  assert.deepEqual(states(s), { coil: true, poles: true, c1314: true, f9596: true, motor: true });
});

test("on relâche S2 : le contact 13-14 garde la bobine alimentée (auto-maintien)", () => {
  const s = run(REST, ["s2-down", "s2-up"]);
  assert.equal(s.s2, false);
  assert.equal(states(s).coil, true);
  assert.equal(states(s).motor, true);
});

test("on appuie sur S1 : KM1 retombe, 13-14 s'ouvre ; S1 relâché, le moteur ne redémarre pas seul", () => {
  const pressed = run(REST, ["s2-down", "s2-up", "s1-down"]);
  assert.deepEqual(states(pressed), { coil: false, poles: false, c1314: false, f9596: true, motor: false });
  assert.equal(states(step(pressed, "s1-up")).motor, false);
});

test("surcharge : 95-96 s'ouvre et produit le même effet ; réarmé, le moteur reste arrêté", () => {
  const tripped = run(REST, ["s2-down", "s2-up", "trip"]);
  assert.deepEqual(states(tripped), { coil: false, poles: false, c1314: false, f9596: false, motor: false });
  assert.equal(states(step(tripped, "reset")).motor, false);
});

test("tous les contacts en série doivent être fermés : S2 ne démarre rien si F1 a déclenché ou si S1 est enfoncé", () => {
  assert.equal(states(run(REST, ["trip", "s2-down"])).coil, false);
  assert.equal(states(run(REST, ["s1-down", "s2-down"])).coil, false);
  assert.equal(states(run(REST, ["trip", "reset", "s2-down"])).coil, true);
});

test("deux schémas, deux appareils communs : KM1 (pôles en puissance, bobine et 13-14 en commande) et F1 (relais en puissance, 95-96 en commande)", () => {
  assert.deepEqual(POWER, ["Q1", "KM1", "F1", "M1"]);
  assert.deepEqual(CONTROL, ["F2", "F1", "S1", "S2", "KM1"]);
  assert.deepEqual(SHARED, ["KM1", "F1"]);
});
