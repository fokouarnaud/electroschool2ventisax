This mini-project is done in the workshop, with your trainer. Depending on the equipment available, follow the oscilloscope variant or the multimeter-only variant. Bring your completed measurement table.

## Goal

Build the module's 5 V supply from a 12 V AC adapter, and measure each stage: rectification, smoothing, ripple and regulation.

## Parts

| Quantity | Component |
|---|---|
| 1 | **enclosed** 230 V to 12 V AC wall adapter, about 10 VA |
| 4 | 1N4001 diodes (or a 1 A bridge rectifier) |
| 1 | 2,200 µF electrolytic capacitor, 25 V or more |
| 1 | 7805 regulator in a TO-220 package and a small heatsink |
| 1 | 330 nF capacitor and 1 of 100 nF |
| 1 | 100 Ω, 1 W resistor and 1 of 47 Ω, 1 W |
| 1 | LED and its 330 Ω resistor (indicator) |
| 1 | oscilloscope (oscilloscope variant) |
| 1 | multimeter |
| 1 | breadboard and wires of adequate size |

## Safety

- Only the **enclosed** adapter is plugged into 230 V. Never open its case and only work on the 12 V side.
- Unplug the adapter before every change, and wait for the capacitor to discharge (the indicator LED goes out).
- Respect the polarity of the 2,200 µF capacitor: fitted the wrong way round, it can burst. Do not lean over it at switch-on.
- The regulator and the resistors get hot: do not touch them while running.

## Oscilloscope variant

1. Build the bridge alone, loaded with 100 Ω. On the oscilloscope, observe the full-wave signal: about 15.6 V peak and a 10 ms period.
2. Add the 2,200 µF capacitor. Measure the peak voltage and the ripple ΔU (AC coupling on the channel to enlarge the ripple). Calculate ΔU ≈ I / (100 × 0.0022) with I ≈ 15 V / 100 Ω = 0.15 A.
3. Add the 7805, its two capacitors and the heatsink, then the indicator LED. Load the output with 100 Ω, then with 47 Ω: the output stays at 5 V and the ripple disappears.

| Quantity | Calculated | Measured |
|---|---|---|
| peak after the bridge | 15.6 V | |
| ΔU with 2,200 µF, 0.15 A | 0.68 V | |
| 7805 output on 100 Ω | 5.0 V | |
| 7805 output on 47 Ω | 5.0 V | |

## Multimeter-only variant

1. Bridge alone, loaded with 100 Ω: measure the voltage on DC volts. The multimeter shows the **average** value, about 0.64 × 15.6 ≈ 9.9 V.
2. Add the capacitor: the DC voltage rises towards 15 V. Disconnect the load: it reaches the peak voltage, about 15.6 V.
3. With the load, switch the multimeter to V~: most meters then show a value related to the ripple (check with your trainer that yours blocks DC on this range).
4. Add the regulator and measure the output with no load, on 100 Ω then on 47 Ω. Calculate the power dissipated in the 7805: P = (Ue − 5) × I.

| Quantity | Calculated | Measured |
|---|---|---|
| bridge alone, average | 9.9 V | |
| with C, no load | 15.6 V | |
| output on 47 Ω | 5.0 V | |
| P in the 7805 on 47 Ω | ≈ 1 W | |

## To conclude

Explain why the no-load voltage after the capacitor exceeds 12 V, and why the regulator gets hotter with the 47 Ω load.
