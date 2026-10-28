// Modèle d'un démarrage direct (moteurs, M2, section 03-puissance-commande) : seule source des états de la figure.
// État : S1 et S2 enfoncés ou non, F1 déclenché ou non, KM1 fermé ou non (Q1 fermé, réseau et 24 V présents).
export const REST = { s1: false, s2: false, f1: false, km: false };
// Commande : le courant n'atteint A1-A2 que si F2, 95-96 de F1 et S1 sont fermés, et S2 enfoncé ou 13-14 de KM1 fermé.
export const coil = (s) => !s.f1 && !s.s1 && (s.s2 || s.km);
const EVENTS = { "s2-down": { s2: true }, "s2-up": { s2: false }, "s1-down": { s1: true }, "s1-up": { s1: false }, trip: { f1: true }, reset: { f1: false } };
export function step(s, event) {
  const next = { ...s, ...EVENTS[event] };
  next.km = coil(next);
  return next;
}
export const run = (s, events) => events.reduce(step, s);
// Puissance : les pôles de KM1 suivent la bobine ; le moteur tourne quand ils sont fermés (Q1 fermé).
export const states = (s) => ({ coil: s.km, poles: s.km, c1314: s.km, f9596: !s.f1, motor: s.km });
export const POWER = ["Q1", "KM1", "F1", "M1"];
export const CONTROL = ["F2", "F1", "S1", "S2", "KM1"];
export const SHARED = POWER.filter((d) => CONTROL.includes(d));
export const PRESS_S = 0.5; // s pendant lesquelles un bouton reste enfoncé (impulsion)
export const TURN_S = 1.2; // s affichées par tour d'arbre (cadence ralentie, F5)
