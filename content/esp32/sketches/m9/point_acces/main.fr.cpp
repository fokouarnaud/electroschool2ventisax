#include <Arduino.h>
#include <WiFi.h>
#include "secrets.h"

void setup() {
  Serial.begin(115200);
  delay(500);
  // Mode point d'accès : l'ESP32 crée son propre réseau
  WiFi.mode(WIFI_AP);
  WiFi.softAP(AP_SSID, AP_PASSWORD);
  Serial.print("Réseau créé, adresse de la carte : ");
  Serial.println(WiFi.softAPIP());  // 192.168.4.1 par défaut
}

void loop() {
}
