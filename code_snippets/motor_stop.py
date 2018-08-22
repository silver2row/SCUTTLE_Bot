#import Adafruit_BBIO.UART as UART
import os
import time
import socket
import serial
import Adafruit_BBIO.ADC as ADC

speed = 128
ir_bound = 500

ser = serial.Serial(port = "/dev/ttyO0", baudrate=9600) # UT0

ADC.setup()
    
data_l = [255, 0, speed]  # Does not need bytearray()
data_r = [255, 1, speed]

ser.write(data_l)
ser.write(data_r)

ser.close()