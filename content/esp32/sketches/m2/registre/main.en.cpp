#include <Arduino.h>
#include "driver/gpio.h"
#include "soc/gpio_reg.h"

const uint8_t LED_PIN = 25;
const uint32_t STEP_MS = 1000;

void setup() {
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  // 1. Arduino: the simplest function
  digitalWrite(LED_PIN, HIGH);
  delay(STEP_MS);
  digitalWrite(LED_PIN, LOW);
  delay(STEP_MS);

  // 2. ESP-IDF: Espressif's driver
  gpio_set_level((gpio_num_t)LED_PIN, 1);
  delay(STEP_MS);
  gpio_set_level((gpio_num_t)LED_PIN, 0);
  delay(STEP_MS);

  // 3. Registers: one bit per pin
  REG_WRITE(GPIO_OUT_W1TS_REG, 1UL << LED_PIN);  // sets bit 25 to 1
  delay(STEP_MS);
  REG_WRITE(GPIO_OUT_W1TC_REG, 1UL << LED_PIN);  // clears bit 25 to 0
  delay(STEP_MS);
}
