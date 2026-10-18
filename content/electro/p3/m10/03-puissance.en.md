A real transformer warms up a little: part of the power drawn by the primary never reaches the secondary.

## The power balance

- **Pp**: power drawn by the primary.
- **Ps**: power delivered by the secondary, Ps = Us × Is for a resistive load.
- **Losses**: Pp − Ps, turned into heat.

**Efficiency** compares what comes out with what goes in:

**η = Ps / Pp**

![Balance: 14 W go into the primary, 12 W come out of the secondary, 2 W of iron and copper losses; efficiency about 86 %](/static/content/electro/en/m10/bilan.svg)

Example: a transformer delivers 12 V and 1 A, so Ps = 12 W, and draws Pp = 14 W. η = 12 / 14 ≈ **86 %**. The remaining 2 W heat the transformer.

## Where do the losses come from?

- **Copper losses**: the winding wire has resistance; the current dissipates R × I² in it. They grow with the load.
- **Iron losses**: the core is magnetised and demagnetised 50 times a second, and stray currents (eddy currents) flow in the iron. These currents are reduced by stacking **thin insulated sheets**: the laminated core. These losses exist even with no load.

Large transformers exceed 95 % efficiency; small models of a few watts are more like 70 to 85 %.

## Apparent power, in VA

A transformer's rating plate gives its power in **volt-amperes** (VA), the product of the voltage and current it can deliver without overheating. The maximum secondary current follows:

**Is max = rating (VA) / Us**

![Rating plate: primary 230 V 50 Hz, secondary 12 V 1 A, rating 12 VA](/static/content/electro/en/m10/plaque.svg)

Example: an 18 VA model with a 9 V secondary can supply Is max = 18 / 9 = **2 A**. Beyond that, it overheats and its voltage collapses.

## Key points

- η = Ps / Pp; the losses (iron and copper) heat the transformer.
- The laminated core limits iron losses.
- Is max = rating in VA / Us.
