A motor installation is described with **two separate circuit diagrams**, drawn vertically: energy and orders flow from top to bottom.

## The power circuit

![Power circuit: L1 L2 L3, isolator Q1, contactor KM1, overload relay F1, motor M1](/static/content/moteurs/en/m2/puissance.svg)

From top to bottom: the three-phase supply L1 L2 L3, the **isolator Q1** that isolates the equipment for lockout, the poles of **contactor KM1** that make and break the motor current, the **overload relay F1** that watches for overload, and the **motor M1**. The horizontal dotted line links the three poles of one device: they move together.

## The control circuit

![Control circuit: fuse F2, contact 95-96 of F1, stop button S1, start button S2 bridged by contact 13-14 of KM1, coil KM1](/static/content/moteurs/en/m2/commande.svg)

It is supplied at extra-low voltage (here 24 V). It is read like a path: current only reaches coil KM1 if **all** the contacts in series are closed.

1. At rest, S2 (start) is open: the coil is not energised, the motor is stopped.
2. Press **S2**: coil KM1 is energised, the contactor closes, the motor starts.
3. Contact **13-14 of KM1**, in parallel with S2, closes at the same time: when S2 is released, the coil stays energised through this contact. This is the **hold-in** (self-latching).
4. Press **S1** (stop, break contact): the path is cut, KM1 drops out, its contact 13-14 opens, the motor stops and does not restart by itself.
5. On overload, contact **95-96 of F1** opens and has the same effect.

## What happens on the panel

In the cabinet, the two diagrams are not two separate pieces of equipment: they share two devices. The poles of KM1 are in the power circuit, but it is its coil A1-A2, in the control circuit, that closes them. The overload relay F1 watches the motor current on the power side, but it is its contact 95-96, on the control side, that acts: it does not cut the motor current itself, it makes KM1 drop out, and the poles of KM1 cut.

The control circuit only carries the small coil current, at 24 V; the power circuit carries the motor current. Pressing S2 never sends the motor current through the button: it energizes the coil, and KM1 makes the motor current. This is what lets a small button, placed far from the motor, control a large one.

[[fig:power_control]]

## Key points

- Power and control are two separate diagrams, read from top to bottom.
- One device (KM1) appears in both: poles in power, coil and contacts in control.
- Hold-in: a 13-14 contact of the contactor in parallel with the start button.
