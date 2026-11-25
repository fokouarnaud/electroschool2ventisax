#include <Arduino.h>

// External LED and its 330 ohm resistor, on GPIO 25
const uint8_t LED_PIN = 25;
// Duration of each LED state, in milliseconds
const uint32_t HALF_PERIOD_MS = 500;

void setup() {
  // Runs once, at power-up
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  Serial.println("Hello, ESP32!");
}

void loop() {
  // Repeats forever
  digitalWrite(LED_PIN, HIGH);
  delay(HALF_PERIOD_MS);
  digitalWrite(LED_PIN, LOW);
  delay(HALF_PERIOD_MS);
}
