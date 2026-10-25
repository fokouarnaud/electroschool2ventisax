A new drive does not know its motor. **Setting up** teaches it the motor, then how the machine must start, run and stop. Parameter names and numbers vary between manufacturers; the concepts are the same everywhere.

## Motor parameters

Copy the **nameplate** (module 2):

![Parameters to enter: voltage 400 V, current 4.8 A, frequency 50 Hz, speed 1,440 rpm, acceleration 5 s, deceleration 3 s, minimum frequency 10 Hz and maximum 50 Hz](/static/content/moteurs/en/m11/parametres.svg)

The rated current sets the drive's built-in **motor thermal protection**, like an overload relay (module 7).

## Ramps and limits

![Ramps: acceleration from 0 to 50 Hz in 5 s, running, then deceleration in 3 s](/static/content/moteurs/en/m11/rampes.svg)

- **Acceleration ramp**: time to go from 0 to rated frequency. Too short, it causes an **overcurrent** trip.
- **Deceleration ramp**: time to return to 0. Too short with a heavy load, the motor becomes a generator, sends back its energy and raises the **DC bus**: **overvoltage** trip. Remedy: lengthen the ramp or add a **braking resistor**.
- **Minimum and maximum frequencies**: they bound the machine speed.
- **Current limit**: it protects the mechanics and the drive.

## Inputs, outputs and control

- 24 V **digital inputs**: run forward, run reverse, preset speeds, reset.
- 0-10 V or 4-20 mA **analogue input**: speed reference from a potentiometer or a PLC (module 12).
- **Outputs**: fault relay, image of speed or current.
- Built-in **PID controller**: the drive adjusts the speed itself to hold a **pressure** or a **flow** measured by a sensor.

The **control mode** (terminals, keypad or fieldbus) is also chosen by parameter; always record the settings in the machine file.

## Key points

- First the motor nameplate, then ramps and limits.
- Deceleration too fast = DC bus overvoltage; braking resistor or longer ramp.
- Analogue reference, 24 V inputs and PID to control the machine.
