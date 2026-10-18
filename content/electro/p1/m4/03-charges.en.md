The method of the previous section applies to every load. Two cases come up all the time: the LED and the relay.

## Driving an LED

A 5 V logic output should not directly power a bright LED or several LEDs. The LED and its series resistor go in the collector, powered from VCC.

![5 V control, RB = 4.7 kΩ, LED and 330 Ω resistor in the collector, VCC = 9 V](/static/content/electro/en/m4/led-transistor.svg)

Example: VCC = 9 V, 2 V red LED, saturated transistor (0.2 V). The LED resistor gets 9 − 2 − 0.2 = 6.8 V: with 330 Ω, the current is 6.8 / 330 ≈ **20.6 mA**. On the base side, with β min = 100, at least 0.21 mA is needed. With 4.7 kΩ: IB = 4.3 / 4.7 ≈ 0.91 mA, more than four times the minimum. Saturation is clean.

## Driving a relay

A **relay** is a mechanical switch operated by a coil. It lets you control a mains appliance, isolated from the electronic circuit. The coil draws several tens of milliamperes: a transistor drives it easily.

![Transistor driving the coil of a 12 V relay, with a flyback diode in parallel with the coil](/static/content/electro/en/m4/relais.svg)

## The flyback diode

A coil resists sudden changes in current. When the transistor turns off, it produces a **voltage spike** of tens or even hundreds of volts, which can destroy the transistor. A **flyback diode**, fitted in parallel with the coil and **in reverse** (cathode towards +VCC), gives this current a path and protects the transistor. It only conducts at the moment of switch-off.

This protection is required for every inductive load: relay, motor, electromagnet, solenoid valve.

## Key points

- The LED and its resistor go in the collector; the resistor voltage is VCC − U_LED − 0.2.
- A relay isolates the electronic circuit from the load it controls.
- A reversed flyback diode across every coil driven by a transistor.
