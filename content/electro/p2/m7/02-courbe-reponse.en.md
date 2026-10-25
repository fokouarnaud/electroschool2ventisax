Sweep the generator's frequency while keeping the same voltage, and measure the current in the series RLC circuit. This gives its **response curve**.

![Current in the series RLC under 1 V: small at low and high frequencies, it peaks at 20 mA at f0 ≈ 5 kHz](/static/content/electro/en/m7/courbe-i.svg)

## A bell-shaped curve

- **Well below f0**, XC is large: the current is small.
- **At f0**, XL and XC cancel: the current reaches its maximum Imax = U / R.
- **Well above f0**, XL is large: the current becomes small again.

In practice, you often watch the voltage across R rather than the current: since Ur = R × I, it has exactly the same shape, and the oscilloscope measures it directly.

## The effect of resistance

Only R limits the current at resonance. What happens if it is increased?

![Two curves: with R = 50 Ω the peak rises to 20 mA and stays narrow; with R = 200 Ω it stays below 5 mA and spreads out](/static/content/electro/en/m7/courbe-r.svg)

- The peak **gets lower**: Imax = U / R falls (5 mA instead of 20 mA under 1 V).
- The peak **gets wider**: the circuit responds to a wider range of frequencies.
- The resonant frequency **does not change**: f0 depends only on L and C.

Every loss counts as resistance: the inductor's wire resistance, the source's, the load's.

## What happens in the circuit

The two circuits on the desk have the same inductor and the same capacitor; only R changes. Far from f0, the leftover reactance |XL − XC| limits the current, and it is the same for both: at f0 / 2 it is 474 Ω, and the currents are close (2.10 mA with 50 Ω, 1.94 mA with 200 Ω). Closer to f0, that reactance melts away and only R is left: the current climbs to U / R, that is 20 mA with 50 Ω but only 5 mA with 200 Ω.

That is why the 50 Ω peak is tall and narrow: it only stands out right next to f0. The 200 Ω peak, low and wide, stays close to its maximum over a wider range of frequencies. Both tops fall on the same dashed line, f0. Sweep the frequencies and follow the two pens.

[[fig:rlc_response]]

## Key points

- The response curve of a series RLC is bell-shaped, centred on f0.
- Increasing R lowers and widens the peak without moving f0.
