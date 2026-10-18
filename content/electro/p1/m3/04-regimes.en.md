Depending on the base current it receives, a transistor works in one of three **regions**.

![Family of IC against VCE curves for three base currents, with the saturation, linear and cut-off regions](/static/content/electro/en/m3/regimes.svg)

## Cut-off

If IB = 0 (base not driven or VBE below about 0.6 V), the transistor does not conduct: **IC ≈ 0**. It behaves like an open switch, and VCE ≈ VCC.

## The linear region

For a moderate base current, IC = β × IB, almost regardless of VCE: the curves are nearly flat. This is the **amplification** region: a small change in IB produces a large change in IC.

## Saturation

If IB is increased further, the collector circuit can no longer supply β × IB: the collector resistor "takes" almost all the voltage. VCE falls to about **0.2 V** and IC is set by the rest of the circuit: IC sat ≈ VCC / RC. The transistor behaves like a closed switch.

## The load line

The collector circuit imposes a simple relation, VCE = VCC − RC × IC, which plots as a straight line on the curve family. Where it crosses the curve of the chosen base current gives the **operating point** Q.

![Load line for VCC = 12 V and RC = 1 kΩ, and quiescent point Q at 6 V and 6 mA](/static/content/electro/en/m3/droite-charge.svg)

With VCC = 12 V and RC = 1 kΩ, the line runs from 12 mA (VCE = 0) to 12 V (IC = 0). A point Q in the middle, around 6 V, leaves the most room for amplification.

## Key points

- Cut-off: IB = 0, IC = 0, open switch.
- Linear: IC = β × IB, amplification.
- Saturation: VCE ≈ 0.2 V, IC ≈ VCC / RC, closed switch.
