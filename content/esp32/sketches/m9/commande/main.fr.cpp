#include <Arduino.h>
#include <WiFi.h>
#include <WebServer.h>
#include "secrets.h"

// Grille du MOSFET de la lampe 12 V (220 ohms, rappel 10 kohms)
const uint8_t LAMP_PIN = 26;

WebServer server(80);

void handleOn() {
  digitalWrite(LAMP_PIN, HIGH);
  server.send(200, "text/plain; charset=utf-8", "lampe allumée");
}

void handleOff() {
  digitalWrite(LAMP_PIN, LOW);
  server.send(200, "text/plain; charset=utf-8", "lampe éteinte");
}

void setup() {
  Serial.begin(115200);
  pinMode(LAMP_PIN, OUTPUT);
  digitalWrite(LAMP_PIN, LOW);
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(250);
  }
  server.on("/on", handleOn);
  server.on("/off", handleOff);
  server.begin();
  Serial.println(WiFi.localIP());
}

void loop() {
  server.handleClient();
}
