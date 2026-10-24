An induction motor's speed depends on its number of poles (module 6): ns = 60 × f / p. To get **two speeds** without a drive, the number of poles is changed.

## The Dahlander motor

The **Dahlander** motor has a single winding per phase, whose connection is changed to halve the number of poles: the two speeds are in a **1 to 2 ratio**.

![Dahlander motor: low speed in delta, supply on 1U 1V 1W; high speed in double star, supply on 2U 2V 2W with 1U 1V 1W joined](/static/content/moteurs/en/m9/dahlander.svg)

- **Low speed** (for example 8 poles, 750 rpm at 50 Hz): the supply arrives on 1U, 1V, 1W; windings in delta.
- **High speed** (4 poles, 1,500 rpm): the supply arrives on 2U, 2V, 2W; terminals 1U, 1V, 1W are **joined together** (double star).

So **three contactors** are needed: KM1 for low speed, KM2 (supply on 2U 2V 2W) and KM3 (star on 1U 1V 1W) for high speed.

![Two-speed motor: KM1 for low speed, KM2 and KM3 for high speed, interlocked with each other](/static/content/moteurs/en/m9/deux-vitesses.svg)

The low-speed and high-speed contactors are **interlocked** electrically and mechanically: closing both would be a short circuit. For speeds in another ratio (1,000 and 1,500 rpm, for example), a motor with **two separate windings** is used.

## The wound-rotor motor

The wound-rotor motor (module 6) starts with rotor resistors removed in steps, by contactors controlled by timers; it can also run slightly slower by leaving part of the resistance in, at the cost of losses. These solutions are now often replaced by a **frequency drive** (module 11), which gives every speed.

## Key points

- Dahlander: two speeds in a 1 to 2 ratio.
- Low speed in delta, high speed in double star.
- Contactors for the two speeds always interlocked.
