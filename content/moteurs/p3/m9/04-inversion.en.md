A conveyor, an overhead crane, a motorised door must run in both directions. A three-phase motor is reversed by **swapping two phases** (module 2): so two contactors are needed.

![Reversing: KM1 supplies the motor for forward; KM2, for reverse, swaps phases L1 and L3](/static/content/moteurs/en/m9/inversion-puissance.svg)

**KM1** supplies the motor in the forward direction, **KM2** in reverse with two phases swapped. If KM1 and KM2 closed at the same time, two phases would be connected directly: a **short circuit**. So they must be **interlocked**.

## The two interlocks

![Electrical interlock: a break contact of KM2 in the branch of coil KM1, and a break contact of KM1 in that of KM2](/static/content/moteurs/en/m9/verrouillage.svg)

- **Electrical interlock**: a break contact (21-22) of KM2 is placed in series with the coil of KM1, and vice versa. While one is closed, the other cannot be energised.
- **Mechanical interlock**: a mechanical device, fitted between the two contactors, physically prevents them closing together, even if a contact welds.

**Always fit both.** To change direction, press stop first; some circuits enforce this, others allow direct reversing at the cost of a high current (category AC-4, module 7).

## Inching

In **inching**, the motor only turns while the button is held: no hold-in. It is used to position a part, a crane, a spindle. A button with a double contact (break in the hold-in branch, make to the coil) gives both normal running and inching on the same circuit. Repeated inching quickly wears the contactors: choose them in AC-4.

## Key points

- Reversing: two contactors, two phases swapped.
- Always two interlocks: electrical and mechanical.
- Inching: no hold-in; contactors in AC-4.
