This mini-project is done in the workshop, with your trainer. Depending on the equipment available, follow the oscilloscope variant or the multimeter-only variant. Bring your completed measurement table.

## Goal

Measure a transformer **on the secondary side only**: its no-load and loaded voltage, its turns ratio, and work out the primary current by calculation.

## Parts

| Quantity | Component |
|---|---|
| 1 | **enclosed** 230 V to 12 V AC (or 9 V AC) wall adapter, about 10 VA |
| 1 | 100 Ω resistor, 2 W or more |
| 1 | 47 Ω resistor, 5 W |
| 1 | small audio output transformer (for example 1 kΩ to 8 Ω) (oscilloscope variant) |
| 1 | signal generator and two-channel oscilloscope (oscilloscope variant) |
| 1 | multimeter |
| 1 | breadboard and wires |

## Safety

- **Never** work on the 230 V side: only the enclosed adapter is plugged into the mains. Never open its case, never measure its primary.
- All measurements are made on the secondary wires (12 V AC), with the adapter unplugged while wiring.
- The 47 Ω resistor dissipates about 3 W: it gets hot, do not touch it during the test and keep the test to one minute.

## Oscilloscope variant

1. First carry out steps 1 to 4 of the multimeter-only variant.
2. Connect the generator (sine, 1 kHz, 2 V peak to peak) to the 1 kΩ winding of the audio transformer. Channel 1 on this winding, channel 2 on the 8 Ω winding.
3. Measure both peak-to-peak voltages and calculate the ratio. Compare with √(1,000 / 8) ≈ 11.2.
4. Swap the two wires of the 8 Ω winding: the channel 2 trace moves into antiphase.
5. Connect the oscilloscope to the adapter's secondary, with no load: check that Upp ≈ 2 × √2 × Urms and that the period is 20 ms.

| Quantity | Calculated | Measured |
|---|---|---|
| audio ratio Up / Us | 11.2 | |
| Us peak to peak (audio) | 0.18 V | |
| secondary period | 20 ms | |

## Multimeter-only variant

1. Adapter plugged in, no load: measure the secondary voltage on V~. It is often above the rated value (for example 13.5 V for a 12 V model).
2. Connect the 100 Ω resistor: measure Us and the current Is (multimeter on A~, in series).
3. Replace it with 47 Ω, then measure Us and Is again.
4. For each load, calculate:
   - the ratio m = Us / 230 (rated mains voltage);
   - the primary current Ip = Is × Us / 230;
   - the voltage drop compared with the no-load measurement.

| Quantity | Calculated (12 V) | Measured |
|---|---|---|
| Us no load | | |
| Is on 100 Ω | 0.12 A | |
| Is on 47 Ω | 0.26 A | |
| Ip on 47 Ω | 13 mA | |
| m | 0.052 | |

## To conclude

Explain why the secondary voltage drops as the current increases, and why Ip is calculated instead of measured.
