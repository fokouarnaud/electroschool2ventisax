Put a resistor R and a capacitor of reactance Xc in series. The current is the same everywhere in the loop. But the voltage across R is in phase with that current, while the capacitor's voltage is shifted by 90°. So the two voltages do not peak at the same moment.

![Series RC circuit under 10 V with R = Xc = 1 kΩ: Ur ≈ 7.07 V, Uc ≈ 7.07 V and I ≈ 7.07 mA](/static/content/electro/en/m6/rc-serie.svg)

## Impedance

The circuit's total opposition to AC is called its **impedance** Z, in ohms. Since R and Xc act at 90° to each other, they combine like the sides of a right-angled triangle:

**Z = √(R² + Xc²)**   then   **Irms = Urms / Z**

![Impedance triangle: R horizontal, Xc vertical, Z on the hypotenuse, φ = 45° when R = Xc](/static/content/electro/en/m6/triangle-z.svg)

Example: R = 1 kΩ and Xc = 1 kΩ, under 10 V RMS.

- Z = √(1,000² + 1,000²) ≈ **1,414 Ω**, not 2,000 Ω.
- I = 10 / 1,414 ≈ **7.07 mA**.
- Ur = R × I ≈ 7.07 V and Uc = Xc × I ≈ 7.07 V.

## The voltages do not simply add up

7.07 V + 7.07 V make 14.14 V, more than the source's 10 V! This is not a mistake: the two voltages are shifted in time. Their RMS values also combine by Pythagoras:

**Ue = √(Ur² + Uc²)**: √(7.07² + 7.07²) ≈ 10 V.

With a multimeter you will therefore measure Ur + Uc greater than Ue: that is normal in an RC circuit.

## Key points

- Z = √(R² + Xc²); I = U / Z.
- In series RC, Ue = √(Ur² + Uc²), not Ur + Uc.
