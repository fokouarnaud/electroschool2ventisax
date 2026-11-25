// Modèle des quatre câblages d'un bouton (esp32, M3, section 02-tirage) : seule source des états de la figure.
// Alimentation 3,3 V ; résistance externe 10 kΩ ; tirages internes d'environ 45 kΩ.
export const VCC = 3.3;
export const R_EXT = 10000;
export const R_INT = 45000;
export const WIRINGS = ["ext-down", "ext-up", "int-up", "int-down"];
// Où le tirage tire la broche : "3v3" (pull-up) ou "gnd" (pull-down) ; externe ou interne.
const PULL = { "ext-down": ["gnd", false], "ext-up": ["3v3", false], "int-up": ["3v3", true], "int-down": ["gnd", true] };
// Pièces : interrupteurs internes fermés, résistance externe (côté) et côté du bouton (toujours opposé au tirage).
export function parts(w) {
  const [side, inside] = PULL[w];
  return { pullUp: inside && side === "3v3", pullDown: inside && side === "gnd", resistor: inside ? null : side, button: side === "3v3" ? "gnd" : "3v3" };
}
// Relâché, le tirage impose son niveau sans courant ; appuyé, le bouton impose l'autre et le courant traverse le tirage.
export function reading(w, pressed) {
  const [side, inside] = PULL[w];
  const high = (side === "3v3") !== pressed;
  return { volts: high ? VCC : 0, level: high ? "HIGH" : "LOW", amps: pressed ? VCC / (inside ? R_INT : R_EXT) : 0 };
}
export const PRESS_S = 0.25; // s de course du bouton (illustratif)
