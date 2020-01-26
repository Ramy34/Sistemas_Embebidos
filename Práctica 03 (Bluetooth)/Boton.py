from bluedot import BlueDot
from signal import pause

def saludo():
    print("hola mundo")
    
def despedida():
    print("hasta pronto")
    
bd = BlueDot()
bd.when_pressed = saludo
bd.when_released = despedida
pause()
