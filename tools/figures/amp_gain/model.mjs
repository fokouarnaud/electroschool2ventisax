// Modèle du rôle de l'amplificateur (M8, section 01-role-gain) : seule source des nombres de la figure.
export const VE = 0.05; // V crête à l'entrée, l'exemple de la section
export const GAIN_MIN = -40;
export const GAIN_MAX = 40;
export const PERIOD_S = 2; // s affichées par période du signal (cadence ralentie, F5)

// Signal d'entrée et de sortie à la phase ph (rad) : la sortie est la copie de l'entrée multipliée par Av.
export const ve = (ph) => VE * Math.sin(ph);
export const vs = (ph, a) => a * ve(ph);
export const peakOut = (a) => Math.abs(a) * VE;
export const gainOf = (out, inp) => out / inp;
export const inverted = (a) => a < 0;
