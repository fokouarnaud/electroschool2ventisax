The mains and transformers supply an **alternating voltage**: it changes direction dozens of times per second (50 times in Cameroon). Yet most electronic circuits need direct current. The diode, which lets current through in one direction only, is the ideal tool to **rectify** this voltage.

![12 V AC source, diode and load resistor: half-wave rectifier](/static/content/electro/en/m2/simple-alternance.svg)

## Half-wave rectification

With a single diode in series, only the positive half-cycles reach the load. During the negative half-cycles, the diode is blocked and the output voltage is zero. The output is therefore a series of "bumps", all on the same side.

![Sine input voltage and rectified voltage: only positive half-cycles pass, reduced by 0.7 V](/static/content/electro/en/m2/redresse-courbe.svg)

Notice that each bump is slightly lower than the input: the conducting diode "takes" its 0.7 V on the way. With a 12 V peak, the output tops out around 11.3 V.

## Towards a steady voltage

This voltage no longer changes sign, but it is far from constant. Two improvements are common:

- the **diode bridge** (four diodes) also rectifies the negative half-cycles: this is full-wave rectification;
- a **smoothing capacitor** placed in parallel with the load charges at each peak and fills the dips, as seen in module 1.

## Key points

- A single diode keeps only the positive half-cycles: half-wave rectification.
- The output peak is about 0.7 V lower.
- A diode bridge and a smoothing capacitor bring the output closer to a steady voltage.
