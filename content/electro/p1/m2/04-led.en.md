The **LED** (light-emitting diode) is a diode that gives off light when it conducts. It follows the same rules as an ordinary diode, with two important differences:

- its threshold voltage is higher and depends on the colour: about 1.8 V for a red LED, 2.1 V for a green one and 3 V for a blue or white one;
- it handles little current: 10 to 20 mA for a standard indicator LED.

![LED symbol, anode and cathode, with typical thresholds by colour](/static/content/electro/en/m2/led-symbole.svg)

## Always a series resistor

Like any conducting diode, an LED does not limit its own current. Connected on its own to a battery, it burns out in an instant. So we add a **series resistor** that sets the current:

**R = (E − U_LED) / I**

![9 V battery, 330 Ω resistor and 2 V red LED: about 21 mA](/static/content/electro/en/m2/led-circuit.svg)

## Example

A red LED (2 V) is to be fed from a 9 V battery at 20 mA. R = (9 − 2) / 0.02 = **350 Ω**. Choose the nearest standard value, 330 Ω, which gives (9 − 2) / 330 ≈ 21 mA: acceptable. To stay under 20 mA, take the next value up, 390 Ω.

The resistor dissipates (9 − 2) × 0.021 ≈ 0.15 W: a 1/4 W part is fine.

## Identifying the legs

The **longer leg** is the anode (+). On the cathode side (−), the package often has a **flat edge**. If in doubt, an LED fitted the wrong way round is not damaged by a few volts: it simply stays off.

## Key points

- LED threshold: 1.8 to 3 V depending on colour; current 10 to 20 mA.
- R = (E − U_LED) / I, then a standard value.
- Longer leg = anode.
