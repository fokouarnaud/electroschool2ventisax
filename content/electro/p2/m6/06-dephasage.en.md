A filter does not only change the signal's amplitude: it also **shifts it in time**. This shift, expressed in degrees, is called the **phase shift** φ (phi). One full period is 360°.

![Input vin and output vout of a low-pass at fc: the output peaks Δt = 0.125 ms after the input, for T = 1 ms](/static/content/electro/en/m6/dephasage.svg)

## Measuring a phase shift on the oscilloscope

Show the input on channel 1 and the output on channel 2, then measure the time gap Δt between two matching points (two peaks, or two rising zero crossings):

**φ = 360° × Δt / T**

Example: Δt = 0.125 ms and T = 1 ms. φ = 360 × 0.125 / 1 = **45°**. With Δt = 0.1 ms and T = 1 ms, φ = 36°.

## Calculating a phase shift

In a series RC circuit, the impedance triangle directly gives the angle between the current and the input voltage:

**tan φ = Xc / R**   so   **φ = arctan(Xc / R)**

![Triangle with R = 1 kΩ and Xc = 577 Ω: tan φ = 0.577 and φ ≈ 30°](/static/content/electro/en/m6/triangle-phi.svg)

Examples:

- R = Xc (that is, at fc): φ = arctan 1 = **45°**;
- R = 1 kΩ and Xc = 577 Ω: φ = arctan 0.577 ≈ **30°**;
- R = 2 kΩ and Xc = 1 kΩ: φ = arctan 0.5 ≈ **26.6°**.

In a series RC, the current **leads** the input voltage (the capacitor pulls the current ahead). A low-pass output, taken across C, lags the input; a high-pass output, taken across R, leads it.

## Key points

- φ = 360° × Δt / T on the oscilloscope.
- φ = arctan(Xc / R) in a series RC.
- At the cut-off frequency, the phase shift is 45°.
