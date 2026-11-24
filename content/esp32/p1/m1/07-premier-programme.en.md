Here is the first complete program. Copy it into `src/main.cpp`, upload it, then open the serial monitor: the built-in LED blinks and the board greets you.

```cpp
#include <Arduino.h>

// Built-in LED of the board (often wired to GPIO 2)
const uint8_t LED_PIN = 2;
// Duration of each LED state, in milliseconds
const uint32_t HALF_PERIOD_MS = 500;

void setup() {
  // Runs once, at power-up
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  Serial.println("Hello, ESP32!");
}

void loop() {
  // Repeats forever
  digitalWrite(LED_PIN, HIGH);
  delay(HALF_PERIOD_MS);
  digitalWrite(LED_PIN, LOW);
  delay(HALF_PERIOD_MS);
}
```

## setup and loop

![Flow of an Arduino program: setup runs once at power-up, then loop repeats forever](/static/content/esp32/en/m1/setup-loop.svg)

- `setup()` runs **once** after each power-up or each press on EN: it sets up the pins and the serial link.
- `loop()` repeats **forever**: it is the heart of the program. On a microcontroller, the program never ends.

## Line by line

- `#include <Arduino.h>` gives access to the Arduino functions (`pinMode`, `digitalWrite`, `delay`, `Serial`).
- `const uint8_t LED_PIN = 2;` names the pin. `uint8_t` is an integer from 0 to 255, enough for a pin number; `const` forbids changing it by mistake. Moving to another pin takes a single line.
- `const uint32_t HALF_PERIOD_MS = 500;`: a 32-bit integer for a duration in milliseconds. The `_MS` suffix recalls the unit.
- `Serial.begin(115200);` opens the serial link at 115200 bit/s, the `monitor_speed` speed.
- `pinMode(LED_PIN, OUTPUT);` makes the pin an output.
- `digitalWrite(LED_PIN, HIGH);` sets it to 3.3 V; `LOW` sets it back to 0 V.
- `delay(HALF_PERIOD_MS);` waits 500 ms. The LED stays on for 500 ms and off for 500 ms: a period of 1 s, that is 1 Hz.

## What happens during upload

![The three steps of uploading: build, writing into Flash, restart](/static/content/esp32/en/m1/televersement.svg)

If the upload fails with a message like *Failed to connect*, hold the BOOT button down at the start of the write, then release it.

## Key points

- `setup()` once, `loop()` forever.
- Name pins and durations with typed constants: `const uint8_t`, `const uint32_t`.
- The program is written into Flash: it starts again on its own at the next power-up.
