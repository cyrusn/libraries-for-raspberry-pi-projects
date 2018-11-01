wfrom gpiozero import Button
from signal import pause

btn = Button(20)

btn.when_pressed = lambda x : print('hello world')

pause()