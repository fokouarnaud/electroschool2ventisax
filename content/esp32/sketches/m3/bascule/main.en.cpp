#include <Arduino.h>

const uint8_t BUTTON_PIN = 4;
const uint8_t LED_PIN = 25;
const uint32_t DEBOUNCE_MS = 20;

// Level read during the previous pass through loop()
int previousLevel = HIGH;
// LED state: 0 off, 1 on
uint8_t ledState = 0;

void setup() {
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  // 1. Read the input
  int level = digitalRead(BUTTON_PIN);
  // 2. Compute: a falling edge (HIGH then LOW) is a new press
  if (previousLevel == HIGH && level == LOW) {
    ledState ^= 1;  // exclusive OR: 0 becomes 1, 1 becomes 0
    delay(DEBOUNCE_MS);
  }
  previousLevel = level;
  // 3. Write the output
  digitalWrite(LED_PIN, ledState);
}
