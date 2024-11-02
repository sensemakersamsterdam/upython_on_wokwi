from time import sleep
import picozero as pz

pot = pz.Pot(27)
servo = pz.Servo(6)

while True:
    pos = pot.value
    servo.value = pos
