from gpiozero import LED
from time import sleep
from RPi import GPIO

led = LED(12)

try:
    while True:
        led.on()
        sleep(1)
        led.off()
        sleep(1)
except:
    GPIO.cleanup()