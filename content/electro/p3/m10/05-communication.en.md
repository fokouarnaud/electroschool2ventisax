In communication electronics, the transformer does much more than step a voltage down. Three uses keep coming up.

## Tuning

A capacitor placed across a winding forms a resonant circuit with it: the transformer then passes only the frequencies close to its resonance. Radio receivers use **IF transformers** (intermediate frequency) in this way, often tuned to **455 kHz**, housed in small metal cans with an adjustable core.

![Tuned transformer: one capacitor across the primary, another across the secondary, tuned to 455 kHz](/static/content/electro/en/m10/fi.svg)

The calculation is the one from Part 2: C = 1 / (4π² × f² × L). With a 680 µH winding, C = 1 / (4π² × 455,000² × 0.00068) ≈ **180 pF** is needed to tune to 455 kHz.

These tuned transformers link the stages of a receiver: they pass the wanted station, reject its neighbours and match impedances from one stage to the next.

## Galvanic isolation

The secondary has **no electrical connection** with the primary: only the magnetic flux links them. This is called **galvanic isolation**.

![Galvanic isolation: primary connected to 230 V, secondary connected to the circuit ground, with no electrical connection between them](/static/content/electro/en/m10/isolement.svg)

- **Safety**: the circuit fed by the secondary is not connected to the mains. This is the principle behind toy power supplies, doorbells and the isolating transformers of repair workshops.
- **Ground loops**: a transformer placed on an audio or telephone line breaks the path of stray currents between two devices and removes the 50 Hz hum.

## The centre tap

A secondary with a **centre tap** delivers two equal and opposite voltages, for example 2 × 12 V. Tied to ground, this tap makes it possible to build a symmetrical ±12 V supply for op-amps, or a two-diode full-wave rectifier (see the next module).

## Key points

- A capacitor across a winding tunes the transformer (455 kHz IF).
- Galvanic isolation: no electrical connection between primary and secondary.
- The centre tap gives two symmetrical voltages.
