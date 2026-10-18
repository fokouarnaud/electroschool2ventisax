A component carrying a current converts electrical energy, most often into heat. **Power** P, in watts (W), tells how fast it does so:

**P = U × I**

Combined with Ohm's law, this gives two very useful forms for a resistor:

**P = R × I²**   and   **P = U² / R**

![100 Ω resistor on 10 V: I = 0.1 A and P = 1 W](/static/content/electro/en/m1/puissance.svg)

## Example

A 100 Ω resistor is connected to 10 V. The current is 10 / 100 = 0.1 A and the power 10 × 0.1 = **1 W**. An ordinary 1/4 W (0.25 W) resistor would heat up until it burns: here you need a part rated at least 2 W, because you always keep a margin (about twice the calculated power).

## The square that changes everything

In P = R × I², the current is squared: doubling the current multiplies the power by four. That is why a small change in current can be enough to make a component run far hotter than it can stand.

![Power dissipated in 100 Ω: 250 mW at 50 mA, 1 W at 100 mA](/static/content/electro/en/m1/puissance-graph.svg)

## Choosing the right part

Each component has a **maximum power** given by the manufacturer: 0.25 W for small breadboard resistors, 0.5 W or more for larger ones. The battery has limits too: it only supplies a reasonable current before its voltage drops.

## Key points

- P = U × I, in watts; 1 mW = 0.001 W.
- For a resistor: P = R × I² = U² / R.
- Choose a power rating of at least twice the calculated power.
