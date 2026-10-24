Two phenomena accompany every operation of a contactor: the **arc** between its power contacts, and the **voltage spike** from its coil when switched off.

## Extinguishing the arc

When the contacts open under load, the current keeps flowing for an instant through the ionised air: that is the arc. It wears the contacts and must be extinguished quickly.

![Extinguishing the arc: it lengthens between the opening contacts, then splits and cools in the plates of the arc chute](/static/content/moteurs/en/m7/arc.svg)

The contactor **lengthens** it (double break, magnetic blow-out) and **splits** it in the metal plates of an **arc chute**, which cool it. On AC, the arc goes out when the current naturally passes through zero, a hundred times a second at 50 Hz; on DC, there is no such zero, which is why breaking DC is harder.

## The coil voltage spike

A coil stores magnetic energy. When its current is cut abruptly, this energy produces a **voltage spike** of several hundred volts, which disturbs nearby electronics (PLCs, sensors) and wears the contact that controls the coil.

![Coil suppression: a diode in parallel on DC, an RC circuit or a varistor on AC](/static/content/moteurs/en/m7/antiparasite.svg)

So a **suppression module** is fitted in parallel across the coil:

- on DC, a **diode** (freewheeling), connected in reverse: very effective, but it slows opening slightly;
- on AC, an **RC circuit** or a **varistor**, which absorb the voltage peak.

On coils controlled by a PLC, suppression is essential.

## Key points

- The arc is lengthened and split in the arc chute.
- Breaking DC is harder: no zero crossing.
- Coil: diode on DC, RC or varistor on AC.
