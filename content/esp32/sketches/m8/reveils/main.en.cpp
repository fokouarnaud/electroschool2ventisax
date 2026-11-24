#include <Arduino.h>
#include "esp_sleep.h"
#include "driver/rtc_io.h"

// Button between GPIO 33 (RTC pin) and GND
const gpio_num_t WAKE_BUTTON = GPIO_NUM_33;
const uint8_t TOUCH_PIN = T0;
const uint32_t TOUCH_THRESHOLD = 30;

void setup() {
  Serial.begin(115200);
  delay(500);
  switch (esp_sleep_get_wakeup_cause()) {
    case ESP_SLEEP_WAKEUP_EXT0:     Serial.println("Woken by the button"); break;
    case ESP_SLEEP_WAKEUP_TOUCHPAD: Serial.println("Woken by touch"); break;
    default:                        Serial.println("First start-up"); break;
  }
  // Wake when GPIO 33 goes low; internal pull-up active during sleep
  rtc_gpio_pullup_en(WAKE_BUTTON);
  rtc_gpio_pulldown_dis(WAKE_BUTTON);
  esp_sleep_enable_ext0_wakeup(WAKE_BUTTON, 0);
  touchSleepWakeUpEnable(TOUCH_PIN, TOUCH_THRESHOLD);
  Serial.println("Sleeping: press the button or touch T0");
  Serial.flush();
  esp_deep_sleep_start();
}

void loop() {
}
