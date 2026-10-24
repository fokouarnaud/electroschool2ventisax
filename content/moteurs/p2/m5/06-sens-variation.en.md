The DC motor is easy to control: its direction by polarity, its speed by voltage.

## Reversing the direction of rotation

For a permanent-magnet motor, just **reverse the polarity** of the armature: the current changes direction, and so do the forces.

![Reversing the direction: with + on the left the motor turns clockwise, with − on the left anticlockwise](/static/content/moteurs/en/m5/inversion.svg)

For a wound-field motor, reverse **either** the armature **or** the field, but not both: reversing both changes nothing. In a machine, reversing is done by two contactors interlocked with each other (module 9), or by an **H-bridge** of transistors.

## Varying speed with PWM

Dropping the voltage with a resistor wastes energy as heat. **Pulse-width modulation** (PWM) is preferred: a transistor connects and disconnects the motor thousands of times per second. The motor, through its inertia and the inductance of its armature, only "sees" the **average voltage**.

![PWM voltage: 12 V pulses with a 30 % duty cycle; the average voltage is 3.6 V](/static/content/moteurs/en/m5/mli.svg)

**Average voltage = duty cycle × supply voltage.** The duty cycle is the share of time during which the transistor conducts. **Example**: 30 % of 12 V gives 3.6 V average. Losses stay low, because the transistor is either off or saturated (module 10).

## Key points

- Permanent magnets: reversing the polarity reverses the direction.
- Wound field: reverse the armature or the field, not both.
- PWM: average voltage = duty cycle × voltage.
