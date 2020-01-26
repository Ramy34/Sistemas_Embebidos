from gpiozero import Button
button = Button(26)
while True:
    if button.is_pressed:
        print("Button is pressed c:")
    else:
        print("Button is not pressed :c")