#!/usr/bin/env python3
# import python libraries
import time
import getopt, sys
import math
import serial

# import rcpy library
# This automatically initizalizes the robotics cape
import rcpy 
import rcpy.mpu9250 as mpu9250

ser = serial.Serial(port = "/dev/ttyO0", baudrate=9600) # UT0

def turn(angle):
    # set state to rcpy.RUNNING
    rcpy.set_state(rcpy.RUNNING)

    # magnetometer ?
    mpu9250.initialize(enable_dmp = True)

    # keep running
    while True:

        # running
        if rcpy.get_state() == rcpy.RUNNING:
            
            data = mpu9250.read()

            tb = data['tb']
            tb_deg = math.degrees(round(tb[2],2))

            print(tb_deg)

            if angle > 0:
                
                if tb_deg < angle:
            
                    data_l = [255, 0, 98]  # Does not need bytearray()
                    data_r = [255, 1, 158]
                    
                    ser.write(data_l)
                    ser.write(data_r)
    
                elif tb_deg > angle:
                    
                    data_l = [255, 0, 128]  # Does not need bytearray()
                    data_r = [255, 1, 128]
                    
                    ser.write(data_l)
                    ser.write(data_r)

            elif angle < 0:
                
                if tb_deg > angle:
            
                    data_l = [255, 0, 158]  # Does not need bytearray()
                    data_r = [255, 1, 98]
                    
                    ser.write(data_l)
                    ser.write(data_r)
    
                elif tb_deg < angle:
                    
                    data_l = [255, 0, 128]  # Does not need bytearray()
                    data_r = [255, 1, 128]
                    
                    ser.write(data_l)
                    ser.write(data_r)
                    
                elif tb_deg > 175 or tb_deg < -175:
                    
                    data_l = [255, 0, 128]  # Does not need bytearray()
                    data_r = [255, 1, 128]
                    
                    ser.write(data_l)
                    ser.write(data_r)
                    
            else:
                continue
                    
            # Rotating clockwise 0 --> 3.14 --> -3.14 --> -0

# exiting program will automatically clean up cape

if __name__ == "__main__":
    turn(-90)
