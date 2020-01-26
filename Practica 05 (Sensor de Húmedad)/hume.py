import Adafruit_DHT
import time
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
archivo = open("Sensor.txt","w")
archivo.write("Datos del sensor \n")
archivo.close()
while True:
    archivo = open("Sensor.txt","a")
    humedad, temperatura = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humedad is not None and temperatura is not None:
        cadena = str("""Temperatura = {0:0.1f}C humedad = {1:0.1f}%""".format(temperatura, humedad))
    else:
        cadena = str("Falla en el sensor")
    archivo.write(cadena + "\n")
    print(cadena)
    archivo.close()
    time.sleep(3);