The **junction field-effect transistor** (JFET) also controls a current, but in a different way: it is driven not by a current but by a **voltage**. Its three leads have other names:

- the **drain** (D), where current enters;
- the **source** (S), where it leaves;
- the **gate** (G), the control electrode.

![N-channel JFET symbol: gate on the left with the arrow pointing in, drain at the top, source at the bottom](/static/content/electro/en/m3/jfet.svg)

## How it works

Between drain and source, current flows through a silicon **channel** (N-type for an N-channel JFET). The gate forms a junction with this channel. By making the gate negative relative to the source, an insulating zone widens and **narrows the channel**: the drain current falls.

- At **VGS = 0**, the channel is wide open: the current is at its maximum, called **IDSS**.
- At **VGS = VGS(off)** (for example −4 V), the channel is completely pinched off: the JFET is **cut off**.

![ID against VGS curve: IDSS = 10 mA at VGS = 0, zero current at VGS(off) = −4 V](/static/content/electro/en/m3/jfet-courbe.svg)

## What changes compared with the bipolar transistor

- The gate, reverse-biased, draws **almost no current**: the JFET does not load the circuit that drives it.
- It conducts **by default** (at VGS = 0) and needs a negative voltage to cut off, whereas a bipolar transistor is off by default.
- Like β for the bipolar transistor, IDSS and VGS(off) vary a lot from one part to another.

## Key points

- JFET: drain, source, gate; voltage control.
- N-channel: conducts at VGS = 0 (IDSS), cut off at a negative VGS(off).
- Gate current almost zero.
