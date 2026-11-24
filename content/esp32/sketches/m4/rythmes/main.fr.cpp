#include <Arduino.h>

const uint8_t LED1_PIN = 25;
const uint8_t LED2_PIN = 26;
const uint32_t LED1_HALF_MS = 500;
const uint32_t LED2_HALF_MS = 120;

uint32_t led1LastMs = 0;
uint32_t led2LastMs = 0;
uint8_t led1State = 0;
uint8_t led2State = 0;

void setup() {
  pinMode(LED1_PIN, OUTPUT);
  pinMode(LED2_PIN, OUTPUT);
}

void loop() {
  uint32_t now = millis();
  // Chaque LED a sa période et son instant de dernier changement
  if (now - led1LastMs >= LED1_HALF_MS) {
    led1LastMs = now;
    led1State ^= 1;
    digitalWrite(LED1_PIN, led1State);
  }
  if (now - led2LastMs >= LED2_HALF_MS) {
    led2LastMs = now;
    led2State ^= 1;
    digitalWrite(LED2_PIN, led2State);
  }
}
