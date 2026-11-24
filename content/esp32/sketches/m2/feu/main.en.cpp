#include <Arduino.h>

// Three LEDs, each with its 330 ohm resistor
const uint8_t GREEN_PIN = 25;
const uint8_t AMBER_PIN = 26;
const uint8_t RED_PIN = 27;
// Cycle durations, in milliseconds
const uint32_t GREEN_MS = 5000;
const uint32_t AMBER_MS = 2000;
const uint32_t RED_MS = 5000;

// Lights a single LED of the traffic light and switches the other two off
void showLight(uint8_t pin) {
  digitalWrite(GREEN_PIN, pin == GREEN_PIN ? HIGH : LOW);
  digitalWrite(AMBER_PIN, pin == AMBER_PIN ? HIGH : LOW);
  digitalWrite(RED_PIN, pin == RED_PIN ? HIGH : LOW);
}

void setup() {
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(AMBER_PIN, OUTPUT);
  pinMode(RED_PIN, OUTPUT);
}

void loop() {
  showLight(GREEN_PIN);
  delay(GREEN_MS);
  showLight(AMBER_PIN);
  delay(AMBER_MS);
  showLight(RED_PIN);
  delay(RED_MS);
}
