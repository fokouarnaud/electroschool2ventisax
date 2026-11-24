#include <Arduino.h>

const uint32_t SERIAL_BAUD = 115200;
const uint8_t SENSOR_PIN = 34;

void setup() {
  // Same speed as monitor_speed in platformio.ini
  Serial.begin(SERIAL_BAUD);
  delay(1000);
  Serial.println("Start-up");
}

void loop() {
  uint16_t raw = analogRead(SENSOR_PIN);
  float volts = raw * 3.3f / 4095.0f;
  Serial.print("Raw value: ");
  Serial.println(raw);
  Serial.printf("Voltage: %.2f V, time: %lu ms\n", volts, (unsigned long)millis());
  delay(1000);
}
