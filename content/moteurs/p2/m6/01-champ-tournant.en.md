The three-phase AC motor has neither commutator nor brushes. Its secret: a **magnetic field that rotates** by itself.

## The rotating field

The stator carries three windings offset by **120°** in space, supplied by the three supply phases, themselves offset by 120° in time. Their three fields add up to a single field, of constant strength, that **rotates** around the motor axis.

![Three coils U, V, W offset by 120°, supplied with three-phase current: their combined field rotates](/static/content/moteurs/en/m6/champ.svg)

## Synchronous speed

The field makes one revolution per supply period for one **pole pair**. With p pole pairs, it turns p times more slowly:

**ns = 60 × f / p**   (ns in rpm, f in Hz)

![Synchronous speed at 50 Hz: 3,000 rpm for 2 poles, 1,500 for 4, 1,000 for 6, 750 for 8](/static/content/moteurs/en/m6/vitesses.svg)

**Example.** A 4-pole motor (p = 2) on the 50 Hz supply: ns = 60 × 50 / 2 = **1,500 rpm**. To change this speed, change the number of poles (multi-speed motor, module 9) or the frequency (drive, module 11).

To reverse the direction of the field, and so of the motor, **swap two phases** (module 2).

[[calc:speed]]

## Key points

- Three windings at 120° + three-phase currents = rotating field.
- ns = 60 × f / p; at 50 Hz: 3,000, 1,500, 1,000, 750 rpm.
- Swapping two phases reverses the direction.
