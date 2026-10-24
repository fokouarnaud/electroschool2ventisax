The principle of the transformer (two windings on a core, Us / Up = Ns / Np) is covered in the Electronics course. Here the focus is the **distribution transformer** that supplies a factory.

## The transformer's rating plate

![Rating plate of a distribution transformer: 630 kVA, 50 Hz, 20 kV / 410 V, 18.2 A / 887 A, vector group Dyn11, short-circuit voltage 4 %, no-load losses 1 kW, load losses 6.5 kW](/static/content/moteurs/en/m3/plaque-transfo.svg)

- **Rated power in kVA**: an apparent power, because the transformer heats according to the current, whatever the load's cos φ.
- **Voltages**: 20 kV on the primary, 410 V no-load on the secondary (slightly more than 400 V, to make up for the voltage drop on load).
- **Rated currents**: I = S / (√3 × U). On the secondary: 630,000 / (1.732 × 410) ≈ **887 A**.
- **Vector group**: Dyn11 (section 5).
- **Short-circuit voltage ucc**: 4 %; it sets the short-circuit current on the secondary, about 887 / 0.04 ≈ 22 kA.

## Losses and efficiency

A transformer has two kinds of losses: **iron losses**, in the core, constant as soon as it is energised (no-load losses), and **copper losses**, in the windings, which grow with the square of the load.

![Efficiency of the 630 kVA transformer versus load: always above 98 %, maximum around 40 % load](/static/content/moteurs/en/m3/rendement.svg)

Efficiency is highest when the two losses are equal. Here: 1 kW = 6.5 kW × x², so x ≈ 0.39: around **40 % load**. An oversized transformer, almost always lightly loaded, wastes its iron losses; an overloaded transformer heats and ages quickly.

For a turns ratio, use the calculator:

[[calc:transformer]]

## Key points

- Power in kVA; I = S / (√3 × U).
- Iron losses constant, copper losses with the square of the load.
- Efficiency highest when iron losses = copper losses.
