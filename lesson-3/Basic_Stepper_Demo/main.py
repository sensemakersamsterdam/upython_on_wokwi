import time
from machine import Pin

EXTRA_DELAY = 5 # ms

direction = Pin(19, Pin.OUT)
step = Pin(20, Pin.OUT)


direction.value(True)

while True:
    for _ in range(400):
        step.value(True)
        time.sleep_ms(1)
        step.value(False)
        time.sleep_ms(1 + EXTRA_DELAY)
    time.sleep(0.5)
    direction.value( not direction.value())

