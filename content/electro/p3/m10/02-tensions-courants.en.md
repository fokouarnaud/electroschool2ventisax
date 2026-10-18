A transformer changes the voltage, but it does not create energy. If the voltage goes down, the current must go up by the same factor.

## Step-down or step-up

- **Ns < Np**: the voltage goes down, it is a **step-down** transformer (230 V to 12 V).
- **Ns > Np**: the voltage goes up, it is a **step-up** transformer (12 V to 230 V in a car inverter, or the high voltage of a gas lighter).

![Two symbols: on the left a primary longer than the secondary, step-down; on the right a longer secondary, step-up](/static/content/electro/en/m10/types.svg)

## The currents

For an ideal transformer, the power going into the primary comes out of the secondary: Up × Ip = Us × Is. The current ratio is therefore **the inverse** of the voltage ratio:

**Is / Ip = Np / Ns**

The low-voltage side is the **high-current** side, and the other way round. That is why the secondary wire of a step-down transformer is thicker than the primary wire.

![Step-down 230 V to 12 V loaded with 12 Ω: the secondary delivers 1 A, the primary draws only about 52 mA](/static/content/electro/en/m10/abaisseur.svg)

Example: 230 V to 12 V, with a 12 Ω load on the secondary.

1. Secondary current: Is = 12 V / 12 Ω = **1 A**.
2. Primary current: Ip = Is × Us / Up = 1 × 12 / 230 ≈ **52 mA**, about 19 times less.

The transformer does not "push" current by itself: the **load** on the secondary sets Is, and the primary adjusts. With no load, the primary draws only a very small no-load current.

[[calc:transformer]]

## Key points

- Ns < Np: step-down; Ns > Np: step-up.
- Us / Up = Ns / Np and Is / Ip = Np / Ns.
- The load sets the secondary current; the primary follows.
