The **Hartley** oscillator is the Colpitts' cousin with the roles swapped. This time it is the **inductor** that is split in two, and a single capacitor closes the resonant circuit.

![Hartley oscillator: below the amplifier, a 2.2 nF capacitor C between two 50 µH inductors L1 and L2 tied to ground](/static/content/electro/en/m9/hartley.svg)

## A tapped inductor

In practice, L1 and L2 are often a single inductor with a **tap** (an intermediate connection) tied to ground. As in the Colpitts, this midpoint puts the two ends in antiphase, and the ratio L1 / L2 sets the share of the signal fed back.

## The frequency

If the two halves do not influence each other (their coupling is neglected), their inductances add up:

**L = L1 + L2**   and   **f = 1 / (2π × √((L1 + L2) × C))**

Example: L1 = L2 = 50 µH, C = 2.2 nF. L = 100 µH and f = 1 / (2π × √(100 µH × 2.2 nF)) ≈ **339 kHz**.

On a real tapped inductor, the coupling between the two halves increases the total inductance a little: the measured frequency is then slightly lower than calculated.

## An easy oscillator to tune

The Hartley has only one capacitor: a single **variable capacitor** is enough to sweep a whole range of frequencies without touching the feedback ratio. It was the local oscillator of many radio receivers.

![Hartley frequency against C, with L1 + L2 = 100 µH: about 712 kHz at 0.5 nF, 339 kHz at 2.2 nF, 225 kHz at 5 nF](/static/content/electro/en/m9/hartley-courbe.svg)

Since f varies as 1 / √C, C must be **quadrupled** to halve the frequency.

## Key points

- Hartley: inductor split in two (L1, L2, tap to ground) and a capacitor C.
- f = 1 / (2π × √((L1 + L2) × C)), coupling neglected.
- A single capacitor: easy to tune with a variable capacitor.
