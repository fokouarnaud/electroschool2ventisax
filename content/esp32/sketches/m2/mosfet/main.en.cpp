#include <Arduino.h>

// MOSFET gate (through 220 ohms), 10 kohm pull-down to GND
const uint8_t MOSFET_PIN = 26;
const uint32_t ON_MS = 2000;
const uint32_t OFF_MS = 2000;

void setup() {
  pinMode(MOSFET_PIN, OUTPUT);
  digitalWrite(MOSFET_PIN, LOW);  // motor stopped at start-up
}

void loop() {
  digitalWrite(MOSFET_PIN, HIGH);  // MOSFET on: the 12 V motor runs
  delay(ON_MS);
  digitalWrite(MOSFET_PIN, LOW);   // MOSFET off: the motor stops
  delay(OFF_MS);
}
