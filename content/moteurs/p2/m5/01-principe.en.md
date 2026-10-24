All electric motors rely on the same meeting: a **current** and a **magnetic field**.

## The Laplace force

A conductor carrying a current I, placed in a magnetic field B, is subject to a force perpendicular to both field and current: **F = B × I × L**, where L is the length of conductor in the field.

![Conductor carrying a current between the N and S poles of a magnet: it is subject to a force F perpendicular to the field](/static/content/moteurs/en/m5/laplace.svg)

**Example.** B = 0.8 T, I = 10 A, L = 0.2 m: F = 0.8 × 10 × 0.2 = 1.6 N. Reversing the current, or reversing the field, reverses the force.

The field can come from **permanent magnets** or an **electromagnet**: a coil carrying a current becomes a magnet, with a north pole and a south pole.

## From force to rotation

Place a **loop** of wire in the field. Its two sides carry the current in opposite directions: they are subject to two opposite forces, which form a **torque**. The loop turns.

![Loop in the field: its two sides are subject to opposite forces and the loop turns about its axis](/static/content/moteurs/en/m5/spire.svg)

But after half a turn, the sides have swapped places: if the current kept its direction, the forces would brake the loop. So the **current in the loop must reverse every half-turn**. That is the job of the **commutator** (next section). A real motor combines many offset loops, for a smooth torque.

## Key points

- F = B × I × L: current + field = force.
- Two opposite forces on a loop = a torque.
- The current must reverse in the loop every half-turn.
