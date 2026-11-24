#include <Arduino.h>

const uint8_t BUTTON_PIN = 4;
const uint8_t GREEN_PIN = 25;
const uint8_t AMBER_PIN = 26;
const uint8_t RED_PIN = 27;
// Un tour de loop() dure 20 ms ; les durées se comptent en tours
const uint32_t TICK_MS = 20;
const uint32_t GREEN_TICKS = 250;  // 5 s
const uint32_t AMBER_TICKS = 100;  // 2 s
const uint32_t RED_TICKS = 250;    // 5 s
const uint32_t BLINK_TICKS = 25;   // 0,5 s en veille

enum Mode { MODE_CYCLE, MODE_STANDBY };
enum Light { LIGHT_GREEN, LIGHT_AMBER, LIGHT_RED };

Mode mode = MODE_CYCLE;
Light light = LIGHT_GREEN;
uint32_t ticks = 0;  // tours écoulés dans l'état courant
int previousLevel = HIGH;
bool amberOn = false;

void setup() {
  Serial.begin(115200);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(AMBER_PIN, OUTPUT);
  pinMode(RED_PIN, OUTPUT);
}

void loop() {
  // 1. Lire l'entrée : un appui change de mode
  int level = digitalRead(BUTTON_PIN);
  if (previousLevel == HIGH && level == LOW) {
    mode = (mode == MODE_CYCLE) ? MODE_STANDBY : MODE_CYCLE;
    light = LIGHT_GREEN;
    ticks = 0;
    Serial.println(mode == MODE_CYCLE ? "cycle" : "veille");
  }
  previousLevel = level;

  // 2. Calculer : compter les tours et changer d'état au bon moment
  ticks++;
  if (mode == MODE_CYCLE) {
    if (light == LIGHT_GREEN && ticks >= GREEN_TICKS) {
      light = LIGHT_AMBER;
      ticks = 0;
    } else if (light == LIGHT_AMBER && ticks >= AMBER_TICKS) {
      light = LIGHT_RED;
      ticks = 0;
    } else if (light == LIGHT_RED && ticks >= RED_TICKS) {
      light = LIGHT_GREEN;
      ticks = 0;
    }
  } else if (ticks >= BLINK_TICKS) {
    amberOn = !amberOn;
    ticks = 0;
  }

  // 3. Écrire les sorties
  bool cycle = (mode == MODE_CYCLE);
  digitalWrite(GREEN_PIN, cycle && light == LIGHT_GREEN ? HIGH : LOW);
  digitalWrite(AMBER_PIN, (cycle && light == LIGHT_AMBER) || (!cycle && amberOn) ? HIGH : LOW);
  digitalWrite(RED_PIN, cycle && light == LIGHT_RED ? HIGH : LOW);

  // La pause de 20 ms rythme la boucle et laisse passer les rebonds
  delay(TICK_MS);
}
