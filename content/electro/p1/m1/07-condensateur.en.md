A closed **switch** behaves like a wire (almost zero resistance); open, like a break (almost infinite resistance). A **capacitor** is made of two plates separated by an insulator: it stores charge, and its capacitance C is measured in farads (F). In practice you meet microfarads (µF) and nanofarads (nF).

![10 V cell, switch K, 10 kΩ resistor and 100 µF capacitor in series](/static/content/electro/en/m1/rc-circuit.svg)

## Charging through a resistor

When the switch closes, the empty capacitor first behaves like a wire: the current is at its maximum, E / R. Then the voltage Uc across it rises and the current falls. When Uc reaches the cell voltage, the current stops: **in steady state, a capacitor blocks direct current**.

How fast it charges depends on the **time constant**:

**τ = R × C**   (in seconds, with R in ohms and C in farads)

With 10 kΩ and 100 µF: τ = 10,000 × 0.000 1 = **1 s**.

![Charging curve: Uc reaches 63 % of E after τ = 1 s and almost 100 % after 5 s](/static/content/electro/en/m1/rc-courbe.svg)

## Landmarks to remember

- After **τ**, the capacitor is charged to about **63 %**.
- After **5 τ**, it is considered fully charged (over 99 %).

Discharging follows the same logic the other way round. RC circuits are used to create delays, filter out interference or hold back the start of a circuit.

## Key points

- Closed switch: wire; open switch: break.
- With DC, a charged capacitor no longer lets current through.
- τ = R × C; 63 % after τ, charged after 5 τ.
