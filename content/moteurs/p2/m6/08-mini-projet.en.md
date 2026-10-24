This mini-project is done in the workshop, with your trainer, on a **disconnected** three-phase induction motor. It is never energised during this mini-project.

## Objective

Read the nameplate, calculate synchronous speed, slip, current and torque, then check the windings with the ohmmeter.

## Safety

- The motor is **disconnected** from any supply and stays so; its supply cable is removed or locked out by the trainer.
- Only **resistances** are measured, with the ohmmeter (a few volts). No insulation tester, no measurement above 24 V, no work on the 230/400 V side.
- Oscilloscope measurements are made on the voltage of a small 12 V motor used as a generator, never on the three-phase motor.

![Ohmmeter connected between U1 and U2 of a disconnected motor, links removed](/static/content/moteurs/en/m6/releve.svg)

## Equipment

| Quantity | Item |
|---|---|
| 1 | disconnected three-phase induction motor, readable plate |
| 1 | multimeter (ohmmeter function) |
| 1 | screwdriver and spanner for the terminal box |
| 1 | small 12 V DC motor and oscilloscope (oscilloscope variant) |

## Oscilloscope variant

1. First take readings 1 to 3 of the multimeter-only variant.
2. Spin by hand the shaft of a small 12 V DC motor used as a generator; channel 1 across its terminals.
3. See that the voltage produced rises with speed: this is the back-EMF of module 5.

## Multimeter-only variant

1. Note the plate: power, voltages, currents, speed, cos φ, efficiency, class, IP.
2. Calculate ns, the slip s, the torque T = P / ω and, on 400 V, the current with the formula from module 2.
3. Open the terminal box, remove the links and note their position.
4. Measure U1-U2, V1-V2, W1-W2, then between U1 and V1 (must be infinite, links removed).
5. Refit the links in star and close the box.

| Quantity | Example (2.2 kW, 1,440 rpm, 4 poles) | Your motor |
|---|---|---|
| ns | 1,500 rpm | |
| slip | 4 % | |
| output torque | 14.6 N·m | |
| U1-U2, V1-V2, W1-W2 | three equal values | |
| U1-V1 without links | infinite | |

## Conclusion

Explain what a V1-V2 resistance half as large as the other two would indicate.
