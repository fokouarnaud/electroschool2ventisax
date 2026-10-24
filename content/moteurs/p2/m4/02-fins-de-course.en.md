Some devices operate by themselves, under the effect of a physical quantity: a position, a temperature, a pressure, a level. They send an on/off order.

## The limit switch

The **limit switch** (or position switch) is operated mechanically by the moving part: a cam presses its roller or lever, and its contacts change over. It stops a carriage at the end of travel, detects a closed door, counts passes.

![Roller limit switch: the moving part's cam presses the roller; its contacts 13-14 and 21-22 change over](/static/content/moteurs/en/m4/fin-course.svg)

Like any safety device, a limit switch that stops a dangerous movement uses a **positive-opening break** contact: the cam forces the contact open, even if a spring breaks.

## Thermostat, pressure switch, float

- The **thermostat** switches at a set temperature (heating, motor protection).
- The **pressure switch** switches at a set pressure (compressor, booster pump).
- The **float** (or level switch) switches at a liquid level (tank, sump).

They all have a **switching differential** (hysteresis): they do not switch at the same threshold in both directions. Without this gap, the motor would start and stop endlessly around the threshold.

![Compressor pressure switch: start when pressure falls to 4 bar, stop when it reaches 6 bar; hysteresis is 2 bar](/static/content/moteurs/en/m4/pressostat.svg)

**Example.** A pressure switch set at 6 bar with a 2 bar differential starts the compressor at 4 bar and stops it at 6 bar. The wider the differential, the less often the motor starts, but the more the pressure varies.

## Key points

- Limit switch: operated by the moving part, positive-opening contacts for safety.
- Thermostat, pressure switch, float: on/off at a threshold.
- Hysteresis prevents repeated starts.
