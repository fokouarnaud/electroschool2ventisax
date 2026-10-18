An **oscillator** produces a periodic signal from a plain DC voltage: the clock of a microcontroller, the carrier of a radio transmitter, the tone of a buzzer. In Part 2, a charged LC circuit oscillated, but died away. Here, the oscillation is sustained.

## A closed loop

An oscillator puts two blocks in a loop:

- an **amplifier** with gain A, which supplies the energy;
- a **feedback network** B (often an LC or RC circuit), which picks the frequency and sends part of the output back to the input.

![Oscillator loop: amplifier A, then network B bringing part of the output back to the input](/static/content/electro/en/m9/boucle.svg)

Unlike the negative feedback of amplifiers, which calms the circuit down, here the feedback is **positive**: the returned signal adds to the one already there.

## The two conditions for oscillation

1. **The loop gain** A × B must be at least 1. Network B attenuates (B is smaller than 1); the amplifier must make up for it. Example: a network returning 1/29 of the signal needs A ≥ 29.
2. **The phase**: the signal must come back to the input **in phase**, with a total phase shift of 0° (or 360°). If the amplifier inverts (180°), the network must provide the missing 180°.

Both conditions are met at **only one frequency**: the oscillation frequency.

## Start-up

No input signal is needed. At switch-on, a tiny amount of noise contains every frequency. At the frequency where the loop is in phase, it is amplified on every round trip: it grows as long as A × B is slightly **greater than 1**.

![Start-up: a tiny oscillation grows on every round trip, then its amplitude settles when A × B comes back to 1](/static/content/electro/en/m9/demarrage.svg)

The amplitude does not grow forever: as the transistor nears saturation, its gain drops and A × B falls back to 1. The amplitude settles.

## Key points

- Oscillator = amplifier + feedback network, in a loop.
- Conditions: A × B ≥ 1 and an in-phase return (0° or 360°).
- Noise is enough to start; saturation limits the amplitude.
