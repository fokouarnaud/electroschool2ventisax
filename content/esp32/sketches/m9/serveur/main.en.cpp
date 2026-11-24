#include <Arduino.h>
#include <WiFi.h>
#include <WebServer.h>
#include "secrets.h"

WebServer server(80);

void handleRoot() {
  server.send(200, "text/html; charset=utf-8", "<h1>Hello from the ESP32</h1>");
}

void handleNotFound() {
  server.send(404, "text/plain; charset=utf-8", "Page not found");
}

void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(250);
  }
  // Each route is connected to its function
  server.on("/", handleRoot);
  server.onNotFound(handleNotFound);
  server.begin();
  Serial.printf("Open http://%s/\n", WiFi.localIP().toString().c_str());
}

void loop() {
  server.handleClient();  // handles the received requests, without blocking
}
