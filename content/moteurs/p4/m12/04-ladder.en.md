**Ladder** (ladder diagram, LD) draws the program like an electrical diagram on its side: two vertical **rails** and, between them, horizontal **rungs**. The logical "current" flows from left to right.

## The elements

- **Make contact** `-| |-`: passes when the bit read is 1.
- **Break contact** `-|/|-`: passes when the bit read is 0.
- **Coil** `-( )-`: writes 1 to its bit when the rung passes, 0 otherwise.
- Contacts **in series**: AND function; contacts **in parallel**: OR function (module 8).

## Start-stop with hold-in

![Start-stop rung: contact %IX0.0 (stop), then %IX0.1 (start) paralleled by contact %QX0.0, then coil %QX0.0](/static/content/moteurs/en/m12/maintien.svg)

- Stop S1 is wired as a **break contact**: at rest, %IX0.0 is 1. In the program, it is therefore tested with a **make** contact.
- Pressing start (%IX0.1 = 1) makes the rung pass: %QX0.0 goes to 1.
- Contact **%QX0.0**, in parallel with start, keeps the rung passing when released: this is the **hold-in**, like a contactor's 13-14 (module 9).
- Pressing stop takes %IX0.0 to 0: the rung opens, the output drops.

## SET and RESET coils

![Coil S: %IX0.1 sets %QX0.0 to 1; coil R: %IX0.0 resets it to 0](/static/content/moteurs/en/m12/set-reset.svg)

An **S** (SET) coil sets its bit to 1 and leaves it there, even when the rung stops passing. An **R** (RESET) coil sets it back to 0. The effect is the same as a hold-in. If both rungs are true at the same time, the **last** one in the program wins: place RESET after SET so that stop has priority.

## Reading rules

- An output should be written by a coil **in only one place** in the program (except SET and RESET pairs).
- Rungs run from **top to bottom**, in scan order.

## Key points

- Make contact: true if the bit is 1; break contact: true if the bit is 0.
- Series = AND; parallel = OR.
- Hold-in: output contact in parallel with start; or SET and RESET.
