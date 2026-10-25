A **programmable logic controller** (PLC) replaces wired relays, timers and counters with a **program**. To change how a machine works, you edit the program instead of rewiring the panel.

## Structure

![PLC: CPU with its memory, input cards linked to sensors and buttons, output cards linked to coils and indicators, 24 V supply and communication](/static/content/moteurs/en/m12/structure.svg)

- The **power supply**, usually 24 V DC.
- The **central processing unit** (CPU) and its **memory**: it runs the program and holds the variables.
- The **inputs**: they read the state of buttons, sensors and contacts.
- The **outputs**: they drive contactor coils, indicators, solenoid valves.
- **Communication**: programming from a computer, exchanges with an operator panel, a drive (module 11) or another PLC.

From a small **programmable relay** with a few inputs to a modular PLC with hundreds of inputs, the principle is the same.

## The scan cycle

The PLC does not handle its inputs as they come: it works in **scans** repeated endlessly.

![Scan cycle: read all inputs, run the program, write all outputs, then start again](/static/content/moteurs/en/m12/cycle.svg)

1. **Read** all inputs and freeze their state in a memory image.
2. **Run** the program from start to end, with that image.
3. **Write** all outputs at once.

One complete turn is the **scan time**, a few milliseconds. Consequences: a pulse shorter than one scan can be missed, and an output changed twice in the program only takes the **last** value.

## Key points

- The program replaces wired logic.
- Power supply, CPU, inputs, outputs, communication.
- Scan: read inputs, run, write outputs; a few ms.
