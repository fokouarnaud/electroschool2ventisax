#include <Arduino.h>
#include "esp_sleep.h"

const uint8_t LED_PIN = 25;
const uint64_t SLEEP_US = 10ULL * 1000000ULL;  // 10 s in microseconds

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, HIGH);
  Serial.println("Awake: measuring...");
  delay(500);  // the time of one measurement
  digitalWrite(LED_PIN, LOW);
  esp_sleep_enable_timer_wakeup(SLEEP_US);
  Serial.println("Sleeping for 10 s");
  Serial.flush();
  esp_deep_sleep_start();  // setup() will start again on wake-up
}

void loop() {
  // Never reached: the board goes back to sleep in setup()
}
