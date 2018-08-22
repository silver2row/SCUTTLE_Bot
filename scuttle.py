# Written By: Daniyal Ansari

# Import Libraries

import time, getopt, sys, math, serial, types, socket, signal, inspect, numpy as np, cv2, argparse, os

import rcpy
import rcpy.mpu9250 as mpu9250  # IMU Library

import Adafruit_BBIO.GPIO as GPIO
import Adafruit_GPIO.I2C as Adafruit_I2C

    #####################################
    #                                   #
    #       Configuration Values        #
    #                                   #
    #####################################

'''

    This configuration section allows you to change properties of the SCUTTLE library code.

'''
    #   Debugging Options

verbose = False
log_output_location = "./scuttle_debugging.log"

    #   ADC Settings

valid_adc_pins = ("AIN0","AIN1","AIN2","AIN3")

    #   IMU Settings

    #   Compass Settings

comapss_i2c = Adafruit_I2C.Device(0x1e,1)   # I2C Bus Device Location

compass_write_registers =      (0x00, 0x02)     # Registers to Write Data to
compass_write_registers_data = (0x70, 0x01)     # Data to Write to Registers

    #   Rotary Encoder Settings

right_encoder = Adafruit_I2C.Device(0x40,1) # Power the Rotary Encoder Address Select Pin to change the address of the left encoder
left_encoder  = Adafruit_I2C.Device(0x41,1) # Power pin A0 to set address to 0x41 (default) or power pin A1 to set address to 0x42

    #   Motor Controller Settings

ser_motor = serial.Serial(port = "/dev/ttyO0", baudrate=9600)   # UART Location of Device Bus

right_motor = 0     # ID of Pololu H-Bridge
left_motor  = 1     # ID of Pololu H-Bridge

    #   UDP Control Settings

ip = "192.168.8.1"      # Set to the interface IP over which you will send UDP Data
port = 1337             # Set to the port to which you will send UDP Data

bufferSize = 1024   # Definitely too much space.

forward_key = 0     # The value the UDP server expects to recieve to perform an action
back_key    = 1
right_key   = 2
left_key    = 3

stop_key    = 4
quit_key    = 5

    #   Ultrasonic Sensor Settings

echo_pin = "P9_23"      # Ultrasonic Echo Pin
trig_pin = "GPIO3_20"   # Ultrasonic Trigger Pin

trigger_pulse_duration = 0.0001     # How long to hold TRIG On dictating pulse length

    #   Color Tracking Settings

camera_number = 0   # Can be listed with "ls /dev/video*"

range_filter = "HSV"    # HSV or RGB

image_size = (240,160)  # Size of Image from Camera. L * W

min_color_values = (  0,   0,   0)  # Minimum Color Values
max_color_values = (255, 255, 255)  # Maximum Color Values

ultrasonic_range = (40,120) # Range in cm to keep object in front of robot

    #############################################
    #                                           #
    #       Configuration Value Checking        #
    #                                           #
    #############################################

#   ADC Settings

#   IMU Settings

#   Compass Settings

#   Rotary Encoder Settings

#   Motor Controller Settings Check

if right_motor == left_motor:

    print("The Right and Left Motors cannot have the same ID!")
    exit()

else:
    pass

#   UDP Control Settings

#   Ultrasonic Sensor Settings

#   Color Tracking Settings

    #################################
    #                               #
    #       Library Functions       #
    #                               #
    #################################

#   ADC

#   IMU

#   Compass

def compass():

    comapss_i2c.write8(compass_write_registers[0],compass_write_registers_data[0])  # Write Value properties to Compass Data Registers
    comapss_i2c.write8(compass_write_registers[1],compass_write_registers_data[1])

    compass_data = i2c.readList(0x03,6)     # Read Data from Compass Registers

    compass_x = np.int16((compass_data[0] << 8) | compass_data[1])*0.92
    compass_z = np.int16((compass_data[2] << 8) | compass_data[3])*0.92
    compass_y = np.int16((compass_data[4] << 8) | compass_data[5])*0.92

    return(compass_x,compass_y,compass_z)   # Return Compass Values

#   Rotary Encoder

def rotaryEncoder(motor=None,unit=None):

    if motor = "right"

        right_encoder.write8(0x02,0x3D)
        right_encoder_data = right_encoder.readList(0xfd,3)
        return(right_encoder_data[0],right_encoder_data[1],right_encoder_data[2])

    elif motor = "left"

        left_encoder.write8(0x02,0x3D)
        left_encoder_data = left_encoder.readList(0xfd,3)
        return(left_encoder_data[0],left_encoder_data[1],left_encoder_data[2])

    else:
        continue

