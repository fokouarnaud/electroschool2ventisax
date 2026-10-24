This mini-project is done in the workshop, with your trainer. You apply the full lockout procedure to a small extra-low-voltage bench.

## Objective

Lock out a 24 V bench, verify the absence of voltage properly, then remove the lockout.

## Safety

- The whole bench runs on **24 V DC**, supplied by a 230 V to 24 V **wall adapter**. Only the adapter is plugged into the mains: never open its case and never work on the 230 V side.
- Even at 24 V, apply the full method: it is the one you will apply tomorrow on a 400 V motor.
- Always wire with the adapter unplugged.

![24 V lockout bench: adapter, lockable isolator, tag and lamp](/static/content/moteurs/en/m1/banc.svg)

## Equipment

| Quantity | Item |
|---|---|
| 1 | 230 V to 24 V DC wall adapter, 1 A |
| 1 | lockable switch-disconnector (or key switch) |
| 1 | 24 V lamp or indicator |
| 1 | personal padlock and a lockout tag |
| 1 | multimeter (and a voltage tester if the workshop has one) |
| 1 | 9 V battery used as a known source |

## Oscilloscope variant

1. Wire adapter, isolator and lamp. Connect channel 1 of the oscilloscope across the lamp.
2. Observe the voltage (a straight line at 24 V). Open the isolator: the trace drops to 0 V. Measure how long the voltage takes to disappear.
3. Apply the steps: isolate, lock (padlock and filled-in tag), identify the lamp, verify the absence of voltage with the multimeter tested on the battery before and after.

## Multimeter-only variant

1. Same wiring. Measure the voltage across the lamp, isolator closed.
2. Open the isolator, fit padlock and tag.
3. Test the multimeter on the 9 V battery, measure across the lamp, then test it again on the battery.
4. Remove the lockout in reverse order and check that the lamp lights again.

| Measurement | Expected | Measured |
|---|---|---|
| lamp voltage, isolator closed | 24 V | |
| battery voltage (check before) | 9 V | |
| lamp voltage, locked out | 0 V | |
| battery voltage (check after) | 9 V | |

## Conclusion

Explain why testing the multimeter on the battery, after the measurement, is essential.
