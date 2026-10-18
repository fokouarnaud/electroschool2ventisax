An **inductor** (or coil) is a wound wire, often around a core. Its inductance L is measured in henries (H); you mostly meet millihenries (mH) and microhenries (µH). In DC, an ideal inductor is just a wire: it lets the current through without opposition.

![10 V RMS source, ammeter and 100 mH inductor](/static/content/electro/en/m5/l-circuit.svg)

## Inductive reactance

In AC, the inductor builds a magnetic field that opposes any change in current. That opposition is the **inductive reactance** XL, in ohms:

**XL = 2π × f × L**   (f in hertz, L in henries)

Example: L = 100 mH. At 50 Hz, XL = 2 × 3.14 × 50 × 0.1 ≈ **31.4 Ω**. At 1 kHz, XL ≈ **628 Ω**.

![XL line for 100 mH: 31.4 Ω at 50 Hz, 314 Ω at 500 Hz, rising with frequency](/static/content/electro/en/m5/xl-courbe.svg)

It is the opposite of the capacitor: **as f rises, XL rises**. Under 10 V RMS at 1 kHz, the 100 mH inductor passes 10 / 628 ≈ 15.9 mA.

[[calc:reactance]]

## Current lags

The inductor slows down changes of current: the current peaks **a quarter of a period after** the voltage. In an inductor, **the current lags the voltage by 90°**.

![In an inductor, the current curve peaks a quarter of a period after the voltage curve](/static/content/electro/en/m5/l-phase.svg)

A real inductor also has the resistance of its wire, which an ohmmeter can measure. It is usually small compared with XL at working frequencies.

## Key points

- XL = 2π × f × L; XL rises with f and with L.
- In DC, an ideal inductor behaves like a wire.
- In an inductor, i lags u by 90°.
