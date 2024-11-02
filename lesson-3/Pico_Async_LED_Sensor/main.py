import uasyncio as asyncio
from machine import Pin
import time

# Define the LED pin
led = Pin(12, Pin.OUT)
f = 0.5

my_event = asyncio.Event()

# Define a coroutine to blink the LED
async def blink_led():
    while True:
        led.value(not led.value())
        await asyncio.sleep(f)  # Blink every f second

# Define a coroutine to read a sensor (simulated here with a print statement)
async def read_sensor():
    n = 0
    while True:
        # Simulate reading a sensor value
        print(f"Reading sensor value for the {n}-th time...")
        n += 1
        await my_event.wait()
        await asyncio.sleep(0.5)
        my_event.clear()


async def change_freq():
    global f

    while True:
        t = time.time() // 10
        #print(t)
        if t % 2 == 0:
            f = 0.5
            print("half a second")
        else:
            f = 2
            print("two seconds")
            if not my_event.is_set():
                my_event.set()
        await asyncio.sleep(0.1)



# Main coroutine to run both tasks concurrently
async def main():
    # Create tasks for blinking LED and reading sensor
    task1 = asyncio.create_task(blink_led())
    task2 = asyncio.create_task(read_sensor())
    task3 = asyncio.create_task(change_freq())  
    
    # Run tasks concurrently
    print( await asyncio.gather(task1, task2, task3) )

# Run the main coroutine
asyncio.run(main())

