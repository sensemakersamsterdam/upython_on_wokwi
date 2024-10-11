import time
from machine import Pin, PWM

STEP_SIZE = 6
PWM_FREQ = 100
PWM_DUTY_MAX = 65535

LED_RED = Pin(19, Pin.OUT)
LED_BLUE = Pin(18, Pin.OUT)
SWITCH_RED = Pin(6, Pin.IN, Pin.PULL_UP )
SWITCH_BLUE = Pin(7, Pin.IN, Pin.PULL_UP )

RED_PWM = PWM(LED_RED, freq=PWM_FREQ)
BLUE_PWM = PWM(LED_BLUE, freq=PWM_FREQ)

def scale_dc(dc_pct):
  return int( dc_pct/100 * PWM_DUTY_MAX )


current_pct_red = 10

while True:
  if SWITCH_RED.value() == 0:
    current_pct_red += STEP_SIZE
  if SWITCH_BLUE.value() == 0:
    current_pct_red -= STEP_SIZE
  current_pct_red = min(max(current_pct_red, 0),100)
  RED_PWM.duty_u16(scale_dc(current_pct_red))
  BLUE_PWM.duty_u16(PWM_DUTY_MAX - scale_dc(current_pct_red))

  print(current_pct_red, scale_dc(current_pct_red))

  time.sleep(0.2)

