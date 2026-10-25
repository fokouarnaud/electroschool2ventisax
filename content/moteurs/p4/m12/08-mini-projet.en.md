This mini-project is done in the workshop, with your trainer, on any **24 V programmable relay**. You program a hold-in, then a timer, then a counter.

## Objective

Write, load and test three ladder programs, and check their behaviour by measurement.

## Safety

- The whole bench is at **24 V DC**, from a wall adapter; the outputs drive indicators or LEDs, never a load on the mains.
- Wire with the power off; have your trainer check the wiring before switching on.

![Bench: 24 V programmable relay, switches on %IX0.0 to %IX0.2, indicators on %QX0.0 and %QX0.1](/static/content/moteurs/en/m12/banc.svg)

## Equipment

| Quantity | Item |
|---|---|
| 1 | 24 V DC programmable relay (any brand) and its software or keypad |
| 1 | 230 V to 24 V DC wall adapter |
| 3 | 24 V push buttons or switches (one with a break contact for stop) |
| 2 | 24 V indicators or LEDs |
| 1 | multimeter; oscilloscope (oscilloscope variant); stopwatch |

**Translate for your brand**: replace %IX0.0, %IX0.1, %IX0.2 with your relay's first three inputs (for example I1, I2, I3) and %QX0.0, %QX0.1 with its first two outputs (Q1, Q2).

## The three programs

1. **Hold-in**: stop %IX0.0 (break contact), start %IX0.1, output %QX0.0.
2. **TON**: %IX0.2 starts a 5 s TON that lights %QX0.1.
3. **CTU**: %IX0.2 increments a CTU with preset 5; Q lights %QX0.1; %IX0.0 resets it.

## Oscilloscope variant

1. Channel 1 on input %IX0.2, channel 2 on output %QX0.1 (ground to 0 V).
2. TON program: measure the delay between the input edge and the output edge; compare with 5 s.
3. Replace it with a 3 s TOF and measure the off-delay.

## Multimeter-only variant

1. Hold-in program: read the voltage of output %QX0.0 with the multimeter after start, then after stop.
2. TON program: time the delay three times and average.
3. CTU program: count the presses until it lights; check that a held press counts only once.

| Test | Expected | Measured |
|---|---|---|
| output after start | 24 V | |
| TON delay | 5 s | |
| presses before CTU Q | 5 | |

## Conclusion

Disconnect the stop button wire while the output is on: what happens, and why is it intended?
