Two small transformers do great service in a cabinet: the current transformer, to measure, and the control transformer, to supply the control circuits safely.

## The current transformer (CT)

You do not pass 200 A through a panel ammeter. The **current transformer** uses the conductor itself as its primary, passing through a toroid; its secondary delivers a **proportional**, standard current, usually **5 A** (or 1 A) for the rated primary current.

![200/5 A current transformer: the conductor passes through the toroid, the secondary feeds a 5 A ammeter](/static/content/moteurs/en/m3/tc.svg)

A 200/5 A CT divides the current by 40. **Example**: the ammeter reads 3.5 A; the current in the conductor is 3.5 × 200 / 5 = **140 A**.

**Safety rule:** **never** leave a CT secondary open while current flows in the primary. The CT would try to force its current into an infinite resistance: a very high voltage would appear across it. Before disconnecting the ammeter, short-circuit the secondary (a shorting terminal block is provided for this).

**Voltage transformers** (VT) are also used to measure HV-A voltages with instruments designed for 100 V.

## The control transformer

Control circuits (buttons, coils, indicators) are supplied by a 400 V / 24 V (or 230 V / 24 V) **control transformer**, protected by a fuse.

![400 V / 24 V control transformer: it isolates the control circuit from the supply and feeds it at extra-low voltage](/static/content/moteurs/en/m3/commande-24v.svg)

It brings two things: **isolation** from the supply (primary and secondary are not electrically connected) and an **extra-low voltage** that protects the operator touching a button. Its power is chosen from the coils it supplies, allowing for their inrush when closing.

## Key points

- 200/5 A CT: real current = reading × 200 / 5.
- A CT secondary is never open in service.
- Control transformer: isolation and ELV for the control circuit.