#   Motor Controller

#       Forward Function

def forward(unit=None,value=None,speed=None):

#       Backward Function

def backward(unit=None,value=None,speed=None):

#       Turning Function

def turn(angle=None,mode=None,speed=30,direction=None):

    turn = True

    rcpy.set_state(rcpy.RUNNING)

    mpu9250.initialize(enable_dmp = True)

    while turn:

        if rcpy.get_state() == rcpy.RUNNING:

            imu_data = mpu9250.read()   # Read Data from Sensors
            imu = imu_data['tb']        # Get imu Value and Convert to Degrees (0 to 180 , -180 to 0)
            imu_deg = (math.degrees(round(imu[2],2))) % 360

            angle = angle % 360

            if mode == "point" or mode == None:

                if angle == 0:

                    data_l = [146, 32]  # Brake
                    data_r = [146, 32]

                # Check Angle is from 0 to 180 or 180 to 360, to determine which direction to turn

                elif 0 < angle and 180 > angle:   # If converted angle is between 0 and 180, point turn counter-clockwise

                    data_l = [255, 0, 128 - speed]  #   Rotate Left
                    data_r = [255, 1, 128 + speed]

                elif 180 < angle and 360 > angle:   # If converted angle is between 180 and 360, point turn clockwise

                    data_l = [255, 0, 128 + speed]  #   Rotate Right
                    data_r = [255, 1, 128 - speed]

            if (imu_deg-2) <= angle and angle <= (imu_deg+2):   # Once Angle is within Range Stop Motors

                data_l = [146, 32]      # Brake
                data_r = [146, 32]

            elif mode == "swing":

                if direction == "forward":

                    if angle == 0:

                        data_l = [146, 32]  # Brake
                        data_r = [146, 32]

                    # Check Angle is from 0 to 180 or 180 to 360, to determine which direction to turn

                    elif 0 < angle and 180 > angle:   # If converted angle is between 0 and 180, point turn counter-clockwise

                        data_l = [255, 0, 128]  #   Rotate Left
                        data_r = [255, 1, 128 + speed]

                    elif 180 < angle and 360 > angle:   # If converted angle is between 180 and 360, point turn clockwise

                        data_l = [255, 0, 128 + speed]  #   Rotate Right
                        data_r = [255, 1, 128]

                if (imu_deg-2) <= angle and angle <= (imu_deg+2):   # Once Angle is within Range Stop Motors

                    data_l = [146, 32]      # Brake
                    data_r = [146, 32]

                elif direction == "backward":

                    if angle == 0:

                        data_l = [146, 32]  # Brake
                        data_r = [146, 32]

                    # Check Angle is from 0 to 180 or 180 to 360, to determine which direction to turn

                    elif 0 < angle and 180 > angle:   # If converted angle is between 0 and 180, point turn counter-clockwise

                        data_l = [255, 0, 128 - speed]  #   Rotate Left
                        data_r = [255, 1, 128]

                    elif 180 < angle and 360 > angle:   # If converted angle is between 180 and 360, point turn clockwise

                        data_l = [255, 0, 128]  #   Rotate Right
                        data_r = [255, 1, 128 - speed]

                if (imu_deg-2) <= angle and angle <= (imu_deg+2):   # Once Angle is within Range Stop Motors

                    data_l = [146, 32]      # Brake
                    data_r = [146, 32]

                else:

                    continue

                ser_motor.write(data_l)     # Send Data to Motor Controllers
                ser_motor.write(data_r)

        data_l = [146, 32]  # Brake
        data_r = [146, 32]

        ser_motor.write(data_l)     # Send Data to Motor Controllers
        ser_motor.write(data_r)

        turn = False

        print("Done!")

        pass

#   UDP Control

def udp_control(ip=None,port=None):

    exit = False

    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    sock.bind((ip, port))   # Start UDP Server

    data_l = [146, 32]  # Brake
    data_r = [146, 32]

    while exit == False:    # Start Infinite Loop and Exit Condition

        data, addr = sock.recvfrom(bufferSize) # buffer size is 1024 bytes

        if data == b"0":
            data_l = [255, 0, 254]  # Go Forward
            data_r = [255, 1, 254]  # Set Left and Right Motor Speeds to Full Forward

        elif data == b"1":
            data_l = [255, 0, 0]    # Go Backwards
            data_r = [255, 1, 0]    # Set Left and Right Motor Speeds to Full Backward

        elif data == b"2":
        	data_l = [255, 0, 254]  # Rotate Right
        	data_r = [255, 1,   0]  # Set Right Motor to Full Backward and Left Motor Speeds to Full Forward

        elif data == b"3":
            data_l = [255, 1, 254]  # Rotate Left
            data_r = [255, 0,   0]  # Set Left Motor to Full Backward and Right Motor Speeds to Full Forward

        elif data == b"4":
        	data_l = [146, 32]      # Brake
        	data_r = [146, 32]      # Set Left and Right Motor Speeds to Brake

        elif data == b"5":
            exit = True             # Quit udp_control()

        else:                       # Throw out any values not expected
            print("Unrecongnized Value!")
        	continue

        ser_motor.write(data_l)     # Send Left Motor Data
        ser_motor.write(data_r)     # Send Right Motor Data

