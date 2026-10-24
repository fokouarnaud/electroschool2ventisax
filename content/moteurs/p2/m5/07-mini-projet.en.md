This mini-project is done in the workshop, with your trainer. You measure a small 12 V DC motor and check the equation U = E + R × I.

## Objective

Measure the armature resistance, the no-load and on-load current, calculate the back-EMF and reverse the direction of rotation.

## Safety

- The bench is supplied at **12 V DC** by a bench supply or a 230 V to 12 V **wall adapter**. Nothing exceeds 24 V and you never work on the 230 V side.
- Clamp the motor to the table: it jumps when it starts. Never stall the shaft for more than a few seconds: the starting current would overheat it.

![Mini-project bench: 12 V supply, ammeter in series and voltmeter across the motor](/static/content/moteurs/en/m5/banc.svg)

## Equipment

| Quantity | Item |
|---|---|
| 1 | 12 V permanent-magnet DC motor, about 10 W |
| 1 | adjustable 12 V supply, 2 A |
| 1 | multimeter (and a second one if possible) |
| 1 | double-pole changeover switch |
| 1 | optical tachometer (optional) |
| 1 | oscilloscope and 12 V PWM module (oscilloscope variant) |

## Oscilloscope variant

1. First take measurements 1 to 4 of the multimeter-only variant.
2. Supply the motor through the PWM module. Channel 1 across the motor.
3. Set three duty cycles (25 %, 50 %, 75 %): measure the average voltage on the screen and note the speed.

## Multimeter-only variant

1. Motor disconnected, measure the armature resistance R with the ohmmeter; turn the shaft slightly between three readings and keep the smallest.
2. Supply 12 V with no load: measure U and I.
3. Brake the shaft slightly (protected finger, or a small load): measure U and I.
4. Calculate E = U − R × I in both cases.
5. Reverse the polarity with the switch: check that the direction changes.

| Quantity | Calculated (R = 1.5 Ω) | Measured |
|---|---|---|
| E no-load (I = 0.3 A) | 11.55 V | |
| E on load (I = 2 A) | 9 V | |
| starting current U / R | 8 A | |

## Conclusion

Explain why E falls when the motor is braked, and why the current rises.
