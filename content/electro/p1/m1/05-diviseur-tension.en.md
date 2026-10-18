Two resistors in series share the source voltage. By taking the voltage at the midpoint, you get a lower voltage, set by the ratio of the resistors: this is the **voltage divider**, one of the most widely used circuits in electronics.

![Voltage divider: R1 = 10 kΩ at the top, R2 = 4.7 kΩ at the bottom, Vout taken at the midpoint](/static/content/electro/en/m1/diviseur.svg)

## The formula

The same current flows through R1 and R2. The output voltage, taken across R2, is:

**Vout = Vin × R2 / (R1 + R2)**

Example: Vin = 12 V, R1 = 10 kΩ and R2 = 4.7 kΩ. Vout = 12 × 4.7 / 14.7 ≈ **3.84 V**. If R1 = R2, the output is exactly half the input.

[[calc:divider]]

## Watch the load

The formula assumes nothing draws current from the output. If you connect a load resistor RL to Vout, it ends up in parallel with R2 and the voltage drops.

![Divider made of two 10 kΩ resistors loaded by RL = 10 kΩ: Vout falls from 6 V to 4 V](/static/content/electro/en/m1/diviseur-charge.svg)

With R1 = R2 = RL = 10 kΩ on 12 V: unloaded, Vout = 6 V. Loaded, R2 and RL in parallel are worth 5 kΩ, and Vout = 12 × 5 / 15 = **4 V**. Rule of thumb: for the load to disturb the divider only slightly, it should be at least ten times larger than R2.

## Key points

- Vout = Vin × R2 / (R1 + R2), with Vout taken across R2.
- A load on the output sits in parallel with R2 and lowers Vout.
- Keep the load at least ten times larger than R2 to stay accurate.
