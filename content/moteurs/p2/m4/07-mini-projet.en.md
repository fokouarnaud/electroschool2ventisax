This mini-project is done in the workshop, with your trainer. You connect a real industrial sensor and measure its range depending on the metal detected.

## Objective

Connect a three-wire PNP inductive sensor, check its output and measure its sensing distance on several metals.

## Safety

- The whole circuit runs on **24 V DC**, supplied by a 230 V to 24 V **wall adapter**. Never work on the 230 V side.
- Wire with the adapter unplugged; swapping brown and blue can destroy the sensor.

![Mini-project bench: 24 V supply, PNP inductive sensor, black output connected to an LED and its 1 kΩ resistor](/static/content/moteurs/en/m4/banc.svg)

## Equipment

| Quantity | Item |
|---|---|
| 1 | 230 V to 24 V DC wall adapter |
| 1 | three-wire PNP inductive sensor, sn = 8 mm (M18) |
| 1 | LED and 1 kΩ resistor (or 24 V indicator) |
| 4 | small plates of steel, stainless steel, aluminium and copper |
| 1 | rule or caliper |
| 1 | multimeter |

## Oscilloscope variant

1. Wire it: brown to +24 V, blue to 0 V, black to the LED and its resistor, return to 0 V.
2. Channel 1 of the oscilloscope on the black output. Pass a steel plate quickly in front of the sensor: observe the output edges.
3. Spin a disc fitted with a screw in front of the sensor: measure the pulse frequency and work out the rotation speed.

## Multimeter-only variant

1. Same wiring. Multimeter on DC volts between the black output and 0 V.
2. Bring the steel plate slowly closer: note the distance at which the output goes to 24 V.
3. Move it away: note the distance at which the output drops back (hysteresis).
4. Repeat with stainless steel, aluminium and copper.

| Metal | Expected distance | Measured distance |
|---|---|---|
| steel | 8 mm | |
| stainless steel | 5.6 mm | |
| aluminium | 3.2 mm | |
| copper | 2.4 mm | |

## Conclusion

For each metal, calculate the measured correction factor (measured distance / distance measured on steel) and compare it with the values in the course.
