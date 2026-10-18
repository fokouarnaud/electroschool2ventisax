A microphone produces a few millivolts, an antenna even less. To move a loudspeaker cone or drive the input of a converter, you need a much bigger signal. That is the job of the **amplifier**: it reproduces the shape of the input signal, only bigger.

![Block diagram: a small 50 mV peak signal enters triangle A, the power supply comes in from the top, a 2 V peak signal comes out](/static/content/electro/en/m8/bloc.svg)

## Where does the energy come from?

The amplifier does not create energy. It draws on its **power supply** (a battery, a 12 V supply) and uses it to build an enlarged copy of the signal. The transistor acts like a tap: a small base current controls a large collector current, supplied by the power supply.

## Gain

**Gain** tells you how many times the signal is enlarged. It is written A and has no unit:

- voltage gain: **Av = vout / vin**;
- current gain: **Ai = iout / iin**;
- power gain: **Ap = Av × Ai**.

Example: 50 mV peak at the input, 2 V peak at the output. Av = 2 / 0.05 = **40**. If the current is also multiplied by 25, the power is multiplied by 40 × 25 = 1,000.

![Both signals on the same axes: vin, tiny, and vout, forty times bigger](/static/content/electro/en/m8/signaux.svg)

Always compare values of the same kind: peak with peak, or rms with rms. The ratio stays the same.

## The sign of the gain

Some circuits give an **inverted** output: when the input rises, the output falls. Their gain is negative, for example Av = −39. The sign only says that the output is in antiphase; the **absolute value** (39) says how much the signal is enlarged. In the exercises, read carefully whether you are asked for the gain "as an absolute value" or "with its sign".

## Key points

- An amplifier enlarges a signal using energy taken from its power supply.
- Av = vout / vin, no unit; Ap = Av × Ai.
- A negative gain means an inverted output.
