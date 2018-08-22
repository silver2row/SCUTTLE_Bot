#import Adafruit_BBIO.UART as UART
import os
import time
import socket
import serial
import Adafruit_BBIO.ADC as ADC

speed = 254
ir_bound = 500

ser = serial.Serial(port = "/dev/ttyO0", baudrate=9600) # UT0

ADC.setup()
    
if ser.isOpen():
    
    while True:

        ir_sense = int(ADC.read_raw("AIN0"))
    
#        speed = int(input("Speed [0-100]: "))
    
        data_l = [255, 0, speed]  # Does not need bytearray()
        data_r = [255, 1, speed]
        
        if ir_sense > ir_bound:

            data_stop_l = [255, 0, 128]  # Does not need bytearray()
            data_stop_r = [255, 1, 128]
    
            ser.write(data_stop_l)
            ser.write(data_stop_r)
    
        else:
            ser.write(data_l)
            ser.write(data_r)

        print(ir_sense)

    ser.close()