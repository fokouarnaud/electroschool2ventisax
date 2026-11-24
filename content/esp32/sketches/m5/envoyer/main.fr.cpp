#include <Arduino.h>

const uint32_t SERIAL_BAUD = 115200;
const uint8_t SENSOR_PIN = 34;

void setup() {
  // Même vitesse que monitor_speed dans platformio.ini
  Serial.begin(SERIAL_BAUD);
  delay(1000);
  Serial.println("Démarrage");
}

void loop() {
  uint16_t raw = analogRead(SENSOR_PIN);
  float volts = raw * 3.3f / 4095.0f;
  Serial.print("Valeur brute : ");
  Serial.println(raw);
  Serial.printf("Tension : %.2f V, temps : %lu ms\n", volts, (unsigned long)millis());
  delay(1000);
}
