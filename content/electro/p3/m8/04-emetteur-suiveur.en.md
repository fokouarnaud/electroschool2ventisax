In the **emitter follower** (or common collector), the collector goes straight to the supply and the output is taken from the **emitter**. This circuit does not enlarge the voltage, but it provides another very valuable service.

![Emitter follower: R1 and R2 of 10 kΩ on the base, collector tied to +12 V, RE of 1 kΩ at the emitter, output through C2 from the emitter](/static/content/electro/en/m8/suiveur.svg)

## A gain close to 1

The emitter always stays about 0.7 V below the base. If the base rises by 1 V, the emitter rises by 1 V: the output **follows** the input. The voltage gain is almost 1 (in practice 0.98 or 0.99), and the output is **not inverted**.

With R1 = R2 = 10 kΩ on 12 V: VB = 6 V, VE ≈ 5.3 V and IE ≈ 5.3 V / 1 kΩ = 5.3 mA.

![Base voltage and emitter voltage: the same sine wave, the same amplitude, the emitter shifted down by 0.7 V](/static/content/electro/en/m8/suiveur-signaux.svg)

## What is a gain of 1 good for?

The follower has a **large current gain** (about β). Seen from the input, a resistor RE in the emitter looks β times bigger:

**Zin ≈ β × RE**

With β = 100 and RE = 1 kΩ, the transistor input presents about 100 kΩ, while the output can deliver several milliamps. (The 5 kΩ R1, R2 divider in parallel lowers the input impedance of the whole circuit here; larger divider resistors are chosen when it matters.)

The follower is therefore used as an **adapter** or **buffer**:

- a delicate source (a sensor, a stage with a high output impedance) is hardly loaded;
- a demanding load (a cable, a small loudspeaker, an LED) is fed by the transistor, not by the source.

## Comparing the two circuits

| Circuit | Voltage gain | Output | Use |
|---|---|---|---|
| Common emitter | high (e.g. −39) | inverted | enlarge the voltage |
| Emitter follower | ≈ 1 | not inverted | buffer, drive a load |

They are often combined: a common-emitter stage for gain, followed by an emitter follower to drive the load.

## Key points

- Output on the emitter, collector to the supply: Av ≈ 1, no inversion.
- High input impedance (≈ β × RE), low output impedance.
- The follower is a buffer between a delicate source and a load.
