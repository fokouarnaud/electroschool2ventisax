Put a resistor, an inductor and a capacitor in series: this is the **series RLC** circuit. The inductor and the capacitor behave in opposite ways, and that is what makes this circuit special.

![Series RLC circuit fed with 1 V: R = 50 Ω, L = 10 mH, C = 100 nF](/static/content/electro/en/m7/rlc-serie.svg)

## XL and XC cancel out

As the frequency rises, XL goes up and XC goes down. Their effects are opposite: the inductor delays the current, the capacitor advances it. In the circuit, their reactances subtract:

**Z = √(R² + (XL − XC)²)**

![XL rises and XC falls with frequency; the two curves cross at f0 ≈ 5 kHz, where XL = XC ≈ 316 Ω](/static/content/electro/en/m7/xl-xc.svg)

There is a frequency where **XL = XC**: the two reactances cancel, leaving only R. This is the **resonant frequency** f0.

## The formula for f0

Writing 2π × f × L = 1 / (2π × f × C) gives:

**f0 = 1 / (2π × √(L × C))**

Example: L = 10 mH and C = 100 nF. L × C = 0.01 × 0.0000001 = 10⁻⁹; √(10⁻⁹) ≈ 0.0000316. f0 = 1 / (2 × 3.14 × 0.0000316) ≈ **5,033 Hz**. At this frequency, XL = XC ≈ 316 Ω.

[[calc:resonance]]

## What happens at resonance

- The impedance is **at its minimum**: Z = R.
- The current is **at its maximum**: I = U / R. Under 1 V with R = 50 Ω: I = 20 mA.
- The voltages across L and across C can be far larger than the source's (here 316 × 0.02 ≈ 6.3 V for a 1 V input), because they cancel each other out.
- Below f0, XC dominates: the circuit is **capacitive**. Above, XL dominates: it is **inductive**.

On the bench below, the three parts are in series: the same flow goes through the valve, the wheel and the bell, and the flow meter measures it. At f0 / 2, the bell dominates (XC = 632 Ω, XL = 158 Ω): the current is only 2.10 mA and it leads Vin. At 2 × f0, the flywheel dominates (XL = 632 Ω): 2.10 mA again, this time lagging. At f0, the inertia of the flywheel and the springiness of the membrane balance out: the needle reaches full scale, I = 20 mA.

Vc and VL are then 6.32 V each for a 1 V input, but they are opposite: they cancel at every instant, and the source only supplies the voltage lost in R (50 Ω × 20 mA = 1 V).

[[fig:lc_resonance]]

## Key points

- f0 = 1 / (2π × √(L × C)): at f0, XL = XC.
- At series resonance: Z = R at its minimum, I = U / R at its maximum.
