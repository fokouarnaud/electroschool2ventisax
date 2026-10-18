Designing a simple LC oscillator takes four steps. Troubleshooting one is mostly a matter of method.

![Four steps: choose f, choose L and calculate C, check the loop gain and the phase, measure and adjust](/static/content/electro/en/m9/procedure.svg)

## Design

1. **Choose the frequency** f you want.
2. **Choose L** from the values available, then **calculate C**: C = 1 / (4π² × f² × L).
3. **Check the loop**: the amplifier must have enough gain to make up for the network (A × B ≥ 1), and the phase must come back to 0°.
4. **Measure and adjust**: components have tolerances (often 5 to 10 %), so C or L is trimmed.

Example: you want 100 kHz with a 100 µH inductor. C = 1 / (4π² × 100,000² × 0.0001) ≈ **25.3 nF**. For a Colpitts, this is Ceq: with C1 = C2, each is twice as large, about 51 nF. With two standard 47 nF capacitors, Ceq = 23.5 nF and f ≈ 104 kHz, close enough.

[[calc:resonance]]

## Measuring the frequency

On an oscilloscope, read the period on the screen, then f = 1 / T. A frequency counter (or the Hz function of some multimeters) gives the value directly.

![Oscilloscope screen: one period spans 4 divisions at 0.25 ms per division, so T = 1 ms and f = 1 kHz](/static/content/electro/en/m9/ecran.svg)

## Troubleshooting: the checklist

When an oscillator will not start, check in this order:

1. **The power supply**: is the voltage present on the circuit?
2. **The bias**: without oscillation, is the transistor in its linear region (VCE around half of VCC)?
3. **The phase**: is the network wired correctly? For an Armstrong, is the feedback winding the right way round?
4. **The gain**: is it enough? Too heavy a load on the output can pull A × B below 1.
5. **The frequency**: if the oscillator runs at the wrong frequency, check the values of L and C.

An oscilloscope probe also adds a small capacitance: connecting it can shift the frequency of an LC oscillator, or even stop it. Measure after a buffer stage when possible.

## Key points

- C = 1 / (4π² × f² × L); adjust after measuring.
- Troubleshooting: supply, bias, phase, gain, then the values of L and C.
- The measuring probe can disturb the oscillator.
