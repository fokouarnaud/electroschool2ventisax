#include <Arduino.h>

const uint8_t LED_PIN = 25;

// Une tâche FreeRTOS : une boucle sans fin qui rend la main par vTaskDelay
void blinkTask(void *parameter) {
  pinMode(LED_PIN, OUTPUT);
  for (;;) {
    digitalWrite(LED_PIN, !digitalRead(LED_PIN));
    vTaskDelay(pdMS_TO_TICKS(250));
  }
}

void setup() {
  Serial.begin(115200);
  // Nom, taille de pile, paramètre, priorité, poignée, cœur
  xTaskCreatePinnedToCore(blinkTask, "blink", 2048, nullptr, 1, nullptr, 0);
}

void loop() {
  // loop() tourne de son côté, sur le cœur 1
  Serial.printf("loop sur le cœur %d\n", xPortGetCoreID());
  delay(1000);
}
