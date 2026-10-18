An AC voltage changes all the time, so you must say **which** value you mean. Three values are used every day.

![Sine wave with a 10 V amplitude: Umax = 10 V, Upp = 20 V and Urms ≈ 7.07 V](/static/content/electro/en/m5/valeurs.svg)

## The three values

- **Peak value** Umax: the top of the sine wave, measured from zero.
- **Peak-to-peak value** Upp: the gap between the top and the bottom, **Upp = 2 × Umax**.
- **RMS value** Urms (root mean square, also called effective value): the DC voltage that would heat a resistor just as much.

For a sine wave:

**Urms = Umax / √2 ≈ 0.707 × Umax**   and   **Umax = Urms × √2 ≈ 1.414 × Urms**

The **average** value of a sine wave is zero: the positive half cancels the negative half. That is why it is not used to describe AC.

## Why the RMS value?

A lamp only "sees" the energy it receives. Under 12 V DC or 12 V **RMS** AC, it shines just as brightly.

![Two identical circuits: a lamp under 12 V DC and a lamp under 12 V RMS shine the same](/static/content/electro/en/m5/efficace.svg)

When mains power is given as "230 V", that is the RMS value. The peak reaches 230 × 1.414 ≈ **325 V**, and the peak-to-peak swing exceeds 650 V: components must withstand that peak.

A multimeter set to **V~** (AC) shows the RMS value of a sine-wave voltage, as long as the frequency stays within its measuring range (often a few hundred hertz for a basic model).

## Key points

- Upp = 2 × Umax; Urms ≈ 0.707 × Umax.
- Stated AC voltages and currents are RMS values.
- 230 V RMS means 325 V peaks.
