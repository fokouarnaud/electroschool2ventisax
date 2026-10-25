// Modèle du déphasage (M6, section 06-dephasage) : seule source des nombres de la figure.
export const R = 1000; // Ω
export const C = 100e-9; // F
export const FC = 1 / (2 * Math.PI * R * C); // ≈ 1 591,5 Hz
export const F_MIN = 10;
export const F_MAX = 100000;

export const xc = (f) => 1 / (2 * Math.PI * f * C);
export const ratio = (f) => 1 / Math.sqrt(1 + (f / FC) ** 2);
// Avance du courant sur Ve : φ = arctan(Xc / R), la formule de la section.
export const leadDeg = (f) => Math.atan(xc(f) / R) * 180 / Math.PI;
// Retard de Vs (aux bornes de C) sur Ve : Vc retarde de 90° sur le courant, d'où 90° − φ = arctan(f / fc).
export const lagDeg = (f) => 90 - leadDeg(f);
// Δt / T = retard / 360°, la mesure de l'oscilloscope.
export const shift = (f) => lagDeg(f) / 360;
// Cadence ralentie (F5) : 2 s à 10 Hz, divisée par 8 sur les quatre décades jusqu'à 100 kHz.
export const periodS = (f) => 2 * 0.125 ** (Math.log10(f / F_MIN) / 4);
