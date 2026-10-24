A single phase does not create a rotating field: a winding fed from single phase produces a field that **pulsates**, with no direction of rotation. So a single-phase cage motor does not start by itself: it needs a starting device.

## The capacitor motor

An **auxiliary winding** is added, offset in space, in series with a **capacitor**. The capacitor shifts the current in this winding: together the two windings create a field that rotates, enough to start.

![Single-phase capacitor motor: main winding between L and N, auxiliary winding in series with an 8 µF capacitor](/static/content/moteurs/en/m6/monophase.svg)

It is the motor of pumps, refrigerator compressors, fans, small 230 V workshop machines. If the capacitor fails, the motor hums but does not start (or only starts if the shaft is spun by hand, which is never done). It is reversed by reversing the connections of **one** of the two windings.

## The shaded-pole motor

A **short-circuited copper ring** surrounds part of each pole; it delays the flux in that part and creates a weak rotating field.

![Shaded-pole motor: a copper ring on part of the pole delays the flux and starts the rotor](/static/content/moteurs/en/m6/bague.svg)

Simple and cheap, but with low torque and low efficiency: small fans, washing-machine pumps, cooker hoods.

## The universal motor

It is a **series commutator motor** (module 5) that works on DC as well as AC, since current and field reverse together. Very fast and light: drills, grinders, vacuum cleaners. Its brushes wear.

## Key points

- Single phase: no rotating field without a starting device.
- Capacitor motor: auxiliary winding + capacitor.
- Universal: series commutator motor, on AC.
