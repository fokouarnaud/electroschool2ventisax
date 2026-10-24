The **contactor** is the remote-controlled switch for motors: a small power (its coil, often at 24 V) controls the opening and closing of a power circuit (the motor, at 400 V).

## Its construction

![Contactor construction: magnetic circuit with its coil, moving armature, return spring and main contacts](/static/content/moteurs/en/m7/constitution.svg)

- The fixed **magnetic circuit** carries the **coil**. When energised, it pulls in the **moving armature**.
- The armature drives the **main contacts** (or poles), which close.
- When the coil is de-energised, a **return spring** pulls the armature back and opens the contacts.

So the contactor is **monostable**: it only stays closed while its coil is energised. A power cut makes it drop out, which protects against unexpected restarts.

## One device in three roles

![Symbol of contactor KM1: coil A1-A2, three power poles 1-2, 3-4, 5-6, auxiliary contacts 13-14 and 21-22](/static/content/moteurs/en/m7/symbole.svg)

On diagrams, the contactor appears in several places, always with the same tag (KM1):

- its **coil** A1-A2 in the control circuit;
- its **power poles** 1-2, 3-4, 5-6 in the power circuit;
- its **auxiliary contacts** (13-14 make, 21-22 break) in the control circuit: hold-in, interlocks, signalling.

The coil closes properly between **85 % and 110 %** of its rated voltage Uc: too low a control voltage makes the contactor pull in poorly, so it chatters and heats.

## Key points

- A coil that pulls in an armature; a spring that pulls it back.
- Monostable: without current, the contactor opens.
- One tag, three places: coil, poles, auxiliaries.
