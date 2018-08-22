# Change the name of this library! Cause it sucks!

#!/usr/bin/env python3
# import python libraries
#!/usr/bin/env python3
# import python libraries
import time
import getopt, sys
import math
import serial
import types

# import rcpy library
# This automatically initizalizes the robotics cape
import rcpy
import rcpy.mpu9250 as mpu9250

ser = serial.Serial(port = "/dev/ttyO0", baudrate=9600) # UT0

def turn(angle=None,mode=None,speed=None,direction=None):

    turn = True

    rcpy.set_state(rcpy.RUNNING)

    mpu9250.initialize(enable_dmp = True)

    while turn:

        if rcpy.get_state() == rcpy.RUNNING:

            # Read Data from Sensors

            data = mpu9250.read()

            # Get Compass Value and Convert to Degrees (0 to 180 , -180 to 0)

            compass = data['tb']
            compass_deg = (math.degrees(round(compass[2],2))) % 360

            angle = angle % 360

#            print(compass)
#            print(compass_deg)

            # First check if Point Turn or Swing Turn

            if mode == "point" or mode == None:

                if angle == 0:
    
                    data_l = [146, 32]  # Brake
                    data_r = [146, 32]

                # Check Angle is from 0 to 180 or 180 to 360, to determine which direction to turn

                elif 0 < angle and 180 > angle:   # If converted angle is between 0 and 180, point turn counter-clockwise
                
                    data_l = [255, 0,  98]  #   Rotate Left
                    data_r = [255, 1, 158]
            
                elif 180 < angle and 360 > angle:   # If converted angle is between 180 and 360, point turn clockwise
                                
                    data_l = [255, 0, 158]  #   Rotate Right
                    data_r = [255, 1,  98]

                ser.write(data_l)
                ser.write(data_r)

            if (compass_deg-2) <= angle and angle <= (compass_deg+2):

                data_l = [146, 32]  # Does not need bytearray()
                data_r = [146, 32]

                ser.write(data_l)
                ser.write(data_r)
                
    
            elif mode == "swing":
            
                continue        
            
            else:
                
                continue

        data_l = [255, 0, 128]  # Does not need bytearray()
        data_r = [255, 1, 128]

        ser.write(data_l)
        ser.write(data_r)
            
        turn = False
            
        print("Done!")
        
        pass
            
def stop(time=None):

    if time == None:

        data_l = [146, 32]  # Does not need bytearray()
        data_r = [146, 32]

        ser.write(data_l)
        ser.write(data_r)
        
    elif time >= int(0):
    
        time.sleep(time)

def end():

    exit()
   