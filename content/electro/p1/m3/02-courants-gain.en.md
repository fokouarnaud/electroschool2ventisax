Three currents flow in a working NPN transistor: the base current **IB**, the collector current **IC** and the emitter current **IE**. The current law from module 1 applies: everything that goes in comes out through the emitter.

**IE = IB + IC**

![NPN transistor with IB entering the base, IC entering the collector and IE leaving the emitter](/static/content/electro/en/m3/courants.svg)

## The current gain β

The collector current is **proportional** to the base current, by a ratio called the **current gain**, written β (beta) or hFE in datasheets:

**IC = β × IB**

β is typically between 100 and 400 for a small transistor. With β = 150, a base current of 50 µA controls a collector current of 150 × 50 µA = **7.5 mA**.

![IC against IB line for β = 150: 50 µA give 7.5 mA](/static/content/electro/en/m3/gain.svg)

Since IB is very small compared with IC, we often take **IE ≈ IC**. In the example: IE = 7.5 mA + 0.05 mA = 7.55 mA.

## A gain that varies

β is not a precise value: it changes from one part to another of the same model (sometimes by a factor of three), with temperature and with current. Datasheets therefore give a **range**, with a minimum value. A good circuit should not depend on the exact value of β: this is what we will see for switching in module 4.

## Key points

- IE = IB + IC, and IE ≈ IC.
- IC = β × IB, with β usually between 100 and 400.
- β varies a lot: calculate with the datasheet's minimum value.
