**Biasing** a transistor means supplying the voltages and currents that put it in the desired state. The simplest circuit uses a base resistor RB connected to a control voltage VBB.

![Base-resistor biasing: VBB = 5 V, RB = 100 kΩ, RC = 1 kΩ, VCC = 12 V](/static/content/electro/en/m3/polarisation.svg)

## Calculating the base current

The base-emitter junction is a conducting diode: it keeps about **0.7 V** across it. Resistor RB therefore gets VBB − 0.7, and Ohm's law gives:

**IB = (VBB − 0.7) / RB**

Example: VBB = 5 V and RB = 100 kΩ. IB = 4.3 V / 100 kΩ = **43 µA**.

## Working out the collector current

With β = 100: IC = 100 × 43 µA = **4.3 mA**. The collector resistor RC = 1 kΩ then takes RC × IC = 4.3 V, leaving between collector and emitter:

**VCE = VCC − RC × IC = 12 − 4.3 = 7.7 V**

If this calculation gave a negative VCE, the transistor could not supply the requested current: it would be saturated (next section).

[[calc:bias]]

## Checking by measurement

Two ammeters let you measure IB and IC at the same time. Their ratio gives the real β of the part under test.

![Same circuit with one ammeter in the base and another in the collector](/static/content/electro/en/m3/polarisation-mesures.svg)

## Key points

- VBE ≈ 0.7 V: IB = (VBB − 0.7) / RB.
- IC = β × IB, then VCE = VCC − RC × IC.
- Real β = measured IC / measured IB.
