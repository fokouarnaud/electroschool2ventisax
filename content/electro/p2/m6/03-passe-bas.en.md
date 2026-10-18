A **filter** lets some frequencies through and attenuates others. The simplest is the **RC low-pass**: a resistor in series, then a capacitor to ground. The output Vout is taken **across the capacitor**.

![Low-pass filter: input Vin, 1 kΩ series resistor, 100 nF capacitor to ground, output Vout across the capacitor](/static/content/electro/en/m6/passe-bas.svg)

## A frequency-dependent voltage divider

The circuit looks like Part 1's voltage divider, with Xc in place of the second resistor. The output ratio is:

**Vout / Vin = Xc / Z = Xc / √(R² + Xc²)**

- **At low frequencies**, Xc is much larger than R: almost all the voltage ends up across the capacitor, **Vout ≈ Vin**.
- **At high frequencies**, Xc becomes small: the capacitor shorts the output, **Vout tends to 0**.

![Response of a 1 kΩ, 100 nF RC low-pass: Vout / Vin is 1 at low frequencies, 0.707 near 1.6 kHz, then falls](/static/content/electro/en/m6/passe-bas-courbe.svg)

## Reading the response curve

The horizontal axis is **logarithmic**: each mark multiplies the frequency by 10 (10 Hz, 100 Hz, 1 kHz…). This shows a wide range of frequencies at a glance. The range where Vout ≈ Vin is the filter's **passband**.

## Common uses

- Removing high-pitched noise (hiss) from an audio signal.
- Smoothing a rippling voltage.
- Keeping only the slow changes of a sensor.

## Key points

- RC low-pass: output across C.
- Low frequencies: Vout ≈ Vin; high frequencies: Vout → 0.
- Vout / Vin = Xc / √(R² + Xc²).
