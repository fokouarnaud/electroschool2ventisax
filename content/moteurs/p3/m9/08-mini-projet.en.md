This mini-project is done in the workshop, with your trainer. You wire an interlocked reversing circuit, then a star-delta start **modelled** with lamps, at extra-low voltage.

## Objective

Check that an electrical interlock prevents any simultaneous closing, and observe the sequence of a star-delta start with its timer.

## Safety

- The whole bench runs on **24 V DC** for control and **12 V** for the lamps and motor, supplied by **wall adapters**. Never work on the 230/400 V side: the star-delta start is only **modelled** with lamps.
- Wire unplugged; have the wiring checked by the trainer before each switch-on.

![Bench: three 24 V relays model KM1 (line), KM2 (star) and KM3 (delta); three 12 V lamps show the sequence; KT1 times the change from star to delta](/static/content/moteurs/en/m9/banc.svg)

## Equipment

| Quantity | Item |
|---|---|
| 1 | 230 V to 24 V DC wall adapter and a 12 V supply |
| 3 | relays or contactors with 24 V coils, with 13-14 and 21-22 contacts |
| 1 | 24 V on-delay timer relay |
| 3 | push buttons (stop, forward, reverse) |
| 3 | 12 V lamps; a 12 V DC motor (reversing) |
| 1 | multimeter; oscilloscope (oscilloscope variant) |

## Oscilloscope variant

1. Wire the modelled star-delta: KM1 and KM2 close together, KT1 opens KM2 then closes KM3.
2. Channel 1 on lamp H2 (star), channel 2 on lamp H3 (delta). Measure the star → delta delay and the **dead time** between H2 going out and H3 lighting: it must never be negative (overlap = short circuit on a real motor).

## Multimeter-only variant

1. Wire the reversing of a 12 V motor with KM1 (forward) and KM2 (reverse), with the electrical interlock (21-22 of one in the coil of the other).
2. Press forward then, without stopping, reverse: check that KM2 does not close.
3. Remove one interlock wire (motor disconnected!): find with the multimeter that both coils can now be energised. Refit the wire.
4. Wire the modelled star-delta and time the delay set on KT1.

| Test | Expected | Observed |
|---|---|---|
| forward then reverse without stop | KM2 stays open | |
| star → delta delay (KT1 at 3 s) | 3 s | |
| H2 and H3 lit together | never | |

## Conclusion

Explain why a mechanical interlock is added when the electrical interlock works.
