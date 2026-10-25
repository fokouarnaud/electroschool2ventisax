// Modèle de la courbe de réponse du RLC série (M7, section 02-courbe-reponse) : seule source des nombres de la figure.
export const L = 0.01; // H
export const C = 100e-9; // F
export const U = 1; // V
export const R1 = 50; // Ω, pic haut et étroit
export const R2 = 200; // Ω, pic bas et large
export const F0 = 1 / (2 * Math.PI * Math.sqrt(L * C)); // ≈ 5 033 Hz, sans R
export const F_LO = 500;
export const F_HI = 10500;
export const SWEEP_S = 8; // durée d'un aller du balayage

export const xl = (f) => 2 * Math.PI * f * L;
export const xc = (f) => 1 / (2 * Math.PI * f * C);
export const z = (f, r) => Math.sqrt(r ** 2 + (xl(f) - xc(f)) ** 2);
export const current = (f, r) => U / z(f, r);
// Balayage en triangle : aller de F_LO à F_HI en SWEEP_S secondes, puis retour.
export const sweepF = (t) => { const u = ((t / SWEEP_S) % 2 + 2) % 2; return F_LO + (F_HI - F_LO) * (u <= 1 ? u : 2 - u); };
