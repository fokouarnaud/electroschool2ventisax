A badly installed drive trips, disturbs neighbouring equipment or damages the motor. The rules follow the principles of IEC 60364 and the manufacturer's instructions.

## The installation chain

![From upstream to the motor: isolator and fuses, line choke, drive, shielded cable, motor, with a common earth](/static/content/moteurs/en/m11/installation.svg)

- **Isolation and protection** upstream: lockable switch-disconnector and fuses or a circuit breaker of the rating given in the instructions.
- **Line choke** (where needed): it reduces harmonics sent back to the supply and protects the rectifier.
- **No contactor between drive and motor** to control running: start and stop through the drive's inputs. A downstream contactor only opens with the drive stopped.
- **Bypass contactor**: it lets the motor run directly on the supply if the drive fails; it is interlocked with the drive's output contactor so the supply is never fed back into the inverter.

## Electromagnetic compatibility

PWM chops hundreds of volts in fractions of a microsecond: the motor cable radiates interference.

![Shielded motor cable, shield clamped 360° at both ends; power and control cables at least 30 cm apart](/static/content/moteurs/en/m11/cem.svg)

- **Shielded** motor cable, shield bonded **all around its circumference** at both ends (clamps, EMC cable glands).
- **Power** and **control** cables at least 30 cm apart; crossings at right angles.
- Input **EMC filter**, built in or added.
- **Short, wide** earth connections, on an unpainted metal mounting plate.

## Ventilation

A drive loses about 2 to 3 % of the power it transmits: 300 W for an 11 kW motor. Respect the free spaces above and below, and size the enclosure ventilation.

## Key points

- Isolate and protect upstream; do not control running with a downstream contactor.
- Shielded cable clamped 360°, power and control separated, short earth.
- Plan for removing the heat losses.
