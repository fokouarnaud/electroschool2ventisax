Ohm's law links the three quantities of the previous section. For a resistor, the voltage across it is proportional to the current through it:

**U = R × I**   so   **I = U / R**   and   **R = U / I**

Always work with consistent units: volts, amperes and ohms, or volts, milliamperes and kilohms (kΩ × mA gives volts directly).

![4.7 kΩ resistor supplied with 12 V, current I to be calculated](/static/content/electro/en/m1/ohm-circuit.svg)

## Example

A 4.7 kΩ resistor is connected to 12 V. The current is I = 12 / 4,700 = 0.002 55 A, that is **2.55 mA**. With "electronics" units: 12 V / 4.7 kΩ = 2.55 mA, with no conversion at all.

## A straight line that reveals the resistance

If you plot voltage against current for a resistor, you get a straight line through the origin. The larger the resistance, the steeper the line: for the same current, more voltage is needed.

![U against I lines for 1 kΩ and 2 kΩ; the steeper one is 2 kΩ](/static/content/electro/en/m1/ohm-graph.svg)

A component whose curve is not a straight line (a diode, a filament lamp) does not follow Ohm's law over its whole range: you cannot give it a single resistance value.

Try the calculator: fill in two quantities and the third one appears.

[[calc:ohm]]

## Key points

- U = R × I: remember this form, the other two follow from it.
- V, mA and kΩ go together without conversion.
- A resistor's characteristic is a straight line through the origin.
