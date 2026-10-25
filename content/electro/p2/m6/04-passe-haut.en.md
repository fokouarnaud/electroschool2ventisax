Swap the resistor and the capacitor: the capacitor goes in series, the resistor goes to ground, and the output is taken **across the resistor**. This gives an **RC high-pass**.

![High-pass filter: input Vin, 100 nF series capacitor, 1 kΩ resistor to ground, output Vout across the resistor](/static/content/electro/en/m6/passe-haut.svg)

## The opposite of the low-pass

The output ratio becomes:

**Vout / Vin = R / Z = R / √(R² + Xc²)**

- **At low frequencies**, Xc is very large: the capacitor blocks nearly everything, **Vout tends to 0**. In DC, Vout = 0: the high-pass removes the DC component.
- **At high frequencies**, Xc becomes small: the capacitor behaves almost like a wire, **Vout ≈ Vin**.

## What happens in the circuit

The capacitor now sits on the signal path. No electron crosses its insulator: each electron arriving on one plate pushes another one off the opposite plate. A current therefore flows through the resistor while the capacitor charges or discharges, and it stops as soon as the capacitor is charged.

- **At low frequency**, each half-cycle lasts a long time: the capacitor has time to charge almost up to the input voltage. Xc is large, the current stays small and the resistor sees almost no voltage: **Vout tends to 0**. In DC, once the capacitor is charged, no current flows any more: Vout = 0.
- **At high frequency**, the current reverses before the capacitor has had time to charge: its voltage stays close to zero. Xc is small, the current is large and almost all the input voltage ends up across the resistor: **Vout ≈ Vin**.

Water helps to see it. The piston pushes water one way then the other (Vin), against the membrane of a bell placed in series (C). Not a drop crosses the membrane, but as it stretches it drives the same volume of water out of the other side, towards a throttled valve that empties into the tray (R to ground). The pressure gauge reads the pressure before the valve, just as Vout is read across R. Slowly, the membrane follows the whole piston movement and its rod rises and falls over its full travel: the flow through the valve stays small and the needle stays near zero. That small flow is strongest when the piston passes the middle of its stroke, almost a quarter period before its top: the needle leads the piston. Quickly, the membrane barely moves: the water flows back and forth through the valve at full rate and the needle follows the piston. At the cutoff frequency fc = 1 / (2π·R·C) ≈ 1.6 kHz, Xc = R: the needle reaches 0.707 of its travel, with a 45° lead.

[[fig:rc_highpass]]

## Reading the response curve

![Response of a 1 kΩ, 100 nF RC high-pass: Vout / Vin starts at 0, is 0.707 near 1.6 kHz and reaches 1 at high frequencies](/static/content/electro/en/m6/passe-haut-courbe.svg)

## Common uses

- **Coupling capacitor**: passing an audio signal from one stage to the next while blocking the DC bias voltage.
- Removing a low hum (50 Hz) from a higher-pitched signal.
- Keeping only the fast changes of a signal.

## How to remember

Ask where the capacitor sits relative to the output:

- capacitor **to ground**, across the output: it shorts the high frequencies, it is a **low-pass**;
- capacitor **in series**, in the signal's path: it blocks the low frequencies, it is a **high-pass**.

## Key points

- RC high-pass: C in series, output across R.
- Low frequencies (and DC): Vout → 0; high frequencies: Vout ≈ Vin.
- Vout / Vin = R / √(R² + Xc²).
