The rectified voltage is always positive, but it is not steady: it rises and falls back to zero a hundred times a second. A **reservoir capacitor** smooths it.

![Smoothing circuit: the bridge output feeds a 2,200 µF capacitor C in parallel with load R of about 31 Ω](/static/content/electro/en/m11/lissage-circuit.svg)

## Charging and discharging

A large electrolytic capacitor is placed **in parallel with the load**, right after the bridge:

1. Near each peak, the rectified voltage exceeds the capacitor's: the diodes conduct and **recharge** C up to the peak.
2. Between two peaks, the rectified voltage falls below the capacitor's: the diodes block, and **C feeds the load**. It discharges slowly.

![Smoothed voltage: it follows the peaks then slopes gently down to the next peak, instead of dropping to zero like the rectified voltage alone](/static/content/electro/en/m11/lissage-courbe.svg)

The output voltage no longer drops to zero: it stays close to the **peak voltage**, with a small sawtooth **ripple**, studied in the next section.

## Watch the no-load voltage

With no load, the capacitor does not discharge: it stays at the **peak voltage**. A 12 V rms adapter therefore gives about **15.6 V DC** after the bridge and the capacitor, not 12 V. The components that follow must withstand it.

## Choosing the capacitor

- **Capacitance**: several hundred to several thousand microfarads, depending on the current (next section).
- **Voltage rating**: above the peak voltage, with a margin; for 15.6 V, choose **25 V**.
- **Polarity**: the electrolytic capacitor is polarised. Its **−** terminal (marked by a stripe) goes to the bridge's **−**. Fitted the wrong way round, it heats up and can burst.

The diodes now conduct only in short bursts near the peaks: their peak current is much larger than the average load current.

## Key points

- The capacitor charges at the peaks and feeds the load between peaks.
- With no load, the output equals the peak voltage (15.6 V for 12 V rms).
- Voltage rating above the peak, and polarity respected.
