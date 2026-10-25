Power electronics switches a motor's energy instead of dissipating it. It all starts with the **diode**: it lets current flow from anode to cathode and blocks it the other way. This module gives a quick recap; for the details, see the [Electronics course in the catalogue](/en/catalogue/), Part 1.

## The single-phase diode bridge

Four diodes in a **bridge** rectify both half-cycles: during one, two diodes conduct; during the other, the other two do. The load gets a current that always flows the same way.

![Bridge of four diodes fed by an AC source; the load is connected across the two bridge outputs](/static/content/moteurs/en/m10/pont.svg)

The voltage obtained is **DC but rippled**: it rises twice per period. A smoothing capacitor makes it almost constant.

## The three-phase bridge

In a drive or an industrial charger, the three-phase supply is rectified with **six diodes**. The DC voltage obtained is about:

**Udc ≈ 1.35 × U** (U: line-to-line voltage)

On a 400 V supply: 1.35 × 400 ≈ **540 V**. The ripple is small, because six "humps" follow each other in each period.

![Output voltage of a three-phase bridge: six humps per period, around 540 V on a 400 V supply](/static/content/moteurs/en/m10/triphase.svg)

## Choosing a power diode

Two values matter: the **average current** it carries and the maximum **reverse voltage** it withstands when blocking. Take a comfortable margin on both, and mount it on a **heat sink**: a power diode drops about 1 V, so 10 W is lost at 10 A.

## Key points

- 4-diode bridge: rectifies both half-cycles.
- 6-diode three-phase bridge: Udc ≈ 1.35 × U, about 540 V on 400 V.
- Choose a diode by its average current and reverse voltage, with a heat sink.
