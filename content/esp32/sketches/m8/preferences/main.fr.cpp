#include <Arduino.h>
#include <Preferences.h>

Preferences prefs;

void setup() {
  Serial.begin(115200);
  delay(1000);
  // «Espace de noms « reglages », en lecture et écriture|Namespace "reglages", read and write»
  prefs.begin("reglages", false);
  uint32_t starts = prefs.getUInt("starts", 0);  // 0 si la clé n'existe pas encore
  starts++;
  prefs.putUInt("starts", starts);
  prefs.end();
  Serial.printf("Démarrages depuis le premier téléversement : %lu\n", (unsigned long)starts);
}

void loop() {
}
