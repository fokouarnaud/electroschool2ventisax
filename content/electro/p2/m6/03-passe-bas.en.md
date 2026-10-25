A **filter** lets some frequencies through and attenuates others. The simplest is the **RC low-pass**: a resistor in series, then a capacitor to ground. The output Vout is taken **across the capacitor**.

![Low-pass filter: input Vin, 1 kΩ series resistor, 100 nF capacitor to ground, output Vout across the capacitor](/static/content/electro/en/m6/passe-bas.svg)

## A frequency-dependent voltage divider

The circuit looks like Part 1's voltage divider, with Xc in place of the second resistor. The output ratio is:

**Vout / Vin = Xc / Z = Xc / √(R² + Xc²)**

- **At low frequencies**, Xc is much larger than R: almost all the voltage ends up across the capacitor, **Vout ≈ Vin**.
- **At high frequencies**, Xc becomes small: the capacitor shorts the output, **Vout tends to 0**.

## What happens in the circuit

With alternating current, electrons do not travel around the circuit: they move back and forth on the spot, and the frequency counts how many times per second they change direction. No electron crosses the capacitor's insulator: it charges one way, then the other.

- **At low frequency**, each half-cycle lasts a long time: the capacitor has time to charge almost up to the input voltage. Xc is large, the current stays small and the resistor drops almost no voltage. The voltage across the capacitor follows the input: **Vout ≈ Vin**.
- **At high frequency**, the current reverses before the capacitor has had time to charge: its voltage stays close to zero. Xc is small, the current is large and almost all the input voltage is dropped across the resistor: **Vout tends to 0**.

Water helps to see it. The piston pushes water one way then the other (Vin), the throttled valve, placed in series, restricts the flow (R) and the bellows, standing in the tray and branched off after the valve, swells under pressure (C to ground). The pressure gauge reads the pressure in the bellows, just as Vout is read across the capacitor. Slowly, the bellows has time to fill and empty completely: the needle follows the piston. Quickly, the water only sloshes back and forth through the valve and the bellows barely moves: the needle stays near zero and lags behind the piston. At the cutoff frequency fc = 1 / (2π·R·C) ≈ 1.6 kHz, Xc = R: the needle only reaches 0.707 of its travel, with a 45° lag.

[[fig:rc_lowpass]]

## Reading the response curve

![Response of a 1 kΩ, 100 nF RC low-pass: Vout / Vin is 1 at low frequencies, 0.707 near 1.6 kHz, then falls](/static/content/electro/en/m6/passe-bas-courbe.svg)

The horizontal axis is **logarithmic**: each mark multiplies the frequency by 10 (10 Hz, 100 Hz, 1 kHz…). This shows a wide range of frequencies at a glance. The range where Vout ≈ Vin is the filter's **passband**.

## Common uses

- Removing high-pitched noise (hiss) from an audio signal.
- Smoothing a rippling voltage.
- Keeping only the slow changes of a sensor.

## Key points

- RC low-pass: output across C.
- Low frequencies: Vout ≈ Vin; high frequencies: Vout → 0.
- Vout / Vin = Xc / √(R² + Xc²).
