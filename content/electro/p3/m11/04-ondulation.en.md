Between two peaks, the capacitor discharges into the load: the voltage falls by an amount **ΔU**, the **residual ripple**. It is simple to calculate.

## The formula

The capacitor alone supplies the load current I for almost the whole time between two peaks, that is 1 / f. The charge it loses is I / f, and its voltage falls by:

**ΔU ≈ I / (f × C)**

with **f = 100 Hz** for full-wave (50 Hz for half-wave).

![Close-up of the smoothed voltage: it swings between 15.6 V and about 13.3 V, a ripple ΔU of about 2.3 V](/static/content/electro/en/m11/ondulation.svg)

Example: I = 0.5 A and C = 2,200 µF, full-wave. ΔU ≈ 0.5 / (100 × 0.0022) ≈ **2.3 V**. The voltage varies between 15.6 V and 13.3 V, and its average is about 15.6 − 2.3 / 2 ≈ **14.5 V**.

[[calc:ripple]]

## Choosing C

Start from the acceptable ripple and turn the formula round:

**C ≈ I / (f × ΔU)**

For 0.5 A and at most 1 V of ripple: C ≈ 0.5 / (100 × 1) = 0.005 F = **5,000 µF**. Take the standard value above or the nearest one: 4,700 µF gives ΔU ≈ 1.1 V.

![Ripple at 0.5 A: 1,000 µF leaves about 5 V of ripple, 4,700 µF about 1.1 V](/static/content/electro/en/m11/condensateurs.svg)

## What the calculation tells you

- The ripple **doubles** if the current doubles.
- It is **halved** if the capacitance is doubled.
- With **half-wave**, f = 50 Hz: for the same ripple, **twice as much** capacitance is needed.

The formula is approximate (it assumes the capacitor discharges for the whole period), but it errs on the safe side: the real ripple is a little smaller.

## Key points

- ΔU ≈ I / (f × C), with f = 100 Hz for full-wave.
- C ≈ I / (f × ΔU) to choose the capacitor.
- Average voltage ≈ peak − ΔU / 2.
