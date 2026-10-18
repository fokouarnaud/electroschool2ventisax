A transistor can also be driven by a **sensor** rather than a switch. The clearest example is the **light dependent resistor** (LDR), whose resistance changes with light.

![An LDR's resistance falls as the light increases: high in dim light, low in full light](/static/content/electro/en/m4/ldr-courbe.svg)

## A resistance that depends on light

In the dark, a common LDR often exceeds 100 kΩ; in full light, it drops to a few hundred ohms. This change is not measured directly: it is placed in a **voltage divider** (module 1), which turns it into a voltage.

## The lamp that lights up at night

A fixed resistor R1 goes at the top and the LDR at the bottom. The midpoint drives the transistor's base.

![10 kΩ R1 at the top, LDR at the bottom, midpoint connected to the base; the lamp is in the collector](/static/content/electro/en/m4/ldr.svg)

- **In daylight**, the LDR is low: the midpoint voltage stays below 0.6 V. The transistor is cut off, the lamp is off.
- **At night**, the LDR becomes large: the midpoint voltage rises above 0.7 V, a base current flows and the transistor saturates. The lamp lights up.

Example: R1 = 10 kΩ, VCC = 9 V. By day, LDR = 500 Ω: the divider voltage is 9 × 0.5 / 10.5 ≈ 0.43 V, below the threshold. At night, LDR = 100 kΩ: unloaded, it would rise to 8.2 V; in reality the base-emitter junction holds it near 0.7 V and the excess becomes base current.

## Setting the threshold

To choose the light level at which the lamp turns on, R1 is replaced by an **adjustable resistor** (potentiometer) in series with a small fixed resistor that protects the base. Swapping the LDR and R1 reverses the behaviour: the lamp then lights up in the light.

## Key points

- LDR: high resistance in the dark, low in the light.
- The voltage divider turns the change in resistance into a change in voltage.
- The base turns on above about 0.7 V; a trimmer sets the threshold.
