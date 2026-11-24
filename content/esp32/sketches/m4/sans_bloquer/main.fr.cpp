#include <Arduino.h>

const uint8_t BUTTON_PIN = 4;
const uint8_t LED_PIN = 25;
const uint8_t BUTTON_LED_PIN = 26;
const uint32_t HALF_PERIOD_MS = 500;

// Instant du dernier changement de la LED, en millisecondes
uint32_t lastToggleMs = 0;
uint8_t ledState = 0;

void setup() {
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUTTON_LED_PIN, OUTPUT);
}

void loop() {
  uint32_t now = millis();
  // Le bouton est lu à chaque tour, des milliers de fois par seconde
  digitalWrite(BUTTON_LED_PIN, digitalRead(BUTTON_PIN) == LOW ? HIGH : LOW);
  // La LED change d'état quand la demi-période est écoulée
  if (now - lastToggleMs >= HALF_PERIOD_MS) {
    lastToggleMs = now;
    ledState ^= 1;
    digitalWrite(LED_PIN, ledState);
  }
}
