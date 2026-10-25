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

## What happens in the circuit

The same current flows through R and C. Across R, the voltage follows the current at the same instant. Across C, it follows the stored charge: it peaks a quarter of a period (90°) after the current, at the moment the current falls to zero and stops charging the capacitor.

The current leads Vin by φ = arctan(Xc / R). The output of a low-pass, taken across C, therefore lags the input by 90° − φ. At fc / 10, Xc = 10 kΩ: φ ≈ 84.3° and the output lags by only 5.7°, almost in phase. At fc, Xc = R: φ = 45° and the lag is also 45°, that is Δt = T / 8. At 10 × fc, φ ≈ 5.7° and the lag approaches 90° (84.3°).

On the chart recorder below, channel 1 records Vin and channel 2 records Vout. Pause it and count the marks under the bracket: each one is 45°. The readout gives Δt / T, then the lag 360° × Δt / T. With Xc = 577 Ω, the current leads by 30° and the output lags by 60°.

[[fig:rc_phase]]

## Key points

- φ = 360° × Δt / T on the oscilloscope.
- φ = arctan(Xc / R) in a series RC.
- At the cut-off frequency, the phase shift is 45°.
