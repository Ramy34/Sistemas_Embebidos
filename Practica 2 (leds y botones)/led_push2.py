from gpiozero import Button,LED
from signal import pause
led = LED(17)
button = Button(2)
button.when_pressed = led.on
button.when_released = led.off
pause()