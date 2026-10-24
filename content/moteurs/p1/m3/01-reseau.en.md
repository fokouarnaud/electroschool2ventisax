The energy that turns a factory motor has often travelled hundreds of kilometres. Its voltage changes several times on the way.

![From power plant to factory: generation, transmission at 400 kV, primary substation, distribution at 20 kV, HV/LV substation, 400 V at the factory](/static/content/moteurs/en/m3/chaine.svg)

1. The **power plant** generates, for example at 20 kV.
2. A transformer steps the voltage up for **transmission** at extra-high voltage (225 or 400 kV).
3. The **primary substation** steps it down for **distribution** at HV-A, often 20 kV.
4. An **HV/LV substation**, at the end of a street or inside the factory itself, steps it down to **400 V line-to-line** (230 V line-to-neutral): the motors' voltage.

## Why raise the voltage?

For the same power, the current is lower when the voltage is higher: in three-phase, I = P / (√3 × U). Yet cable losses equal **3 × R × I²**: they vary with the square of the current.

![Line losses to carry 100 kW with 0.1 Ω per conductor: 6.25 kW at 400 V, 2.5 W at 20 kV](/static/content/moteurs/en/m3/pertes-ligne.svg)

**Example.** Carrying 100 kW over a line of 0.1 Ω per conductor:

- at 400 V: I = 100,000 / (1.732 × 400) = 144 A, losses = 3 × 0.1 × 144² ≈ **6.25 kW**;
- at 20 kV: I = 2.89 A, losses = 3 × 0.1 × 2.89² ≈ **2.5 W**.

A voltage 50 times higher divides the losses by 50² = 2,500. That is why power is carried at high voltage and stepped down only close to the users.

## Key points

- Generation, transmission (EHV), distribution (HV-A), then 400 V at the HV/LV substation.
- I = P / (√3 × U); losses = 3 × R × I².
- Multiplying the voltage by k divides the losses by k².
