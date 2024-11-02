import time
from machine import Pin, PWM, I2C
from pcf8574 import PCF8574
from hd44780 import HD44780
from lcd import LCD

SWITCH_UP = Pin(7, Pin.IN, Pin.PULL_UP)
SWITCH_DOWN = Pin(8, Pin.IN, Pin.PULL_UP)
LED_RED = Pin(22, Pin.OUT)
LED_GREEN = Pin(21, Pin.OUT)

MAX_DUTY = 65535

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
pcf = PCF8574(i2c)
hd44780 = HD44780(pcf, num_lines=2, num_columns=16)
lcd = LCD(hd44780, pcf)
lcd.backlight_on()
lcd.write_lines("MicroPython\nHello people...")


def pct_2_dc(pct):
  return int(pct/100 * MAX_DUTY)

def led_by_button():
  while True:
    if SWITCH_UP.value() == 0:
      LED_GREEN.value(1)
    else:
      LED_GREEN.value(0)

    if SWITCH_DOWN.value() == 0:
      LED_RED.value(1)
    else:
      LED_RED.value(0)

    time.sleep(0.05)
  
def led_pwm():
  STEP = 5
  FREQ = 50

  current_duty_cycle = old_duty_cycle = 50
  pwm_r = PWM(LED_RED, freq=FREQ, duty_u16=pct_2_dc(current_duty_cycle))
  pwm_g = PWM(LED_GREEN, freq=FREQ, duty_u16=MAX_DUTY - pct_2_dc(current_duty_cycle))

  while True:
    if SWITCH_UP.value() == 0:
      current_duty_cycle = max(0, min(100, current_duty_cycle + STEP))

    if SWITCH_DOWN.value() == 0:
      current_duty_cycle = max(0, min(100, current_duty_cycle - STEP))

    # print(current_duty_cycle, pct_2_dc(current_duty_cycle), pwm_r.duty_u16())

    if current_duty_cycle != old_duty_cycle:
      pwm_r.duty_u16(pct_2_dc(current_duty_cycle))
      pwm_g.duty_u16(MAX_DUTY - pct_2_dc(current_duty_cycle))
      lcd.write_lines(f"Red is at {current_duty_cycle}%\nGreen is at {100-current_duty_cycle}%")
      old_duty_cycle = current_duty_cycle

    time.sleep(0.03)




led_pwm()