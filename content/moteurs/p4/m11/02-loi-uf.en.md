Lowering only the frequency is not enough: the windings' reactance would also fall, the current would rise and the motor would saturate. The drive therefore lowers the **voltage together** with the frequency.

## V/f control

By keeping the ratio **V / f constant**, the motor's magnetic **flux** stays constant, and so does its available **torque**. For a 400 V 50 Hz motor: V / f = 400 / 50 = **8 V/Hz**.

![V/f law: 200 V at 25 Hz, 400 V at 50 Hz; above 50 Hz, the voltage levels off at 400 V](/static/content/moteurs/en/m11/uf.svg)

- At 25 Hz, the drive supplies 8 × 25 = **200 V**.
- Above 50 Hz, the voltage can no longer rise: the flux falls, and so does the torque. This is **field weakening**, usable with care to slightly exceed rated speed.
- At very low speeds, a **compensation** ("boost") setting adds a little voltage to overcome the winding resistance.

## The whole curve shifts

![Torque-speed curves at 25 Hz and 50 Hz: same shape, same maximum torque, shifted in speed](/static/content/moteurs/en/m11/courbes.svg)

At each frequency, the motor keeps its torque-speed curve, shifted: it always runs close to its synchronous speed, with low **slip**. Calculate the synchronous speed and slip for a given frequency:

[[calc:speed]]

## Vector control

V/f control is enough for pumps and fans. For a conveyor, a hoist or a machine that starts under load, **vector control** is chosen: the drive continuously calculates the motor's magnetic state from its currents and separates the part that creates flux from the part that creates torque. Result: high torque from low speeds, precise speed despite load changes.

Vector control requires the **nameplate** to be entered correctly and, often, an **auto-tune** to be run: the drive measures the motor's characteristics itself at standstill.

## Key points

- Constant V / f: constant flux and torque; 8 V/Hz for a 400 V 50 Hz motor.
- Above 50 Hz, field weakening: torque falls.
- Vector control: high torque at low speed; nameplate and auto-tune are essential.
