#include <Arduino.h>

const uint8_t BUTTON_PIN = 4;
const uint8_t GREEN_PIN = 25;
const uint8_t AMBER_PIN = 26;
const uint8_t RED_PIN = 27;
const uint32_t DEBOUNCE_MS = 20;

// The four states of the machine
enum State { STATE_OFF, STATE_RED, STATE_AMBER, STATE_GREEN };

State state = STATE_OFF;
int previousLevel = HIGH;

void setup() {
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(AMBER_PIN, OUTPUT);
  pinMode(RED_PIN, OUTPUT);
}

void loop() {
  // 1. Read the input and detect a press
  int level = digitalRead(BUTTON_PIN);
  if (previousLevel == HIGH && level == LOW) {
    // 2. Compute: each press moves on to the next state
    switch (state) {
      case STATE_OFF:   state = STATE_RED;   break;
      case STATE_RED:   state = STATE_AMBER; break;
      case STATE_AMBER: state = STATE_GREEN; break;
      case STATE_GREEN: state = STATE_OFF;   break;
    }
    delay(DEBOUNCE_MS);
  }
  previousLevel = level;
  // 3. Write the outputs from the state
  digitalWrite(RED_PIN, state == STATE_RED ? HIGH : LOW);
  digitalWrite(AMBER_PIN, state == STATE_AMBER ? HIGH : LOW);
  digitalWrite(GREEN_PIN, state == STATE_GREEN ? HIGH : LOW);
}
