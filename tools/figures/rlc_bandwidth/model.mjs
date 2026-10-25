// Modèle de la bande passante du RLC série (M7, section 03-bande-passante) : seule source des nombres de la figure.
export const L = 0.01; // H
export const C = 100e-9; // F
export const R1 = 50; // Ω, Q ≈ 6,3
export const R2 = 200; // Ω, Q ≈ 1,6
export const F0 = 1 / (2 * Math.PI * Math.sqrt(L * C)); // ≈ 5 033 Hz
export const F_LO = 2000;
export const F_HI = 8000;
export const SWEEP_S = 8; // durée d'un aller du balayage

export const xl = (f) => 2 * Math.PI * f * L;
export const xc = (f) => 1 / (2 * Math.PI * f * C);
// I / Imax = R / Z, avec Imax = U / R à f0.
export const ratio = (f, r) => r / Math.sqrt(r ** 2 + (xl(f) - xc(f)) ** 2);
export const q = (r) => xl(F0) / r;
// Fréquences où XL − XC = ∓R, donc I / Imax = 0,707 : ω = √((R/2L)² + ω0²) ∓ R/2L.
export const f1 = (r) => (Math.sqrt((r / (2 * L)) ** 2 + 1 / (L * C)) - r / (2 * L)) / (2 * Math.PI);
export const f2 = (r) => (Math.sqrt((r / (2 * L)) ** 2 + 1 / (L * C)) + r / (2 * L)) / (2 * Math.PI);
export const band = (r) => f2(r) - f1(r);
// Balayage en triangle : aller de F_LO à F_HI en SWEEP_S secondes, puis retour.
export const sweepF = (t) => { const u = ((t / SWEEP_S) % 2 + 2) % 2; return F_LO + (F_HI - F_LO) * (u <= 1 ? u : 2 - u); };
