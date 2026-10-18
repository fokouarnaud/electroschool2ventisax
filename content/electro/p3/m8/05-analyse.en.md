Before connecting a signal generator, check that an amplifier is properly biased. This **DC analysis** takes a few minutes, first on paper and then with a multimeter.

## The method

For the module's circuit (12 V, R1 = 47 kΩ, R2 = 10 kΩ, RC = 3.9 kΩ, RE ≈ 1 kΩ):

| Step | Calculation | Result |
|---|---|---|
| 1. VB | 12 × 10 / 57 | 2.1 V |
| 2. VE | VB − 0.7 | 1.4 V |
| 3. IC ≈ IE | VE / RE | 1.4 mA |
| 4. VC | 12 − IC × RC | 6.5 V |
| 5. VCE | VC − VE | 5.1 V |

With a multimeter, measure VB, VE and VC with respect to ground: if the difference from the calculation is more than about 10 %, look for a wiring error or a resistor of the wrong value.

## The load line

All the possible operating points of the transistor lie on a straight line, the **load line**, joining:

- **cut-off**: IC = 0, VCE = VCC = 12 V;
- **saturation**: VCE ≈ 0, IC sat = VCC / (RC + RE) = 12 V / 4.9 kΩ ≈ **2.45 mA**.

![Load line from 2.45 mA to 12 V, with the quiescent point Q at 5.1 V and 1.4 mA, near the middle](/static/content/electro/en/m8/droite.svg)

The quiescent point Q (5.1 V; 1.4 mA) is close to the middle: the signal can swing up and down on both sides without hitting a limit.

## Clipping

If the output signal becomes too large, the transistor reaches cut-off on one side or saturation on the other. The sine wave is then **clipped**: its tops are flattened and the sound becomes distorted.

![VCE too large: its peaks are flattened at 12 V (cut-off) and its troughs near 0 V (saturation)](/static/content/electro/en/m8/ecretage.svg)

Here, VC can fall by about 4.9 V (down to VE + 0.2 V) before saturation. The output stays clean up to about **4.9 V peak**, which means an input of at most 4.9 / 39 ≈ **0.13 V peak** with a gain of 39.

A quiescent point too close to saturation or cut-off reduces this margin on one side: clipping then appears even with small signals, on only one half of the sine wave.

## Key points

- DC analysis: VB, VE, IC, VC then VCE, checked with a multimeter.
- Load line: from IC sat = VCC / (RC + RE) to VCE = VCC.
- A quiescent point in the middle gives the largest output without clipping.
