// Du programme à la broche de la carte (esp32, M1, section 02-architecture) : seule source des valeurs de la figure.
// digitalWrite(25, niveau) : le CPU écrit le masque 1 << 25 dans GPIO_OUT_W1TS (HIGH) ou GPIO_OUT_W1TC (LOW) ; le bit 25 de
// GPIO_OUT change ; la matrice GPIO et l'IO MUX relient ce bit au plot 25 ; le plot ferme P (3,3 V) ou N (GND) ; G25 suit.
export const PIN = 25;
export const STAGES = ["cpu", "bus", "reg", "mux", "pad", "board"];
const hex = (n) => "0x" + n.toString(16).toUpperCase().padStart(8, "0");
export function write(high) {
  const mask = 2 ** PIN;
  const address = high ? 0x3ff44008 : 0x3ff4400c;
  return {
    mask, maskHex: hex(mask), register: high ? "GPIO_OUT_W1TS_REG" : "GPIO_OUT_W1TC_REG", address, addressHex: hex(address),
    bit: high ? 1 : 0, closed: high ? "P" : "N", volts: high ? 3.3 : 0, led: high,
  };
}
// Étape courante n (1 à 6) : les étapes avant elle sont franchies par le signal.
export const reached = (step, stage) => STAGES.indexOf(stage) < step - 1;
export const STEP_S = 1.6; // s par étape en lecture automatique (illustratif)
