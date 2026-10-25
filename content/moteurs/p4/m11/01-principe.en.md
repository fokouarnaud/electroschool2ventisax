An induction motor's speed depends on the **frequency** of its supply (module 6): ns = 60 × f / p. To vary it, a device that produces an adjustable frequency is needed: the **frequency drive** (or frequency converter).

## Three stages

![Drive: the 400 V 50 Hz supply goes through a rectifier, charges the DC bus to 540 V, then a PWM inverter feeds the motor](/static/content/moteurs/en/m11/blocs.svg)

1. The **rectifier** (six-diode bridge, module 10) turns the three-phase supply into DC.
2. The **DC bus**, with its large capacitors, stores this voltage: about **540 V** on a 400 V supply.
3. The **inverter**, made of six IGBTs, chops the DC bus to recreate a three-phase supply whose **frequency** and **voltage** are adjustable.

**Danger**: the bus capacitors stay charged for several minutes after switch-off. Wait for the delay marked on the device (often 5 to 15 min) and **verify the absence of voltage** on the bus before any work (module 1).

## Pulse-width modulation

The inverter does not produce a true sine wave: it sends pulses of **variable width**, at a few kilohertz. Because the motor windings are inductive, the **current** smooths these pulses and becomes almost sinusoidal.

![Inverter pulses whose width varies; their average, and the motor current, follow a sine wave](/static/content/moteurs/en/m11/mli.svg)

## What the drive provides

- **Soft start**: current limited to about 1.5 In, instead of 6 to 8 In direct-on-line.
- **Adjustable speed**, with energy savings on pumps and fans.
- Built-in **protection** of the motor (overload, overcurrent) and of the drive.
- Reversing and braking controlled by parameters.

## Key points

- Rectifier, DC bus (≈ 540 V on 400 V), IGBT inverter.
- PWM produces an almost sinusoidal current of adjustable frequency.
- The DC bus remains dangerous for several minutes after switch-off.
