IEC 61131-3 defines three timer blocks. Each has an input **IN**, a duration **PT** (preset time, written for example `T#5s`), an output **Q** and an elapsed time **ET**.

## TON: on-delay

![TON block: contact %IX0.2 on IN, PT = T#5s, output Q to coil %QX0.1](/static/content/moteurs/en/m12/ton.svg)

When **IN goes to 1**, the block counts; after PT, **Q goes to 1**. If IN drops before the end, timing restarts from zero. When IN drops, Q drops at once. It is the equivalent of the **on-delay timer relay** (module 8): star-delta changeover, delayed start of a conveyor.

## TOF: off-delay

Q goes to 1 **as soon as IN goes to 1**. When IN drops, Q stays at 1 **for PT**, then drops. It is the **off-delay timer relay**: a fan that keeps running after a motor stops, stair lighting.

## TP: pulse

A rising edge on IN produces on Q a **pulse lasting PT**, however long the button is held. Handy for a 2 s horn before a machine starts.

![Timing diagrams: TON delays Q's rise, TOF delays its fall, TP gives a fixed-length pulse](/static/content/moteurs/en/m12/chronos.svg)

## Example: star-delta

The star-delta changeover of module 9 becomes: %QX0.0 (line) and %QX0.1 (star) on start; a 5 s TON started by %QX0.0; when it has elapsed, %QX0.1 drops and %QX0.2 (delta) rises, with a break contact of %QX0.1 in series for interlocking. The **electrical** interlock between contactors stays wired: safety is never left to the program alone.

## Key points

- TON: Q rises PT after IN; TOF: Q drops PT after IN; TP: a pulse of PT.
- Duration written T#5s, T#500ms.
- Safety interlocks stay wired.
