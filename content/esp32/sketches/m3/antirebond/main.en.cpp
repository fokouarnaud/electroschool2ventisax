#include <Arduino.h>

const uint8_t BUTTON_PIN = 4;
const uint8_t LED_PIN = 25;
// Duration of the bounces to let pass
const uint32_t DEBOUNCE_MS = 20;

// Last accepted level: released at start
int stableLevel = HIGH;

void setup() {
  Serial.begin(115200);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  int level = digitalRead(BUTTON_PIN);
  if (level != stableLevel) {
    // A change: wait for the bounces to end, then read again
    delay(DEBOUNCE_MS);
    if (digitalRead(BUTTON_PIN) == level) {
      stableLevel = level;
      Serial.println(stableLevel == LOW ? "pressed" : "released");
    }
  }
  digitalWrite(LED_PIN, stableLevel == LOW ? HIGH : LOW);
}
