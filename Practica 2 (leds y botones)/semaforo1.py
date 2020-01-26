from gpiozero import LEDBoard
from time import sleep

leds = LEDBoard(5,6,13,19,26,17)
while True:
    leds.value = (1,0,0,0,0,1)
    sleep(5)
    x=5
    while (x > 0):
        leds.value = (0,1,0,0,0,1)
        sleep(1)
        leds.value = (0,0,0,0,0,1)
        sleep(1)
        x = x - 1
    leds.value = (0,0,1,1,0,0)
    sleep(5)
    x=5
    while (x > 0):
        leds.value = (0,0,1,0,1,0)
        sleep(1)
        leds.value = (0,0,1,0,0,0)
        sleep(1)
        x = x - 1
