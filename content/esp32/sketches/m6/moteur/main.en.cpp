#include <Arduino.h>

const uint8_t POT_PIN = 34;
// MOSFET gate, through 220 ohms
const uint8_t MOTOR_PIN = 26;
const uint32_t PWM_FREQ_HZ = 5000;
const uint8_t PWM_BITS = 8;

void setup() {
  Serial.begin(115200);
  ledcAttach(MOTOR_PIN, PWM_FREQ_HZ, PWM_BITS);
}

void loop() {
  uint16_t raw = analogRead(POT_PIN);
  // 0 to 4095 brought down to 0 to 255
  uint32_t duty = map(raw, 0, 4095, 0, 255);
  ledcWrite(MOTOR_PIN, duty);
  Serial.printf("duty cycle: %lu %%\n", (unsigned long)(duty * 100 / 255));
  delay(200);
}
