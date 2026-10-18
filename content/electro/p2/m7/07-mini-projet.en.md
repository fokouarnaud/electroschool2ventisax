This mini-project is done in the workshop, with your trainer. Depending on the equipment available, follow the oscilloscope variant or the multimeter-only variant. Bring your completed measurement table.

## Goal

Show the resonance of a series RLC circuit or, without a generator, check by measurement that a series RLC fed at 50 Hz behaves as the calculation predicts.

## Parts

| Quantity | Component |
|---|---|
| 1 | breadboard and wires |
| 1 | 100 Ω, 0.5 W resistor |
| 1 | 10 mH inductor and one 100 mH inductor (rated 100 mA or more) |
| 1 | 100 nF non-polarised capacitor and one 10 µF (film, 63 V or more) |
| 1 | signal generator and two-channel oscilloscope (oscilloscope variant) |
| 1 | **enclosed** 230 V to 12 V AC wall adapter (transformer, multimeter-only variant) |
| 1 | multimeter |

## Safety

- Only the enclosed adapter is plugged into 230 V. Never open its case and only work on the 12 V side.
- Unplug the adapter or switch off the generator before every change to the circuit.
- Near resonance, the voltage across the capacitor can exceed the source's: only use capacitors rated 63 V or more and do not touch the circuit while it is powered.
- All oscilloscope and generator ground clips go to the same point: the bottom of the resistor.

## Oscilloscope variant

1. Calculate f0 for L = 10 mH and C = 100 nF (about 5 kHz), then the expected bandwidth BW = R / (2π × L), about 1.6 kHz with R = 100 Ω.
2. Build in series: generator, capacitor, inductor, 100 Ω resistor to ground. Channel 1 on the generator output, channel 2 across R (a picture of the current).
3. Set the generator to sine, 2 V peak to peak. Sweep the frequency from 1 kHz to 20 kHz and find where Ur is largest: that is f0.
4. Record Ur at the frequencies in the table. Look for f1 and f2, where Ur is 0.707 × Ur max, and calculate BW = f2 − f1 and Q = f0 / BW.
5. Compare with the calculation. The inductor's wire resistance adds to R: the measured bandwidth is often a little wider.

| f | 2 kHz | 4 kHz | measured f0 | 6 kHz | 10 kHz | f1 | f2 |
|---|---|---|---|---|---|---|---|
| Upp across R | | | | | | | |

| Quantity | Measured | Calculated |
|---|---|---|
| f0 | | 5,033 Hz |
| BW | | 1,592 Hz |
| Q | | 3.2 |

## Multimeter-only variant

Without a generator, the frequency stays at 50 Hz. Choose L = 100 mH and C = 10 µF: f0 ≈ 159 Hz, so at 50 Hz the circuit is **below** its resonance.

1. Calculate at 50 Hz: XL ≈ 31.4 Ω, XC ≈ 318 Ω, Z = √(R² + (XL − XC)²) ≈ 304 Ω.
2. Build in series: adapter, 100 Ω resistor, 100 mH inductor, 10 µF capacitor, multimeter on mA~.
3. Record the current, then the RMS voltages across the adapter, R, L and C.
4. Check that Ue ≈ √(Ur² + (UL − UC)²). Notice that UC is larger than Ue.
5. Calculate the capacitance that would give resonance at 50 Hz with 100 mH: C = 1 / (4π² × 50² × 0.1) ≈ 101 µF. Explain why it is hard to reach with film capacitors.

| Quantity | Measured | Calculated (under 12 V) |
|---|---|---|
| I | | 39.5 mA |
| Ur | | 3.95 V |
| UL | | 1.24 V |
| UC | | 12.6 V |

## To conclude

Explain why the voltage across the capacitor can exceed the source's, and what limits the height of the resonance peak.
