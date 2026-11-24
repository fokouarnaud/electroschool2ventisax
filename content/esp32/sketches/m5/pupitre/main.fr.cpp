#include <Arduino.h>

const uint8_t BUTTON_PIN = 4;
const uint8_t GREEN_PIN = 25;
const uint8_t AMBER_PIN = 26;
const uint8_t RED_PIN = 27;

void showLight(uint8_t pin) {
  digitalWrite(GREEN_PIN, pin == GREEN_PIN ? HIGH : LOW);
  digitalWrite(AMBER_PIN, pin == AMBER_PIN ? HIGH : LOW);
  digitalWrite(RED_PIN, pin == RED_PIN ? HIGH : LOW);
}

void setup() {
  Serial.begin(115200);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(AMBER_PIN, OUTPUT);
  pinMode(RED_PIN, OUTPUT);
  showLight(RED_PIN);
  Serial.println("Commandes : vert, orange, rouge, bouton, aide");
}

void loop() {
  if (Serial.available() == 0) {
    return;
  }
  String line = Serial.readStringUntil('\n');
  line.trim();
  line.toLowerCase();
  if (line == "vert") {
    showLight(GREEN_PIN);
  } else if (line == "orange") {
    showLight(AMBER_PIN);
  } else if (line == "rouge") {
    showLight(RED_PIN);
  } else if (line == "bouton") {
    Serial.println(digitalRead(BUTTON_PIN) == LOW ? "appuyé" : "relâché");
    return;
  } else if (line == "aide") {
    Serial.println("vert, orange, rouge : allume la couleur ; bouton : état du bouton");
    return;
  } else {
    Serial.printf("Commande inconnue : %s\n", line.c_str());
    return;
  }
  Serial.printf("Feu : %s\n", line.c_str());
}
