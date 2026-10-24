The **squirrel-cage induction motor** is by far the most widespread motor in industry: rugged, simple, with no sliding contact.

## The cage rotor

Its rotor is a **squirrel cage**: aluminium (or copper) bars housed in a stack of laminations, joined at each end by a short-circuiting ring. No terminal, no wire to the outside.

![Squirrel-cage rotor: aluminium bars joined at each end by a short-circuiting ring](/static/content/moteurs/en/m6/cage.svg)

The stator's rotating field sweeps the bars and **induces** currents in them. These currents, in the field, are subject to Laplace forces: the rotor is dragged along in the direction of the field.

## Slip

If the rotor turned exactly at the speed of the field, the bars would no longer be swept: no more current, no more torque. So the rotor always turns **slightly slower** than the field: it is **asynchronous**. The relative difference is the **slip**:

**s = (ns − n) / ns**

**Example.** ns = 1,500 rpm, n = 1,440 rpm: s = 60 / 1,500 = 0.04, that is **4 %**. At full load, slip is generally 2 to 6 %.

## Torque versus speed

![Induction motor torque versus speed: starting torque, maximum torque around 1,230 rpm, rated point near 1,440 rpm](/static/content/moteurs/en/m6/couple.svg)

At start-up, the motor draws **5 to 8 times its rated current** and delivers a torque close to its rated torque. It accelerates, passes through its **maximum torque**, then settles where its torque equals the load's, close to synchronism. If the load increases, it slows slightly, the slip rises and so does the torque.

## Key points

- Cage rotor: short-circuited bars, no connection.
- s = (ns − n) / ns; 2 to 6 % on load.
- Direct-on-line starting: 5 to 8 times the rated current.
