The **operational amplifier** (op-amp) is an integrated circuit containing dozens of transistors that are already biased. No more worrying about quiescent points: two resistors are enough to set an accurate gain.

## A huge gain, kept under control

The op-amp has two inputs, **−** (inverting) and **+** (non-inverting), and one output. It amplifies the difference between its inputs with a huge gain, around 100,000. Used as it is, it saturates at the slightest difference.

So part of the output is fed back to the − input: this is **negative feedback**. The op-amp then adjusts its output so that its two inputs stay at almost the same voltage, and the gain depends only on the resistors.

## The inverting amplifier

The signal reaches the − input through Rin; Rf connects the output to the − input; the + input is grounded.

**Av = −Rf / Rin**

![Inverting op-amp: Rin of 10 kΩ at the input, Rf of 47 kΩ from the output to the minus input, plus input grounded](/static/content/electro/en/m8/aop-inverseur.svg)

With Rin = 10 kΩ and Rf = 47 kΩ: Av = −47 / 10 = **−4.7**. An input of 0.5 V gives −2.35 V.

## The non-inverting amplifier

The signal reaches the + input; Rf goes from the output to the − input, and Rin from the − input to ground.

**Av = 1 + Rf / Rin**

![Non-inverting op-amp: the signal on the plus input, Rf of 47 kΩ from the output to the minus input, Rin of 10 kΩ from the minus input to ground](/static/content/electro/en/m8/aop-non-inverseur.svg)

With the same resistors: Av = 1 + 4.7 = **5.7**, without inversion. If Rf = 0 (a plain wire) and there is no Rin, Av = 1: this is the op-amp **follower**, a perfect buffer.

[[calc:gain]]

## The limit: the power supply

The output cannot go beyond the supply voltages. Powered from ±12 V, a common op-amp delivers at most about ±10.5 V. With a gain of −4.7, an input of 3 V would require −14.1 V: the output **saturates** around −10.5 V and the signal is clipped.

## Key points

- Inverting: Av = −Rf / Rin. Non-inverting: Av = 1 + Rf / Rin.
- Negative feedback makes the gain accurate: it depends only on the resistors.
- The output stays limited by the power supply.
