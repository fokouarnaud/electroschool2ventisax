Every terminal of a device carries an engraved **marking**, and the diagram uses the same markings. They are what lets you wire and troubleshoot without mistakes.

## Contact markings

![IEC markings: power poles 1-2, 3-4, 5-6; make contact 13-14; break contact 21-22; coil A1-A2; overload relay 95-96 and 97-98](/static/content/moteurs/en/m2/contacts.svg)

- **Power poles**: single digits, 1-2, 3-4, 5-6 (odd input, even output).
- **Auxiliary contacts**: two digits. The first is a **sequence number** (1st, 2nd contact of the device), the second gives the **function**: 3-4 for a **make** contact, 1-2 for a **break** contact. Hence 13-14 (first contact, make), 21-22 (second contact, break), 33-34, 43-44…
- **Coil**: A1 and A2.
- **Overload relay**: 95-96 (break contact that cuts the control) and 97-98 (make contact that lights a fault indicator).

The devices themselves carry a letter: **Q** for power isolating and protection devices, **KM** for contactors, **F** for protection (overload relay, fuses), **S** for buttons, **H** for indicators, **M** for motors.

## The motor terminal plate

![Terminal plate: inputs U1 V1 W1 at the top, outputs W2 U2 V2 at the bottom, offset by one place](/static/content/moteurs/en/m2/bornes.svg)

A three-phase motor has three windings: U1-U2, V1-V2, W1-W2. On the plate, the outputs are **offset** (W2 under U1, U2 under V1, V2 under W1): this offset lets you make the star and delta connections with simple straight links (section 5).

## Key points

- 13-14 make, 21-22 break, A1-A2 coil, 95-96 overload relay.
- Q, KM, F, S, H, M: the letter gives the device's function.
- Terminal plate: U1 V1 W1 at the top, W2 U2 V2 at the bottom.
