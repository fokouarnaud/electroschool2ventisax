#include <Arduino.h>
#include "esp_sleep.h"

// Stored in RTC memory: survives deep sleep, not power-off
RTC_DATA_ATTR uint32_t bootCount = 0;
// Ordinary SRAM variable: reset at every wake-up
uint32_t ramCount = 0;

void setup() {
  Serial.begin(115200);
  delay(500);
  bootCount++;
  ramCount++;
  Serial.printf("bootCount = %lu, ramCount = %lu\n", (unsigned long)bootCount, (unsigned long)ramCount);
  esp_sleep_enable_timer_wakeup(5ULL * 1000000ULL);
  Serial.flush();
  esp_deep_sleep_start();
}

void loop() {
}
