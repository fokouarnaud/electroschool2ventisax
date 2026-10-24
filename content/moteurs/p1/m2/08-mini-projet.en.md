This mini-project is done in the workshop, with your trainer. You wire a small circuit from its diagram, then read the plate of a real motor.

## Objective

Go from diagram to wiring without mistakes, and use a nameplate.

## Safety

- The circuit is supplied at **24 V DC** by a 230 V to 24 V **wall adapter**. Never work on the 230 V side and never open the adapter.
- Wire with the adapter unplugged; have your wiring checked by the trainer before plugging it in.
- The three-phase motor used in part 2 is **disconnected** and stays so: you only read its plate and look at its terminal plate.

![24 V circuit: make button S1 lights H1; break button S2 switches H2 off when pressed](/static/content/moteurs/en/m2/lampes.svg)

## Equipment

| Quantity | Item |
|---|---|
| 1 | 230 V to 24 V DC wall adapter |
| 2 | push buttons (one make, one break) |
| 2 | 24 V indicators or lamps |
| 1 | terminal block, wires, ferrules |
| 1 | multimeter |
| 1 | disconnected three-phase motor, readable plate |

## Oscilloscope variant

1. Wire the circuit and check with the multimeter, de-energised, the continuity of each branch.
2. Switch on. Channel 1 across H1, channel 2 across H2.
3. Press S1 then S2: see on both traces that the lamps change state at the same moment as the buttons, and note any contact bounce when pressing.

## Multimeter-only variant

1. Wire the circuit from the diagram, adapter unplugged.
2. De-energised, measure the resistance of S1 and S2 at rest then pressed: check that S1 is a make contact and S2 a break contact.
3. Switch on and measure the voltage across each lamp, buttons at rest then pressed.
4. On the disconnected motor, note the plate and state the connection to use on a 400 V supply.

| Measurement | Expected | Measured |
|---|---|---|
| S1 at rest | open circuit | |
| S2 at rest | a few ohms at most | |
| H1, S1 pressed | 24 V | |
| H2, S2 pressed | 0 V | |
| motor connection on 400 V | | |

## Conclusion

Explain why a diagram is always drawn with the contacts at rest.
