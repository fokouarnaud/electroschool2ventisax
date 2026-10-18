Almost every electronic circuit wants a **DC** voltage that is steady. The mains supplies AC. A **power supply** bridges the gap in four steps.

![Power supply chain: transformer, rectifier, filter, regulator then load, with the voltage shape under each block](/static/content/electro/en/m11/chaine.svg)

1. The **transformer** steps down the 230 V and isolates the circuit from the mains (previous module).
2. The **rectifier** (diodes) lets current flow in one direction only.
3. The **filter** (a capacitor) fills in the dips of the rectified voltage.
4. The **regulator** holds a fixed voltage, whatever the load.

## Refresher: the diode rectifies

In Part 1 (module "The diode"), a single diode was already rectifying AC: it conducts when its anode is more positive than its cathode, and blocks the other way. This is **half-wave** rectification.

## The values to know

A transformer is always specified by its **rms** voltage. The diode, however, sees the **peak** voltage:

**Umax = Urms × √2**

With a 12 V rms secondary: Umax = 12 × 1.414 ≈ **17 V**. After the diode (about 0.7 V threshold), the output reaches 17 − 0.7 ≈ **16.3 V** peak.

![Half-wave rectification: the 17 V peak input in grey, the 16.3 V peak output in green, only the positive half-cycles get through](/static/content/electro/en/m11/simple.svg)

## The drawback of half-wave

Every other half-cycle is lost. The output voltage drops to zero for 10 ms in every 20 ms period: a big capacitor will be needed to fill these gaps, and the ripple will stay at **50 Hz**. The diode bridge, in the next section, does better.

## Key points

- Power supply: transformer, rectifier, filter, regulator.
- Umax = Urms × √2; a diode takes away about 0.7 V.
- Half-wave loses every other half-cycle.
