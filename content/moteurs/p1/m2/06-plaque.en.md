The **nameplate** is the motor's identity card. Everything needed to connect it, protect it and replace it is on it.

![Nameplate of a 2.2 kW motor: 230 V delta or 400 V star, 8.3 A or 4.8 A, 1,440 rpm, cos φ 0.81, 50 Hz, efficiency 82 %, IP55, class F, duty S1](/static/content/moteurs/en/m2/plaque.svg)

| Marking | Meaning |
|---|---|
| 230 V Δ / 400 V Y | possible voltages and connections |
| 8.3 A / 4.8 A | rated current for each voltage |
| 2.2 kW | **output** power, mechanical, on the shaft |
| 1,440 rpm | full-load speed (synchronous: 1,500 rpm) |
| cos φ 0.81 | power factor |
| η 82 % | efficiency |
| IP55 | protection against dust and water jets |
| class F | insulation class (155 °C at most) |
| S1 | continuous duty |

## Choosing the connection

One winding of this motor can take **230 V** (the lower of the two voltages). So choose the connection that gives it 230 V.

![Choosing the connection: on a 400 V supply connect in star, on a 230 V supply in delta](/static/content/moteurs/en/m2/tensions.svg)

On the usual 400 V supply, this motor is connected **in star** and draws 4.8 A. A motor marked 400 V Δ / 690 V Y, on the other hand, is connected in delta on that same supply.

## Working out the current

The rated current follows from the other markings: I = P / (√3 × U × cos φ × η) = 2,200 / (1.732 × 400 × 0.81 × 0.82) ≈ **4.8 A**. Check it with the calculator:

[[calc:motor_current]]

## Key points

- The nameplate power is the output power, on the shaft.
- The lower voltage on the plate is the voltage of one winding.
- 400 V supply and 230 V Δ / 400 V Y: star connection.
