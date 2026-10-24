A motor can be destroyed in two ways: by a **short circuit** (huge current, in a fraction of a second) or by an **overload** (current slightly too high, but for minutes, which cooks the insulation). It is protected against both.

## Against short circuits

Type **aM fuses** (motor rated, which let the starting current through) or the **magnetic** trip of a motor circuit breaker clear the short circuit in a few milliseconds.

## Against overloads: the overload relay

The **overload relay** continuously measures the current in each phase. If the current exceeds its **setting** for long enough, it opens its 95-96 contact, placed in the control circuit: the contactor drops out. It reacts faster the heavier the overload; it also detects the loss of a phase.

![Trip curves: class 10 trips within 10 s at 7.2 times the setting, class 20 within 20 s](/static/content/moteurs/en/m7/declenchement.svg)

The **trip class** says how quickly it trips at 7.2 times its setting (the current of a stalled motor): **class 10**, within 10 s, for normal starts; **class 20**, within 20 s, for long starts (high inertia: fan, crusher), otherwise the relay would trip during every start.

## Setting

![Setting the overload relay: the dial is set to 4.8 A, the rated current read on the motor plate, within a 4 to 6 A range](/static/content/moteurs/en/m7/reglage.svg)

The relay is set to the **motor's rated current** read on its plate, for the supply voltage (4.8 A for the module 2 motor connected in star on 400 V), with no margin added. Choose a relay whose range brackets this current. The calculator below works out this current from the plate:

[[calc:motor_current]]

After a trip, find the cause (stalled motor, lost phase, excessive load) **before** resetting.

## Key points

- Short circuits: aM fuses or magnetic trip; overloads: overload relay.
- Class 10 normal, class 20 for long starts.
- Setting = nameplate current, no margin.