#   Ultrasonic Sensor

def ultrasonic(unit=None):	# Unit: Raw, cm, inches

    GPIO.setup(echo_pin, GPIO.IN)   # Setup Echo GPIO Pin
    GPIO.setup(trig_pin, GPIO.OUT)  # Setup Trig GPIO Pin

    pulseEnd = 0
    pulseStart = time.time()            # Grabs Current Time
    GPIO.output(TRIG, True)             # Sets Trig Pin High for Start of Pulse
    time.sleep(trigger_pulse_duration)  # Delay to Create Pulse Length
    GPIO.output(TRIG, False)            # Sets Trig Pin Low to End Pulse

    while (GPIO.input(ECHO) == 0):      # Waits for Return of Pulse by Checking For High on Echo Pin
        pulseStart = time.time()
        if (pulseStart - pulseEnd) > timeout:   # If Program does not get Echo HIGH move on
            break
        else:
            pass
    while GPIO.input(ECHO) == 1:        # Once Recieves Echo check Time
        pulseEnd = time.time()

    pulseDuration = pulseEnd - pulseStart   # Calculate Pulse Return Time
    distance = pulseDuration * 17150
    distance = round(distance, 2)           # Round Datapoint

    if unit == "raw":
        ultrasonic_distance = distanceMeasurement(trig_pin, echo_pin)       # Return Raw Value
        return ultrasonic_distance

    elif unit == "cm":
        ultrasonic_distance = distanceMeasurement(trig_pin, echo_pin)       # Return Value in cm
        return ultrasonic_distance

    elif unit == "inches":
        ultrasonic_distance = round(distanceMeasurement(trig_pin, echo_pin) * 0.39, 0)  # Return Value in Inches
        return ultrasonic_distance

    else:
        print(unit, "is not a valid unit!")
        exit()

#   Color Tracking

def chase_color(color_range=None):      # Probably need to get a better method of entering data in function

#    x_pos = 0
#    y_pos = 0

    camera = cv2.VideoCapture(camera_number)
    camera.set(3, image_size[0])
    camera.set(4, image_size[1])

    while True:

       ret, image = camera.read()

       if not ret:
           break

       if range_filter == 'RGB':
           frame_to_thresh = image.copy()
       else:
        frame_to_thresh = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        thresh = cv2.inRange(frame_to_thresh, (15, 147, 148), (64, 255, 255))

        kernel = np.ones((5,5),np.uint8)
        mask = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None

        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            ((x_pos, y_pos), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

         ultrasonic_distance = ultrasonic("cm"):	# Unit: Raw, cm, inches

        if x_pos > 0 and x_pos < 40:

            data_l = [255, 0, 128 - speed]  # Does not need bytearray()
            data_r = [255, 1, 128 + speed]

        elif x_pos > 40 and x_pos < ((image_size[1]/3) * 2):

            if ultrasonic_distance < 80 and ultrasonic_distance > 30:

                data_l = [146, 32]  # Does not need bytearray()
                data_r = [146, 32]

            elif ultrasonic_distance > 30 or ultrasonic_distance > 80:

                data_l = [255, 0, 128 + speed]  # Does not need bytearray()
                data_r = [255, 1, 128 + speed]  # Does not need bytearray()

            elif ultrasonic_distance < 30:

                data_l = [255, 0, 128 - speed]  # Does not need bytearray()
                data_r = [255, 1, 128 - speed]  # Does not need bytearray()

        elif x_pos > ((image_size[1]/3) * 2):

            data_l = [255, 0, 128 + speed]  # Does not need bytearray()
            data_r = [255, 1, 128 - speed]

        elif x_pos > image_size[1]:   # If

            pass

        ser.write(data_l)
        ser.write(data_r)

        if ultrasonic == True:

            n = n + 1

            if n > 10:

                ultrasonic_distance = distanceMeasurement(trig_pin, echo_pin)

                if abs(ultrasonic_distance) > 10000:

                    ultrasonic_distance = 30

                time.sleep(0.1)

                n = 0

        else:

            continue
