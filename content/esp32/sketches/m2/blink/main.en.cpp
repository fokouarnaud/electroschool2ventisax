#include <Arduino.h>

// External LED and its 330 ohm resistor, in direct logic
const uint8_t LED_PIN = 25;
// Duration of each state, in milliseconds
const uint32_t HALF_PERIOD_MS = 500;

void setup() {
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_PIN, HIGH);  // 3.3 V: the LED lights up
  delay(HALF_PERIOD_MS);
  digitalWrite(LED_PIN, LOW);   // 0 V: the LED goes out
  delay(HALF_PERIOD_MS);
}
