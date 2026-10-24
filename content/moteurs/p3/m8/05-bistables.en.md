An ordinary relay is **monostable**: it drops out as soon as its coil is de-energised. **Latching** relays keep their state **without current**: they have a memory.

## The impulse relay

Each **pulse** on the impulse relay's coil makes its contact **change state**: one pulse closes, the next opens, and so on. Between two pulses, the coil is not energised.

![Impulse relay: each pulse on the coil changes the state of the contact, which then stays in its position](/static/content/moteurs/en/m8/telerupteur.svg)

**Classic use**: lighting a long corridor controlled by several push buttons, all **in parallel**: any of them switches on or off. As many buttons as needed can be added with only two wires.

## The two-coil relay

A two-coil latching relay has a **set** coil (S) and a **reset** coil (R). A pulse on S closes it, a pulse on R opens it; it stays in its state without drawing current.

![Two-coil latching relay: a pulse on S sets, a pulse on R resets; the state is stored without current](/static/content/moteurs/en/m8/bistable.svg)

## Beware of safety

A latching relay **keeps its state after a power cut**: when the voltage returns, the output may be active. To control a motor, the contactor with hold-in is therefore preferred, as it **drops out** on a power cut and avoids any unexpected restart. Latching relays suit lighting, signalling and state memories.

## Key points

- Impulse relay: each pulse changes the state.
- Two-coil latching relay: S sets, R resets.
- Memory kept through a power cut: never for starting a motor.
