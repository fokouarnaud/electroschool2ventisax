A factory of a certain size receives power at HV-A and has its own **distribution substation**.

![Factory substation: HV-A 20 kV incomer, isolation, 630 kVA transformer, main low-voltage board at 400 V and its protected feeders](/static/content/moteurs/en/m3/poste.svg)

- The **HV-A incomer** goes through an isolating and protection device.
- The **transformer** (here 630 kVA) steps 20 kV down to 400 V.
- The **main LV board** shares the energy among **feeders**, each protected by a circuit breaker: workshops, lighting, large motors.

Each feeder in turn supplies sub-distribution boards, closer to the machines. The protection devices are chosen so that, in a fault, **only the breaker closest to the fault** trips: this is **discrimination** (selectivity). So a short circuit on one machine does not stop the whole workshop.

## The motor control centre

When a workshop has many motors (pumps, conveyors, fans), their feeders are grouped in a **motor control centre** (MCC).

![Motor control centre: a vertical busbar supplies drawers, each fitted with a complete motor feeder](/static/content/moteurs/en/m3/mcc.svg)

A busbar supplies identical **drawers**; each contains a complete motor feeder: isolation and protection (Q), contactor (KM), overload relay (F). A faulty drawer is pulled out and replaced in minutes, without stopping the other motors. Everything is grouped, marked and accessible for maintenance.

## Key points

- Factory substation: HV-A incomer, transformer, main LV board, feeders.
- Discrimination: only the breaker closest to the fault trips.
- MCC: one complete drawer per motor, replaceable.
