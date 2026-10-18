This mini-project is done in the workshop, with your trainer. Depending on the equipment available, follow the oscilloscope variant or the multimeter-only variant. Bring your completed measurement table.

## Goal

Build the module's common-emitter amplifier, check its quiescent point, then measure its voltage gain and compare it with the calculation (Av ≈ −RC / RE1 = −39).

## Parts

| Quantity | Component |
|---|---|
| 1 | breadboard and wires |
| 1 | general-purpose NPN transistor (BC547 or 2N2222) |
| 1 | resistor of each value: 47 kΩ, 10 kΩ, 3.9 kΩ, 910 Ω, 100 Ω |
| 2 | 10 µF capacitors (C1, C2) and 1 of 100 µF (CE), 25 V or more |
| 1 | 12 V DC bench supply, or an enclosed 12 V DC mains adapter |
| 1 | signal generator and two-channel oscilloscope (oscilloscope variant) |
| 1 | **enclosed** 230 V to 9 V AC wall adapter and two resistors of 100 kΩ and 1 kΩ (multimeter-only variant) |
| 1 | multimeter |

## Safety

- Only the enclosed units (12 V supply, 9 V AC adapter) are plugged into 230 V. Never open their case and only work on the low-voltage side.
- Switch off the supply before every change to the circuit.
- Respect the polarity of electrolytic capacitors ("−" stripe towards the lower voltage): reversed, a capacitor heats up and can burst.

## Oscilloscope variant

1. Wire the circuit shown in the section "The gain of the common-emitter stage". With no input signal, measure VB, VE and VC with the multimeter and compare with the calculation (2.1 V; 1.4 V; 6.5 V).
2. Set the generator to sine, 1 kHz, 100 mV peak to peak. Channel 1 on the input vin (before C1), channel 2 on the output vout (after C2), common grounds.
3. Read the peak-to-peak amplitudes and calculate abs(Av) = vout / vin. Observe the antiphase.
4. Disconnect CE and measure again: the gain should drop to about 3.9.
5. Put CE back and increase vin until you see clipping. Note the input amplitude at which it appears.

| Measurement | Calculated | Measured |
|---|---|---|
| VB | 2.1 V | |
| VE | 1.4 V | |
| VC | 6.5 V | |
| vin peak to peak | 100 mV | |
| vout peak to peak | 3.9 V | |
| abs(Av) with CE | 39 | |
| abs(Av) without CE | 3.9 | |

## Multimeter-only variant

Without a generator, the signal comes from the 9 V AC adapter, reduced by a divider.

1. Wire the circuit and check VB, VE and VC as in the oscilloscope variant.
2. Connect the adapter to a divider: 100 kΩ in series, then 1 kΩ to ground. With nothing connected, the voltage across the 1 kΩ is about 9 × 1 / 101 ≈ 89 mV rms; it drops a little once the amplifier is connected, which is why vin is measured.
3. Connect this point to C1. Measure on V~ (or mV~) the voltage vin on the C1 side, then vout after C2.
4. Calculate abs(Av) = vout / vin with the rms values and compare with 39. The multimeter does not show the inversion: note it from the course.

| Measurement | Calculated | Measured |
|---|---|---|
| vin rms | ≈ 89 mV unloaded | |
| vout rms | 39 × vin | |
| abs(Av) | 39 | |

## To conclude

Explain why the measured gain is a little below 39, and why it drops when CE is removed.
