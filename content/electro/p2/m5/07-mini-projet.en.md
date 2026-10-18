This mini-project is done in the workshop, with your trainer. Depending on the equipment available, follow the oscilloscope variant or the multimeter-only variant. Bring your completed measurement table.

## Goal

Measure the values of a sine-wave voltage, then check by measurement a capacitor's reactance and how it changes with frequency or capacitance.

## Parts

| Quantity | Component |
|---|---|
| 1 | breadboard and wires |
| 2 | **non-polarised** (film) 1 µF capacitors, rated 63 V or more |
| 2 | non-polarised (film) 2.2 µF capacitors, 63 V or more |
| 1 | 10 Ω, 0.25 W resistor |
| 1 | signal generator and two-channel oscilloscope (oscilloscope variant) |
| 1 | **enclosed** 230 V to 12 V AC wall adapter (transformer, multimeter-only variant) |
| 1 | multimeter |

## Safety

- Only the enclosed adapter is plugged into 230 V. Never open its case and only work on the 12 V side.
- Unplug the adapter or switch off the generator before every change to the circuit.
- Never use an electrolytic (polarised) capacitor in AC.
- An ammeter always goes in series, never straight across a source.
- All oscilloscope and generator ground clips go to the same point of the circuit.

## Oscilloscope variant

1. Set the generator: sine, 1 kHz, 4 V peak to peak. Watch it on channel 1 and measure Upp, Umax and T; calculate f.
2. Build in series: generator output, 1 µF capacitor, 10 Ω resistor to ground. Channel 2 measures the voltage across the 10 Ω resistor.
3. The current is Imax = Umax(channel 2) / 10. Since the resistor is small compared with Xc, almost all the voltage is across the capacitor: Xc ≈ Umax(channel 1) / Imax.
4. Compare with Xc = 1 / (2π × f × C), that is 159 Ω at 1 kHz.
5. Repeat at 500 Hz then at 2 kHz. How does Xc change?

| f | Umax channel 1 | Umax channel 2 | Imax | Measured Xc | Calculated Xc |
|---|---|---|---|---|---|
| 500 Hz | | | | | 318 Ω |
| 1 kHz | | | | | 159 Ω |
| 2 kHz | | | | | 80 Ω |

## Multimeter-only variant

1. Measure the adapter's RMS voltage with no load, on V~. Calculate Umax = Urms × 1.414. (A 12 V adapter often reads a little more with no load.)
2. Connect in series: adapter, multimeter on mA~, 2.2 µF capacitor. Record the RMS current.
3. Measure the RMS voltage across the capacitor with the multimeter on V~.
4. Calculate Xc = Urms / Irms and compare with 1 / (2π × 50 × 0.0000022) ≈ 1,447 Ω.
5. Put the second 2.2 µF capacitor in parallel with the first (4.4 µF). What happens to the current and to Xc?

| Circuit | RMS U | RMS I | Measured Xc | Calculated Xc |
|---|---|---|---|---|
| Adapter, no load | | - | - | - |
| 2.2 µF | | | | 1,447 Ω |
| 2 × 2.2 µF in parallel | | | | 723 Ω |

## To conclude

Write in one sentence how Xc changes with frequency and with capacitance, and what explains the gaps between measurement and calculation (capacitor tolerance, instrument accuracy).
