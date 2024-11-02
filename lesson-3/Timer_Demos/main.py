from machine import Timer, Pin
from micropython import schedule
from time import sleep

print("hi")

led = Pin(4, Pin.OUT)

t1 = Timer()
t2 = Timer()

def hi(tim):
    if tim is t1:
        n = 1
    elif tim is t2:
        n = 2
    else:
        n = "?"
        
    print(f"Hello {n} from timer interrupt.")
    led.value( not led.value() )


def intermediate(tim):
    schedule(hi, tim)



t1.init(period=1500, mode=Timer.PERIODIC, callback=intermediate)
t2.init(period=1300, mode=Timer.PERIODIC, callback=intermediate)

while True:
    sleep(4)
    print("Hi from main.")