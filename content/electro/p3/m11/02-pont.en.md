The **diode bridge** (or Graetz bridge) uses four diodes to recover **both half-cycles**: this is **full-wave** rectification.

![Four diodes in a diamond: AC comes in at the top and bottom, load R is connected between + on the right and − on the left](/static/content/electro/en/m11/pont.svg)

## How it works

- During the positive half-cycle, current flows through one diode to the **+** terminal, through the load, then back through the opposite diode.
- During the negative half-cycle, the **other two** diodes conduct, and the current flows through the load **in the same direction**.

At every moment, the current flows through **two diodes** in series. The voltage drop is therefore about 2 × 0.7 = **1.4 V**:

**Umax out ≈ Urms × √2 − 1.4 V**

With 12 V rms: 17 − 1.4 ≈ **15.6 V** peak.

![Full-wave rectification: both half-cycles come out positive, 15.6 V peak, and the voltage repeats every 10 ms](/static/content/electro/en/m11/double.svg)

## A doubled frequency

The rectified voltage now has **two humps per mains period**: it repeats every 10 ms, so at **100 Hz**. For the filter, this is a big advantage: the dips are half as long, so twice as easy to fill in.

## Choosing the diodes

Each diode must withstand:

- the average **current** of the load (a diode from the 1N4001 to 1N4007 family handles 1 A);
- the **reverse voltage** while it blocks, roughly the peak voltage (17 V here). Leave a margin: a 1N4001 withstands 50 V.

Ready-made bridges also exist, in a single package with four legs marked **~**, **~**, **+** and **−**.

Another solution exists: a centre-tapped transformer (previous module) and only two diodes. It also gives full-wave rectification, with a single diode drop, but needs a secondary twice as long.

## Key points

- Four-diode bridge: both half-cycles pass, two diodes conduct at a time.
- Umax out ≈ Urms × √2 − 1.4 V.
- Ripple at 100 Hz instead of 50 Hz.
