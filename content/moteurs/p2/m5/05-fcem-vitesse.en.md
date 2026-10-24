When the armature turns in the field, its conductors cut the field lines: a voltage is **induced** in them, as in a dynamo. This voltage opposes the supply voltage: it is the **back electromotive force** E (back-EMF). It is proportional to speed.

## The armature equation

The applied voltage U is shared between the back-EMF E and the voltage drop across the armature resistance R:

**U = E + R × I**   so   **I = (U − E) / R**

![Armature model: the source U feeds the resistance R in series with the back-EMF E; U = E + R × I](/static/content/moteurs/en/m5/fcem.svg)

**Example.** A 12 V motor has an armature resistance R = 1.5 Ω and draws I = 2 A when running. E = U − R × I = 12 − 1.5 × 2 = **9 V**. The power converted into mechanical power is E × I = 9 × 2 = 18 W.

## Starting current

At standstill, the motor is not turning: E = 0. The starting current is therefore I = U / R, with nothing to limit it.

**Example.** The same motor at start-up: I = 12 / 1.5 = **8 A**, four times its running current. Then, as it gathers speed, E rises and the current falls.

![Starting current: it starts at several times the rated current and falls as the motor gathers speed](/static/content/moteurs/en/m5/demarrage.svg)

For large motors, this current would be destructive: the voltage is limited at start-up (resistors, or a drive that raises the voltage gradually).

## Speed

As E is proportional to speed, at constant flux: **n is roughly proportional to U − R × I**. So the speed of a DC motor is set by setting **the armature voltage**.

## Key points

- U = E + R × I; E proportional to speed.
- At start-up, E = 0: I = U / R, a high current.
- Speed is set by the armature voltage.
