This mini-project is done in the workshop, with your trainer. You wire the most common control circuit in industry, start/stop with hold-in, on a real contactor, at extra-low voltage.

## Objective

Wire a contactor with a 24 V coil, start and stop buttons and a hold-in, make it switch a 12 V motor, measure its pull-in and drop-out voltages, and observe the effect of coil suppression.

## Safety

- The control circuit is at **24 V DC** (230 V to 24 V wall adapter), the power circuit at **12 V DC**: nothing exceeds 24 V and you never work on the 230 V side.
- Wire every circuit unplugged; have the wiring checked before switching on.

![Bench: 24 V control with stop S1, start S2, hold-in contact 13-14 and coil KM1; the KM1 pole switches a 12 V motor](/static/content/moteurs/en/m7/banc.svg)

## Equipment

| Quantity | Item |
|---|---|
| 1 | contactor with a 24 V DC coil and a 13-14 auxiliary contact |
| 2 | push buttons (stop break contact, start make contact) |
| 1 | 230 V to 24 V DC adapter and an adjustable 0 to 24 V supply |
| 1 | 12 V DC motor and its 12 V supply |
| 1 | 1N4007 diode (suppression) |
| 1 | multimeter; oscilloscope (oscilloscope variant) |

## Oscilloscope variant

1. Wire the control and power circuits as in the diagram; check start, hold-in and stop.
2. Channel 1 of the oscilloscope across the coil, without diode. Press stop: observe the voltage spike when switching off.
3. Add the diode in reverse across the coil (cathode on A1) and repeat: the spike disappears.

## Multimeter-only variant

1. Wire and check operation (start, hold-in, stop).
2. Measure the coil current when running (multimeter in series).
3. Supply the coil from the adjustable supply: raise the voltage slowly and note the **pull-in voltage** (closing), then lower it and note the **drop-out voltage**.

| Quantity | Expected | Measured |
|---|---|---|
| pull-in voltage | ≤ 85 % of 24 V, that is ≤ 20.4 V | |
| drop-out voltage | clearly lower | |
| coil current (3 W coil) | about 125 mA | |

## Conclusion

Explain why the motor does not restart by itself when the supply is reconnected after being cut while running.
