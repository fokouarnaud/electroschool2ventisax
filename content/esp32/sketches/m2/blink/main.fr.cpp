#include <Arduino.h>

// LED externe et sa résistance de 330 ohms, en logique directe
const uint8_t LED_PIN = 25;
// Durée de chaque état, en millisecondes
const uint32_t HALF_PERIOD_MS = 500;

void setup() {
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_PIN, HIGH);  // 3,3 V : la LED s'allume
  delay(HALF_PERIOD_MS);
  digitalWrite(LED_PIN, LOW);   // 0 V : la LED s'éteint
  delay(HALF_PERIOD_MS);
}
