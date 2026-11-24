#include <Arduino.h>

const uint8_t BUZZER_PIN = 27;
// C, E, G, high C, in hertz
const uint32_t NOTES_HZ[] = {262, 330, 392, 523};
const uint32_t NOTE_MS = 300;

void setup() {
  ledcAttach(BUZZER_PIN, 1000, 8);
}

void loop() {
  for (uint32_t note : NOTES_HZ) {
    ledcWriteTone(BUZZER_PIN, note);
    delay(NOTE_MS);
  }
  ledcWriteTone(BUZZER_PIN, 0);  // silence
  delay(1000);
}
