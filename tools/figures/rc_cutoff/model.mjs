// Modèle de la fréquence de coupure (M6, section 05-coupure) : seule source des nombres de la figure.
export const R = 1000; // Ω
export const C = 100e-9; // F
export const FC = 1 / (2 * Math.PI * R * C); // ≈ 1 591,5 Hz
export const F_MIN = 10;
export const F_MAX = 100000;

export const xc = (f) => 1 / (2 * Math.PI * f * C);
// Vs/Ve aux bornes du condensateur (sortie du passe-bas).
export const ratio = (f) => 1 / Math.sqrt(1 + (f / FC) ** 2);
// VR/Ve aux bornes de la résistance : égale à Vs/Ve quand Xc = R.
export const ratioR = (f) => 1 / Math.sqrt(1 + (FC / f) ** 2);
export const phaseDeg = (f) => -Math.atan(f / FC) * 180 / Math.PI;
// Cadence ralentie (F5) : 2 s à 10 Hz, divisée par 8 sur les quatre décades jusqu'à 100 kHz.
export const periodS = (f) => 2 * 0.125 ** (Math.log10(f / F_MIN) / 4);
// Phase de VR (aux bornes de la vanne) : le courant, et donc VR, avance de +arctan(fc/f) sur Ve.
export const phaseRDeg = (f) => phaseDeg(f) + 90;
