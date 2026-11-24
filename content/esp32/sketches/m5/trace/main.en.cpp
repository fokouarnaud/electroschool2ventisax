#include <Arduino.h>

const uint8_t BUTTON_PIN = 4;
const uint8_t LED_PIN = 25;
// Set to false to turn the trace off without touching the rest
const bool TRACE = true;

int previousLevel = HIGH;
uint8_t ledState = 0;

void setup() {
  Serial.begin(115200);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  int level = digitalRead(BUTTON_PIN);
  if (previousLevel == HIGH && level == LOW) {
    ledState ^= 1;
    delay(20);
  }
  if (TRACE && level != previousLevel) {
    Serial.printf("level=%d state=%d t=%lu ms\n", level, ledState, (unsigned long)millis());
  }
  previousLevel = level;
  digitalWrite(LED_PIN, ledState);
}
