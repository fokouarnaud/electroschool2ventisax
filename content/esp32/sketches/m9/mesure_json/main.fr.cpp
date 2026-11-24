#include <Arduino.h>
#include <WiFi.h>
#include <WebServer.h>
#include "secrets.h"

const uint8_t POT_PIN = 34;

WebServer server(80);

void handleMeasure() {
  uint32_t millivolts = analogReadMilliVolts(POT_PIN);
  // Un texte JSON : des paires nom et valeur entre accolades
  String json = "{\"tension_mV\": " + String(millivolts) + "}";
  server.send(200, "application/json", json);
}

void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(250);
  }
  server.on("/mesure", handleMeasure);
  server.begin();
  Serial.println(WiFi.localIP());
}

void loop() {
  server.handleClient();
}
