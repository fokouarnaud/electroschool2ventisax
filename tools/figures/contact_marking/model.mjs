// Modèle des repères des contacts (moteurs, M2, section 02-reperage) : seule source des repères et des états de la figure.
export const STROKE = 5; // course de l'équipage mobile (unités du dessin)
export const TOUCH = 2; // décalage maximal du pont sur ses plots pour que le contact soit fermé
export const TRAVEL_S = 0.6; // s affichées pour la course entière (cadence ralentie, F5)

// Contact auxiliaire : numéro d'ordre, puis 3-4 à fermeture ou 1-2 à ouverture.
export const marking = (order, kind) => (kind === "make" ? [`${order}3`, `${order}4`] : [`${order}1`, `${order}2`]);
export function decode(a, b) {
  const order = Math.floor(+a / 10);
  if (order < 1 || Math.floor(+b / 10) !== order) return null;
  const pair = `${+a % 10}${+b % 10}`;
  return pair === "34" ? { order, kind: "make" } : pair === "12" ? { order, kind: "break" } : null;
}
// Pôle de puissance n : entrée impaire, sortie paire.
export const pole = (n) => [2 * n - 1, 2 * n];
// Décalage du pont par rapport à ses plots quand l'équipage a parcouru la fraction t de sa course (0 au repos, 1 bobine alimentée).
export const offset = (kind, t) => (kind === "make" ? (t - 1) * STROKE : t * STROKE);
export const closed = (kind, t) => Math.abs(offset(kind, t)) <= TOUCH + 1e-9;
