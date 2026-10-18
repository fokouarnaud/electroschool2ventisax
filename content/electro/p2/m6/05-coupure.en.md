A filter does not cut sharply: the output falls gradually. To describe it with a single number, we define its **cut-off frequency** fc.

![Xc falls with frequency and crosses the R = 1 kΩ line at the cut-off frequency](/static/content/electro/en/m6/coupure.svg)

## Xc = R

The cut-off frequency is the one where the capacitor's reactance equals the resistance. Writing 1 / (2π × f × C) = R gives:

**fc = 1 / (2π × R × C)**

Example: R = 1 kΩ and C = 100 nF. fc = 1 / (2 × 3.14 × 1,000 × 0.0000001) ≈ **1,592 Hz**, about 1.6 kHz.

To choose a component, turn the formula round: **R = 1 / (2π × fc × C)** or **C = 1 / (2π × fc × R)**. For fc = 1 kHz with C = 100 nF, you need R ≈ 1,592 Ω.

[[calc:cutoff]]

## 70.7 % of the input, or −3 dB

At fc, Xc = R: Z = √(R² + R²) = R × √2. The output is then Vin / √2:

**At fc: Vout ≈ 0.707 × Vin**, for a low-pass as for a high-pass.

Engineers say that at fc the filter attenuates by **3 decibels (−3 dB)**. Simply remember: −3 dB ≈ 70.7 % of the input voltage. With Vin = 5 V at the cut-off frequency, Vout ≈ 3.54 V.

![Low-pass: the output is about 99 % of the input at fc / 10, 70.7 % at fc and 10 % at 10 × fc](/static/content/electro/en/m6/attenuation.svg)

## Landmarks one decade apart

For an RC low-pass:

- at **fc / 10**, Vout ≈ 99 % of Vin: the signal passes;
- at **fc**, Vout ≈ 70.7 % of Vin;
- at **10 × fc**, Vout ≈ 10 % of Vin: the signal is strongly attenuated.

For a high-pass it is the reverse: 10 % at fc / 10 and 99 % at 10 × fc.

## Key points

- fc = 1 / (2π × R × C): at fc, Xc = R.
- At fc, Vout ≈ 0.707 × Vin (−3 dB).
- One decade above fc, a low-pass only lets about 10 % through.
