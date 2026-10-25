Now place the inductor and the capacitor **side by side**, in parallel. This circuit is often called a **tank circuit** (or rejector), because it blocks the way at its resonant frequency.

![AC source, 10 kΩ series resistor, then a 10 mH inductor and a 100 nF capacitor in parallel](/static/content/electro/en/m7/lc-parallele.svg)

## The same resonant frequency

Resonance still happens when XL = XC, so at the same frequency as the series circuit (ideal components):

**f0 = 1 / (2π × √(L × C))**

With 10 mH and 100 nF, f0 ≈ 5 kHz; with 10 mH and 10 nF, f0 ≈ 15.9 kHz.

## The opposite behaviour

- **Far from f0**, one of the two branches has a low reactance (C at high frequencies, L at low ones): it shorts the circuit, so the impedance is low.
- **At f0**, the currents in L and in C are equal and opposite: they circulate between the inductor and the capacitor without going through the source. Seen from outside, the impedance is **at its maximum** and the current drawn from the source is **at its minimum**.

![Impedance of a 10 mH (with 10 Ω of losses) and 100 nF tank: low everywhere except around f0, where it climbs towards 10 kΩ](/static/content/electro/en/m7/z-parallele.svg)

This is the opposite of the series circuit, whose impedance is at its minimum at f0.

| At resonance | Series circuit | Parallel circuit |
|---|---|---|
| Impedance | minimum (Z = R) | maximum |
| Source current | maximum | minimum |

## What happens in the circuit

On the bench below, the Rs = 10 kΩ valve feeds the tank; the line flow meter and the flywheel mark share the same scale. At f0 / 2, the inductor lets almost everything through: the tank is only 211 Ω, the voltage across it falls to 0.021 × Vin and the line current, 99.8 µA, is almost that of Rs alone. At 2 × f0, the bell shorts the tank instead, with the same result.

At f0, the water pushed into the inductor comes back through the bell, then sets off again: 1.58 mA swing back and forth between L and C, while the line only supplies 50.0 µA, thirty times less, just enough to make up for the inductor's 10 Ω of losses. The tank is then 10 kΩ, as much as Rs: half the input voltage appears across it (Vt ≈ 0.500 × Vin).

[[fig:lc_tank]]

## What is a tank circuit for?

Fed through a resistor, a tank circuit has a voltage across it that is **largest at f0** and small elsewhere. So it **selects** one frequency: it is the heart of radio receivers' tuning circuits, and of Part 3's oscillators.

## Key points

- Parallel LC: same f0 as series LC.
- At f0, maximum impedance and minimum source current.
- Fed through R, the tank circuit keeps the frequency f0.
