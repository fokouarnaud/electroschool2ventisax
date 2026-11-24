#include <Arduino.h>

const uint8_t POT_PIN = 34;
const uint8_t TOUCH_PIN = T0;
const uint8_t LED_PIN = 25;
const uint32_t PWM_FREQ_HZ = 5000;
const uint8_t PWM_BITS = 8;
const uint32_t TOUCH_THRESHOLD = 30;

bool lampOn = false;
bool wasTouched = false;

void setup() {
  Serial.begin(115200);
  ledcAttach(LED_PIN, PWM_FREQ_HZ, PWM_BITS);
}

void loop() {
  // 1. Lire les entrées
  bool touched = touchRead(TOUCH_PIN) < TOUCH_THRESHOLD;
  uint16_t raw = analogRead(POT_PIN);
  // 2. Calculer : un nouveau contact allume ou éteint
  if (touched && !wasTouched) {
    lampOn = !lampOn;
    Serial.println(lampOn ? "allumée" : "éteinte");
  }
  wasTouched = touched;
  uint32_t duty = lampOn ? map(raw, 0, 4095, 0, 255) : 0;
  // 3. Écrire la sortie
  ledcWrite(LED_PIN, duty);
  delay(30);
}
