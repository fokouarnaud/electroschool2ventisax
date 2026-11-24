#include <Arduino.h>

// Curseur du potentiomètre sur GPIO 34 (ADC 1, entrée seule)
const uint8_t POT_PIN = 34;

void setup() {
  Serial.begin(115200);
}

void loop() {
  uint16_t raw = analogRead(POT_PIN);              // 0 à 4095
  uint32_t millivolts = analogReadMilliVolts(POT_PIN);  // tension corrigée
  Serial.printf("brut=%u, %lu mV\n", raw, (unsigned long)millivolts);
  delay(500);
}
