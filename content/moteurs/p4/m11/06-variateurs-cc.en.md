Before frequency drives, variable speed meant the **DC motor** (module 5). It is still found on older machines, rolling mills, winders and hoists.

## The principle

The speed of a separately excited DC motor is almost proportional to its **armature voltage**. A **thyristor bridge** (module 10), fed by the supply, provides this voltage; the **firing angle** adjusts it.

![DC drive: a thyristor bridge rectifies the supply; the firing angle sets the armature voltage, hence the speed](/static/content/moteurs/en/m11/pont-cc.svg)

The drive also feeds the **field winding** at constant voltage, and regulates the armature current to limit torque. A **tachogenerator** or an encoder measures speed for control.

Small permanent-magnet motors are rather controlled by a transistor **chopper** (PWM), as in the module 10 mini-project.

## The four quadrants

![The four quadrants: motoring and braking in each direction of rotation](/static/content/moteurs/en/m11/quadrants.svg)

- Quadrants 1 and 3: the motor **drives** the load, one way or the other.
- Quadrants 2 and 4: the motor **brakes** the load, which drives it (lowering a load, slowing a flywheel).

A **single-quadrant** drive only runs one way. A **regenerative** drive with two back-to-back bridges works in all four quadrants and **returns** braking energy **to the supply**, instead of burning it in a resistor. The principle also exists for frequency drives (active front end).

## Maintenance

The DC motor needs its **brushes** and **commutator** monitored (module 5); this is the main reason it is replaced by induction motors on frequency drives.

## Key points

- Thyristor bridge: the firing angle sets the armature voltage and the speed.
- Four quadrants: motoring or braking in each direction.
- Regenerative: braking energy returns to the supply.
