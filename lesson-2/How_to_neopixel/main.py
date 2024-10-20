import time
from neopixel import NeoPixel
from machine import Pin

N_LEDS = 16
NEO_PIN = Pin(14)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pix = NeoPixel(NEO_PIN, N_LEDS)

print(f"There are {pix.n} pixels")

for n in range(N_LEDS):
    pix[n] = (23, n * 40 + 40, 100)
    pix.write()
    time.sleep(.3)


