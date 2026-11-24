#include <Arduino.h>
#include <WiFi.h>
#include "secrets.h"

void setup() {
  Serial.begin(115200);
  delay(500);
  // Access point mode: the ESP32 creates its own network
  WiFi.mode(WIFI_AP);
  WiFi.softAP(AP_SSID, AP_PASSWORD);
  Serial.print("Network created, board address: ");
  Serial.println(WiFi.softAPIP());  // 192.168.4.1 by default
}

void loop() {
}
