The **Colpitts** oscillator is one of the most widely used up to a few tens of megahertz. Its feedback network is an LC circuit whose capacitor is split in two.

![Colpitts oscillator: below the amplifier, a 100 µH inductor L between two 10 nF capacitors C1 and C2 tied to ground](/static/content/electro/en/m9/colpitts.svg)

## The capacitive divider

Capacitors C1 and C2 are in series in the loop of the resonant circuit, with their common point at ground. They play two roles:

- together with L, they set the **frequency**;
- they form a **divider**: the ratio C1 / C2 sets the share of the signal sent back to the amplifier. Because the midpoint is grounded, the two ends of the LC circuit are in antiphase: the network provides the 180° the inverting amplifier lacks.

## The frequency

Two capacitors in series are equivalent to a single, smaller capacitor **Ceq**:

**Ceq = C1 × C2 / (C1 + C2)**

![Two 10 nF capacitors in series are equivalent to a single 5 nF one](/static/content/electro/en/m9/ceq.svg)

The resonance formula from Part 2 then applies:

**f = 1 / (2π × √(L × Ceq))**

Example: L = 100 µH, C1 = C2 = 10 nF. Ceq = 10 × 10 / 20 = 5 nF, and f = 1 / (2π × √(100 µH × 5 nF)) ≈ **225 kHz**.

To check this result, enter L and Ceq (not C1 or C2) in the calculator:

[[calc:resonance]]

## Adjusting the frequency

The frequency is changed by changing L (an inductor with an adjustable core) or the capacitors. To keep the same feedback ratio, C1 and C2 are changed together, or a small variable capacitor is added across L.

## Key points

- Colpitts: inductor L and a capacitive divider C1, C2 with a grounded midpoint.
- Ceq = C1 × C2 / (C1 + C2); f = 1 / (2π × √(L × Ceq)).
- The ratio C1 / C2 sets the share of the signal fed back.
