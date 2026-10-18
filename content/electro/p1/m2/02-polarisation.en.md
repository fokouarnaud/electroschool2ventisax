A diode is said to be **biased** according to the way voltage is applied to it.

## Forward bias

The anode is connected to the **+** side and the cathode to the **−** side. As soon as the voltage exceeds the threshold (about 0.7 V for silicon), the diode conducts: it behaves almost like a wire, with a drop of about 0.7 V across it. The lamp lights up.

![Conducting diode: 6 V cell, diode in the forward direction and lit lamp](/static/content/electro/en/m2/directe.svg)

Careful: a conducting diode does not limit the current. In a real circuit, a resistor or the load itself must set this current, otherwise the diode heats up and is destroyed.

## Reverse bias

Turn the diode round: the cathode is on the **+** side. The depletion zone widens and the diode is **blocked**: the current is practically zero (a few microamperes at most for a silicon diode). The lamp stays off, and almost all of the cell voltage ends up across the diode.

![Blocked diode: same circuit with the diode reversed, no current, lamp off](/static/content/electro/en/m2/inverse.svg)

## A protection tool

This property is used every day: a diode in series at the input of a device protects it from a battery fitted the wrong way round. The price to pay is the 0.7 V drop when everything is connected correctly.

## Key points

- Forward: anode to +, the diode conducts with about 0.7 V across it.
- Reverse: cathode to +, the diode blocks.
- A conducting diode does not limit current: add a resistor.
