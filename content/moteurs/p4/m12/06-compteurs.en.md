A **counter** counts **rising edges**: each 0-to-1 transition of its input. It is used to count parts, cycles, turns.

## CTU: up counter

![CTU block: sensor %IX0.3 on CU, reset %IX0.4 on R, preset PV = 10, output Q to %QX0.2](/static/content/moteurs/en/m12/ctu.svg)

- **CU**: each rising edge adds 1 to the current value **CV**.
- **PV**: the preset. When CV ≥ PV, output **Q goes to 1**.
- **R**: reset; CV returns to 0 and Q drops.

A sensor that stays at 1 in front of a stationary part counts only **once**: only the edge counts.

![Counting: each pass of the sensor adds 1; at the third part (PV = 3), Q goes to 1 and stays there](/static/content/moteurs/en/m12/comptage.svg)

## CTD: down counter

- **CD**: each rising edge subtracts 1 from CV.
- **LD** (load): loads the preset PV into CV.
- **Q goes to 1 when CV ≤ 0**.

Example: a magazine of 20 parts. LD loads 20; each part taken counts down; at 0, Q lights the "magazine empty" indicator.

## Limits

- A pulse shorter than one **scan time** can be missed: for very fast parts or an encoder, a **high-speed counter input** is used.
- Depending on the PLC, a counter value is lost or kept at power-off (**retentive** variable): check this for a production counter.

## Key points

- CTU: counts edges on CU; Q when CV ≥ PV; R resets.
- CTD: counts down on CD; LD loads PV; Q when CV ≤ 0.
- Edges, not levels; high-speed counter for brief signals.
