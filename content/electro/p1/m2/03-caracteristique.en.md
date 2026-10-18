A diode's **characteristic** is the curve of the current through it against the voltage across it. It sums up its whole behaviour.

![Current-voltage curve of a silicon diode: no current in reverse, then a sharp rise near 0.7 V](/static/content/electro/en/m2/caracteristique.svg)

## Reading the curve

- **In reverse** (negative voltage), the current stays almost zero: the diode blocks.
- **Forward, below the threshold**, the current remains very small.
- **Around 0.7 V**, the curve turns sharply upwards: a little extra voltage makes the current soar. That is why the voltage across a conducting diode is considered roughly constant, between 0.6 and 0.8 V depending on the current.

It is not a straight line: a diode **does not follow Ohm's law**. Its current is not calculated with U / R, but from the rest of the circuit.

## The practical calculation

In a loop with a resistor, subtract the diode threshold, then apply Ohm's law to the resistor:

**I = (E − 0.7) / R**

Example: 5 V cell, 470 Ω resistor. I = (5 − 0.7) / 470 ≈ **9.1 mA**. A voltmeter across the diode reads about 0.7 V.

![5 V cell, 470 Ω resistor and conducting diode, voltmeter across the diode reading about 0.7 V](/static/content/electro/en/m2/mesure.svg)

## Key points

- The characteristic is not a straight line: no Ohm's law for the diode.
- Conducting diode: about 0.7 V across it, whatever the current.
- I = (E − 0.7) / R in a loop with a resistor.
