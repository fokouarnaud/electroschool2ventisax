#include <Arduino.h>

// Button between GPIO 4 and GND, internal pull-up to 3.3 V
const uint8_t BUTTON_PIN = 4;
// LED and its 330 ohm resistor
const uint8_t LED_PIN = 25;

void setup() {
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  // 1. Read the input: with the internal pull-up, pressed gives LOW
  bool pressed = (digitalRead(BUTTON_PIN) == LOW);
  // 2. Write the output
  digitalWrite(LED_PIN, pressed ? HIGH : LOW);
}
