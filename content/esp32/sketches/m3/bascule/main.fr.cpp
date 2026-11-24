#include <Arduino.h>

const uint8_t BUTTON_PIN = 4;
const uint8_t LED_PIN = 25;
const uint32_t DEBOUNCE_MS = 20;

// Niveau lu au passage précédent dans loop()
int previousLevel = HIGH;
// État de la LED : 0 éteinte, 1 allumée
uint8_t ledState = 0;

void setup() {
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  // 1. Lire l'entrée
  int level = digitalRead(BUTTON_PIN);
  // 2. Calculer : un front descendant (HIGH puis LOW) est un nouvel appui
  if (previousLevel == HIGH && level == LOW) {
    ledState ^= 1;  // OU exclusif : 0 devient 1, 1 devient 0
    delay(DEBOUNCE_MS);
  }
  previousLevel = level;
  // 3. Écrire la sortie
  digitalWrite(LED_PIN, ledState);
}
