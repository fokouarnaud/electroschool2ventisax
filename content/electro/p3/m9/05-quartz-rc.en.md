LC oscillators suit high frequencies, but they drift a little with temperature and tolerances. Two other families meet other needs: the **crystal** for accuracy, the **RC network** for low frequencies.

## The crystal

A **crystal** is a small slice of quartz that vibrates mechanically when a voltage is applied, at a frequency set by its size and cut. Electrically, it behaves like a resonant circuit with an enormous quality factor.

![Crystal symbol, a slice between two electrodes, with Q ≈ 50,000, compared with an LC circuit with Q ≈ 50](/static/content/electro/en/m9/quartz.svg)

With a Q of several tens of thousands, the bandwidth is tiny: the oscillator can only run at that frequency. Part of a Colpitts' LC network is simply replaced by the crystal.

Examples:

- **32,768 Hz** in watches: that is 2 to the power 15. Dividing by two 15 times gives exactly 1 pulse per second.
- **16 MHz** to clock a microcontroller.

## The Wien-bridge oscillator

From a few hertz to a few hundred kilohertz, inductors become bulky. An **RC** network is used instead: the **Wien bridge**, with a non-inverting op-amp.

![Wien-bridge oscillator: R and C in series from the output to the plus input, R and C in parallel from the plus input to ground, Rf of 20 kΩ and Rin of 10 kΩ on the minus input](/static/content/electro/en/m9/wien.svg)

The network (R and C in series, then R and C in parallel) gives **no phase shift** at a single frequency, where it returns exactly **1/3** of the signal:

**f = 1 / (2π × R × C)**

With R = 10 kΩ and C = 16 nF: f = 1 / (2π × 10,000 × 0.000000016) ≈ **995 Hz**, so about 1 kHz.

The non-inverting op-amp adds no phase shift; it must make up for the 1/3 attenuation, so it needs a gain of at least **3**: Av = 1 + Rf / Rin = 1 + 20 / 10 = 3. In practice the gain is made slightly higher to ensure start-up, then the amplitude is limited (two diodes in parallel across part of Rf, for example).

## Key points

- Crystal: very high Q, very stable frequency (32,768 Hz, 16 MHz…).
- Wien bridge: f = 1 / (2π × R × C), the network returns 1/3 of the signal.
- The Wien-bridge op-amp needs a gain of at least 3.
