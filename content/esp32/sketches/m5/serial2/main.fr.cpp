#include <Arduino.h>

// UART 2 : RX sur GPIO 16, TX sur GPIO 17
const uint8_t RX2_PIN = 16;
const uint8_t TX2_PIN = 17;
const uint32_t LINK_BAUD = 9600;

void setup() {
  Serial.begin(115200);
  Serial2.begin(LINK_BAUD, SERIAL_8N1, RX2_PIN, TX2_PIN);
}

void loop() {
  // Ce qui est tapé dans le moniteur part vers l'autre carte
  while (Serial.available() > 0) {
    Serial2.write(Serial.read());
  }
  // Ce que l'autre carte envoie s'affiche dans le moniteur
  while (Serial2.available() > 0) {
    Serial.write(Serial2.read());
  }
}
