#include <Arduino.h>
#include <Wire.h>

// I2C bus: SDA on GPIO 21, SCL on GPIO 22
const uint8_t SDA_PIN = 21;
const uint8_t SCL_PIN = 22;

void setup() {
  Serial.begin(115200);
  Wire.begin(SDA_PIN, SCL_PIN);
  delay(1000);
  Serial.println("Scanning the I2C bus...");
  uint8_t found = 0;
  for (uint8_t address = 1; address < 127; address++) {
    Wire.beginTransmission(address);
    // 0: a device acknowledged its address
    if (Wire.endTransmission() == 0) {
      Serial.printf("Device found at 0x%02X\n", address);
      found++;
    }
  }
  Serial.printf("%u device(s)\n", found);
}

void loop() {
}
