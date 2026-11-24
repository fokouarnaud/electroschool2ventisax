#include <Arduino.h>

// LED intégrée de la carte (souvent reliée à GPIO 2)
const uint8_t LED_PIN = 2;
// Durée de chaque état de la LED, en millisecondes
const uint32_t HALF_PERIOD_MS = 500;

void setup() {
  // Exécuté une seule fois, à la mise sous tension
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  Serial.println("Bonjour, ESP32 !");
}

void loop() {
  // Répété sans fin
  digitalWrite(LED_PIN, HIGH);
  delay(HALF_PERIOD_MS);
  digitalWrite(LED_PIN, LOW);
  delay(HALF_PERIOD_MS);
}
