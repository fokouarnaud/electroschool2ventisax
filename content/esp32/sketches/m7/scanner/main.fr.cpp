#include <Arduino.h>
#include <Wire.h>

// Bus I2C : SDA sur GPIO 21, SCL sur GPIO 22
const uint8_t SDA_PIN = 21;
const uint8_t SCL_PIN = 22;

void setup() {
  Serial.begin(115200);
  Wire.begin(SDA_PIN, SCL_PIN);
  delay(1000);
  Serial.println("Recherche sur le bus I2C...");
  uint8_t found = 0;
  for (uint8_t address = 1; address < 127; address++) {
    Wire.beginTransmission(address);
    // 0 : un appareil a acquitté son adresse
    if (Wire.endTransmission() == 0) {
      Serial.printf("Appareil trouvé en 0x%02X\n", address);
      found++;
    }
  }
  Serial.printf("%u appareil(s)\n", found);
}

void loop() {
}
