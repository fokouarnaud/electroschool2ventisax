The JFET, seen in Part 1 as a switch, can also amplify. Its great strength: its **gate draws almost no current**, so the circuit input does not load the source.

![Common-source JFET amplifier: C1 and RG of 1 MΩ on the gate, RD of 2.2 kΩ at the drain, RS of 470 Ω bypassed by CS at the source](/static/content/electro/en/m8/jfet-ampli.svg)

## Self-biasing

An N-channel JFET conducts most when VGS = 0 and turns off when VGS reaches its cut-off voltage, here **−4 V**. To amplify, it is placed in between, with the gate slightly negative with respect to the source.

The trick: the gate is tied to ground through RG (1 MΩ, no current flows through it), and a resistor **RS** is placed in the source. The current ID flowing through it lifts the source above ground, which makes the gate negative with respect to the source:

**VGS = −ID × RS**

![Transfer curve: ID is 8 mA at VGS = 0 and falls to zero at −4 V; the quiescent point is around −1.5 V and 3.1 mA](/static/content/electro/en/m8/jfet-courbe.svg)

Example: for a quiescent point at VGS = −1.5 V and ID ≈ 3.1 mA, choose RS = 1.5 V / 3.1 mA ≈ 480 Ω, so **470 Ω** as a standard value. The drain then sits at about 12 − 3.1 mA × 2.2 kΩ ≈ **5.1 V**.

## Gain

For a JFET, we talk about **transconductance** gm: how many milliamps ID changes when VGS changes by 1 V. It is given in millisiemens (mS = mA/V) and read from the datasheet or from the slope of the curve at the quiescent point. With RS bypassed by CS:

**Av ≈ −gm × RD**

With gm = 2.5 mS and RD = 2.2 kΩ: Av ≈ −2.5 × 2.2 = **−5.5**. As with the common emitter, the output is inverted.

## JFET or bipolar?

- The **bipolar** transistor gives more gain for the same current.
- The **JFET** offers a huge input impedance (here, that of RG: 1 MΩ) and little noise: it is found at the front of microphones, probes and measuring instruments.

## Key points

- Self-biasing: RG to ground, VGS = −ID × RS.
- Av ≈ −gm × RD, inverted output.
- The JFET's strength: an input that does not load the source.
