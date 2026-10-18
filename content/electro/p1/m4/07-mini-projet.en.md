This mini-project closes part 1. It is done in the workshop, with your trainer, and draws on all four modules: voltage divider, LED, transistor and switching.

## Goal

Build a night light that turns on automatically when the light fades.

## Parts

| Quantity | Component |
|---|---|
| 1 | breadboard and wires |
| 1 | 9 V battery and its clip |
| 1 | light dependent resistor (LDR) |
| 1 | BC547 NPN transistor |
| 1 | 47 kΩ trimmer and a 1 kΩ resistor |
| 1 | white LED and a 330 Ω resistor |
| 1 | multimeter |

## Steps

1. Measure the LDR's resistance in the light, then while covering it with your hand. Write down both values.
2. Calculate the LED resistor for about 15 mA from 9 V, with the transistor saturated.
3. Build the divider: 47 kΩ trimmer in series with 1 kΩ at the top, LDR at the bottom, midpoint to the base.
4. Place the LED and its resistor in the collector, emitter to ground.
5. Adjust the trimmer so the LED lights up when you cover the LDR.
6. Measure VBE and VCE in both states (light, dark).

## Measurement table

| State | R LDR | VBE | VCE | LED |
|---|---|---|---|---|
| Light | | | | off |
| Dark | | | | on |

## Going further

Add a second transistor in cascade (section 5) to get the opposite effect: an LED that lights up in the light.
