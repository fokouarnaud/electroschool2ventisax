A multimeter gives an RMS value; it does not show the shape of the signal. To see a voltage change over time, you use an **oscilloscope**, and to produce an adjustable sine wave, a **signal generator** (function generator).

![Oscilloscope screen with a grid: the sine wave spans 4 divisions peak to peak and one period lasts 5 divisions](/static/content/electro/en/m5/ecran.svg)

## The signal generator

A signal generator has three main settings: the **waveform** (sine, square, triangle), the **frequency** (from a few hertz to several hundred kilohertz) and the **amplitude**. It is connected like a source: one signal terminal and one ground terminal.

## Reading the oscilloscope screen

The screen is divided into **divisions** (often 10 across and 8 high).

- The vertical setting, in **volts per division** (V/div), gives the voltage scale.
- The **timebase**, in seconds per division (ms/div, µs/div), gives the time scale.

Example from the screen above, at 2 V/div and 1 ms/div:

- the sine wave spans 4 divisions peak to peak: Upp = 4 × 2 = **8 V**, so Umax = 4 V;
- one period lasts 5 divisions: T = 5 × 1 ms = **5 ms**, so f = 1 / 0.005 = **200 Hz**.

Pick settings that fit one or two periods across the width and fill at least half the height: the reading is more accurate.

## The test bench

![The generator feeds the circuit; oscilloscope channel 1 watches the input, channel 2 the output, all grounds connected](/static/content/electro/en/m5/banc.svg)

With two channels, you compare a circuit's input (channel 1) and output (channel 2). Be careful: on most instruments **the grounds of the generator and of both channels are connected together** (and often to earth). All ground clips must therefore go **to the same point** of the circuit; placing one elsewhere short-circuits part of the circuit.

## Key points

- Upp = number of vertical divisions × V/div.
- T = number of horizontal divisions × timebase; f = 1 / T.
- All grounds at the same point.
