At the other end of the control chain, **actuators** turn an electrical order into a physical action.

## The solenoid valve

A **solenoid valve** opens or closes the passage of a fluid (compressed air, water, gas). Its coil, when energised, pulls a moving plunger that clears the passage; a spring closes it again when the coil is de-energised.

![Solenoid valve: the energised 24 V coil pulls the plunger, which opens the passage for the fluid; symbol YV1](/static/content/moteurs/en/m4/electrovanne.svg)

On the diagram, its coil is marked **YV**. Choose its voltage (often 24 V), its state at rest (**normally closed** or normally open) and the fluid it handles. Solenoid valves drive the pneumatic cylinders of machines.

## The stepper motor

A **stepper motor** turns by a fixed angle, a **step**, for each pulse received. A common motor makes **200 steps per revolution**, that is 360 / 200 = **1.8° per step**.

![Stepper motor: 200 steps per revolution, 1.8° per pulse; position is known without a sensor](/static/content/moteurs/en/m4/pas-a-pas.svg)

**Example.** To turn a quarter of a revolution (90°), 90 / 1.8 = **50 pulses** are needed. As each pulse gives one step, the position is known **without a sensor**, as long as the motor does not "skip" steps under too heavy a load. It is used in 3D printers, small CNC machines, motorised valves.

## The servomotor

The **servomotor** is a motor combined with a position sensor (encoder) and a drive that constantly corrects the gap between the wanted and the measured position: a **closed loop**. More accurate and faster than a stepper, it equips robots and machine tools.

## Key points

- Solenoid valve: coil YV, normally closed or open.
- Stepper: 200 steps per revolution, 1.8° per step, position without a sensor.
- Servomotor: closed loop with an encoder.
