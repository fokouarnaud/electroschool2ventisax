#include <Arduino.h>

const uint8_t LED_PIN = 25;
// The timer counter moves one step per microsecond (1 MHz)
const uint32_t TIMER_FREQ_HZ = 1000000;
const uint64_t ALARM_TICKS = 1000000;  // 1000000 steps = 1 s

hw_timer_t *timer = nullptr;
volatile bool tick = false;

void IRAM_ATTR onTimer() {
  tick = true;
}

void setup() {
  pinMode(LED_PIN, OUTPUT);
  timer = timerBegin(TIMER_FREQ_HZ);
  timerAttachInterrupt(timer, onTimer);
  timerAlarm(timer, ALARM_TICKS, true, 0);  // alarm repeated forever
}

void loop() {
  if (tick) {
    tick = false;
    digitalWrite(LED_PIN, !digitalRead(LED_PIN));
  }
}
