#include <Arduino.h>
#include <SPI.h>
#include <SD.h>

// Default SPI bus: SCK 18, MISO 19, MOSI 23; each device has its CS
const uint8_t SD_CS_PIN = 5;
const uint8_t POT_PIN = 34;
const uint32_t PERIOD_MS = 5000;
const char *LOG_PATH = "/journal.csv";

uint32_t lastMs = 0;

void setup() {
  Serial.begin(115200);
  if (!SD.begin(SD_CS_PIN)) {
    Serial.println("microSD card missing or badly wired");
    return;
  }
  if (!SD.exists(LOG_PATH)) {
    File file = SD.open(LOG_PATH, FILE_WRITE);
    file.println("time_ms;voltage_mV");
    file.close();
  }
}

void loop() {
  uint32_t now = millis();
  if (now - lastMs >= PERIOD_MS) {
    lastMs = now;
    // Open for append, write one line, close at once
    File file = SD.open(LOG_PATH, FILE_APPEND);
    if (file) {
      file.printf("%lu;%lu\n", (unsigned long)now, (unsigned long)analogReadMilliVolts(POT_PIN));
      file.close();
    }
  }
}
