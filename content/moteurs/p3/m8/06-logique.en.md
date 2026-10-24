With contacts, **logic functions** can be built: this is **wired logic**, the ancestor of the PLC (module 12). A contact operated or a lamp lit is written 1, otherwise 0.

## AND, OR, NOT

![AND function: two contacts A and B in series; the lamp lights only if A and B are operated](/static/content/moteurs/en/m8/et.svg)

- **AND**: contacts **in series**. The lamp lights if A **and** B are operated. Example: a press that only comes down if the operator presses two buttons at once, one hand on each (two-hand control).

![OR function: two contacts A and B in parallel; the lamp lights if A or B is operated](/static/content/moteurs/en/m8/ou.svg)

- **OR**: contacts **in parallel**. The lamp lights if A **or** B (or both) is operated. Example: several start buttons for the same motor (module 9).

![NOT function: a break contact; the lamp is lit as long as A is not operated](/static/content/moteurs/en/m8/non.svg)

- **NOT**: a **break** contact. The lamp is lit as long as A is **not** operated.

## Truth tables

| A | B | AND | OR | NAND | NOR |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 | 0 |

- **NAND**: two **break contacts in parallel**; the lamp only goes out if A and B are both operated.
- **NOR**: two **break contacts in series**; the lamp goes out as soon as A or B is operated. This is the logic of **stops**: several stop buttons in series, any of them can stop everything.

## Key points

- Series = AND, parallel = OR, break contact = NOT.
- Stops in series (NOR), starts in parallel (OR).
- The truth table gives the output for every combination.
