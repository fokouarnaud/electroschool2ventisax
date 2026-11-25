#include <Arduino.h>

// LED on GPIO 25: it blinks to show that the program is running
const uint8_t LED_PIN = 25;
const uint32_t BLINK_MS = 1000;

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  // Leaves time to open the serial monitor
  delay(2000);
  Serial.println("Chip identity card:");
  Serial.printf("Model: %s, revision %d\n", ESP.getChipModel(), ESP.getChipRevision());
  Serial.printf("Cores: %d, frequency: %lu MHz\n", ESP.getChipCores(), (unsigned long)ESP.getCpuFreqMHz());
  Serial.printf("Flash: %lu bytes\n", (unsigned long)ESP.getFlashChipSize());
  Serial.printf("Free SRAM: %lu bytes\n", (unsigned long)ESP.getFreeHeap());
}

void loop() {
  // Toggles the LED
  digitalWrite(LED_PIN, !digitalRead(LED_PIN));
  delay(BLINK_MS);
}
