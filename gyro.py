import smbus
import time

import RPi.GPIO as gpio

class Gyro():

    PWR_M   = 0x6B
    DIV   = 0x19
    CONFIG       = 0x1A
    GYRO_CONFIG  = 0x1B
    INT_EN   = 0x38
    ACCEL_X = 0x3B
    ACCEL_Y = 0x3D
    ACCEL_Z = 0x3F
    GYRO_X  = 0x43
    GYRO_Y  = 0x45
    GYRO_Z  = 0x47
    TEMP = 0x41
    bus = smbus.SMBus(1)

    Device_Address = 0x68   # device address
    AxCal=0
    AyCal=0
    AzCal=0
    GxCal=0
    GyCal=0
    GzCal=0
    
    def _init_(self, address):
        self.device_address = address
        
        
        
        
        
        
        
        