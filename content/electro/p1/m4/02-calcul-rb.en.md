For a transistor to saturate reliably, it must get **enough** base current, even with the part that has the lowest gain. The method fits in four steps.

![5 V control, RB to be calculated, 100 Ω load in the collector, VCC = 9 V](/static/content/electro/en/m4/calcul-rb.svg)

## The method

1. **Saturation current** of the load: IC sat = (VCC − 0.2) / RC.
2. **Minimum base current** with the datasheet's minimum gain: IB min = IC sat / β min.
3. **Safety margin**: take IB = 2 × IB min (some designers go up to 5 or 10 times).
4. **Base resistor**: RB = (Vin − 0.7) / IB, then the **lower** standard value.

## Example

VCC = 9 V, load RC = 100 Ω, control Vin = 5 V, β min = 100.

1. IC sat = (9 − 0.2) / 100 = **88 mA**.
2. IB min = 88 mA / 100 = 0.88 mA.
3. IB = 2 × 0.88 = **1.76 mA**.
4. RB = (5 − 0.7) / 1.76 mA ≈ **2.44 kΩ**, so 2.2 kΩ as a standard value.

We take the lower value because a smaller resistor gives **more** base current, hence an even safer saturation.

![IC against IB: the current levels off at 88 mA from 880 µA, the margin doubles that base current](/static/content/electro/en/m4/saturation-courbe.svg)

## What if you overdo it?

Beyond saturation, raising IB no longer raises IC: the curve levels off. Too much base current is useless and needlessly loads the control circuit. Also check that the control circuit can supply IB: a microcontroller output generally handles twenty or so milliamperes at most.

## Key points

- IC sat = (VCC − 0.2) / RC; IB min = IC sat / β min.
- Margin: IB = 2 × IB min at least.
- RB = (Vin − 0.7) / IB, then the lower standard value.
