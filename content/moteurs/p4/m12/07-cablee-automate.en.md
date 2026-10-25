Moving from relay control to a PLC is done methodically, starting from the existing control diagram.

## The method

![The vertical diagram S1, S2, KM1 becomes a ladder rung: S1 on %IX0.0, S2 on %IX0.1, KM1 on %QX0.0](/static/content/moteurs/en/m12/conversion.svg)

1. **List** the inputs (buttons, limit switches, sensors, overload relay contacts) and outputs (coils, indicators); give each an address and a name in the variable table.
2. **Wire** the inputs and outputs to the PLC.
3. **Translate** each branch of the diagram into a ladder rung: contacts in series and in parallel as before, timers as TON or TOF blocks, auxiliary relays as %MX bits.
4. **Test** without power (contactors without motor or power breaker open), simulating each input and watching the LEDs.

## The break-contact trap

A stop button is wired as a **break contact**, as in wired logic. At rest, its input is 1; in the ladder, it is therefore tested with a **make** contact.

![Stop button wired as a break contact: %IX0.0 is 1 at rest and is tested with a make contact; a broken wire stops the machine](/static/content/moteurs/en/m12/securite.svg)

This is **fail-safe** design: if the wire breaks or the button is disconnected, the input goes to 0 and the machine stops. A stop wired as a make contact would not show it was cut and could no longer stop the machine.

## What stays wired

- The **emergency stop** cuts the output supply directly or goes through a **safety relay** or a safety PLC; it is never left to the standard program alone (module 9).
- **Interlocks** between reversing or star-delta contactors stay wired in addition to the program.
- **Overload relay** contacts cut the coil directly, and are also read by an input to report the fault.

## Benefits and limits

The PLC reduces wiring, makes changes and diagnosis easier (LEDs, variable states online). In return it needs a saved, documented program: always keep an **up-to-date copy** of the program with the machine file.

## Key points

- List, wire, translate, test without power.
- Stop wired as a break contact, tested as make: fail-safe.
- Emergency stop and interlocks stay wired.
