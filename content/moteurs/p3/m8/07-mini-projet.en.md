This mini-project is done in the workshop, with your trainer. You set a timer relay and build logic functions with two relays, at extra-low voltage.

## Objective

Check the on-delay and off-delay functions, then wire the AND and OR functions with buttons, two relays and indicators.

## Safety

- The whole bench runs on **24 V DC**, supplied by a 230 V to 24 V **wall adapter**. Never work on the 230 V side.
- Wire with the adapter unplugged; check the relays' pinout in their instructions before wiring.

![Bench: 24 V supply, relays KA1 and KA2, timer relay KT1, buttons S1 and S2, indicators H1 and H2](/static/content/moteurs/en/m8/banc.svg)

## Equipment

| Quantity | Item |
|---|---|
| 1 | 230 V to 24 V DC wall adapter |
| 2 | 24 V relays with changeover contact, on sockets |
| 1 | 24 V multifunction timer relay |
| 2 | make push buttons |
| 2 | 24 V indicators |
| 1 | stopwatch (or phone); multimeter; oscilloscope (oscilloscope variant) |

## Oscilloscope variant

1. Set KT1 to on-delay, 2 s. Channel 1 on its coil, channel 2 on its contact output (to H1).
2. Press S1: measure on the screen the delay between the two channels.
3. Switch to the flasher function: measure the period and the ratio between on time and off time.

## Multimeter-only variant

1. Set KT1 to on-delay, 5 s: time the delay between pressing and H1 lighting, five times, and average.
2. Switch to off-delay, 5 s: time the delay between releasing and H1 going out.
3. Wire S1 and S2 driving KA1 and KA2; their 11-14 contacts **in series** to H1 (AND function), **in parallel** to H2 (OR function). Fill in the truth table.

| S1 | S2 | H1 (AND) expected | H2 (OR) expected | H1, H2 observed |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | |
| 0 | 1 | 0 | 1 | |
| 1 | 0 | 0 | 1 | |
| 1 | 1 | 1 | 1 | |

## Conclusion

Compare the measured delay with the setting: what difference, as a percentage? Why repeat the measurement several times?
