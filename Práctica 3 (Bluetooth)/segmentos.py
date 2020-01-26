from bluedot import BlueDot
from gpiozero import LEDBoard
from time import sleep

leds = LEDBoard(26,19,13,6,5,21,20,16)
def ramses():
    print("Holi c:")
    leds.value = (0,0,0,0,1,0,1,0)
    sleep(1)
    leds.value = (1,1,1,1,1,0,1,0)
    sleep(1)
    leds.value = (1,0,1,0,1,0,1,0)
    sleep(1)
    leds.value = (1,0,1,1,0,1,1,0)
    sleep(1)
    leds.value = (1,1,0,1,1,1,1,0)
    sleep(1)
    leds.value = (1,0,1,1,0,1,1,0)
    sleep(1)
    
def josue():
    print("Awa en el joy0")
    leds.value = (0,1,1,1,0,0,0,0)
    sleep(1)
    leds.value = (1,1,1,1,1,1,0,0)
    sleep(1)
    leds.value = (1,0,1,1,0,1,1,0)
    sleep(1)
    leds.value = (0,1,1,1,1,1,0,0)
    sleep(1)
    leds.value = (1,0,0,1,1,1,1,0)
    sleep(1)
    
def israel():
    print("No se :s")
    leds.value = (0,1,1,0,0,0,0,0)
    sleep(1)
    leds.value = (1,0,1,1,0,1,1,0)
    sleep(1)
    leds.value = (0,0,0,0,1,0,1,0)
    sleep(1)
    leds.value = (1,1,1,0,1,1,1,0)
    sleep(1)
    leds.value = (1,0,0,1,1,1,1,0)
    sleep(1)
    leds.value = (0,0,0,1,1,1,0,0)
    sleep(1)

leds.value = (1,1,1,1,1,1,1,1)
bd = BlueDot()
bd.when_pressed = ramses
bd.when_released = israel
bd.wait_for_swipe()
josue()
sleep(1)