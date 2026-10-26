A receiver's antenna picks up the signals of every station at once. To listen to just one, a **tuning circuit** is used: an LC tank whose resonant frequency is set to the station's.

![Antenna connected to a tank made of a 100 µH inductor and a variable capacitor of about 253 pF, followed by an amplifier](/static/content/electro/en/m7/accord.svg)

## The variable capacitor

To change station, C is varied with a **variable capacitor** (symbol crossed by an arrow): that is the tuning knob of older radios. Since f0 = 1 / (2π × √(L × C)):

- **decreasing C** makes f0 **go up**;
- **increasing C** (or L) makes f0 **go down**.

## Calculating the tuning capacitance

Turn the formula round to find C when f0 and L are known:

**C = 1 / (4π² × f0² × L)**

Example: L = 100 µH and a station at 1 MHz. 4π² ≈ 39.48; f0² = 10¹²; C = 1 / (39.48 × 10¹² × 0.0001) ≈ **253 pF**.

Another example: for 100 kHz with L = 1 mH, C ≈ 2.53 nF.

![Three stations at 0.9, 1 and 1.1 MHz; the curve of the circuit tuned to 1 MHz passes the middle station and attenuates the other two](/static/content/electro/en/m7/stations.svg)

## Selectivity in practice

A tuning circuit needs a **high enough Q** to separate two neighbouring stations, without being too narrow, or it would cut part of the transmitted sound. Real receivers combine several tuned circuits and amplifiers, which are Part 3 topics.

## What happens in the circuit

The antenna brings all three stations at once to the tank made of the 100 µH inductor and the variable capacitor. Turning the knob slides the moving plates between the fixed ones: the facing area grows, C rises and f0 falls. Plates out (180 pF), the circuit is tuned to 1.19 MHz; plates in (360 pF), to 0.839 MHz.

Set to 253 pF, it resonates at 1 MHz: the middle station gets through entirely, while the 0.9 MHz and 1.1 MHz stations only get through at 12 % and 13 % (Q = 40). At 313 pF, the 0.9 MHz station gets through instead, and the 1.1 MHz one drops to 6 %.

[[fig:lc_tuning]]

## Key points

- The tuning circuit is an LC tank set to the station's frequency.
- C = 1 / (4π² × f0² × L).
- Decreasing C raises f0.
