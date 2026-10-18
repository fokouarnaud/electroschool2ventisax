The JFET introduced in module 3 can also be used as a switch. Its big difference from the bipolar transistor is how it is driven: a **voltage** on the gate, and almost no current.

![N-channel JFET: LED and 470 Ω resistor in the drain, VDD = 9 V; switch K connects the gate to −5 V](/static/content/electro/en/m4/jfet-interrupteur.svg)

## The two states

- **Gate tied to the source** (VGS = 0): the channel is open, the JFET conducts. The LED lights up.
- **Gate taken below VGS(off)** (for example −5 V for a JFET whose VGS(off) is −3 V): the channel is pinched off, the JFET is cut off. The LED goes out.

Mind the direction: an N-channel JFET **conducts at rest** and needs a negative voltage to turn off. It is the opposite of an NPN, which stays off until it receives base current.

![ID against VGS: the JFET conducts at VGS = 0 and turns off below VGS(off) = −3 V](/static/content/electro/en/m4/jfet-blocage.svg)

## A margin to turn it off

VGS(off) varies from part to part: the datasheet gives a range, for example from −0.5 V to −6 V. To guarantee cut-off, the gate voltage must be more negative than the worst value of the range.

## When to prefer the JFET?

- When the control circuit can supply **no current**: the gate draws almost nothing.
- To **switch small signals**, for example to route an audio signal, because the channel behaves like a plain resistor when it conducts.

For high-power loads, the MOSFET transistor is preferred today; you will meet it in a later part.

## Key points

- N-channel JFET: conducts at VGS = 0, cut off below VGS(off).
- A negative gate voltage is needed to turn it off.
- Current-free control: ideal for switching small signals.
