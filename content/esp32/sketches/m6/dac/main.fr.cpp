#include <Arduino.h>

// Sortie du DAC 1 : GPIO 25
const uint8_t DAC_PIN = 25;

void setup() {
}

void loop() {
  // Rampe de 0 à 3,3 V en 256 marches
  for (int value = 0; value <= 255; value++) {
    dacWrite(DAC_PIN, value);
    delay(10);
  }
}
