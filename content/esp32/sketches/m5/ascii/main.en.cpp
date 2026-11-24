#include <Arduino.h>

void setup() {
  Serial.begin(115200);
  Serial.println("Type characters then Enter");
}

void loop() {
  // available(): number of received bytes waiting
  while (Serial.available() > 0) {
    int code = Serial.read();  // the oldest byte, or -1
    Serial.printf("character '%c': code %d\n", (char)code, code);
  }
}
