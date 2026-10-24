A three-phase transformer has three windings on the primary and three on the secondary. Each group can be connected in star or in delta, like the windings of a motor.

## Phase voltage and line voltage

On a three-phase supply with neutral, two voltages are measured:

![400 V supply: 230 V between a phase and neutral (phase voltage V), 400 V between two phases (line voltage U)](/static/content/moteurs/en/m3/tensions-triphase.svg)

- the **phase voltage** V, between a phase and neutral: **230 V**;
- the **line voltage** U, between two phases: **400 V**.

They are linked by **U = √3 × V**: 1.732 × 230 ≈ 400 V. A single-phase load (lighting, socket) is connected between phase and neutral; a three-phase motor, across the three phases.

## The Dyn11 vector group

A transformer's connection is written with letters: capital for the primary, lower case for the secondary. **D** or **d**: delta; **Y** or **y**: star; **n**: neutral brought out. The number gives the shift between primary and secondary, in clock hours (11 = 330°).

![Dyn11 vector group: primary in delta, secondary in star with the neutral brought out](/static/content/moteurs/en/m3/dyn11.svg)

**Dyn11** is the most common vector group for distribution transformers:

- the **delta primary** needs no neutral on the HV-A side;
- the **star secondary with neutral** provides both 400 V line-to-line and 230 V line-to-neutral;
- it handles unbalanced single-phase loads well.

Two transformers can only be paralleled if they have the same clock number.

## Key points

- V = 230 V, U = 400 V, U = √3 × V.
- D/d delta, Y/y star, n neutral brought out, number = clock number.
- Dyn11: 400 V and 230 V available on the secondary.
