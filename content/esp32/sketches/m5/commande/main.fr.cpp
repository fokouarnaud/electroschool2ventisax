#include <Arduino.h>

const uint8_t LED_PIN = 25;

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  Serial.println("Commandes : on, off, etat");
}

void loop() {
  if (Serial.available() > 0) {
    // Une ligne entière, jusqu'à Entrée
    String line = Serial.readStringUntil('\n');
    line.trim();
    if (line == "on") {
      digitalWrite(LED_PIN, HIGH);
      Serial.println("LED allumée");
    } else if (line == "off") {
      digitalWrite(LED_PIN, LOW);
      Serial.println("LED éteinte");
    } else if (line == "etat") {
      Serial.println(digitalRead(LED_PIN) == HIGH ? "allumée" : "éteinte");
    } else {
      Serial.printf("Commande inconnue : %s\n", line.c_str());
    }
  }
}
