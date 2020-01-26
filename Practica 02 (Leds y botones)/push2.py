from gpiozero import Button
button = Button(26)
button.wait_for_press()
print("Button was pressed")