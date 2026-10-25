// Modèle du passe-bas RL (M6, section 07-filtres-rl) : seule source des nombres de la figure.
export const R = 100; // Ω
export const L = 0.01; // H
export const FC = R / (2 * Math.PI * L); // ≈ 1 591,5 Hz
export const F_MIN = 10;
export const F_MAX = 100000;

export const xl = (f) => 2 * Math.PI * f * L;
// Vs/Ve aux bornes de R (sortie du passe-bas RL) = I·R/Ve.
export const ratio = (f) => R / Math.sqrt(R ** 2 + xl(f) ** 2);
// Retard du courant (et de Vs, en phase avec lui) sur Ve : φ = arctan(XL / R).
export const lagDeg = (f) => Math.atan(xl(f) / R) * 180 / Math.PI;
// Tension aux bornes de la bobine : VL/Ve = XL/Z, en avance de 90° sur le courant, soit 90° − φ sur Ve.
export const coilRatio = (f) => xl(f) / Math.sqrt(R ** 2 + xl(f) ** 2);
export const coilPhaseDeg = (f) => 90 - lagDeg(f);
// Cadence ralentie (F5) : 2 s à 10 Hz, divisée par 8 sur les quatre décades jusqu'à 100 kHz.
export const periodS = (f) => 2 * 0.125 ** (Math.log10(f / F_MIN) / 4);
