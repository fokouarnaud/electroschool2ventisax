**Direct-on-line starting** connects the motor in one go to the full supply voltage. It is the simplest and most widespread: the power circuit from module 2, start/stop control with hold-in.

## Control from several stations

A long machine can have several control stations. The rule follows from wired logic (module 8):

![Control from two stations: stops S1 and S3 in series, starts S2 and S4 in parallel with the hold-in contact KM1](/static/content/moteurs/en/m9/postes.svg)

- **stop** buttons are wired **in series**: any of them de-energises the coil;
- **start** buttons are wired **in parallel**, with the **hold-in** contact: any of them energises it.

## The starting current

![Direct-on-line starting current: about 7 times the rated current during acceleration, then the running current](/static/content/moteurs/en/m9/courant-direct.svg)

During acceleration, the motor draws **6 to 8 times its rated current**. **Example**: a 10 A motor draws about 70 A for one to a few seconds. This peak causes a **voltage drop** on the line (lamps on the same supply dim), and a mechanical jolt on the machine (belts, gears).

So direct-on-line starting suits **small and medium** motors, on a supply that can take this inrush, and machines that accept a sudden start. Beyond that, start at reduced voltage (next section) or with a drive (module 11).

## Key points

- Stops in series, starts in parallel with the hold-in.
- Direct-on-line: 6 to 8 times In, mechanical jolt.
- For small and medium powers.
