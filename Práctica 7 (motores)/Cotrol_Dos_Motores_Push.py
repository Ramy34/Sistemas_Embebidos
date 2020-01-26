from gpiozero import Robot,Button
from time import sleep

robot = Robot(left=(4,14), right=(17,18))
buttonA = Button(26)
buttonB = Button(20)

while True:
    print("Hola")
    if buttonA.wait_for_press():
        robot.forward()
        print("Boton A")
        sleep(4)
        #sleep(1)
        #robot.right()
        #sleep(1)
    if buttonB.wait_for_press():
        robot.right()
        print("Boton B")
        sleep(4)
        #robot.forward()
        #sleep(1)
    robot.stop()
    sleep(5)
