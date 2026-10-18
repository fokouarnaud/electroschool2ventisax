When a current reaches a **node**, a point where several wires meet, it splits between the branches. Nothing is lost: the sum of the currents entering a node equals the sum of the currents leaving it. This is the **current law** (Kirchhoff's current law).

![Current I splitting into I1, I2 and I3 between three branches](/static/content/electro/en/m1/trois-branches.svg)

## Which branch takes most current?

Parallel branches share the same voltage U. Each one therefore carries I = U / R: **the branch with the lowest resistance takes the most current**. Current prefers the easiest path, without ignoring the others.

For two branches, the split can be written directly:

**I1 = I × R2 / (R1 + R2)**   and   **I2 = I × R1 / (R1 + R2)**

Notice the swap: the current in R1 depends on R2, and the other way round.

![6 V cell, 1 kΩ and 2 kΩ in parallel: I = 9 mA splits into 6 mA and 3 mA](/static/content/electro/en/m1/diviseur-courant.svg)

## Example

A 6 V cell feeds 1 kΩ and 2 kΩ in parallel. Work out each branch with Ohm's law: I1 = 6 / 1 = **6 mA** and I2 = 6 / 2 = **3 mA**. The cell supplies I = 6 + 3 = 9 mA. Check with the formula: I1 = 9 × 2 / 3 = 6 mA.

Calculating branch by branch is often the safest way: it avoids putting the wrong resistor on top of the fraction.

## Key points

- Current law: the sum of incoming currents equals the sum of outgoing currents.
- In parallel, the branch with the lowest resistance takes the most current.
- I1 = I × R2 / (R1 + R2): the top of the fraction is the other resistor.
