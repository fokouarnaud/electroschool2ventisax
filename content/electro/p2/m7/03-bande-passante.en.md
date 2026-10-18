A resonant circuit does not respond only at f0: it also passes nearby frequencies. Two quantities measure that width: the **bandwidth** and the **quality factor** Q.

![I / Imax curve around 5 kHz: it stays above 0.707 between f1 and f2, a bandwidth of about 796 Hz](/static/content/electro/en/m7/bande.svg)

## Bandwidth

We reuse the filters' threshold: 0.707 of the maximum, that is −3 dB. The two frequencies where the current is 0.707 × Imax are called f1 (below f0) and f2 (above). The **bandwidth** is the gap between them:

**BW = f2 − f1**

Example: f1 = 9.5 kHz and f2 = 10.5 kHz give BW = 1 kHz.

## The Q factor

Q compares the resonant frequency with the bandwidth:

**Q = f0 / BW**   so   **BW = f0 / Q**

For a series RLC circuit, Q can also be calculated from the components: **Q = XL / R**, with XL taken at f0.

Example with this module's circuit: L = 10 mH, C = 100 nF, R = 50 Ω. At f0 ≈ 5,033 Hz, XL ≈ 316 Ω, so Q ≈ 316 / 50 ≈ **6.3**, and BW ≈ 5,033 / 6.3 ≈ **796 Hz**. This gives f1 ≈ 4.65 kHz and f2 ≈ 5.45 kHz.

![Two normalised curves: Q ≈ 6.3 gives a narrow peak, Q ≈ 1.6 a wide one](/static/content/electro/en/m7/q.svg)

## Selective or broad

- **High Q** (small R): narrow bandwidth, the circuit is **selective**. It can tell two close frequencies apart, like two radio stations.
- **Low Q** (large R): wide bandwidth, the circuit accepts a whole range of frequencies.

At resonance, the voltage across L or C is **Q times** the source voltage: with Q = 20 and 1 V at the input, 20 V appear across the capacitor. Choose components that can withstand it.

## Key points

- BW = f2 − f1, measured at 0.707 × Imax.
- Q = f0 / BW; in series RLC, Q = XL / R at f0.
- High Q: selective circuit and large overvoltages across L and C.
