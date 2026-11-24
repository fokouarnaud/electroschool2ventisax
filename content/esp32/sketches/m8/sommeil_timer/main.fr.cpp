#include <Arduino.h>
#include "esp_sleep.h"

const uint8_t LED_PIN = 25;
const uint64_t SLEEP_US = 10ULL * 1000000ULL;  // 10 s en microsecondes

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, HIGH);
  Serial.println("Réveillé : mesure...");
  delay(500);  // le temps d'une mesure
  digitalWrite(LED_PIN, LOW);
  esp_sleep_enable_timer_wakeup(SLEEP_US);
  Serial.println("Je dors 10 s");
  Serial.flush();
  esp_deep_sleep_start();  // setup() recommencera au réveil
}

void loop() {
  // Jamais atteinte : la carte se rendort dans setup()
}
