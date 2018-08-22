#!/usr/bin/env python3
# import python libraries
import time
import getopt, sys
import math

# import rcpy library
# This automatically initizalizes the robotics cape
import rcpy 
import rcpy.mpu9250 as mpu9250

# defaults
enable_magnetometer = False
show_compass = False
show_gyro = False
show_accel = False
show_quat = False
show_tb = False
sample_rate = 100
enable_fusion = False
show_period = False
newline = '\r'

def main():
    # set state to rcpy.RUNNING
    rcpy.set_state(rcpy.RUNNING)

    # magnetometer ?
    mpu9250.initialize(enable_dmp = True,
                       dmp_sample_rate = sample_rate,
                       enable_fusion = enable_fusion,
                       enable_magnetometer = enable_magnetometer)


    # keep running
    while True:

        # running
        if rcpy.get_state() == rcpy.RUNNING:
            
            data = mpu9250.read()

            compass = data['tb']
            compass_deg = math.degrees(round(compass[2],2))

            if compass_deg < 0:
                
                compass_deg = (180 - abs(compass_deg)) + 180


            print(compass_deg)

            time.sleep(0.1)

# exiting program will automatically clean up cape

if __name__ == "__main__":
    main()