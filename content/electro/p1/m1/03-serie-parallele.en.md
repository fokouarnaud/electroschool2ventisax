Few circuits contain a single resistor. Two basic arrangements let you replace several resistors with one, called the **equivalent resistance** (Req).

## In series: resistances add up

Resistors are in series when **the same current** flows through them, one after the other. Their equivalent resistance is the sum:

**Req = R1 + R2 + R3**

![Three resistors of 1 kΩ, 2.2 kΩ and 3.3 kΩ in series: Req = 6.5 kΩ](/static/content/electro/en/m1/serie.svg)

With 12 V across the three resistors above, the current is 12 V / 6.5 kΩ ≈ 1.85 mA. The voltage is then shared: each resistor gets R × I, and the three voltages add up to 12 V again.

## In parallel: the equivalent resistance goes down

Resistors are in parallel when they are connected **between the same two points**: they all have the same voltage. You add their reciprocals:

**1 / Req = 1 / R1 + 1 / R2**   and, for two resistors,   **Req = (R1 × R2) / (R1 + R2)**

![4 kΩ and 12 kΩ in parallel: Req = 3 kΩ](/static/content/electro/en/m1/parallele.svg)

Example: 4 kΩ and 12 kΩ in parallel give 48 / 16 = **3 kΩ**. The equivalent resistance is always **smaller than the smallest** resistor: you have opened one more path for the current. Two equal resistors in parallel are worth half of one of them.

## Reading a resistor's value

Small resistors carry colour bands: two digits, then a multiplier. Yellow (4), violet (7), red (× 100) gives 4,700 Ω, that is 4.7 kΩ.

[[calc:resistor]]

## Key points

- Series: same current, resistances add up.
- Parallel: same voltage, Req is smaller than the smallest resistor.
- Two equal resistors R in parallel are worth R / 2.
