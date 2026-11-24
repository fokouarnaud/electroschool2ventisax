#include <Arduino.h>

const uint8_t BUTTON_PIN = 4;
const uint8_t LED_PIN = 25;
const uint32_t MIN_WAIT_MS = 2000;
const uint32_t MAX_WAIT_MS = 5000;

enum Step { STEP_WAIT, STEP_LIT, STEP_DONE };

Step step = STEP_WAIT;
uint32_t stepStartMs = 0;
uint32_t waitMs = 0;
volatile uint32_t pressMs = 0;
volatile bool pressed = false;

void IRAM_ATTR onPress() {
  if (!pressed) {
    pressMs = millis();
    pressed = true;
  }
}

void startRound() {
  digitalWrite(LED_PIN, LOW);
  waitMs = random(MIN_WAIT_MS, MAX_WAIT_MS);
  stepStartMs = millis();
  pressed = false;
  step = STEP_WAIT;
  Serial.println("Attendez que la LED s'allume...");
}

void setup() {
  Serial.begin(115200);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(LED_PIN, OUTPUT);
  randomSeed(esp_random());
  attachInterrupt(digitalPinToInterrupt(BUTTON_PIN), onPress, FALLING);
  startRound();
}

void loop() {
  uint32_t now = millis();
  if (step == STEP_WAIT) {
    if (pressed) {
      Serial.println("Trop tôt ! On recommence.");
      delay(1000);
      startRound();
    } else if (now - stepStartMs >= waitMs) {
      digitalWrite(LED_PIN, HIGH);
      stepStartMs = now;
      step = STEP_LIT;
    }
  } else if (step == STEP_LIT && pressed) {
    Serial.printf("Temps de réaction : %lu ms\n", (unsigned long)(pressMs - stepStartMs));
    step = STEP_DONE;
    stepStartMs = now;
  } else if (step == STEP_DONE && now - stepStartMs >= 3000) {
    startRound();
  }
}
