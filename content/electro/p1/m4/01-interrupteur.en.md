In the previous module, the transistor amplified. Here, we only use its two extreme regions: **cut-off** and **saturation**. It then becomes a **controlled switch**: a small base current turns on or off a load that draws much more.

![NPN transistor: the lamp is in the collector, switch K and RB drive the base](/static/content/electro/en/m4/interrupteur.svg)

## The two states

- **Cut off**: no base current. The transistor does not conduct, IC = 0 and the whole of VCC appears between collector and emitter. The lamp is off, as with an open switch.
- **Saturated**: enough base current. VCE falls to about 0.2 V and the lamp gets almost all the voltage. It lights up, as with a closed switch.

![Cut-off compared with saturation: open switch and lamp off, closed switch and lamp on](/static/content/electro/en/m4/bloque-sature.svg)

## Why not stay in between?

In both extreme states, the transistor stays fairly cool: cut off, no current flows through it; saturated, the voltage across it is very low. The power it dissipates is VCE × IC. In the linear region, both VCE and IC are large and the transistor heats up: switching must therefore be **clean**, without lingering in between.

Example: a 9 V, 100 mA lamp. Saturated, the transistor dissipates 0.2 × 0.1 = 0.02 W. Halfway, with 4.5 V and 50 mA, it would dissipate 0.225 W, more than ten times as much.

## Why a transistor rather than a real switch?

Because the control can come from a circuit that only supplies a few milliamperes: a microcontroller output, a sensor, a logic gate. The transistor links this weak signal to a demanding load.

## Key points

- Switching: cut off (open switch) or saturated (closed switch).
- Saturated, VCE ≈ 0.2 V: the transistor stays cool.
- Avoid the in-between region, which heats the transistor.
