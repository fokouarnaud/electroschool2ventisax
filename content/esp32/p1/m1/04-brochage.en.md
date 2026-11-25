The board exposes 38 pins, 19 on each side, but they are not all alike. Knowing their **categories** avoids most beginner failures: a board that no longer boots, a program that crashes as soon as a button is wired.

![Pinout of the 38-pin DevKit board: Flash pins, input-only pins, strapping pins, safe pins and power](/static/content/esp32/en/m1/brochage.svg)

## Reading the silkscreen

On the DevKitC V4 and its clones, each pin has a name printed next to it. A GPIO pin is written with the letter **G** followed by its number: **G25** is GPIO 25, the one the program writes as `25`. The other names stand for a function: **3V3**, **5V**, **GND** for the supply, **EN** for restart, **TXD** and **RXD** for the serial link, **SVP** and **SVN** for GPIO 36 and 39, **SD0** to **SD3**, **CMD** and **CLK** for the Flash. Depending on the clone maker, you will sometimes read IO25 or just 25: it is the same pin.

## Four categories

![The four pin categories and their rule of use](/static/content/esp32/en/m1/categories.svg)

**Flash pins: GPIO 6 to 11.** They connect the chip to its Flash memory, the one holding the program. Touching them cuts the chip off from its program: it crashes. They are **never** used. On the board they are marked CLK, SD0 to SD3 and CMD.

**Input-only pins: GPIO 34, 35, 36 and 39.** They can read, not write: you cannot light an LED with them. They have no internal pull resistor either (module M3). They suit a potentiometer or an analog sensor very well. On the board, 36 and 39 are marked SVP and SVN (sometimes VP and VN).

**Strapping pins: GPIO 0, 2, 5, 12 and 15.** The chip reads their state **at boot** to choose its mode. A component that forces them to a level at the wrong moment prevents booting or uploading. Example: GPIO 12 high at boot makes the chip believe its Flash runs at 1.8 V, and it does not start. They can be used with care once the chip has booted. On some other boards, GPIO 2 carries a built-in LED; the DevKitC V4 has none.

**Safe pins: all the others.** GPIO 4, 13, 14, 16 to 19, 21 to 23, 25 to 27, 32 and 33 suit an LED, a button or a MOSFET.

## Reserved pins

- **GPIO 1 (TX) and GPIO 3 (RX)** carry the serial link with the computer: leave them to uploading and the serial monitor.
- **GPIO 21 (SDA) and GPIO 22 (SCL)** are the usual pins of the I2C bus (module M7).

## Key points

- Never GPIO 6 to 11.
- GPIO 34 to 39: input only, no internal pull.
- GPIO 0, 2, 5, 12, 15: care at boot.
- To start with: 4, 13, 16 to 19, 21 to 23, 25 to 27, 32, 33.
