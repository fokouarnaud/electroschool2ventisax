To reduce the inrush current at start-up, the motor is first supplied at a **reduced voltage**, then at full voltage.

## Star-delta starting

The motor must be designed to run **in delta** on the supply (for example 400 V Δ / 690 V Y on a 400 V supply) and have its **six terminals** accessible. It starts in **star**: each winding gets only 400 / √3 = 231 V. Then a timer switches it to **delta**.

![Star-delta starter: KM1 supplies the motor, KM2 forms the star point during starting, then KM3 connects the windings in delta](/static/content/moteurs/en/m9/etoile-triangle.svg)

1. **KM1** (line) and **KM2** (star) close: the motor starts in star.
2. After a few seconds (on-delay timer, module 8), **KM2** opens then **KM3** (delta) closes.
3. KM2 and KM3 are **interlocked**: closing both at once would be a short circuit.

In star, the line **current** and the starting **torque** are both **divided by 3** compared with direct-on-line starting. The motor must therefore be able to start its load with a third of its torque: fans, centrifugal pumps, machines started unloaded. Check with the calculator:

[[calc:stardelta]]

![Starting current: about 7 In direct-on-line, about 2.3 In star-delta, about 3 In with a set soft starter](/static/content/moteurs/en/m9/courants.svg)

## Other methods

- **Stator resistors**: resistors in series with the motor absorb part of the voltage, then are short-circuited.
- **Soft starter**: thyristors (module 10) raise the voltage **gradually** along an adjustable ramp. No jolt, current limited to a chosen value (often 3 to 4 In), soft stop possible for pumps (no water hammer). It is today the most common solution when a drive is not needed.

## Key points

- Star-delta: current and torque divided by 3; motor designed for delta.
- KM2 and KM3 interlocked.
- Soft starter: voltage ramp by thyristors.
