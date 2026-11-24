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
  // 1. Read the inputs
  bool touched = touchRead(TOUCH_PIN) < TOUCH_THRESHOLD;
  uint16_t raw = analogRead(POT_PIN);
  // 2. Compute: a new touch switches on or off
  if (touched && !wasTouched) {
    lampOn = !lampOn;
    Serial.println(lampOn ? "on" : "off");
  }
  wasTouched = touched;
  uint32_t duty = lampOn ? map(raw, 0, 4095, 0, 255) : 0;
  // 3. Write the output
  ledcWrite(LED_PIN, duty);
  delay(30);
}
