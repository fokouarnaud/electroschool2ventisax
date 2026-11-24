#include <Arduino.h>

const uint8_t BUTTON_PIN = 4;
const uint8_t LED_PIN = 25;
const uint8_t BUTTON_LED_PIN = 26;
const uint32_t HALF_PERIOD_MS = 500;

void setup() {
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUTTON_LED_PIN, OUTPUT);
}

void loop() {
  // The button is read only once a second
  digitalWrite(BUTTON_LED_PIN, digitalRead(BUTTON_PIN) == LOW ? HIGH : LOW);
  digitalWrite(LED_PIN, HIGH);
  delay(HALF_PERIOD_MS);  // meanwhile, nothing else happens
  digitalWrite(LED_PIN, LOW);
  delay(HALF_PERIOD_MS);
}
