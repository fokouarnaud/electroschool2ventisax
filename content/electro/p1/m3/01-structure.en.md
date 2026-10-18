The **bipolar transistor** is made of three stacked layers of doped silicon: either N-P-N or P-N-P. Each layer has its own lead:

- the **emitter** (E), which emits the charge carriers;
- the **base** (B), a very thin central layer used as the control;
- the **collector** (C), which collects most of the current.

You can picture it as two PN junctions back to back, but with a base so thin that a small base current is enough to let a large current through between collector and emitter. That is the whole point of the transistor: **a small current controls a large one**.

## NPN and PNP

The symbol has an arrow on the emitter, showing the direction of current in the base-emitter junction:

- for an **NPN**, the arrow points out: current enters through the base and collector and leaves through the emitter;
- for a **PNP**, the arrow points in: everything is reversed, the emitter goes towards +.

![NPN transistor symbol, base on the left, collector at the top, emitter at the bottom with the arrow pointing out](/static/content/electro/en/m3/npn.svg)

![PNP transistor symbol, with the emitter arrow pointing in](/static/content/electro/en/m3/pnp.svg)

A memory aid: for the NPN, the arrow is "**N**ot **P**ointing i**N**", it points out.

## Packages

Common small transistors (BC547, 2N2222 for NPN; BC557, 2N2907 for PNP) come in a three-legged plastic package. The order of the leads **changes from one model to another**: always check the datasheet before wiring.

## Key points

- Three leads: base (control), collector, emitter.
- NPN: arrow pointing out; PNP: arrow pointing in.
- Lead order depends on the model: read the datasheet.
