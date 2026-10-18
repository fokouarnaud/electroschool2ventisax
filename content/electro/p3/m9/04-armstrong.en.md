In the **Armstrong** oscillator, feedback goes through a small **transformer**: a feedback winding, magnetically coupled to the inductor of the tuned circuit, sends the signal back to the amplifier input.

![Armstrong oscillator: the tuned circuit L and C of 10 nF at the amplifier output, coupled to a feedback winding connected to its input](/static/content/electro/en/m9/armstrong.svg)

## What each part does

- The **tuned circuit** (primary inductor L and capacitor C) sets the frequency: f = 1 / (2π × √(L × C)).
- The **feedback winding**, wound on the same former, picks up part of the magnetic field and sends it back to the input. Its number of turns sets how much signal is fed back.

Example: L = 1 mH and C = 10 nF give f = 1 / (2π × √(1 mH × 10 nF)) ≈ **50.3 kHz**.

## Winding direction matters

The transformer can return a voltage in phase or in antiphase, depending on which way the feedback winding is connected. On diagrams, a **dot** marks the start of each winding: two dots on the same side mean voltages in phase.

![Two transformers: dots on the same side, the output is in phase with the input; opposite dots, it is in antiphase](/static/content/electro/en/m9/points.svg)

If the amplifier inverts, the transformer must invert too so that the loop comes back in phase. An Armstrong that refuses to oscillate often has its feedback winding connected the wrong way round: **swap its two wires**, and it starts.

## Where is it found?

The Armstrong is historic: it was one of the first valve oscillators, used in early radio sets. It remains an excellent example for understanding feedback, because the path of the returned signal is easy to see.

## Key points

- Armstrong: LC tuned circuit at the output, coupled feedback winding to the input.
- f = 1 / (2π × √(L × C)).
- The winding dots show the phase; reversing the feedback winding can start the oscillation.
