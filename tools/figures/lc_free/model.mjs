// Modèle de l'oscillation libre d'un LC avec pertes (M7, section 06-oscillateurs) : seule source des nombres de la figure.
export const L = 0.01; // H
export const C = 100e-9; // F
export const V0 = 1; // V, charge initiale du condensateur
export const W0 = 1 / Math.sqrt(L * C); // rad/s
export const F0 = W0 / (2 * Math.PI); // ≈ 5 033 Hz
export const SLOW = 2; // s affichées par période réelle (cadence ralentie, F5)

export const q = (r) => Math.sqrt(L / C) / r;
export const alpha = (r) => r / (2 * L);
export const omegaD = (r) => Math.sqrt(W0 ** 2 - alpha(r) ** 2);
export const period = (r) => 2 * Math.PI / omegaD(r);
// Régime libre, condensateur chargé à V0 et courant nul à t = 0.
export const vc = (t, r) => V0 * Math.exp(-alpha(r) * t) * (Math.cos(omegaD(r) * t) + alpha(r) / omegaD(r) * Math.sin(omegaD(r) * t));
export const current = (t, r) => -C * V0 * W0 ** 2 / omegaD(r) * Math.exp(-alpha(r) * t) * Math.sin(omegaD(r) * t);
export const energyC = (t, r) => 0.5 * C * vc(t, r) ** 2;
export const energyL = (t, r) => 0.5 * L * current(t, r) ** 2;
