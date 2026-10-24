**Proximity sensors** detect an object **without touching it**: no wear, no bounce, thousands of detections per second possible.

## Inductive or capacitive

- The **inductive sensor** creates an alternating magnetic field at its face; a **metal** part approaching disturbs it and the sensor switches. It only sees metals.
- The **capacitive sensor** reacts to any object that changes the capacitance in front of its face: metal, but also wood, plastic, liquid, grain. It is used to detect a level through the wall of a plastic tank.

![M18 inductive sensor facing a steel target; it switches when the target enters its rated range sn = 8 mm](/static/content/moteurs/en/m4/inductif.svg)

The **rated sensing distance sn** is given for a steel target. For other metals, it is multiplied by a **correction factor**: about 0.7 for stainless steel, 0.4 for aluminium, 0.3 for copper. **Example**: a sensor with sn = 8 mm detects aluminium at 8 × 0.4 ≈ 3.2 mm.

## Three-wire connection

Common sensors have **three wires**: **brown** to +24 V, **blue** to 0 V, **black** for the output.

![Three-wire sensor: in PNP, the black output supplies +24 V to the load connected to 0 V; in NPN, the load is connected to +24 V and the output pulls it to 0 V](/static/content/moteurs/en/m4/pnp-npn.svg)

- **PNP**: when the object is detected, the output **sources** +24 V to the load, connected between the output and 0 V. This is the most common output in Europe and on PLCs.
- **NPN**: the output **sinks** the load to 0 V; the load is connected between +24 V and the output.

A PNP sensor connected to an input designed for NPN does not work: always check the sensor's label and the input's documentation.

## Key points

- Inductive: metals only; capacitive: almost anything.
- sn is given for steel; correction factor for other metals.
- Brown +24 V, blue 0 V, black output; PNP sources +24 V.
