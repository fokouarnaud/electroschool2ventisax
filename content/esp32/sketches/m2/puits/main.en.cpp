#include <Arduino.h>

// LED wired in inverted logic: from 3.3 V to the pin
const uint8_t LED_PIN = 26;
// In inverted logic, LOW lights and HIGH switches off
const uint8_t LED_ON = LOW;
const uint8_t LED_OFF = HIGH;
const uint32_t HALF_PERIOD_MS = 500;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LED_OFF);
}

void loop() {
  digitalWrite(LED_PIN, LED_ON);
  delay(HALF_PERIOD_MS);
  digitalWrite(LED_PIN, LED_OFF);
  delay(HALF_PERIOD_MS);
}
