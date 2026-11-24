#include <Arduino.h>

// Traffic light: three LEDs with their 330 ohm resistors
const uint8_t GREEN_PIN = 25;
const uint8_t AMBER_PIN = 26;
const uint8_t RED_PIN = 27;
// Gate of the MOSFET that drives the 12 V lamp (220 ohms, 10 kohm pull-down)
const uint8_t LAMP_PIN = 32;
const uint32_t GREEN_MS = 5000;
const uint32_t AMBER_MS = 2000;
const uint32_t RED_MS = 5000;

// Lights a single LED; the 12 V lamp lights up with red
void showLight(uint8_t pin) {
  digitalWrite(GREEN_PIN, pin == GREEN_PIN ? HIGH : LOW);
  digitalWrite(AMBER_PIN, pin == AMBER_PIN ? HIGH : LOW);
  digitalWrite(RED_PIN, pin == RED_PIN ? HIGH : LOW);
  digitalWrite(LAMP_PIN, pin == RED_PIN ? HIGH : LOW);
}

void setup() {
  Serial.begin(115200);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(AMBER_PIN, OUTPUT);
  pinMode(RED_PIN, OUTPUT);
  pinMode(LAMP_PIN, OUTPUT);
  digitalWrite(LAMP_PIN, LOW);
}

void loop() {
  Serial.println("green");
  showLight(GREEN_PIN);
  delay(GREEN_MS);
  Serial.println("amber");
  showLight(AMBER_PIN);
  delay(AMBER_MS);
  Serial.println("red: 12 V lamp on");
  showLight(RED_PIN);
  delay(RED_MS);
}
