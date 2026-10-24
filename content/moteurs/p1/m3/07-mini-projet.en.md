This mini-project is done in the workshop, with your trainer. You measure a transformer on its secondary side only and work out its efficiency and voltage drop.

## Objective

Measure the secondary voltage and current of a small transformer no-load and on load, and calculate the apparent power, the voltage drop and the primary current.

## Safety

- **Never work on the 230 V side**: only a **moulded adapter** or **moulded transformer** 230 V to 12 V AC is plugged into the mains. Never open its case and never measure its primary.
- All measurements are made on the secondary (12 V AC), adapter unplugged while wiring.
- The load resistor gets hot: do not touch it during the test and limit the test to one minute.
- No circuit in this module exceeds 24 V.

![Mini-project bench: moulded 230 V to 12 V AC adapter, resistive load, ammeter and voltmeter on the secondary](/static/content/moteurs/en/m3/banc.svg)

## Equipment

| Quantity | Item |
|---|---|
| 1 | moulded 230 V to 12 V AC adapter, about 12 VA |
| 1 | 22 Ω resistor, 10 W |
| 1 | 47 Ω resistor, 5 W |
| 1 | multimeter (and a second one if possible) |
| 1 | oscilloscope (oscilloscope variant) |
| 1 | terminal block and wires |

## Oscilloscope variant

1. First take measurements 1 to 3 of the multimeter-only variant.
2. Connect the oscilloscope to the no-load secondary: measure the peak voltage and check that Urms ≈ Upeak / √2 and that the period is 20 ms (50 Hz).
3. Connect the 22 Ω load and see that the sine wave stays clean, slightly smaller.

| Quantity | Calculated | Measured |
|---|---|---|
| period | 20 ms | |
| no-load peak voltage (12 V rms) | 17 V | |

## Multimeter-only variant

1. Measure the no-load secondary voltage (V~). It is often above 12 V, for example 13.5 V.
2. Connect the 47 Ω load: measure Us and Is (multimeter on A~, in series).
3. Replace it with 22 Ω, then measure Us and Is again.
4. Calculate for each load: the apparent power S = Us × Is, the voltage drop compared with no-load (in %), and the primary current Ip ≈ Is × Us / 230.

| Quantity | Calculated (12 V) | Measured |
|---|---|---|
| Is on 47 Ω | 0.26 A | |
| Is on 22 Ω | 0.55 A | |
| S on 22 Ω | 6.5 VA | |
| Ip on 22 Ω | 29 mA | |

## Conclusion

Explain why the secondary voltage drops when the current rises, and why the primary current is calculated rather than measured.
