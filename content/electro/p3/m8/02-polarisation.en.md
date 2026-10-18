To amplify a signal that goes up and down, the transistor must already conduct a little at rest, well inside its linear region. This rest setting is called **biasing** and it sets the **quiescent point** (IC, VCE).

## The problem with a base resistor alone

In Part 1, a single resistor RB set the base current. But IC = β × IB, and β varies a lot: from 100 to 300 for the same part number, and it changes with temperature. With IB = 13 µA, one transistor gives 1.3 mA, the next one 3.9 mA: the second one saturates. The circuit depends on whichever transistor you happen to pick.

## The base divider and the emitter resistor

The usual solution uses a **voltage divider** R1, R2 on the base and an **emitter resistor** RE.

![Circuit biased by a base divider: R1 of 47 kΩ and R2 of 10 kΩ set VB, RC of 3.9 kΩ at the collector, RE of 1 kΩ at the emitter, on 12 V](/static/content/electro/en/m8/pont.svg)

The calculation takes four steps, with VCC = 12 V, R1 = 47 kΩ, R2 = 10 kΩ, RC = 3.9 kΩ and RE = 1 kΩ:

1. Base voltage (voltage divider): VB = 12 × 10 / (47 + 10) ≈ **2.1 V**.
2. Emitter voltage, 0.7 V lower: VE ≈ 2.1 − 0.7 = **1.4 V**.
3. Emitter current: IE = VE / RE ≈ 1.4 V / 1 kΩ = **1.4 mA**, and IC ≈ IE.
4. Collector-emitter voltage: VCE = VCC − IC × (RC + RE) ≈ 12 − 1.4 mA × 4.9 kΩ ≈ **5.1 V**.

β appears in none of these lines: the quiescent point no longer depends on the transistor.

![IC against β: with RB only, IC climbs up to saturation; with the divider and RE, it stays close to 1.3 to 1.4 mA](/static/content/electro/en/m8/beta.svg)

## Why it works

If IC rises (a "stronger" transistor, or heat), VE = IE × RE rises too. Since VB is held by the divider, VBE drops, which reduces the base current: the circuit corrects itself. This is **negative feedback**.

For VB to stay well fixed, the divider current must be large compared with IB. Rule of thumb: **R2 ≤ β × RE / 10**. Here, with β = 100: 10 kΩ ≤ 100 × 1 kΩ / 10 = 10 kΩ, the rule holds.

## Key points

- Biasing sets the quiescent point (IC, VCE) in the middle of the useful range.
- Base divider + RE: VB from the divider, VE = VB − 0.7 V, IC ≈ VE / RE.
- The quiescent point hardly depends on β any more.
