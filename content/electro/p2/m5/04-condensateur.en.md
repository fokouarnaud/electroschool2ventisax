In DC, a charged capacitor blocks the current (Part 1, module 1). In AC, the voltage keeps changing: the capacitor charges, discharges and charges again the other way. So a current flows in the circuit all the time.

![10 V RMS source, ammeter and 1 µF capacitor: an alternating current flows](/static/content/electro/en/m5/c-circuit.svg)

## Capacitive reactance

The capacitor opposes AC to a greater or lesser extent. This opposition is called **capacitive reactance** Xc, in ohms:

**Xc = 1 / (2π × f × C)**   (f in hertz, C in farads)

Example: C = 1 µF at 50 Hz. Xc = 1 / (2 × 3.14 × 50 × 0.000001) ≈ **3,183 Ω**, about 3.18 kΩ. At 1 kHz, the same capacitance shows only **159 Ω**.

![Xc curve for 1 µF: very large at low frequencies, it falls as the frequency rises](/static/content/electro/en/m5/xc-courbe.svg)

Remember the trend: **as f rises, Xc falls**. If the frequency doubles, Xc is halved. In DC (f = 0), Xc becomes infinite: the capacitor blocks again.

Reactance is used like a resistance in Ohm's law: **Irms = Urms / Xc**. Under 10 V RMS at 50 Hz, the 1 µF capacitor passes 10 / 3,183 ≈ 3.14 mA.

[[calc:reactance]]

## Current leads

The current is largest when the voltage changes fastest, that is when it crosses zero. As a result, in a capacitor **the current leads the voltage by a quarter of a period (90°)**.

![In a capacitor, the current curve peaks a quarter of a period before the voltage curve](/static/content/electro/en/m5/c-phase.svg)

## Key points

- Xc = 1 / (2π × f × C); Xc falls when f or C rises.
- Irms = Urms / Xc.
- In a capacitor, i leads u by 90°.
- In AC, only use **non-polarised** capacitors (ceramic, film): an electrolytic capacitor connected the wrong way round can heat up and burst.
