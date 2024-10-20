from machine import Pin
from neopix_matrix import NeoPixMatrix as NPM
from neopixel import NeoPixel
from time import sleep

N_ROWS = 8
N_COLS = 8
NEO_PIN = Pin(15)

pixel_array = NeoPixel(NEO_PIN, N_ROWS * N_COLS)
neo_mat = NPM(pixel_array, N_ROWS, N_COLS)

neo_mat.set_pix(3, 4, NPM.GREEN, show=True)
sleep(3)

def do_some_color(color):
    neo_mat.set_row(0, NPM.RED)
    neo_mat.set_row(3, color)
    neo_mat.set_row(7, NPM.BLUE, show=True)
    sleep(3)


def do_some_more_color():
    neo_mat.set_col(0, (255, 255, 0))
    neo_mat.set_col(3, (0, 255, 255))
    neo_mat.set_col(7, (255, 0, 255), show=True)
    sleep(3)


do_some_color(NPM.GREEN)
do_some_color(NPM.RED)
do_some_more_color()
neo_mat.clear()

print("Done!")
