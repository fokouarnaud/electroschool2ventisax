A motor whose insulation deteriorates can make its **frame** live: this is an **insulation fault**. Anyone who then touches the frame suffers an **indirect contact**: they touch a part that should never have been live. Two complementary measures protect them: earthing the exposed parts and automatic disconnection.

## Earthing the exposed parts

All accessible metal parts (motor frames, cabinets, cable trays) are connected to the **protective conductor PE** (green and yellow), itself connected to the earth electrode. In a fault, the current finds an easy path to earth instead of flowing through a person.

![Insulation fault: the phase touches the motor frame; the PE conductor carries the fault current back to the earth electrode](/static/content/moteurs/en/m1/defaut.svg)

Earthing alone is not enough: as long as the fault lasts, the frame stays at a dangerous voltage relative to the ground. The supply must be **cut**, and fast.

## The residual current device (RCD)

The RCD watches the difference between the current leaving on the line and the current returning on the neutral. Without a fault, they are equal. If part of the current escapes to earth (through the PE or through a person), the difference appears and the RCD trips.

![RCD principle: the toroid compares the outgoing current I1 and the returning current I2; if the difference reaches 30 mA, the trip opens the circuit](/static/content/moteurs/en/m1/ddr.svg)

- A **30 mA** RCD (high sensitivity) protects people, including against an accidental direct contact.
- A 300 mA RCD mostly protects installations against fire.
- It is tested regularly with its "test" button.

**Example.** I1 = 10 A and I2 = 9.97 A: the difference is 30 mA, a 30 mA RCD trips. The load current (10 A) plays no part: only the difference counts.

## Key points

- Insulation fault: the frame becomes live; this is called indirect contact.
- Exposed parts connected to PE + automatic disconnection.
- The 30 mA RCD trips as soon as 30 mA leak out of the circuit.
