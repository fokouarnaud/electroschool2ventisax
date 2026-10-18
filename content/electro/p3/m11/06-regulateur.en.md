The **integrated regulator** replaces the Zener as soon as the current exceeds a few tens of milliamps. The **78xx** family is the most common: three legs, a fixed output voltage, and almost nothing to calculate.

![7805 regulator: input Ue with a 330 nF capacitor, 5 V output with a 100 nF capacitor, ground pin in the middle](/static/content/electro/en/m11/regulateur.svg)

## The 78xx

- The last two digits give the output voltage: **7805** for 5 V, **7809** for 9 V, **7812** for 12 V. The **79xx** family does the same for negative voltages.
- Three pins: **input** (IN), **ground** (GND), **output** (OUT). The pinout depends on the package: always check the datasheet.
- It delivers up to about **1 A**, and protects itself against overheating and short circuits.

The manufacturer recommends two small capacitors placed **as close as possible to the pins**: about 330 nF at the input and 100 nF at the output. They stop the regulator from oscillating.

## The dropout voltage

A 78xx needs headroom: its input must stay at least **2 V above** its output at every moment, ripple troughs included. For a 7805, Ue ≥ **7 V** is therefore needed.

Example: with the smoothing of the previous section (15.6 V peak, 2.3 V of ripple), the input falls to 13.3 V at its lowest: more than enough.

## The power to dissipate

All the excess voltage is burnt off in the regulator:

**P = (Ue − Us) × I**

Example: Ue ≈ 12 V, Us = 5 V and I = 0.5 A. P = (12 − 5) × 0.5 = **3.5 W**. Without a **heatsink**, a TO-220 package hardly dissipates more than 1 to 2 W: it must be mounted on a heatsink, or a lower input voltage must be chosen.

## The complete supply

The whole module comes together: transformer, bridge, reservoir capacitor, regulator.

![Complete 5 V supply: 230 V to 12 V transformer, diode bridge, 2,200 µF capacitor, 7805 regulator and a 100 nF output capacitor](/static/content/electro/en/m11/alim-complete.svg)

This is the diagram of most small linear power supplies, and of this module's mini-project.

## Key points

- 78xx: fixed output (7805 = 5 V), about 1 A, 330 nF and 100 nF capacitors close to the pins.
- The input must stay at least 2 V above the output.
- P = (Ue − Us) × I; above 1 to 2 W, a heatsink is needed.
