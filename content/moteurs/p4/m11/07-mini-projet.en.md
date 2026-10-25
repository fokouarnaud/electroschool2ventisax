This mini-project is done in the workshop, with your trainer. You prepare **on paper** the setup of a drive for a real motor, then reproduce ramps on a 12 V model.

## Objective

Go from a motor's nameplate to a complete, justified setup sheet, and visualise an acceleration ramp.

## Safety

- **No three-phase drive** is connected: setup is done on paper, from the nameplate of a **disconnected** motor.
- The ramp model uses the 12 V PWM module from module 10, fed by a wall adapter; no voltage above 24 V.
- If a real drive is in the workshop, do not open it: its DC bus remains dangerous after switch-off.

![Setup sheet: motor voltage, current, frequency and speed, acceleration and deceleration ramps](/static/content/moteurs/en/m11/tableau.svg)

## Equipment

| Quantity | Item |
|---|---|
| 1 | disconnected induction motor with a legible nameplate |
| 1 | blank setup sheet and a drive manual (paper or PDF) |
| 1 | 12 V PWM module, 12 V motor and 12 V supply (module 10) |
| 1 | multimeter; oscilloscope (oscilloscope variant) |
| 1 | stopwatch |

## Oscilloscope variant

1. Fill in the sheet from the nameplate: voltage, current, frequency, speed; calculate the rated slip.
2. Choose the ramps (5 s and 3 s) and the minimum and maximum frequencies; justify each choice.
3. On the model, probe the PWM output: turn the potentiometer slowly over 5 s and watch the pulses widen gradually, an image of a ramp.

## Multimeter-only variant

1. Fill in and justify the sheet as above.
2. On the model, read the motor's average voltage every second while turning the potentiometer up over 5 s; plot the ramp obtained.
3. Calculate the voltage the drive would supply at 25 Hz according to the V/f law.

| Quantity | Nameplate | Chosen parameter | Justification |
|---|---|---|---|
| voltage | | | |
| current | | | |
| speed | | | |
| acceleration ramp | | 5 s | |

## Conclusion

Explain what would happen with a 0.5 s deceleration ramp on a high-inertia machine.
