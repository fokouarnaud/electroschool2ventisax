You do not program the module on its own: it is soldered onto a **development board**. The course uses the **ESP32-DevKitC V4**, Espressif's reference board, or one of its many **38-pin clones**: same pinout, same layout, sometimes another USB-serial chip. The board adds everything needed to plug it into a computer and wire it on a breadboard.

![ESP32-DevKitC V4 board seen from above: ESP32-WROOM-32 module and its antenna at the top, 3.3 V regulator, USB-serial bridge, red power LED, micro-USB port between the EN and BOOT buttons, 19 pins on each side](/static/content/esp32/en/m1/carte.svg)

## What the board adds to the module

Lay the board in front of you, USB port towards you. From top to bottom:

- **The ESP32-WROOM-32 module**, under its metal shield. The strip without a shield, at the very top, is the printed **antenna**: put neither metal nor wires on it, or the Wi-Fi will suffer.
- **The 3.3 V regulator** (often an AMS1117, three legs and a tab): it lowers the 5 V from USB to 3.3 V, the chip voltage.
- **The USB-serial bridge** (CP2102 chip on the original board, CP2102 or CH340 on clones): it turns the computer's USB into a serial link the ESP32 understands. You sometimes need to install its driver on the computer.
- **The red LED**: it lights as soon as the board is powered. It is a power indicator; **no LED of the board is wired to a GPIO pin**. To see a program act, you wire an external LED (section 7).
- **The micro-USB port**: it powers the board and carries the program and the messages. Use a cable that carries data, not a charge-only cable.
- **The EN button**, left of the port: it restarts the chip, like a reset button.
- **The BOOT button**, right of the port: held during a restart, it puts the chip into upload mode. Most of the time the computer does this on its own through the USB-serial bridge.

## The power supply

![Board power supply: the 5 V from USB goes through the regulator, which supplies 3.3 V to the chip; 5V and 3V3 pins](/static/content/esp32/en/m1/alimentation.svg)

Two pins of the board give access to the supply:

- **5V** (bottom left): wired to the USB 5 V. Useful to power a 5 V sensor, never to drive an input of the chip.
- **3V3** (top left): the regulator output. It powers your small 3.3 V sensors, as long as you stay modest (a few tens of milliamps).

Three **GND** pins give the ground, the 0 V reference of every signal: one on the left between G12 and G13, two on the right (at the very top and between G21 and G19).

## On the breadboard

The board is wide: set in the middle of an ordinary breadboard, it often leaves a single free row of holes on one side. Two solutions: two breadboards side by side, the board straddling their joint, or male-female wires plugged straight onto its pins.

> **30-pin variant.** Some DevKit boards have only 30 pins: they mostly leave out the Flash pins (GPIO 6 to 11). The GPIO numbers do not change; find them on your board's silkscreen before wiring. The ESP32-S3 and ESP32-C3 are different chips: their pinout differs, always check it.

## Key points

- The DevKitC V4 adds USB, the USB-serial bridge, the 3.3 V regulator, the power LED and the EN and BOOT buttons to the module.
- Its only LED is a power indicator: an LED driven by the program is wired externally.
- The 5V pin comes from USB; the chip itself works at 3.3 V.
