#include <Arduino.h>
#include <WiFi.h>
#include <WebServer.h>
#include "secrets.h"

const uint8_t POT_PIN = 34;
const uint8_t LAMP_PIN = 26;

WebServer server(80);
bool lampOn = false;

// La page relit /mesure toutes les 2 s, sans se recharger
const char *PAGE =
  "<!doctype html><html><head><meta charset=\"utf-8\">"
  "<meta name=\"viewport\" content=\"width=device-width\">"
  "<title>ESP32</title></head><body style=\"font-family:sans-serif;text-align:center\">"
  "<h1>Tableau de bord</h1><p>Tension : <b id=\"v\">-</b> mV</p>"
  "<p><button onclick=\"fetch('/on')\">Allumer</button> "
  "<button onclick=\"fetch('/off')\">Éteindre</button></p>"
  "<script>setInterval(function(){fetch('/mesure').then(r=>r.json())"
  ".then(d=>{document.getElementById('v').textContent=d.tension_mV;});},2000);</script>"
  "</body></html>";

void handleRoot() {
  server.send(200, "text/html; charset=utf-8", PAGE);
}

void handleMeasure() {
  String json = "{\"tension_mV\": " + String(analogReadMilliVolts(POT_PIN)) + ", \"lampe\": " + (lampOn ? "true" : "false") + "}";
  server.send(200, "application/json", json);
}

void handleOn() {
  lampOn = true;
  digitalWrite(LAMP_PIN, HIGH);
  server.send(200, "text/plain", "ok");
}

void handleOff() {
  lampOn = false;
  digitalWrite(LAMP_PIN, LOW);
  server.send(200, "text/plain", "ok");
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
  server.on("/", handleRoot);
  server.on("/mesure", handleMeasure);
  server.on("/on", handleOn);
  server.on("/off", handleOff);
  server.begin();
  Serial.printf("Tableau de bord : http://%s/\n", WiFi.localIP().toString().c_str());
}

void loop() {
  server.handleClient();
}
