# Test for the library below
# https://github.com/Tijndagamer/mpu6050

from mpu6050 import mpu6050
from time import sleep

sensor = mpu6050(0x68)

while True:
    print(sensor.get_accel_data())
#     print(sensor.get_temp())
#     print(sensor.get_gyro_data())
    sleep(0.5)
    