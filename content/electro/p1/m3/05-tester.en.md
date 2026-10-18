A doubtful transistor can be checked in a few seconds with a multimeter in **diode mode** (diode symbol on the selector). This mode passes a small current and displays the voltage of the junction under test.

## The two-diode model

For testing, an NPN behaves like two diodes whose anodes are joined at the base: a base-collector diode and a base-emitter diode. For a PNP, both diodes are reversed.

![An NPN seen as two diodes: from the base to the collector and from the base to the emitter](/static/content/electro/en/m3/modele-diodes.svg)

## The procedure for an NPN

1. Red probe (+) on the base, black probe (COM) on the emitter: you read about **0.6 to 0.7 V**.
2. Red probe on the base, black on the collector: about **0.6 to 0.7 V** as well.
3. Swap the probes on these two junctions: the meter shows **OL** (open circuit).
4. Between collector and emitter, both ways: **OL**.

![Multimeter in diode mode, red probe on the base, black probe on the emitter: 0.65 V](/static/content/electro/en/m3/test-be.svg)

## Interpreting

- A reading close to **0 V** on a junction: it is shorted, the transistor is dead.
- **OL** both ways on a junction: it is open.
- If both junctions conduct with the **black** probe on the base, you have a PNP.

This test also finds the base of an unknown transistor: it is the only lead that conducts towards the other two. The base-emitter junction usually reads slightly higher than the base-collector junction.

## Key points

- Diode mode: about 0.65 V on each junction the right way, OL the other way.
- Collector-emitter: OL both ways.
- Near 0 V: short circuit; OL everywhere: open.
