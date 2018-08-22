#import Adafruit_BBIO.UART as UART
import os
import time
import socket
import serial
import Adafruit_BBIO.ADC as ADC

ser = serial.Serial(port = "/dev/ttyO0", baudrate=9600) # UT0

ADC.setup()
    
# Fast Spin   

data_l = [255, 0, 0]  # Does not need bytearray()
data_r = [255, 1, 254]

# Slow Spin 

#data_l = [255, 0, 98]  # Does not need bytearray()
#data_r = [255, 1, 158]


ser.write(data_l)
ser.write(data_r)

ser.close()