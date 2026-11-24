#include <Arduino.h>
#include <WiFi.h>
#include "secrets.h"

const uint32_t CHECK_MS = 5000;
uint32_t lastCheckMs = 0;

void connectWifi() {
  Serial.print("Connexion");
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  uint32_t startMs = millis();
  while (WiFi.status() != WL_CONNECTED && millis() - startMs < 15000) {
    delay(250);
    Serial.print(".");
  }
  if (WiFi.status() == WL_CONNECTED) {
    Serial.printf("\nConnecté : %s, signal %d dBm\n", WiFi.localIP().toString().c_str(), WiFi.RSSI());
  } else {
    Serial.println("\nÉchec : nouvelle tentative plus tard");
  }
}

void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);  // station : rejoindre la box
  connectWifi();
}

void loop() {
  uint32_t now = millis();
  // Toutes les 5 s, on vérifie la connexion et on la relance si besoin
  if (now - lastCheckMs >= CHECK_MS) {
    lastCheckMs = now;
    if (WiFi.status() != WL_CONNECTED) {
      WiFi.disconnect();
      connectWifi();
    }
  }
}
