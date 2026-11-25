#include <Arduino.h>

// LED de GPIO 25 : elle clignote pour montrer que le programme tourne
const uint8_t LED_PIN = 25;
const uint32_t BLINK_MS = 1000;

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  // Laisse le temps d'ouvrir le moniteur série
  delay(2000);
  Serial.println("Carte d'identité de la puce :");
  Serial.printf("Modèle : %s, révision %d\n", ESP.getChipModel(), ESP.getChipRevision());
  Serial.printf("Cœurs : %d, fréquence : %lu MHz\n", ESP.getChipCores(), (unsigned long)ESP.getCpuFreqMHz());
  Serial.printf("Flash : %lu octets\n", (unsigned long)ESP.getFlashChipSize());
  Serial.printf("SRAM libre : %lu octets\n", (unsigned long)ESP.getFreeHeap());
}

void loop() {
  // Inverse l'état de la LED
  digitalWrite(LED_PIN, !digitalRead(LED_PIN));
  delay(BLINK_MS);
}
