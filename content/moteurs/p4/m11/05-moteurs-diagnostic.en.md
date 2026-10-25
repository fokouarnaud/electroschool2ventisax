A standard motor runs on a drive, provided a few limits are respected. And when the drive trips, its message guides troubleshooting.

## Derating at low speed

A **self-ventilated** motor is cooled by the fan on its own shaft. At low speed, this fan blows much less: the motor can no longer deliver its rated torque continuously without overheating.

![Allowable continuous torque: about 0.6 Tn at very low speed for a self-ventilated motor, against 1 Tn with forced ventilation](/static/content/moteurs/en/m11/declassement.svg)

For a machine running long at low speed and full load (conveyor, extruder), choose **forced ventilation** (separate fan) or an oversized motor. Pumps and fans, whose torque falls with speed, do not have this problem.

## Other constraints

- **Insulation**: the steep PWM edges stress the winding insulation; with a long cable, choose a motor designed for drives or add an **output filter**.
- **Bearings**: stray currents may flow through the bearings; careful earthing, even an insulated bearing on large motors.
- **Overspeed**: above 50 Hz, check the mechanical rating (bearings, balancing, fan).
- **Thermal sensor**: a sensor in the windings, wired to the drive, protects better than a calculation.

## Fault diagnosis

![Common faults: overcurrent, DC bus overvoltage, undervoltage, overheating, and their likely causes](/static/content/moteurs/en/m11/defauts.svg)

Method:

1. **Read** the fault code and history before resetting; note the conditions (starting, braking, load).
2. **Interpret**: a fault at start points to the ramp or the motor; when braking, the DC bus; random, the supply or EMC.
3. **Check with the power off** (bus discharged, absence of voltage verified): insulation of the cable and of the motor **disconnected from the drive**, tightness of connections, fans.
4. **Correct** the parameter or the cause, then reset.

Never test a motor's insulation with the drive connected: the test voltage would destroy the inverter.

## Key points

- Self-ventilated at low speed: reduced continuous torque; forced ventilation if needed.
- Watch insulation, bearings and overspeed.
- Read the fault, interpret, check with power off, correct.
