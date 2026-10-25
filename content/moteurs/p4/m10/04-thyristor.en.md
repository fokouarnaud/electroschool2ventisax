The **thyristor** is a diode that is **switched on by command**. It blocks both ways until it is triggered; a current pulse on its **gate** makes it conduct from anode to cathode.

![Thyristor symbol: anode A, cathode K and gate G; a pulse on G makes it conduct, it turns off when its current falls to zero](/static/content/moteurs/en/m10/thyristor.svg)

## It does not turn off by itself

Once triggered, the thyristor **stays on** even if the gate pulse disappears. It only turns off when its current falls below a small value, the **holding current**. On AC, this happens naturally at each zero crossing: that is why the thyristor rules circuits fed by the 50 Hz supply.

## Controlled rectification

By delaying triggering by an angle **α** after the start of each half-cycle, only part of the wave gets through: the **average voltage** falls as α increases.

![Thyristor triggered at α = 60°: only the end of each positive half-cycle reaches the load](/static/content/moteurs/en/m10/angle.svg)

- α = 0°: the thyristor behaves like a diode, maximum average voltage.
- α = 90°: half of each positive half-cycle, average voltage halved.
- α close to 180°: almost nothing left.

A **thyristor bridge** is thus used to adjust the armature voltage of a DC motor (module 11) or to charge batteries.

## Testing it

Thyristor disconnected, multimeter as an ohmmeter: between A and K, very high resistance both ways; between G and K, a junction like a diode. A thyristor that reads "short" between A and K is shorted.

## Key points

- Thyristor: triggered by the gate, turns off when its current falls to zero.
- On AC, it turns off by itself at each zero crossing.
- Delaying the trigger (angle α) reduces the average voltage.
