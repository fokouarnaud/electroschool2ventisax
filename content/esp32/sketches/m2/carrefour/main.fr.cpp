#include <Arduino.h>

// Feu tricolore : trois LED avec leur résistance de 330 ohms
const uint8_t GREEN_PIN = 25;
const uint8_t AMBER_PIN = 26;
const uint8_t RED_PIN = 27;
// Grille du MOSFET qui commande la lampe 12 V (220 ohms, rappel 10 kohms)
const uint8_t LAMP_PIN = 32;
const uint32_t GREEN_MS = 5000;
const uint32_t AMBER_MS = 2000;
const uint32_t RED_MS = 5000;

// Allume une seule LED ; la lampe 12 V s'allume avec le rouge
void showLight(uint8_t pin) {
  digitalWrite(GREEN_PIN, pin == GREEN_PIN ? HIGH : LOW);
  digitalWrite(AMBER_PIN, pin == AMBER_PIN ? HIGH : LOW);
  digitalWrite(RED_PIN, pin == RED_PIN ? HIGH : LOW);
  digitalWrite(LAMP_PIN, pin == RED_PIN ? HIGH : LOW);
}

void setup() {
  Serial.begin(115200);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(AMBER_PIN, OUTPUT);
  pinMode(RED_PIN, OUTPUT);
  pinMode(LAMP_PIN, OUTPUT);
  digitalWrite(LAMP_PIN, LOW);
}

void loop() {
  Serial.println("vert");
  showLight(GREEN_PIN);
  delay(GREEN_MS);
  Serial.println("orange");
  showLight(AMBER_PIN);
  delay(AMBER_MS);
  Serial.println("rouge : lampe 12 V allumée");
  showLight(RED_PIN);
  delay(RED_MS);
}
