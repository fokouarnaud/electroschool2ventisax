#include <Arduino.h>

const uint8_t LED_PIN = 25;

// A FreeRTOS task: an endless loop that hands back control with vTaskDelay
void blinkTask(void *parameter) {
  pinMode(LED_PIN, OUTPUT);
  for (;;) {
    digitalWrite(LED_PIN, !digitalRead(LED_PIN));
    vTaskDelay(pdMS_TO_TICKS(250));
  }
}

void setup() {
  Serial.begin(115200);
  // Name, stack size, parameter, priority, handle, core
  xTaskCreatePinnedToCore(blinkTask, "blink", 2048, nullptr, 1, nullptr, 0);
}

void loop() {
  // loop() runs on its own, on core 1
  Serial.printf("loop on core %d\n", xPortGetCoreID());
  delay(1000);
}
