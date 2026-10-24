A motor draws two kinds of power. **Active power P** (in kW) is really turned into mechanical work and heat. **Reactive power Q** (in kvar) magnetises the motor: it flows back and forth between the supply and the motor without being consumed, but it drives current. The supply must deliver the **apparent power S** (in kVA).

## The power triangle

The three powers form a right-angled triangle: S² = P² + Q². The angle φ between P and S gives the **power factor** cos φ = P / S.

![Power triangle: active P horizontal, reactive Q vertical, apparent S as hypotenuse, angle φ between P and S](/static/content/moteurs/en/m3/triangle.svg)

In three-phase: **P = √3 × U × I × cos φ**, **Q = √3 × U × I × sin φ**, **S = √3 × U × I**.

**Example.** An installation draws 100 kW with cos φ = 0.8. S = P / cos φ = 125 kVA and Q = √(125² − 100²) = 75 kvar.

## Losses and correction

A poor cos φ drives more current for the same useful power: cables and transformer heat more, and the supplier often bills the reactive energy. **Capacitors** are then installed to supply part of the reactive power themselves: this is **power factor correction**.

![Correction: with capacitors, Q falls from 75 kvar to 33 kvar for 100 kW, and cos φ rises from 0.8 to 0.95](/static/content/moteurs/en/m3/compensation.svg)

The reactive power to install is: **Qc = P × (tan φ1 − tan φ2)**, where φ1 is the angle before correction and φ2 the target angle.

**Example.** P = 100 kW, cos φ1 = 0.8 (tan φ1 = 0.75), cos φ2 = 0.95 (tan φ2 = 0.329): Qc = 100 × (0.75 − 0.329) ≈ **42 kvar**. After correction, Q is only 33 kvar and S falls from 125 to 105 kVA.

## Key points

- S² = P² + Q²; cos φ = P / S.
- P = √3 × U × I × cos φ in three-phase.
- Correction: Qc = P × (tan φ1 − tan φ2).
