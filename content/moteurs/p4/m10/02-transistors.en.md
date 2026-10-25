A power transistor is not used here to amplify: it is a **fast switch**. It is either **off** (no current) or **saturated** (almost no voltage across it). Detailed recap: [Electronics course in the catalogue](/en/catalogue/), Part 1, transistor as a switch.

## Bipolar and MOSFET

- The **bipolar transistor** is driven by a base **current**; the stronger the load, the larger the drive current needed.
- The **MOSFET** is driven by a gate-source **voltage** (often 10 V); once switched, its gate draws almost nothing. It switches very fast and dominates below a few hundred volts.

![A MOSFET drives a 12 V motor; a freewheeling diode across the motor carries its current at each switch-off](/static/content/moteurs/en/m10/mosfet.svg)

## The freewheeling diode

A motor or a coil **opposes** the interruption of its current: without care, a voltage spike would destroy the transistor. The **freewheeling diode**, reverse-connected across the load, lets that current decay gently. It was already seen on contactor coils (module 7).

## Why switching dissipates little

The power lost in the transistor is **P = U × I** across it:

![Off: 12 V and 0 A, so 0 W; saturated: 0.1 V and 2 A, so 0.2 W, while the load gets 24 W](/static/content/moteurs/en/m10/pertes.svg)

In both states, one of the two factors is almost zero. Losses come mainly from the **switching instants**, when voltage and current coexist briefly: the more often it switches, the hotter it gets.

## Key points

- In power circuits, the transistor is a switch: off or saturated.
- Bipolar driven by current, MOSFET by voltage.
- A freewheeling diode is mandatory on an inductive load.
- Low losses, mainly due to switching.
