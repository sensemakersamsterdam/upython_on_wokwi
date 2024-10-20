from machine import Pin
from neopixel import NeoPixel
from time import sleep

N_NEOPIX_1 = 64
NEO_PIN_1 = Pin(15)

N_NEOPIX_2 = 1
NEO_PIN_2 = Pin(27)

pixels_1 = NeoPixel(NEO_PIN_1, N_NEOPIX_1)
pixels_2 = NeoPixel(NEO_PIN_2, N_NEOPIX_2)

for n in range(N_NEOPIX_1):
  pixels_1[n] = (255,255,255)
pixels_2[0] = (0, 0, 255)

pixels_1.write()

pixels_2.write()

# 1 LED = 5 mA 
# 3 LED = 15 mA
# 64 * 3 * 5 mA

# Log 1 on led = 5V  3.5 - 5V
# Log 0 on LED = 0V  0V - 1.5V

# Log 1 on Pico = 3.3V  2.2 - 3.3V
# Log 0 on Pico = 0V  0V - 1.5V
