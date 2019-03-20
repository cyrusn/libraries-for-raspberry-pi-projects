#! /user/bin/env python3
from picamera import PiCamera
from datetime import datetime
from os import path


class StubLED:
    def on(self):
        pass

    def off(self):
        pass


class Picroscope:
    def __init__(self, led=None, rotation=0, captureDir="/home/pi/Desktop"):
        self.captureDir = captureDir
        self.led = led if led else StubLED()
        self.camera = PiCamera()
        self.camera.rotation = rotation
        self.preview = False

    def capture(self):
        if self.preview:
            now = datetime.now().isoformat()
            file = path.join(self.captureDir, format(now), ".jpg")
            print("Image Captured: ", path)
            self.camera.capture(file)

    def toggle_preview(self):
        self.preview = not self.preview
        if self.preview:
            self.led.on()
            self.camera.start_preview()
        else:
            self.led.off()
            self.camera.stop_preview()

    @property
    def help_text(self):
        return (
            "Press left button to start preview.\n"
            + "Press right button while previewing to capture image.\n"
            + "Press ctrl-C to stop the programme."
        )


if __name__ == "__main__":
    from gpiozero import Button, LED
    from signal import pause

    led = LED(19)
    left_button = Button(20)
    right_button = Button(21)
    picroscope = Picroscope(led=led, rotation=90, captureDir="/home/pi/Desktop/Images")

    print(microscope.help_text)
    left_button.when_pressed = picroscope.toggle_preview
    right_button.when_pressed = picroscope.capture
    pause()
