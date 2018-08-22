#import Adafruit_BBIO.UART as UART
import os
import time
import socket
import serial
import Adafruit_BBIO.ADC as ADC

speed_l =254
speed_r =254

ir_bound = 500

ser = serial.Serial(port = "/dev/ttyO0", baudrate=9600) # UT0

ADC.setup()
    
if ser.isOpen():
    
    while True:

        ir_sense = int(ADC.read_raw("AIN0"))
    
#        speed = int(input("Speed [0-100]: "))
    
        data_l = [255, 0, speed_l]  # Does not need bytearray()
        data_r = [255, 1, speed_r]
        
        if ir_sense > ir_bound:

#            data_stop_l = [255, 0, 128]  # Does not need bytearray()
#            data_stop_r = [255, 1, 128]
    
#            ser.write(data_stop_l)
#            ser.write(data_stop_r)
 
            data_turn_l = [255, 0, 0]  # Does not need bytearray()
            data_turn_r = [255, 1, 254]
    
            ser.write(data_turn_l)
            ser.write(data_turn_r)

            time.sleep(.5)
    
        else:
            ser.write(data_l)
            ser.write(data_r)

        print(ir_sense)

    ser.close()

