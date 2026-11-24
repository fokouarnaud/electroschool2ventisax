#include <Arduino.h>
#include <Wire.h>
#include <SPI.h>
#include <SD.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <Adafruit_BME280.h>

const uint8_t SD_CS_PIN = 5;
const uint32_t PERIOD_MS = 10000;
const char *LOG_PATH = "/station.csv";

Adafruit_SSD1306 display(128, 64, &Wire, -1);
Adafruit_BME280 bme;
bool sdReady = false;
uint32_t lastMs = 0;

void showOnScreen(float temperature, float humidity) {
  display.clearDisplay();
  display.setTextSize(2);
  display.setCursor(0, 0);
  display.printf("%.1f C\n", temperature);
  display.printf("%.0f %%\n", humidity);
  display.setTextSize(1);
  display.println(sdReady ? "log: yes" : "log: no");
  display.display();
}

void setup() {
  Serial.begin(115200);
  Wire.begin(21, 22);
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.setTextColor(SSD1306_WHITE);
  if (!bme.begin(0x76)) {
    Serial.println("BME280 not found");
  }
  sdReady = SD.begin(SD_CS_PIN);
}

void loop() {
  uint32_t now = millis();
  if (lastMs != 0 && now - lastMs < PERIOD_MS) {
    return;
  }
  lastMs = now;
  float temperature = bme.readTemperature();
  float humidity = bme.readHumidity();
  showOnScreen(temperature, humidity);
  Serial.printf("%lu;%.1f;%.1f\n", (unsigned long)now, temperature, humidity);
  if (sdReady) {
    File file = SD.open(LOG_PATH, FILE_APPEND);
    if (file) {
      file.printf("%lu;%.1f;%.1f\n", (unsigned long)now, temperature, humidity);
      file.close();
    }
  }
}
