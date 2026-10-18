The circuit biased in the previous section becomes an amplifier as soon as you give it an input and an output. This is the **common-emitter** stage, the most widespread transistor amplifier.

![Common-emitter amplifier: C1 at the input, C2 at the output, RE split into RE1 of 100 Ω and RE2 of 910 Ω, CE of 100 µF across RE2](/static/content/electro/en/m8/ec.svg)

## Coupling capacitors

- **C1** brings the signal to the base without disturbing the bias: it passes AC and blocks DC.
- **C2** picks up the voltage variation at the collector and blocks the 6.5 V DC present there.
- **CE**, the **bypass** capacitor, shorts RE2 for the AC signal, but not for DC.

RE has been split into RE1 = 100 Ω and RE2 = 910 Ω: 1,010 Ω in total, so the quiescent point hardly changes. For the signal, however, only RE1 remains in series with the emitter.

## Voltage gain

The signal adds a small variation vin to the base. The emitter follows it, so the current varies by vin / RE1, and this current flows through RC. The gain is:

**Av ≈ −RC / RE1**

where RE1 is the **unbypassed** part of the emitter resistance. Here, Av ≈ −3,900 / 100 = **−39**. With 50 mV peak at the input, the output is 39 × 0.05 ≈ **1.95 V peak**.

In practice you measure a little less, because the base-emitter junction adds its own small resistance (about 25 mV / IE, so 18 Ω here) to RE1.

[[calc:gain]]

## Inversion

Why the minus sign? When vin rises, IC increases, the voltage drop across RC increases and the collector voltage **falls**. The output is in **antiphase** with the input: a 180° phase shift.

![Two aligned plots: vin of 50 mV peak on top, vout of 1.95 V peak below, falling when vin rises](/static/content/electro/en/m8/inversion.svg)

Without CE, the whole RE (1,010 Ω) would stay in the emitter: Av ≈ −3,900 / 1,010 ≈ −3.9. Bypassing part of RE therefore multiplies the gain by ten while keeping a stable quiescent point.

## Key points

- C1 and C2 pass the signal and block DC; CE bypasses part of RE.
- Av ≈ −RC / RE (unbypassed part).
- The common-emitter output is inverted.
