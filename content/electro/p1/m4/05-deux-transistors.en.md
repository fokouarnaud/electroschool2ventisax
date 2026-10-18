When one transistor is not enough, two are combined. Two circuits are worth knowing.

## The Darlington: multiplying the gain

The emitter of the first transistor feeds the base of the second directly, and both collectors are joined. The output current of the first becomes the base current of the second: the gains **multiply**.

**total β ≈ β1 × β2**

![Darlington pair: the emitter of the first transistor drives the base of the second, collectors joined](/static/content/electro/en/m4/darlington.svg)

With two transistors of gain 100, the total gain reaches about 10,000: a base current of 50 µA is then enough to control 500 mA. The Darlington is used to drive heavy loads (motors, LED strips) from a very weak signal.

It has two drawbacks:

- the total base-emitter voltage doubles, about **1.4 V** (two junctions in series);
- when saturated, its collector-emitter voltage stays around **0.7 to 1 V**, more than a single transistor: it runs hotter.

Ready-made Darlingtons also exist in a single package (the TIP120, for example).

## Two cascaded stages: inverting the control

In the second circuit, the collector of the first transistor drives the base of the second. When the first conducts, it pulls its collector towards 0 V and starves the second of base current: the second turns off. When the first is off, the second saturates.

![Two stages: the collector of the first transistor drives the base of the second, which lights the lamp](/static/content/electro/en/m4/cascade.svg)

This circuit **inverts** the logic. With the light sensor from the previous section, for example, it lets you turn a lamp on in daylight rather than at night without rearranging the divider.

## Key points

- Darlington: total β ≈ β1 × β2, VBE ≈ 1.4 V, higher VCE sat.
- Two cascaded stages: the second does the opposite of the first.
- Pick the circuit according to the need: more gain, or inverted logic.
