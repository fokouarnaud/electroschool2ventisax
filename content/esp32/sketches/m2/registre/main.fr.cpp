#include <Arduino.h>
#include "driver/gpio.h"
#include "soc/gpio_reg.h"

const uint8_t LED_PIN = 25;
const uint32_t STEP_MS = 1000;

void setup() {
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  // 1. Arduino : la fonction la plus simple
  digitalWrite(LED_PIN, HIGH);
  delay(STEP_MS);
  digitalWrite(LED_PIN, LOW);
  delay(STEP_MS);

  // 2. ESP-IDF : le pilote d'Espressif
  gpio_set_level((gpio_num_t)LED_PIN, 1);
  delay(STEP_MS);
  gpio_set_level((gpio_num_t)LED_PIN, 0);
  delay(STEP_MS);

  // 3. Registres : un bit par broche
  REG_WRITE(GPIO_OUT_W1TS_REG, 1UL << LED_PIN);  // met le bit 25 à 1
  delay(STEP_MS);
  REG_WRITE(GPIO_OUT_W1TC_REG, 1UL << LED_PIN);  // remet le bit 25 à 0
  delay(STEP_MS);
}
