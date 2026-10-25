// Modèle de la résonance RLC série (M7, section 01-lc-serie) : seule source des nombres de la figure.
export const R = 50; // Ω
export const L = 0.01; // H
export const C = 100e-9; // F
export const U = 1; // V crête
export const F0 = 1 / (2 * Math.PI * Math.sqrt(L * C)); // ≈ 5 033 Hz
export const F_MIN = 10;
export const F_MAX = 100000;

export const xl = (f) => 2 * Math.PI * f * L;
export const xc = (f) => 1 / (2 * Math.PI * f * C);
export const z = (f) => Math.sqrt(R ** 2 + (xl(f) - xc(f)) ** 2);
export const current = (f) => U / z(f);
// Avance du courant sur Ve : positive sous f0 (XC domine), nulle à f0, négative au-dessus (XL domine).
export const leadDeg = (f) => Math.atan((xc(f) - xl(f)) / R) * 180 / Math.PI;
export const vc = (f) => current(f) * xc(f);
export const vl = (f) => current(f) * xl(f);
// Cadence ralentie (F5) : 2 s à 10 Hz, divisée par 8 sur les quatre décades jusqu'à 100 kHz.
export const periodS = (f) => 2 * 0.125 ** (Math.log10(f / F_MIN) / 4);
