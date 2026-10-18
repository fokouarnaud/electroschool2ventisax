An ordinary reverse-biased diode eventually gives way if the voltage gets too high: this is **breakdown**, often destructive. The **Zener diode** is designed to work precisely in that region, without damage, at an exact voltage called the **Zener voltage** (Vz): 3.3 V, 5.1 V, 12 V…

![Characteristic of a 5.1 V Zener: forward conduction near 0.7 V and sharp reverse conduction at 5.1 V](/static/content/electro/en/m2/zener-courbe.svg)

## A voltage that stays put

Forward-biased, a Zener behaves like a normal diode. Reverse-biased, it blocks up to Vz, then conducts while keeping an almost constant voltage across it, even when the current varies a lot. This property makes it a simple **voltage regulator**.

It is always fitted **in reverse**: cathode on the positive side.

![12 V battery, 330 Ω series resistor, 5.1 V Zener and load RL in parallel](/static/content/electro/en/m2/zener-regulateur.svg)

## Sizing the series resistor

The resistor R takes up the difference between the input voltage and Vz, and limits the current:

**I = (E − Vz) / R**

Example: E = 12 V, Vz = 5.1 V, R = 330 Ω. I = 6.9 / 330 ≈ **21 mA**. This current is shared between the Zener and the load. As long as the load takes less than 21 mA, the Zener holds its output at 5.1 V, even if the battery wears down to 10 V.

Check the Zener's power: with no load, it takes all the current, that is 5.1 × 0.021 ≈ 0.11 W. A 0.5 W part leaves a comfortable margin.

## Key points

- The Zener is fitted in reverse and holds Vz across it.
- A series resistor is required: I = (E − Vz) / R.
- The load current must stay below that current.
