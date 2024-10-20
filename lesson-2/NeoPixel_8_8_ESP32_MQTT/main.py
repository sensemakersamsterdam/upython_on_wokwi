from machine import Pin
from neopixel import NeoPixel
from neopix_matrix import NeoPixMatrix as NPM
from time import sleep
import wifi_mqtt as wm

N_ROW = 8
N_COL = 8
N_NEOPIX = N_ROW * N_COL
NEO_PIN = Pin(13)


def do_some_flashing():
    """
    This function iterates over each row of the NeoPixel matrix, sets the row to red,
    and then pauses for a short duration before moving to the next row. After all rows
    have been set to red, the function then iterates over each column of the NeoPixel
    matrix, sets the column to blue, and then pauses for a short duration before moving
    to the next column.

    Parameters:
    None

    Returns:
    None
    """
    for r in range(N_ROW):
        neo_mat.set_row(r, NPM.RED, show=True)
        sleep(0.1)
    for c in range(N_COL):
        neo_mat.set_col(c, NPM.BLUE, show=True)
        sleep(0.1)


def incoming(topic, message):
    def parse_check_message(message):
        """Parse and check the incoming message.

        Args:
            message (str): The incoming message in the format "R/C,rc_num,red,green,blue".

        Returns:
            tuple: A tuple containing row_col (str), rc_num (int), and a tuple of the color
                   (red, green, blue) if the message is valid.
            None: If the message is invalid.
        """
        message = message.decode("utf-8")  # bytes -> str
        try:
            row_col, rc_num, red, green, blue = message.split(",")
            row_col = row_col.upper()
            rc_num = int(rc_num)
            red = int(red)
            green = int(green)
            blue = int(blue)
            assert row_col in [
                "R",
                "C",
                "X",
            ], "Use R or C for row or column and X to clear."
            assert (
                0 <= rc_num < N_ROW
            ), f"Row/Col number out of range: 0 <= {rc_num} <= {N_ROW}."
            assert 0 <= red <= 255, f"Red out of range: 0 <= {red} <= 255."
            assert 0 <= green <= 255, f"Green out of range: 0 <= {green} <= 255."
            assert 0 <= blue <= 255, f"Blue out of range: 0 <= {blue} <= 255."
        except Exception as e:
            print(f"Error parsing message: {message} - {e}")
            return None, 0, (0, 0, 0)
        return row_col, rc_num, (red, green, blue)

    row_col, rc_num, color = parse_check_message(message)
    if row_col == "R":
        neo_mat.set_row(rc_num, color, show=True)
    elif row_col == "C":
        neo_mat.set_col(rc_num, color, show=True)
    elif row_col == "X":
        neo_mat.clear()


pixel_array = NeoPixel(NEO_PIN, N_NEOPIX)  # Create the NeoPixel "hardware"
neo_mat = NPM(
    pixel_array, N_ROW, N_COL
)  # Create the NeoPixel matrix, injecting the hardware

do_some_flashing()

wm.connect_mqtt_on_wifi(
    ssid="Wokwi-GUEST", listen_topic="wokwi-gijs", on_incoming=incoming
)

neo_mat.clear()

wm.mqtt_loop(forever=True)
