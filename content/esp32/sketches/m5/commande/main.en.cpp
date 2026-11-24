#include <Arduino.h>

const uint8_t LED_PIN = 25;

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  Serial.println("Commands: on, off, state");
}

void loop() {
  if (Serial.available() > 0) {
    // A whole line, up to Enter
    String line = Serial.readStringUntil('\n');
    line.trim();
    if (line == "on") {
      digitalWrite(LED_PIN, HIGH);
      Serial.println("LED on");
    } else if (line == "off") {
      digitalWrite(LED_PIN, LOW);
      Serial.println("LED off");
    } else if (line == "state") {
      Serial.println(digitalRead(LED_PIN) == HIGH ? "on" : "off");
    } else {
      Serial.printf("Unknown command: %s\n", line.c_str());
    }
  }
}
