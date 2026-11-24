#include <Arduino.h>
#include <SPI.h>
#include <SD.h>

// Bus SPI par défaut : SCK 18, MISO 19, MOSI 23 ; chaque appareil a son CS
const uint8_t SD_CS_PIN = 5;
const uint8_t POT_PIN = 34;
const uint32_t PERIOD_MS = 5000;
const char *LOG_PATH = "/journal.csv";

uint32_t lastMs = 0;

void setup() {
  Serial.begin(115200);
  if (!SD.begin(SD_CS_PIN)) {
    Serial.println("Carte microSD absente ou mal câblée");
    return;
  }
  if (!SD.exists(LOG_PATH)) {
    File file = SD.open(LOG_PATH, FILE_WRITE);
    file.println("temps_ms;tension_mV");
    file.close();
  }
}

void loop() {
  uint32_t now = millis();
  if (now - lastMs >= PERIOD_MS) {
    lastMs = now;
    // Ouvrir en ajout, écrire une ligne, fermer aussitôt
    File file = SD.open(LOG_PATH, FILE_APPEND);
    if (file) {
      file.printf("%lu;%lu\n", (unsigned long)now, (unsigned long)analogReadMilliVolts(POT_PIN));
      file.close();
    }
  }
}
