#include <Arduino.h>

// DAC 1 output: GPIO 25
const uint8_t DAC_PIN = 25;

void setup() {
}

void loop() {
  // Ramp from 0 to 3.3 V in 256 steps
  for (int value = 0; value <= 255; value++) {
    dacWrite(DAC_PIN, value);
    delay(10);
  }
}
