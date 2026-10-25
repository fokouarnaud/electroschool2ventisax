Power components need **control**: pulses at the right moment, at the right frequency, with the right width. That job falls to integrated circuits.

## The 555 and PWM

A **555** wired as an **astable** produces a square-wave signal. With a potentiometer, the **duty cycle** is adjusted: the fraction of the period when the output is at 1. This is **pulse-width modulation** (PWM).

![A 555 astable, with R1, a potentiometer and a capacitor C, supplies the PWM signal that drives the power transistor](/static/content/moteurs/en/m10/555.svg)

On a DC motor, the **average voltage** is:

**Uavg = duty cycle × U**

With 12 V and a 25 % duty cycle, the motor sees 3 V on average; its speed follows. The switching frequency, around a kilohertz or more, is too fast for the motor to feel.

## Op-amps and microcontrollers

- The **operational amplifier** compares, filters and shapes measurements (current, speed); as a comparator, it produces an on/off signal.
- The **microcontroller** generates several PWM signals, measures, regulates and communicates: it is the heart of modern drives.

Between the control and the power component, a **driver** or an **optocoupler** supplies the gate current and **isolates** the low voltage from the power circuit.

## Electrostatic discharge

A human body can charge to several thousand volts walking on a carpet. The discharge, often imperceptible, is enough to puncture the gate of a MOSFET or an IGBT.

![Discharge protection: earthed wrist strap, antistatic mat, shielded bag](/static/content/moteurs/en/m10/esd.svg)

- Wear an earthed **wrist strap** and work on an antistatic **mat**.
- Keep boards and components in their **shielded bag** until fitting; hold them by the edges.
- Never touch a component's pins or the tracks of a drive board.

## Key points

- A 555 astable produces PWM; Uavg = duty cycle × U.
- Microcontroller and driver control the power components.
- Wrist strap, mat and shielded bag against electrostatic discharge.
