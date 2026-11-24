#include <Arduino.h>

// Bouton entre GPIO 4 et GND, tirage interne vers 3,3 V
const uint8_t BUTTON_PIN = 4;
// LED et sa résistance de 330 ohms
const uint8_t LED_PIN = 25;

void setup() {
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  // 1. Lire l'entrée : avec le tirage interne, appuyé donne LOW
  bool pressed = (digitalRead(BUTTON_PIN) == LOW);
  // 2. Écrire la sortie
  digitalWrite(LED_PIN, pressed ? HIGH : LOW);
}
