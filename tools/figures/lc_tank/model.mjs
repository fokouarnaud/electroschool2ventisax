// Modèle du circuit bouchon (M7, section 04-lc-parallele) : seule source des nombres de la figure.
// Les phaseurs ne servent qu'au calcul ; la figure et le texte n'affichent que des amplitudes et des sens.
export const U = 1; // V crête
export const RS = 10000; // Ω, résistance en série
export const RL = 10; // Ω, pertes de la bobine (courbe de la section)
export const L = 0.01; // H
export const C = 100e-9; // F
export const F0 = 1 / (2 * Math.PI * Math.sqrt(L * C)); // ≈ 5 033 Hz
export const F_MIN = 10;
export const F_MAX = 100000;

const cx = (re, im) => ({ re, im });
const add = (a, b) => cx(a.re + b.re, a.im + b.im);
const mul = (a, b) => cx(a.re * b.re - a.im * b.im, a.re * b.im + a.im * b.re);
const div = (a, b) => { const d = b.re ** 2 + b.im ** 2; return cx((a.re * b.re + a.im * b.im) / d, (a.im * b.re - a.re * b.im) / d); };
const polar = (a) => ({ amp: Math.hypot(a.re, a.im), deg: Math.atan2(a.im, a.re) * 180 / Math.PI });
const zl = (f) => cx(RL, 2 * Math.PI * f * L);
const zc = (f) => cx(0, -1 / (2 * Math.PI * f * C));
const zt = (f) => div(mul(zl(f), zc(f)), add(zl(f), zc(f)));
const i0 = (f) => div(cx(U, 0), add(cx(RS, 0), zt(f)));
const v0 = (f) => mul(i0(f), zt(f));

export const zTank = (f) => polar(zt(f)).amp;
// Amplitude et phase (en degrés, par rapport à Ve) du courant de ligne, de la tension du bouchon et des courants de branche.
export const line = (f) => polar(i0(f));
export const tankV = (f) => polar(v0(f));
export const coil = (f) => polar(div(v0(f), zl(f)));
export const cap = (f) => polar(div(v0(f), zc(f)));
// Cadence ralentie (F5) : 2 s à 10 Hz, divisée par 8 sur les quatre décades jusqu'à 100 kHz.
export const periodS = (f) => 2 * 0.125 ** (Math.log10(f / F_MIN) / 4);
