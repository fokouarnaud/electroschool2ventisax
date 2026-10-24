The **solid-state contactor** does the same job as a contactor, but without moving parts: **thyristors** (or triacs) replace the contacts.

![Solid-state contactor: two back-to-back thyristors per phase, driven by an isolated 24 V signal, mounted on a heatsink](/static/content/moteurs/en/m7/statique.svg)

Per phase, two thyristors connected **back to back** each pass one half-cycle. A small control signal (often 24 V), isolated by an optocoupler, makes them conduct. How thyristors work is covered in module 10.

## Advantages and limits

- **No mechanical wear**: millions of operations, at very high rates (furnaces, resistors switched constantly).
- **Silent** and arc-free; switching possible at zero crossing (module 8).
- But semiconductors have a **voltage drop** of about 1.5 V when conducting: they **heat up**.

![Heating: about 1.5 W per ampere per phase, that is 45 W at 10 A and 112.5 W at 25 A on three phases](/static/content/moteurs/en/m7/dissipation.svg)

**Example.** At 10 A on three phases: P ≈ 1.5 × 10 × 3 = **45 W**, which must be removed by a well-ventilated **heatsink**. An electromechanical contactor of the same rating dissipates only a few watts.

- On failure, a semiconductor often fails **short-circuit**: the solid-state contactor does not isolate, so an isolating device is always needed upstream.

## Key points

- Back-to-back thyristors instead of contacts: no wear.
- About 1.5 W per ampere per phase: a heatsink is essential.
- Never isolates: isolator upstream.
