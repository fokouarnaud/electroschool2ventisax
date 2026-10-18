This mini-project is done in the workshop, with your trainer. Depending on the equipment available, follow the oscilloscope variant or the multimeter-only variant. Bring your completed measurement table.

## Goal

Build an RC low-pass filter, record its response and check the calculated cut-off frequency.

## Parts

| Quantity | Component |
|---|---|
| 1 | breadboard and wires |
| 1 | 1 kΩ resistor and one 10 kΩ resistor, 0.25 W |
| 3 | non-polarised capacitors (film, 63 V or more): 100 nF, 330 nF, 1 µF |
| 1 | signal generator and two-channel oscilloscope (oscilloscope variant) |
| 1 | **enclosed** 230 V to 12 V AC wall adapter (transformer, multimeter-only variant) |
| 1 | multimeter |
| 1 | calculator with √ and tan⁻¹ |

## Safety

- Only the enclosed adapter is plugged into 230 V. Never open its case and only work on the 12 V side.
- Unplug the adapter or switch off the generator before every change to the circuit.
- Non-polarised capacitors only.
- All oscilloscope and generator ground clips go to the same point: the bottom of the capacitor.

## Oscilloscope variant

1. Calculate fc for R = 1 kΩ and C = 100 nF (about 1.6 kHz).
2. Build the low-pass: generator, series resistor, capacitor to ground. Channel 1 on the input, channel 2 on the output (across C).
3. Set the generator to sine, 4 V peak to peak. For each frequency in the table, measure Upp at the input and at the output, then the time gap Δt between the two curves.
4. Calculate Vout / Vin and φ = 360° × Δt / T. Compare with the expected values.
5. Plot Vout / Vin against frequency and find the frequency where the ratio is 0.707.

| f | Input Upp | Output Upp | Vout / Vin | Expected Vout / Vin | Δt | φ | Expected φ |
|---|---|---|---|---|---|---|---|
| 160 Hz | | | | 0.995 | | | 5.7° |
| 500 Hz | | | | 0.954 | | | 17.4° |
| 1.6 kHz | | | | 0.705 | | | 45° |
| 5 kHz | | | | 0.303 | | | 72.3° |
| 16 kHz | | | | 0.099 | | | 84.3° |

## Multimeter-only variant

The adapter's frequency is fixed (50 Hz), so you change C to place 50 Hz below, at or above the cut-off frequency.

1. Build: adapter, 10 kΩ resistor in series, capacitor back to the adapter's other terminal.
2. For each capacitor, calculate fc = 1 / (2π × 10,000 × C).
3. Measure on V~ the input voltage Ue, the voltage Ur across R and the voltage Uc across C (the low-pass output).
4. Calculate Uc / Ue and check that √(Ur² + Uc²) ≈ Ue.

| C | fc | Ue | Ur | Uc | Uc / Ue | Expected Uc / Ue |
|---|---|---|---|---|---|---|
| 100 nF | 159 Hz | | | | | 0.954 |
| 330 nF | 48 Hz | | | | | 0.694 |
| 1 µF | 16 Hz | | | | | 0.303 |

## To conclude

Explain why Ur + Uc is larger than Ue, and say for which circuit 50 Hz is closest to the cut-off frequency.
