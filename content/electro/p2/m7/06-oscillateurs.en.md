An LC circuit does more than respond to one frequency: charged just once, it starts to **oscillate on its own** at its resonant frequency. This is the principle of oscillators, studied in Part 3.

![Two states of an LC circuit: the charged capacitor stores electric energy, then the inductor carrying the maximum current stores magnetic energy](/static/content/electro/en/m7/echange.svg)

## An exchange of energy

Charge a capacitor, then connect it to an inductor:

1. The capacitor discharges into the inductor. Its **electric energy** moves into the inductor's magnetic field: when it is empty, the current is at its maximum and all the energy is **magnetic**.
2. The inductor opposes the fall of the current: it keeps pushing it and charges the capacitor again **the other way round**.
3. The cycle starts again in the other direction, then again, at the frequency f0 = 1 / (2π × √(L × C)).

You can compare this back-and-forth to a swing: the energy moves from height (the capacitor) to speed (the inductor) and back.

## Oscillations that die away

In a real circuit, the inductor's wire and the connections have a resistance that turns part of the energy into heat on every swing. The oscillation keeps its frequency, but its amplitude falls: it is a **damped oscillation**.

![Damped oscillation: the sine wave keeps its period but its amplitude shrinks, following an envelope that tends to zero](/static/content/electro/en/m7/amortie.svg)

The higher the Q factor (low losses), the longer the oscillation lasts.

## Sustaining the oscillation

To get a permanent sine wave, the **energy lost** on each cycle must be **given back** to the circuit at the right moment, just as you push a swing at the right time. That job goes to an **amplifier** (a transistor) that feeds part of the signal back: the result is an **oscillator**. Amplifiers and oscillators are covered in Part 3.

## Key points

- In an LC circuit, energy moves from the capacitor to the inductor and back, at frequency f0.
- Losses damp the oscillation.
- An oscillator makes up for these losses with an amplifier.
