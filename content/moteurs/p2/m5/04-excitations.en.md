When the field is wound, it can be connected to the armature in several ways. This connection, called **excitation**, completely changes how the motor behaves.

## The series motor

The field, in **thick wire**, is in **series** with the armature: the same current flows through both. At start-up, this current is high, so is the field: the **starting torque is very high**.

![Series motor: the thick-wire field is in series with the armature; high starting torque](/static/content/moteurs/en/m5/serie.svg)

But its speed varies a lot with load, and **no-load, it runs away**: it must never run without a load coupled to it. It is found in car starter motors, traction (old trams, trucks) and, as the **universal motor**, in portable tools (module 6).

## The shunt motor

The field, in **thin wire**, is connected in **parallel** (shunt) across the armature: it receives a constant voltage, so the field stays constant.

![Shunt motor: the thin-wire field is in parallel with the armature; almost constant speed](/static/content/moteurs/en/m5/shunt.svg)

Its **speed stays almost constant** whatever the load: machine tools, fans, conveyors. Beware: if the field circuit opens while running, the field disappears and the motor can run away.

## The compound motor

The **compound motor** combines a series field and a shunt field: good starting torque and stable speed, with no risk of running away no-load. It suits presses, lifts, rolling mills.

| Excitation | Starting torque | Speed | No-load |
|---|---|---|---|
| series | very high | very variable | runs away |
| shunt | medium | almost constant | stable |
| compound | high | stable | stable |

## Key points

- Series: high starting torque, never no-load.
- Shunt: almost constant speed.
- Compound: the best of both.
