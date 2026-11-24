#include <Arduino.h>
#include <Preferences.h>
#include "esp_sleep.h"

const uint8_t POT_PIN = 34;
const uint64_t SLEEP_US = 10ULL * 1000000ULL;

RTC_DATA_ATTR uint32_t wakeCount = 0;
Preferences prefs;

void setup() {
  Serial.begin(115200);
  delay(200);
  wakeCount++;
  uint32_t millivolts = analogReadMilliVolts(POT_PIN);
  // The maximum survives even a power-off: it is stored in Flash
  prefs.begin("enregistreur", false);
  uint32_t maxMv = prefs.getUInt("max_mv", 0);
  if (millivolts > maxMv) {
    maxMv = millivolts;
    prefs.putUInt("max_mv", maxMv);  // write only when the value changes
  }
  prefs.end();
  Serial.printf("wake-up %lu: %lu mV, maximum %lu mV\n",
                (unsigned long)wakeCount, (unsigned long)millivolts, (unsigned long)maxMv);
  esp_sleep_enable_timer_wakeup(SLEEP_US);
  Serial.flush();
  esp_deep_sleep_start();
}

void loop() {
}
