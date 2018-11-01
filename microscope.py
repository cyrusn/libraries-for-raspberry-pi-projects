#! /user/bin/env python3
from gpiozero import Button, LED
from picamera import PiCamera
from datetime import datetime
from signal import pause

led = LED(19)
left_button = Button(20)
right_button = Button(21)
camera = PiCamera()
camera.rotation = 90
previewOn = False
lightOn = False

IMAGE_LOCATION = '/home/pi/Desktop/Images'

def capture():
    global previewOn
    if previewOn:    
        now = datetime.now().isoformat()
        path = IMAGE_LOCATION+'/{}.jpg'.format(now)
        print('Image Captured: ', path)
        camera.capture(path)

def togglePreview():
    global previewOn
    previewOn = not previewOn
    if previewOn:
        led.on()
        camera.start_preview()
    else:
        led.off()
        camera.stop_preview()


left_button.when_pressed = togglePreview

right_button.when_pressed = capture


print('Press left button to start preview.\nPress right button while previewing to capture image.\nPress ctrl-C to stop the programme.')

pause()
