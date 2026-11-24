#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_BME280.h>

const uint8_t BME_ADDRESS = 0x76;  // 0x77 sur certains modules
const uint32_t PERIOD_MS = 2000;

Adafruit_BME280 bme;
uint32_t lastMs = 0;

void setup() {
  Serial.begin(115200);
  Wire.begin(21, 22);
  if (!bme.begin(BME_ADDRESS)) {
    Serial.println("BME280 introuvable");
  }
}

void loop() {
  uint32_t now = millis();
  if (now - lastMs >= PERIOD_MS) {
    lastMs = now;
    float temperature = bme.readTemperature();      // °C
    float humidity = bme.readHumidity();            // %
    float pressure = bme.readPressure() / 100.0f;   // Pa vers hPa
    Serial.printf("T = %.1f °C, H = %.1f %%, P = %.1f hPa\n", temperature, humidity, pressure);
  }
}
