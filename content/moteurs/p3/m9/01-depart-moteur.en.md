A **motor circuit** (or feeder) is the set of devices between the board and the motor. Four functions must always be provided, following the principles of IEC 60364:

![Motor circuit: isolation by Q1, short-circuit protection by fuses, control by KM1, overload protection by F1](/static/content/moteurs/en/m9/depart.svg)

1. **Isolate**: separate the circuit from the supply for lockout (module 1); lockable isolator or switch-disconnector.
2. **Protect against short circuits**: aM fuses or a circuit breaker's magnetic trip, at the head of the circuit.
3. **Control**: make and break the current in service; contactor.
4. **Protect against overloads**: overload relay (module 7) or a motor circuit breaker's thermal trip.

A **motor circuit breaker** combines isolation and both protections on its own; with a contactor, it forms a complete, compact motor circuit.

## Conductor size

The motor cable must carry its current **without heating** beyond what its insulation tolerates, and without too much **voltage drop**. The current-carrying capacity depends on the cross-section, the metal, the insulation, the **installation method** (in conduit, on a cable tray, buried), the ambient temperature and the number of neighbouring cables.

![Order of magnitude of copper current-carrying capacity: 1.5 mm² about 16 A, 2.5 mm² about 21 A, 4 mm² about 28 A, 6 mm² about 36 A](/static/content/moteurs/en/m9/section.svg)

These values are only an order of magnitude: always choose the size from the tables of the applicable regulations, applying their correction factors, then check that the protection really protects the cable. **Example**: for a 4.8 A motor (module 2), 1.5 mm² is ample for current; over a long distance, voltage drop will decide.

## Key points

- Isolate, protect against short circuits, control, protect against overloads.
- Motor circuit breaker + contactor: a complete motor circuit.
- Conductor size depends on current, installation method and length.
