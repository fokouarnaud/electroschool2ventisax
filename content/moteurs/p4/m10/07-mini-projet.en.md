This mini-project is done in the workshop, with your trainer. You adjust the speed of a 12 V motor by PWM, then the brightness of a 12 V lamp with a triac dimmer.

## Objective

Relate duty cycle to average voltage and speed, then observe the effect of a triac's firing angle.

## Safety

- The whole bench stays at **extra-low voltage**: 12 V DC for the PWM, 12 V AC for the dimmer, never above 24 V.
- The 12 V AC comes from a **moulded transformer** or a 230 V to 12 V AC wall adapter: never touch the 230 V side, measure on the secondary only.
- The module's heat sink can get hot; wire with the power off.

![Bench: 12 V supply, PWM module and 12 V motor; moulded 12 V AC transformer, triac dimmer and 12 V lamp](/static/content/moteurs/en/m10/banc.svg)

## Equipment

| Quantity | Item |
|---|---|
| 1 | 12 V DC supply (wall adapter) |
| 1 | 12 V PWM module with MOSFET or IGBT, with potentiometer |
| 1 | 12 V DC motor |
| 1 | moulded 230 V to 12 V AC transformer |
| 1 | low-voltage triac dimmer module and a 12 V incandescent lamp |
| 1 | multimeter; oscilloscope and signal generator (oscilloscope variant) |

## Oscilloscope variant

1. Probe the PWM module output (ground to 0 V). Set the potentiometer for a duty cycle of 25 %, 50 % then 75 %; note the switching frequency.
2. For each setting, measure the average voltage with the multimeter and compare it with duty cycle × 12 V.
3. On the dimmer, observe the voltage across the lamp (differential probe or isolation transformer, never on the 230 V side): find the firing angle for three knob positions.

## Multimeter-only variant

1. Measure the average voltage across the motor for five potentiometer positions.
2. Count the shaft turns (tape marker) over 10 s or estimate the speed; plot speed against voltage.
3. On the dimmer, measure the RMS voltage across the lamp for three positions and note the brightness.

| Setting | Duty cycle | Calculated Uavg | Measured Uavg | Speed |
|---|---|---|---|---|
| 1 | 25 % | 3 V | | |
| 2 | 50 % | 6 V | | |
| 3 | 75 % | 9 V | | |

## Conclusion

Explain why the PWM module's transistor stays fairly cool although it controls the whole motor current.
