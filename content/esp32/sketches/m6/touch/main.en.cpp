#include <Arduino.h>

// T0 is pin GPIO 4
const uint8_t TOUCH_PIN = T0;
const uint8_t LED_PIN = 25;
// Threshold chosen between the value without and with a finger
const uint32_t TOUCH_THRESHOLD = 30;

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  uint32_t value = touchRead(TOUCH_PIN);
  bool touched = (value < TOUCH_THRESHOLD);  // the value drops when touched
  digitalWrite(LED_PIN, touched ? HIGH : LOW);
  Serial.printf("touch=%lu %s\n", (unsigned long)value, touched ? "touched" : "");
  delay(100);
}
