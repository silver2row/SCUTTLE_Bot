#import Adafruit_BBIO.UART as UART
import os
import time
import socket
import serial

#UART.setup("UART5")
 
ser = serial.Serial(port = "/dev/ttyO0", baudrate=9600) # UT0

if ser.isOpen():

    print("Serial is Connected!")

    while True:
    
        speed = int(input("Speed [0-100]: "))
    
        data_l = [255, 0, speed]  # Does not need bytearray()
        data_r = [255, 1, speed]
    
        ser.write(data_l)
        ser.write(data_r)

    ser.close()