A **timer relay** (tag **KT**) introduces an adjustable delay between an order and the action of its contact. Two basic functions: delay on closing (**on-delay**) and delay on opening (**off-delay**).

## The on-delay timer

The contact closes **t seconds after** the coil is energised; it opens immediately when the coil is de-energised. If the coil is switched off before the delay has elapsed, the contact never closes.

![On-delay timer: the coil is energised at 0, the contact closes after the delay t and opens as soon as the coil is switched off](/static/content/moteurs/en/m8/ton.svg)

**Uses**: switching from star to delta after starting (module 9), staggered starting of several motors so their currents are not drawn at the same time, an alarm that only trips after a minimum duration.

## The off-delay timer

The contact closes **immediately** on the order and only opens **t seconds after** the order ends.

![Off-delay timer: the contact closes as soon as the control signal comes on and opens only the delay t after it goes off](/static/content/moteurs/en/m8/tof.svg)

**Uses**: a fan that keeps running after a motor stops to cool it, stairway lighting, a pump that drains a circuit after shutdown.

## Symbols and setting

On the diagram, the timed contact carries a small **half-circle** on its stem, showing the direction of the delay; its coil is marked with a cross or a shaded box depending on the function. The delay is set with a dial, after first choosing a **range** (0.1 to 1 s, 1 to 10 s, 1 to 10 min…).

## Key points

- On-delay: delay on closing.
- Off-delay: delay on opening.
- Choose the range, then set the delay.
