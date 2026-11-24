#include <Arduino.h>

void setup() {
  Serial.begin(115200);
  Serial.println("Tapez des caractères puis Entrée");
}

void loop() {
  // available() : nombre d'octets reçus en attente
  while (Serial.available() > 0) {
    int code = Serial.read();  // le plus ancien octet, ou -1
    Serial.printf("caractère '%c' : code %d\n", (char)code, code);
  }
}
