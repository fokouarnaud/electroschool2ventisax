#include <Arduino.h>

// Potentiometer wiper on GPIO 34 (ADC 1, input only)
const uint8_t POT_PIN = 34;

void setup() {
  Serial.begin(115200);
}

void loop() {
  uint16_t raw = analogRead(POT_PIN);              // 0 to 4095
  uint32_t millivolts = analogReadMilliVolts(POT_PIN);  // corrected voltage
  Serial.printf("raw=%u, %lu mV\n", raw, (unsigned long)millivolts);
  delay(500);
}
