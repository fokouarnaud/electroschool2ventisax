The **relay** is the contactor's little brother: same principle (a coil that pulls an armature), but contacts designed for **small currents**, a few amps. It does not switch motors; it **processes the control signals**: multiply an order, invert a state, isolate two circuits.

![Electromechanical relay: the 24 V coil pulls the armature, which moves the common from the break contact to the make contact](/static/content/moteurs/en/m8/relais.svg)

Its most common contact is the **changeover**: a common that touches the **break** contact when the coil is de-energised, and switches to the **make** contact when it is energised.

![Changeover contact of relay KA1: common 11, break 12, make 14](/static/content/moteurs/en/m8/inverseur.svg)

Relays are tagged **KA**. Their contacts are numbered like a contactor's: 11-12-14 for a first changeover (11 common, 12 break, 14 make), 21-22-24 for the second.

## Why a relay

- **Isolate**: the coil (24 V DC) and the contacts (a 230 V AC load, for example) have no electrical link.
- **Amplify**: a 0.5 A PLC output controls, through a relay, a more powerful circuit.
- **Multiply**: a single order closes several contacts, towards several circuits.

**Example.** A 0.4 W, 24 V relay coil draws I = P / U = 0.4 / 24 ≈ **17 mA**: a PLC output drives it easily.

## Key points

- Relay: small currents, signal processing; tag KA.
- Changeover: 11 common, 12 break, 14 make.
- It isolates, amplifies and multiplies an order.
