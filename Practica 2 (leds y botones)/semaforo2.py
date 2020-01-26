from gpiozero import LEDBoard,Button
from time import sleep

leds = LEDBoard(5,6,13,19,26,17)
boton = Button(2)

def semaforo(n):
    while True:
        sleep(5)
        if boton.is_pressed:
            if n == 0:
                n = 1
        else:
            if n == 2:
                n = 3
                
        if n == 0:
            leds.value = (1,0,0,0,0,1)
            sleep(5)
            n = n + 1
        elif n == 1:
            x=5
            while (x > 0):
                leds.value = (0,1,0,0,0,1)
                sleep(1)
                leds.value = (0,0,0,0,0,1)
                sleep(1)
                x = x - 1
            n = n + 1
        elif n == 2:
            leds.value = (0,0,1,1,0,0)
            sleep(5)
        elif n == 3:
            x=5
            while (x > 0):
                leds.value = (0,0,1,0,1,0)
                sleep(1)
                leds.value = (0,0,1,0,0,0)
                sleep(1)
                x = x - 1
            n = 0
def main():
    n = 0 
    semaforo(n)
    
main()