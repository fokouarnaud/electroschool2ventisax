A phone charger, a house doorbell, an amplifier's power supply: they all start by stepping down the 230 V of the mains. The component that does this with no moving parts and almost no losses is the **transformer**.

## Two coils, one core

A transformer puts two windings of insulated wire on the same laminated iron **core**:

- the **primary**, with Np turns, receives the AC voltage Up;
- the **secondary**, with Ns turns, delivers the voltage Us.

![Frame-shaped laminated core, with the primary connected to an AC source on the left leg and the secondary connected to a lamp on the right leg](/static/content/electro/en/m10/principe.svg)

The two windings do not touch. The alternating current in the primary creates a **changing magnetic flux** in the core; this flux passes through the secondary and produces a voltage there: this is **induction**, already met with the inductor in Part 2.

## AC only

A DC voltage creates a constant flux, and a flux that does not change induces nothing: the secondary stays at 0 V. Worse, the primary coil then offers only the low resistance of its wire, and the current becomes huge. **A transformer only works with AC.**

## The turns ratio

Every turn "sees" the same flux change, hence the same voltage. The voltage is therefore shared according to the number of turns:

**Us / Up = Ns / Np**

The ratio **m = Ns / Np** is called the **turns ratio**.

![Transformer symbol: two windings facing each other and two lines for the core, with Up on the left, Us on the right and the relation Us / Up = Ns / Np](/static/content/electro/en/m10/symbole.svg)

Example: a 1,150-turn primary on 230 V and a 60-turn secondary. Us = 230 × 60 / 1,150 = **12 V**, and m = 60 / 1,150 ≈ 0.052.

## Key points

- Primary and secondary are coupled by the core's flux, with no electrical contact.
- A transformer only works with AC.
- Us / Up = Ns / Np; m = Ns / Np.
