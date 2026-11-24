#include <Arduino.h>

const uint8_t BUTTON_PIN = 4;
const uint8_t GREEN_PIN = 25;
const uint8_t AMBER_PIN = 26;
const uint8_t RED_PIN = 27;

void showLight(uint8_t pin) {
  digitalWrite(GREEN_PIN, pin == GREEN_PIN ? HIGH : LOW);
  digitalWrite(AMBER_PIN, pin == AMBER_PIN ? HIGH : LOW);
  digitalWrite(RED_PIN, pin == RED_PIN ? HIGH : LOW);
}

void setup() {
  Serial.begin(115200);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(AMBER_PIN, OUTPUT);
  pinMode(RED_PIN, OUTPUT);
  showLight(RED_PIN);
  Serial.println("Commands: green, amber, red, button, help");
}

void loop() {
  if (Serial.available() == 0) {
    return;
  }
  String line = Serial.readStringUntil('\n');
  line.trim();
  line.toLowerCase();
  if (line == "green") {
    showLight(GREEN_PIN);
  } else if (line == "amber") {
    showLight(AMBER_PIN);
  } else if (line == "red") {
    showLight(RED_PIN);
  } else if (line == "button") {
    Serial.println(digitalRead(BUTTON_PIN) == LOW ? "pressed" : "released");
    return;
  } else if (line == "help") {
    Serial.println("green, amber, red: lights the colour; button: button state");
    return;
  } else {
    Serial.printf("Unknown command: %s\n", line.c_str());
    return;
  }
  Serial.printf("Light: %s\n", line.c_str());
}
