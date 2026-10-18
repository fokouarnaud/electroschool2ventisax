Swap the resistor and the capacitor: the capacitor goes in series, the resistor goes to ground, and the output is taken **across the resistor**. This gives an **RC high-pass**.

![High-pass filter: input Vin, 100 nF series capacitor, 1 kΩ resistor to ground, output Vout across the resistor](/static/content/electro/en/m6/passe-haut.svg)

## The opposite of the low-pass

The output ratio becomes:

**Vout / Vin = R / Z = R / √(R² + Xc²)**

- **At low frequencies**, Xc is very large: the capacitor blocks nearly everything, **Vout tends to 0**. In DC, Vout = 0: the high-pass removes the DC component.
- **At high frequencies**, Xc becomes small: the capacitor behaves almost like a wire, **Vout ≈ Vin**.

![Response of a 1 kΩ, 100 nF RC high-pass: Vout / Vin starts at 0, is 0.707 near 1.6 kHz and reaches 1 at high frequencies](/static/content/electro/en/m6/passe-haut-courbe.svg)

## Common uses

- **Coupling capacitor**: passing an audio signal from one stage to the next while blocking the DC bias voltage.
- Removing a low hum (50 Hz) from a higher-pitched signal.
- Keeping only the fast changes of a signal.

## How to remember

Ask where the capacitor sits relative to the output:

- capacitor **to ground**, across the output: it shorts the high frequencies, it is a **low-pass**;
- capacitor **in series**, in the signal's path: it blocks the low frequencies, it is a **high-pass**.

## Key points

- RC high-pass: C in series, output across R.
- Low frequencies (and DC): Vout → 0; high frequencies: Vout ≈ Vin.
- Vout / Vin = R / √(R² + Xc²).
