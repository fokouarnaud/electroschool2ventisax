#include <Arduino.h>

// Grille du MOSFET (à travers 220 ohms), rappel de 10 kohms vers GND
const uint8_t MOSFET_PIN = 26;
const uint32_t ON_MS = 2000;
const uint32_t OFF_MS = 2000;

void setup() {
  pinMode(MOSFET_PIN, OUTPUT);
  digitalWrite(MOSFET_PIN, LOW);  // moteur arrêté au démarrage
}

void loop() {
  digitalWrite(MOSFET_PIN, HIGH);  // MOSFET passant : le moteur 12 V tourne
  delay(ON_MS);
  digitalWrite(MOSFET_PIN, LOW);   // MOSFET bloqué : le moteur s'arrête
  delay(OFF_MS);
}
