Every terminal of a device carries an engraved **marking**, and the diagram uses the same markings. They are what lets you wire and troubleshoot without mistakes.

## Contact markings

![IEC markings: power poles 1-2, 3-4, 5-6; make contact 13-14; break contact 21-22; coil A1-A2; overload relay 95-96 and 97-98](/static/content/moteurs/en/m2/contacts.svg)

- **Power poles**: single digits, 1-2, 3-4, 5-6 (odd input, even output).
- **Auxiliary contacts**: two digits. The first is a **sequence number** (1st, 2nd contact of the device), the second gives the **function**: 3-4 for a **make** contact, 1-2 for a **break** contact. Hence 13-14 (first contact, make), 21-22 (second contact, break), 33-34, 43-44…
- **Coil**: A1 and A2.
- **Overload relay**: 95-96 (break contact that cuts the control) and 97-98 (make contact that lights a fault indicator).

The devices themselves carry a letter: **Q** for power isolating and protection devices, **KM** for contactors, **F** for protection (overload relay, fuses), **S** for buttons, **H** for indicators, **M** for motors.

## What happens inside the contactor

Inside the contactor, each contact is made of two fixed contacts, connected to its two terminals, and a bridge that joins them when it covers them. All the bridges are carried by the same moving carriage. When A1-A2 receives its voltage (24 V here), the coil pulls the carriage and all the bridges slide together: poles 1-2, 3-4, 5-6 and contacts 13-14 and 43-44 close, contacts 21-22 and 31-32 open. When the coil is no longer energized, a spring brings the carriage back and everything returns to rest.

"Make" and "break" therefore say what the contact does when the coil is energized, starting from its state at rest: this is why a diagram shows every contact at rest, with the coil de-energized. The second digit of the marking is enough to know it without opening the device: 3-4, open at rest; 1-2, closed at rest. The first digit only numbers the contacts of the block, from 1 to 4.

[[fig:contact_marking]]

## The motor terminal plate

![Terminal plate: inputs U1 V1 W1 at the top, outputs W2 U2 V2 at the bottom, offset by one place](/static/content/moteurs/en/m2/bornes.svg)

A three-phase motor has three windings: U1-U2, V1-V2, W1-W2. On the plate, the outputs are **offset** (W2 under U1, U2 under V1, V2 under W1): this offset lets you make the star and delta connections with simple straight links (section 5).

## What happens on the plate

Each winding joins an input at the back to an output at the front, but not the one just below it: U1 is on the left at the back, U2 in the middle at the front. This offset by one place is what lets you connect the motor with straight links.

In **star**, a horizontal link joins W2, U2 and V2: the three winding ends form the common point, and each winding sits between a phase (L1, L2 or L3, arriving on U1, V1 or W1) and that point. It receives U / √3, about 230 V on a 400 V supply.

In **delta**, three vertical links join U1 to W2, V1 to U2 and W1 to V2: each one joins the start of a winding to the end of another, so the three windings close into a loop. Each one then sits between two phases and receives the whole of U, 230 V on a 230 V supply. If the outputs were not offset (U2 under U1), a vertical link would join the two ends of the same winding: it would short-circuit it instead of connecting it.

[[fig:terminal_plate]]

## Key points

- 13-14 make, 21-22 break, A1-A2 coil, 95-96 overload relay.
- Q, KM, F, S, H, M: the letter gives the device's function.
- Terminal plate: U1 V1 W1 at the top, W2 U2 V2 at the bottom.
