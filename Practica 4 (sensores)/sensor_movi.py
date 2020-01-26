from gpiozero import MotionSensor, LED
from time import sleep
from signal import pause

pir = MotionSensor(4)
led = LED(16)


    
    #pir.when_motion = led.on
pir.when_motion = led.on
    #pir.when_no_motion = led.off
pir.when_no_motion = led.off
    #sleep(5)
print("ya memori")
pause()
    
