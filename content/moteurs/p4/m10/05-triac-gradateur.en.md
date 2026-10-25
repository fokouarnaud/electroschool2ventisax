The **triac** is equivalent to two thyristors connected back to back in a single package, with a single gate. A pulse makes it conduct **both ways**: it controls an AC current directly.

![Triac symbol: terminals A2 and A1, gate G; it conducts both ways](/static/content/moteurs/en/m10/triac.svg)

## The dimmer

The **dimmer** (AC power controller) adjusts the power of an AC load by delaying the triac's triggering in each half-cycle, positive and negative. It is used for lighting, heating and small universal motors (drill, fan).

![Dimmer triggered at 90°: the lamp gets the second half of each half-cycle, positive and negative](/static/content/moteurs/en/m10/gradateur.svg)

For a **resistive** load, triggering at 90° delivers about **half the power**. The simplest trigger circuit is a resistor-capacitor network and a **diac**, which sends a pulse when the capacitor voltage reaches about thirty volts; a potentiometer sets the angle.

## Precautions

- A phase-angle dimmer produces **harmonics** and interference: a filter is added.
- An **inductive** load (motor, transformer) needs a switching-aid network (an RC **snubber**) and sometimes a sturdier triac.
- An **induction motor**'s speed cannot be adjusted by a dimmer: its speed depends on frequency (module 6). The dimmer is at best a **soft starter** (module 9).

## The solid-state relay

A solid-state relay (module 8) contains a triac or two thyristors, switched at **zero voltage**: they only do on/off, without angle control.

## Key points

- Triac: conducts both ways after a gate pulse.
- Dimmer: delaying the trigger reduces power; 90° gives about half on a resistive load.
- No speed control of an induction motor by a dimmer: a frequency drive is needed.
