A **starter** brings together what is needed to start a motor, stop it and protect it against overloads.

## The manual starter

![Manual starter: a motor circuit breaker Q1 with a rotary knob supplies the motor directly](/static/content/moteurs/en/m2/manuel.svg)

The simplest is a **motor circuit breaker**: a single device that isolates, protects against short circuits (magnetic trip) and against overloads (adjustable thermal trip). It is operated by hand, with a rotary knob or two push buttons. It suits small machines controlled on the spot: bench grinder, booster pump.

Its limit: it cannot be controlled remotely, by a PLC or by a sensor, and it does not drop out after a power cut unless designed to.

## The remote-controlled starter

![Remote-controlled starter: circuit breaker, contactor, overload relay, motor; the contactor is controlled remotely by buttons](/static/content/moteurs/en/m2/telecommande.svg)

The functions are then separated: a **circuit breaker** (or fuses) protects against short circuits, a **contactor** driven by its coil makes and breaks the current, an **overload relay** watches for overload. The coil can be controlled from anywhere: buttons, limit switch, PLC.

A decisive safety advantage: after a power cut, the contactor drops out and **the motor does not restart by itself** when the voltage returns (the hold-in is lost). A new press on start is needed.

## Key points

- Motor circuit breaker: all-in-one manual starter.
- Remote-controlled starter: circuit breaker, contactor, overload relay.
- The contactor drops out on a power cut: no unexpected restart.
