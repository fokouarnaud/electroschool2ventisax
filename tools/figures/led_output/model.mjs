// Modèle d'une sortie qui commande une LED (esp32, M2, section 03-source-puits) : seule source des états de la figure.
// Broche à 3,3 V ou 0 V par l'un de ses deux interrupteurs (P vers 3,3 V, N vers GND) ; LED rouge Vf = 2,0 V et 330 Ω en série.
export const VCC = 3.3;
export const VF = 2.0;
export const R = 330;
export const WIRINGS = ["source", "sink"];
// Source : broche, R, LED, GND ; allumée au niveau haut. Puits : 3,3 V, LED, R, broche ; allumée au niveau bas.
export function output(w, high) {
  const lit = w === "source" ? high : !high;
  const amps = lit ? (VCC - VF) / R : 0;
  return { volts: high ? VCC : 0, closed: high ? "P" : "N", lit, amps, flow: lit ? (w === "source" ? "out" : "in") : null, vr: lit ? VCC - VF : 0, vled: lit ? VF : 0 };
}
export const MOVE_S = 0.25; // s de course du drapeau GPIO_OUT (illustratif)
