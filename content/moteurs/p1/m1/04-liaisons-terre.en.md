The **earthing system** states how, on one side, the transformer neutral and, on the other, the installation's exposed parts are connected to earth. It is written with two letters: the first concerns the neutral (T: earthed, I: isolated), the second the exposed parts (T: connected to an earth, N: connected to the neutral). The principles are set by the international standard IEC 60364.

## TT system

The neutral is earthed at the supplier's substation, the exposed parts at an earth electrode belonging to the installation. A fault drives a small current through the two earth electrodes: it is not enough to trip a circuit breaker, so the **RCD trips on the first fault**. This is the most common system in homes and small workshops.

![TT system: neutral and exposed parts connected to two separate earth electrodes; the RCD trips on the first fault](/static/content/moteurs/en/m1/tt.svg)

## TN system

The exposed parts are connected to the neutral, which is itself earthed. An insulation fault becomes a **line-to-neutral short circuit**: the current is high, and the breaker or fuse trips on the first fault. In TN-C, neutral and protection share one conductor, the **PEN**; in TN-S, they are separate (N and PE). It is found in factories that have their own transformer.

![TN system: the exposed parts are connected to the neutral by the PEN conductor; a fault becomes a short circuit and the breaker trips](/static/content/moteurs/en/m1/tn.svg)

## IT system

The neutral is isolated from earth (or connected through a high impedance). A first fault drives only a tiny current: the supply is **not cut**, a **permanent insulation monitor** signals it and maintenance tracks it down. A second fault on another phase, however, must trip. It is chosen when an outage would be dangerous or costly: operating theatre, continuous process.

![IT system: isolated neutral; the first fault is signalled by the insulation monitor, not cut](/static/content/moteurs/en/m1/it.svg)

## Key points

- TT: RCD, trips on the first fault.
- TN: the fault is a short circuit, the breaker trips on the first fault.
- IT: first fault signalled, continuity of service.
