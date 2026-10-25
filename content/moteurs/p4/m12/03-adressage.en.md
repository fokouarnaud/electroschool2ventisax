Each input, output or memory has an **address**. The **IEC 61131-3** standard defines a neutral way of writing it, used throughout this module.

## Reading an address

![Breakdown of %IX0.1: % direct variable, I input, X bit, 0 byte number, 1 bit number](/static/content/moteurs/en/m12/bits.svg)

- **%**: variable directly linked to hardware.
- **I**: input; **Q**: output; **M**: internal memory.
- **X**: a single bit (digital).
- **0.1**: byte 0, bit 1. The bits of a byte run from 0 to 7.

So **%IX0.0** is the first input, **%QX0.0** the first output and **%MX0.0** the first memory bit. The ninth input is %IX1.0.

## Memory bits

A **%MX** memory bit is not linked to any terminal: it stores an intermediate state ("cycle running", "fault latched"), as an auxiliary relay would.

## Correspondence with manufacturers

Each manufacturer has its own notation. On your hardware, the manual gives the correspondence:

![Correspondence: input 0 is written %IX0.0 in IEC, I0.0 at Siemens, %I0.0 at Schneider; output 0: %QX0.0, Q0.0, %Q0.0; memory 0: %MX0.0, M0.0, %M0](/static/content/moteurs/en/m12/adresses.svg)

Simple programmable relays often number their terminals (I1, I2… and Q1, Q2…). Always keep a **variable table**: address, name ("S2_start"), comment.

## Symbols

In a program, each address is given a **symbolic name**. The program then reads like the machine diagram: "Stop_S1", "KM1_motor".

## Key points

- %I input, %Q output, %M memory; X one bit; byte.bit.
- Correspondence table with the brand used.
- A variable table with meaningful names.
