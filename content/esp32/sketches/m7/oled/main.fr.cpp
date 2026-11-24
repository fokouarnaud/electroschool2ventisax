#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

const uint8_t SCREEN_WIDTH = 128;
const uint8_t SCREEN_HEIGHT = 64;
const uint8_t OLED_ADDRESS = 0x3C;

// -1 : l'écran n'a pas de broche de remise à zéro reliée
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

void setup() {
  Serial.begin(115200);
  Wire.begin(21, 22);
  if (!display.begin(SSD1306_SWITCHCAPVCC, OLED_ADDRESS)) {
    Serial.println("Écran introuvable : vérifiez le câblage et l'adresse");
    return;
  }
  display.clearDisplay();
  display.setTextColor(SSD1306_WHITE);
  display.setTextSize(2);
  display.setCursor(0, 0);
  display.println("ESP32");
  display.setTextSize(1);
  display.setCursor(0, 24);
  display.println("Bonjour !");
  display.drawRect(0, 40, 128, 20, SSD1306_WHITE);
  // Rien ne s'affiche avant display()
  display.display();
}

void loop() {
}
