An inductor can replace the capacitor in a filter. Its reactance XL changes the opposite way to Xc: it **rises** with frequency. So the roles are swapped.

![RL low-pass filter: 10 mH inductor in series, 100 Ω resistor to ground, output Vout across the resistor](/static/content/electro/en/m6/rl-passe-bas.svg)

## RL low-pass and high-pass

With the inductor **in series** and the output **across R**:

- at low frequencies, XL is small: the inductor lets the signal through, Vout ≈ Vin;
- at high frequencies, XL becomes large: the inductor blocks, Vout → 0.

That is a **low-pass**. Taking the output **across the inductor** instead gives a **high-pass**.

| Filter | In series | Output across |
|---|---|---|
| RC low-pass | R | C |
| RC high-pass | C | R |
| RL low-pass | L | R |
| RL high-pass | R | L |

## What happens in the circuit

An inductor opposes changes of current: the voltage across it is L times the rate at which the current changes. At low frequencies the current changes slowly: the inductor needs almost no voltage and almost all the input voltage ends up across R (Vout ≈ Vin). At high frequencies the current would have to change very fast: the inductor takes almost all the voltage, the current stays small and Vout → 0.

On the bench below, the flywheel turbine plays the inductor: set going by the water, it resists every change of direction. At fc / 10, XL = 10 Ω, ten times less than R: Vout ≈ 0.995 × Vin and the current lags by only 5.7°. At fc, XL = R = 100 Ω: Vout ≈ 0.707 × Vin and the lag is 45°. At 10 × fc, XL = 1 kΩ: Vout ≈ 0.0995 × Vin and the lag reaches 84.3°.

[[fig:rl_lowpass]]

## Impedance, cut-off and phase shift

The formulas follow the same pattern as for RC, with XL:

- **Z = √(R² + XL²)**;
- **fc = R / (2π × L)**: at fc, XL = R and Vout ≈ 0.707 × Vin;
- **φ = arctan(XL / R)**; in a series RL, the current **lags** the input voltage.

Example: R = 100 Ω and L = 10 mH. fc = 100 / (2 × 3.14 × 0.01) ≈ **1,592 Hz**. With R = 220 Ω and the same inductor, fc ≈ 3,501 Hz.

![Response of the 100 Ω, 10 mH RL low-pass: Vout / Vin is 1 at low frequencies and 0.707 near 1.6 kHz](/static/content/electro/en/m6/rl-courbe.svg)

## RC or RL?

At audio frequencies, capacitors are small, cheap and accurate: RC is preferred. Inductors are used rather when currents are large (power supply filters, loudspeaker crossovers) or at high frequencies (radio).

## Key points

- XL rises with f: inductor in series and output across R give a low-pass.
- fc = R / (2π × L).
- In a series RL, the current lags the voltage.
