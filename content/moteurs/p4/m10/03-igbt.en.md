The **IGBT** (insulated-gate bipolar transistor) combines the best of both transistors: it is **voltage-driven** like a MOSFET, and **withstands high voltages and currents** like a bipolar. It is the component of variable-speed drives (module 11) and inverters.

## Symbol and terminals

![IGBT symbol with its gate G, collector C and emitter E; a diode is connected in antiparallel](/static/content/moteurs/en/m10/igbt.svg)

- **G** (gate): the control, typically +15 V to conduct, 0 V or a negative voltage to block.
- **C** (collector) and **E** (emitter): the path of the power current.
- An **antiparallel diode**, often built into the module, carries a motor's return current.

When on, an IGBT drops about **1.5 to 2 V**, almost independently of current: at 20 A it already loses 30 to 40 W, hence its large heat sinks.

## Power modules

IGBTs come in **modules**: two IGBTs form a **leg** (one to +, the other to −), and a three-phase inverter has three. Control is handled by a dedicated circuit, the **driver**, which isolates the gate from the control electronics and prevents both IGBTs of a leg from conducting together.

## Choosing between MOSFET, IGBT and thyristor

![Comparison: MOSFET up to a few hundred volts and very fast; IGBT from 600 to 1,700 V for drives; thyristor up to several kV, slow](/static/content/moteurs/en/m10/comparaison.svg)

## Testing an IGBT

Power off, capacitors discharged, multimeter on diode test: between E and C you measure the antiparallel diode (about 0.4 V one way, nothing the other). Between G and the other terminals, no conduction: a shorted gate means a destroyed component.

## Key points

- IGBT: voltage-driven, withstands 600 to 1,700 V; the drive component.
- Drop of 1.5 to 2 V when on.
- Legs of two IGBTs; a driver is mandatory.
