The sensors of the previous section say **yes or no**. Others measure a **value**: a temperature, a speed, a position.

## Measuring a temperature

The **Pt100 probe** is a platinum wire whose resistance is **100 Ω at 0 °C** and rises by about **0.385 Ω per degree**: R ≈ 100 × (1 + 0.00385 × T).

![Pt100 probe: 100 Ω at 0 °C, 138.5 Ω at 100 °C, an almost perfect straight line](/static/content/moteurs/en/m4/pt100.svg)

**Example.** A reading of 119.25 Ω gives T = (119.25 / 100 − 1) / 0.00385 = **50 °C**. **Thermocouples** (two welded metals that produce a small voltage) measure higher temperatures. Motor windings also carry **PTC thermistors**, which change resistance sharply at a given temperature and drive a protection relay.

## Measuring a speed and a position

The **incremental encoder** is a slotted disc mounted on the shaft; a light beam passing through the slots produces **one pulse per slot**.

![Incremental encoder: the slotted disc breaks a beam; each slot produces a pulse](/static/content/moteurs/en/m4/codeur.svg)

With N pulses per revolution: speed (rev/s) = pulses per second / N. **Example**: a 500-pulse encoder delivers 1,000 pulses in one second: 1,000 / 500 = 2 rev/s, that is **120 rpm**. Counting pulses from a reference position also gives the position. An **absolute encoder** gives the position directly as a digital code, even after a power cut.

For simple rotation monitoring, a **tachogenerator** gives a voltage proportional to speed.

## Key points

- Pt100: 100 Ω at 0 °C, + 0.385 Ω per degree.
- Encoder: speed = pulses per second / pulses per revolution.
- Absolute encoder: position kept after a power cut.
