#include <Arduino.h>

// T0 est la broche GPIO 4
const uint8_t TOUCH_PIN = T0;
const uint8_t LED_PIN = 25;
// Seuil choisi entre la valeur sans doigt et la valeur avec doigt
const uint32_t TOUCH_THRESHOLD = 30;

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  uint32_t value = touchRead(TOUCH_PIN);
  bool touched = (value < TOUCH_THRESHOLD);  // la valeur chute quand on touche
  digitalWrite(LED_PIN, touched ? HIGH : LOW);
  Serial.printf("touch=%lu %s\n", (unsigned long)value, touched ? "touché" : "");
  delay(100);
}
