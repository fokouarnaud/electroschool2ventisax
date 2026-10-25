**Digital** (on/off) inputs and outputs know only two states: 0 or 1. In industry, they almost always work at **24 V DC**.

## Inputs

![Input wiring: S1 (stop, break contact) on %IX0.0, S2 (start, make contact) on %IX0.1, PNP sensor B1 on %IX0.2, all fed from +24 V](/static/content/moteurs/en/m12/entrees.svg)

- A closed contact brings **+24 V** to the input terminal: the PLC reads **1**. Open contact: it reads **0**.
- A 3-wire **PNP sensor** (module 4) connects directly: brown to +24 V, blue to 0 V, black to the input. This type of input is called **"sink"** or positive logic.
- An **LED** per input, on the PLC, shows the state read: the first troubleshooting tool.

## Outputs

![Output wiring: %QX0.0 feeds the coil of contactor KM1, %QX0.1 the indicator H1, with return to 0 V](/static/content/moteurs/en/m12/sorties.svg)

Two technologies:

| | **Relay** output | **Transistor** output |
|---|---|---|
| voltage | DC or AC | DC only (24 V) |
| current | 2 to 8 A | about 0.5 A |
| speed | slow, mechanical wear | fast, no wear |

An output **never drives a motor directly**: it feeds a contactor coil, which switches the power. On a DC coil, add a **freewheeling diode** (module 7).

## Analogue inputs

For a temperature, a pressure or a speed reference, **analogue inputs** (0-10 V or 4-20 mA) are used, converted into a number. This module covers digital only.

## Key points

- Digital at 24 V: closed contact = 1.
- PNP sensor straight onto an input; status LED for troubleshooting.
- Relay or transistor output; power always goes through a contactor.
