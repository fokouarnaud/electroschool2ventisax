The human body conducts current. What injures is not the voltage itself but the **current flowing through the body**, its duration and its path. The voltage sets that current through the body's resistance.

## Very low thresholds

At 50 Hz AC, a few milliamps are enough to cause serious effects. The values below are orders of magnitude for an adult and a contact of a few seconds: they vary from one person to another.

![Indicative thresholds: perception around 0.5 mA, cannot let go around 10 mA, breathing stops around 30 mA, fibrillation around 75 mA](/static/content/moteurs/en/m1/seuils.svg)

- **0.5 mA**: a tingling is felt.
- **10 mA**: the hand muscles contract, you can no longer let go of the conductor.
- **30 mA**: breathing can stop. This is the value chosen for the residual current devices that protect people.
- **75 mA and above**: risk of heart fibrillation, fatal without quick help.

Duration matters as much as intensity: the longer the contact, the lower the dangerous threshold. So does the path: a current crossing the chest (hand to hand, hand to feet) is the most dangerous.

## Calculating the current through the body

Apply Ohm's law to the body: I = U / R. The body's resistance between a hand and the feet is about 1,000 Ω for damp skin, more for dry skin, much less with a wound.

![Direct contact with a 230 V phase: the current flows through the hand, the body and the feet, then returns through the ground](/static/content/moteurs/en/m1/corps.svg)

**Example.** A person touches a 230 V phase, barefoot on a damp floor (R ≈ 1,000 Ω). I = 230 / 1,000 = 0.23 A, that is **230 mA**: far above the fibrillation threshold. At 24 V, in the same conditions, I = 24 / 1,000 = 24 mA: still unpleasant, but below the breathing threshold, and in practice dry skin cuts this current to a few milliamps. That is why every circuit in this course is wired at **extra-low voltage, 24 V at most**.

## Key points

- Current kills: 30 mA can stop breathing.
- I = U / R with R ≈ 1,000 Ω for a damp body.
- Duration and path make it worse; working de-energised remains the first protection.
