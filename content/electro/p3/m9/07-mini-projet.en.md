This mini-project is done in the workshop, with your trainer. Depending on the equipment available, follow the oscilloscope variant or the multimeter-only variant. Bring your completed measurement table.

## Goal

Make an op-amp Wien bridge oscillate, measure its frequency and compare it with the calculation f = 1 / (2π × R × C), then check that a gain of at least 3 is needed for it to start.

## Parts

| Quantity | Component |
|---|---|
| 1 | breadboard and wires |
| 1 | dual op-amp (TL072 or equivalent) |
| 2 | 9 V batteries and their clips (±9 V supply) |
| 2 | 10 kΩ resistors (R) and 1 of 10 kΩ (Rin) |
| 1 | 47 kΩ potentiometer wired as a variable resistor (Rf) |
| 2 | 16 nF (or 15 nF) film capacitors, and 2 of 1 µF film (multimeter-only variant) |
| 2 | 100 kΩ resistors (multimeter-only variant) |
| 2 | LEDs of different colours and a 1 kΩ resistor |
| 1 | **passive** piezo buzzer (no built-in oscillator) |
| 1 | oscilloscope (oscilloscope variant) |
| 1 | multimeter |

## Safety

- The circuit runs on two 9 V batteries: no connection to 230 V is needed in this mini-project.
- Check the op-amp pinout (notch, pin 1) and the battery polarity before connecting them: an op-amp powered the wrong way round heats up and is destroyed.
- Disconnect one battery before every change to the circuit.

## Oscilloscope variant

1. Calculate f for R = 10 kΩ and C = 16 nF (about 995 Hz).
2. Wire the Wien bridge from the section "Crystals and RC oscillators", with Rf replaced by the potentiometer turned to maximum.
3. Connect the oscilloscope to the output. Slowly turn the potentiometer: note the value of Rf (measured with the ohmmeter, circuit disconnected) at which oscillation starts. Check that it is close to 20 kΩ (a gain of 3).
4. Set Rf just above the threshold for a clean sine wave, then measure the period and calculate f.
5. Connect the passive buzzer to the output through the 1 kΩ resistor: you hear the 1 kHz tone.

| Quantity | Calculated | Measured |
|---|---|---|
| Rf at start-up | 20 kΩ | |
| T | 1.005 ms | |
| f | 995 Hz | |

## Multimeter-only variant

Without an oscilloscope, slow the oscillator down so you can see it.

1. Replace both R with 100 kΩ and both C with 1 µF: f = 1 / (2π × 100,000 × 0.000001) ≈ 1.6 Hz.
2. Connect the two LEDs back to back at the output, in series with the 1 kΩ resistor, to ground: they light up in turn.
3. Count the flashes of one LED over 30 s and work out f (about 48 flashes expected).
4. Put back R = 10 kΩ and C = 16 nF. Measure the output voltage on V~ (the multimeter gives an indicative value at 1 kHz) and listen to the tone on the passive buzzer.

| Quantity | Calculated | Measured |
|---|---|---|
| flashes in 30 s | ≈ 48 | |
| f (slow version) | 1.6 Hz | |
| Rf at start-up | 20 kΩ | |

## To conclude

Explain why the oscillator does not start while Rf is below about 20 kΩ, and why the sine wave becomes distorted when Rf is increased too much.
