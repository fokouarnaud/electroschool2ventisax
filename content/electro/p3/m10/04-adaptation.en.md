A transformer does not only change voltages and currents: it also changes how a load is "seen" from the primary. It is used to **match** a load to a source.

## The impedance reflected to the primary

A load Zs connected to the secondary behaves, seen from the primary, like an impedance:

**Zp = Zs × (Np / Ns)²**

The turns ratio appears **squared**: it acts once on the voltage and once on the current.

![Amplifier connected to the primary of a 10 to 1 transformer, whose secondary feeds an 8 Ω loudspeaker](/static/content/electro/en/m10/adaptation.svg)

Example: an 8 Ω loudspeaker behind a transformer with Np / Ns = 10. Zp = 8 × 10² = **800 Ω**.

![Seen from the primary, the 8 Ω loudspeaker behaves like an 800 Ω resistor](/static/content/electro/en/m10/equivalent.svg)

## Why match?

A source delivers the most power to its load when the load impedance **equals** its own internal impedance. A transistor or valve stage that needs about 800 Ω of load could deliver almost nothing to an 8 Ω loudspeaker connected directly: the transformer resolves this mismatch.

## Choosing the ratio

Use the relation the other way round:

**Np / Ns = √(Zp / Zs)**

Example: to make a 4 Ω load look like 1 kΩ, Np / Ns = √(1,000 / 4) = √250 ≈ **15.8**.

These matching transformers are found in transistor radios, valve amplifiers, public-address lines and antennas (matching a 75 Ω cable to a 300 Ω antenna, for example: a turns ratio of √4 = 2).

## Key points

- Zp = Zs × (Np / Ns)²: the turns ratio acts squared.
- Power transfer is greatest when the impedances are equal.
- Np / Ns = √(Zp / Zs).
