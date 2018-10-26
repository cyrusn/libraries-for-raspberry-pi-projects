from gpiozero import Button, LED
from picamera import PiCamera
from datetime import datetime
from signal import pause
from time import sleep

led = LED(19)
left_button = Button(20)
right_button = Button(21)
camera = PiCamera()
camera.rotation = 90
previewOn = False
lightOn = False


def capture():
    led.on()
    
    now = datetime.now().isoformat()
    path = '/home/pi/Desktop/testCamera/{}.jpg'.format(now)
    print('Image Captured: ', path)
    camera.capture(path)
    sleep(0.5)
    led.off()

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

pause()