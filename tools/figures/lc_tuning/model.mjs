// Modèle du circuit d'accord (M7, section 05-accord) : seule source des nombres de la figure.
export const L = 100e-6; // H
export const Q = 40; // facteur de qualité de la courbe « stations » de la section
export const CMIN = 180e-12; // F, lames sorties
export const CMAX = 360e-12; // F, lames rentrées
export const STATIONS = [0.9e6, 1e6, 1.1e6]; // Hz
export const SWEEP_S = 8; // durée d'un aller du balayage

export const f0 = (c, l = L) => 1 / (2 * Math.PI * Math.sqrt(l * c));
export const cTune = (f, l = L) => 1 / (4 * Math.PI ** 2 * f ** 2 * l);
// Part d'une station de fréquence f qui traverse le circuit accordé sur fr (1 à la résonance).
export const response = (f, fr) => 1 / Math.sqrt(1 + (Q * (f / fr - fr / f)) ** 2);
// Recouvrement des lames : la capacité croît avec la surface en regard, de 0° (180 pF) à 180° (360 pF).
export const overlapDeg = (c) => 180 * (c - CMIN) / (CMAX - CMIN);
// Balayage en triangle : aller de CMIN à CMAX en SWEEP_S secondes, puis retour.
export const sweepC = (t) => { const u = ((t / SWEEP_S) % 2 + 2) % 2; return CMIN + (CMAX - CMIN) * (u <= 1 ? u : 2 - u); };
