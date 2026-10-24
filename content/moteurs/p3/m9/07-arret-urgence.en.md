Every machine that presents a hazard carries one or more **emergency stops**. Their rules come from the standard **IEC 60204-1** (electrical equipment of machines).

## The emergency stop

![Emergency stop: red mushroom-head button, break contact, latching, at the head of the control circuit; resetting does not restart](/static/content/moteurs/en/m9/au.svg)

- A **red mushroom-head** button on a **yellow** background, easy to reach and strike.
- A positive-opening **break** contact, at the **head** of the control circuit: pressing it cuts everything, even if a wire breaks (a broken wire has the same effect as pressing).
- **Latching**: it stays pressed until it is deliberately **reset** (by turning or pulling).
- **Resetting does not restart**: after resetting, a new start order is needed. Thanks to the hold-in, the contactor has dropped out and the machine waits.

Several emergency stops are wired **in series** (NOR logic, module 8). On hazardous machines, the function goes through a **safety relay** that monitors its own contacts and the wiring. The emergency stop never replaces lockout for an intervention (module 1).

## The manual-off-auto selector

A pump or compressor can run by itself (controlled by a pressure switch, a float, a PLC) or by hand for a test. A **three-position selector** chooses the mode.

![Manual-off-auto control of a pump: in manual, button S2 controls KM1; in auto, the pressure switch; in 0, nothing](/static/content/moteurs/en/m9/manuel-auto.svg)

- **Manual**: the selector's 13-14 contact feeds the start button; the operator controls.
- **0**: no order passes; rest and intervention position.
- **Auto**: the 23-24 contact feeds the pressure switch; it starts and stops the pump by itself.

The protections (overload relay, emergency stop) stay in series **in every mode**.

## Key points

- Emergency stop: red on yellow, break contact, latching, at the head of the control circuit.
- Resetting does not restart.
- Manual-off-auto: one selector, protections always in series.
