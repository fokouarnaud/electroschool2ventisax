After smoothing, the voltage still ripples and changes with the load and the mains. For a truly fixed voltage, it must be **regulated**. The simplest solution, already seen in Part 1 (module "The diode"), is the **Zener diode**.

![Zener regulator: Ue of 15 V, series resistor Rs of 200 Ω, 9.1 V Zener and load R of 455 Ω in parallel](/static/content/electro/en/m11/zener.svg)

## Refresher on the principle

A Zener connected in **reverse** holds an almost constant voltage across it, its Zener voltage Uz, as long as enough current flows through it. The series resistor **Rs** takes up the difference between the input voltage and Uz.

## Sizing Rs

The current in Rs splits between the Zener (Iz) and the load (I):

**Rs = (Ue − Uz) / (Iz + I)**

Example: Ue = 15 V, Uz = 9.1 V, a 20 mA load and 10 mA reserved for the Zener. Rs = (15 − 9.1) / 0.03 ≈ 197 Ω, so **200 Ω**.

## Checking the powers

The hardest case for the Zener is **no load**: all the current in Rs goes through it.

- Iz max = (15 − 9.1) / 200 ≈ 29.5 mA, and Pz = 9.1 × 0.0295 ≈ **0.27 W**: choose a 0.5 W Zener.
- In Rs: P = (15 − 9.1)² / 200 ≈ 0.17 W: a 0.25 W resistor is enough, 0.5 W is more comfortable.

## The lower limit

Regulation only holds if the input stays high enough. With the 20 mA load (455 Ω), at least Ue = Uz + Rs × I = 9.1 + 200 × 0.02 ≈ **13.1 V** is needed. Below that, the Zener stops conducting and the output follows the input.

![Output against input: it rises with Ue up to about 13.1 V, then stays fixed at 9.1 V](/static/content/electro/en/m11/zener-courbe.svg)

With a smoothing capacitor, it is the **trough** of the ripple that must stay above this limit.

## The Zener's limits

The Zener regulator wastes current all the time and only suits small currents (a few tens of milliamps). For more, an integrated regulator is used, next section.

## Key points

- Rs = (Ue − Uz) / (Iz + I).
- Check the Zener power with no load: Pz = Uz × Iz max.
- The input must stay above Uz + Rs × I.
