#include <Arduino.h>

const uint8_t BUTTON_PIN = 4;
const uint32_t DEBOUNCE_MS = 50;

// Shared with the interrupt routine: volatile
volatile uint32_t pressCount = 0;
volatile uint32_t lastPressMs = 0;

// Interrupt routine: short, in fast memory
void IRAM_ATTR onPress() {
  uint32_t now = millis();
  if (now - lastPressMs >= DEBOUNCE_MS) {
    lastPressMs = now;
    pressCount++;
  }
}

void setup() {
  Serial.begin(115200);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(BUTTON_PIN), onPress, FALLING);
}

void loop() {
  static uint32_t shownCount = 0;
  if (pressCount != shownCount) {
    shownCount = pressCount;
    Serial.printf("Presses: %lu\n", (unsigned long)shownCount);
  }
}
