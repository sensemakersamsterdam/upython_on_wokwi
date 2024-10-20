import time
from machine import Pin

RED_LED = Pin(19, Pin.OUT)
RED_BLUE = Pin(18, Pin.OUT)

while True:
    current_value = RED_LED.value()
    RED_LED.value(not current_value)
    RED_BLUE.value(current_value)
    time.sleep(0.25)
