# -*- coding: utf-8 -*-
from time import sleep
from gpiozero import LightSensor, PWMLED
from gpiozero import Button
from gpiozero import Motor
from datetime import datetime

#Sensores a utilizar
sensorAfuera = LightSensor(14)
sensorAdentro = LightSensor(15) 
led = PWMLED(2)
ir = Button(18)
switch = Button(17)
motor = Motor(forward = 3, backward = 4)

#Variable global
estado = 'i'
bc = False
bf = False
bp = False

#Estados
def EDOi(entrada): #Inicio
    global estado
    global bf
    print('Estado Inicial')
    #Transiciónes
    if(ir.is_pressed):
        print("Puerta cerrada")
        bp = True
    else:
        print("Puerta abierta")
        bp = False
    if(switch.is_pressed):
        print("Switch apagado")
        led.value = 0.0
        bf = False
    else:
        print("Switch encendido")
        led.value = 1.0
        bf = True
    if(bp):
        if (sensorAfuera.value >= 0.2 and sensorAdentro.value <= 0.05): #Luz afuera, oscuridad adentro
            estado = 0
        elif (sensorAfuera.value <= 0.05 and sensorAdentro.value <= 0.05): #Oscuridad afuera, oscuridad adentro
            estado = 1
        elif(sensorAfuera.value <= 0.05 and sensorAdentro.value >= 0.2): #Oscuridad afuera, luz adentro
            estado = 2
        elif(sensorAfuera.value >= 0.2 and sensorAdentro.value >= 0.2): #Luz afuera, Luz adentro
            estado = 3
        else:
            estado = 'i'
            archivo.close()
        print("el valor del sensor de afuera es de: " + str(sensorAfuera.value))
        print("el valor del sensor de adentro es de: " + str(sensorAdentro.value))

def EDO0(entrada): #Luz afuera, oscuridad adentro
    global estado
    global bc
    global bf
    print("Luz afuera, oscuridad adentro")
    if(bc == False): #Se abre la cortina
        motor.forward()
        sleep(1)
        motor.stop()
        bc = True
        archivo = open("Log.txt","a")
        now = datetime.now()
        cadena = str(now) + ": Cortina abierta."
        archivo.write(cadena + "\n")
        archivo.close()
    estado = 'i'
        
def EDO1(entrada): #Oscuridad afuera, oscuridad adentro
    global estado
    global bc
    global bf
    print("Oscuridad afuera, oscuridad adentro")
    archivo = open("Log.txt","a")
    if(bc):
        motor.backward()
        sleep(1)
        motor.stop()
        now = datetime.now()
        cadena = str(now) + ": Cortina cerrada"
        archivo.write(cadena + "\n")
        bc = False
    if(bf == False):
        led.value = 1.0
        bf = True
        now = datetime.now()
        cadena = str(now) + ": Luz encendida."
        archivo.write(cadena + "\n")
    archivo.close()
    estado = 'i'

def EDO2(entrada): #Oscuridad afuera, luz adentro
    global estado
    global bc
    global bf
    print("Oscuridad afuera, luz adentro")
    archivo = open("Log.txt","a")
    if(bc):
        motor.backward()
        sleep(1)
        motor.stop()
        now = datetime.now()
        cadena = str(now) + ": Cortina abierta."
        archivo.write(cadena + "\n")
        archivo.close()
        bc = False
    if(bf == False):
        led.value = 1.0
        bf = True
        now = datetime.now()
        cadena = str(now) + ": Luz encendida."
        archivo.write(cadena + "\n")
    archivo.close()
    estado = 'i'

def EDO3(entrada): #Luz afuera, luz adentro
    global estado
    global bc
    global bf
    print("Luz afuera, luz adentro")
    estado = 'i'

#Finite State Machine (FSM)   
def FSM(entrada):
    global estado
    switch = {
       'i':EDOi,
        0 :EDO0,
        1 :EDO1,
        2 :EDO2,
        3 :EDO3,
    }
    func = switch.get(estado, lambda: None)
    return func(entrada)

#Programa Principal
archivo = open("Log.txt","a")
archivo.write("Estado de los sensores.\n")
archivo.close()
while True:
    FSM('i')
    sleep(2)