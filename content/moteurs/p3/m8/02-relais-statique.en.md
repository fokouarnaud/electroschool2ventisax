The **solid-state relay** (SSR) replaces the coil and contacts with electronics.

![Solid-state relay: the 24 V control lights an LED in an optocoupler, which drives a triac connected to the load](/static/content/moteurs/en/m8/ssr.svg)

- On the control side, the signal lights a small **LED** in an **optocoupler**: isolation between control and load is provided by light.
- On the load side, a **triac** (or two thyristors) conducts as long as the control signal is present.

With no moving part, it does not wear, makes no noise, does not bounce and switches very fast: it suits frequent switching (temperature control of a furnace, for example).

## Zero-voltage switching

Most solid-state relays for resistive loads **wait for the voltage to cross zero** before switching. By making or breaking the current when the voltage is zero, they avoid current peaks and interference.

![Zero switching: the order arrives mid half-cycle, the relay waits for the next zero crossing to close](/static/content/moteurs/en/m8/zero.svg)

At 50 Hz, the voltage crosses zero every **10 ms**: switching is delayed by 10 ms at most.

## Its limits

Like the solid-state contactor (module 7), it has a **voltage drop** of about 1 to 1.5 V when conducting and **heats up**: it is mounted on a heatsink above a few amps. It lets a small **leakage current** through when off: a small lamp can stay dimly lit. And it often fails short-circuit: it is never used to isolate.

## Key points

- Optocoupler + triac: isolation by light, no wear.
- Zero voltage: switching delayed by 10 ms at most at 50 Hz.
- Voltage drop, heat and leakage current.
