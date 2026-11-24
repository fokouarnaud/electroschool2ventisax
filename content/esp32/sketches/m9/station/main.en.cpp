#include <Arduino.h>
#include <WiFi.h>
#include "secrets.h"

const uint32_t CHECK_MS = 5000;
uint32_t lastCheckMs = 0;

void connectWifi() {
  Serial.print("Connecting");
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  uint32_t startMs = millis();
  while (WiFi.status() != WL_CONNECTED && millis() - startMs < 15000) {
    delay(250);
    Serial.print(".");
  }
  if (WiFi.status() == WL_CONNECTED) {
    Serial.printf("\nConnected: %s, signal %d dBm\n", WiFi.localIP().toString().c_str(), WiFi.RSSI());
  } else {
    Serial.println("\nFailed: will try again later");
  }
}

void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);  // station: join the router
  connectWifi();
}

void loop() {
  uint32_t now = millis();
  // Every 5 s, check the connection and restart it if needed
  if (now - lastCheckMs >= CHECK_MS) {
    lastCheckMs = now;
    if (WiFi.status() != WL_CONNECTED) {
      WiFi.disconnect();
      connectWifi();
    }
  }
}
