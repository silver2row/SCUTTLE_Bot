import Adafruit_GPIO.I2C as Adafruit_I2C
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import numpy as np
import socket
import struct
import subprocess
import time
import rcpy.mpu9250 as mpu9250
import motor_control
import compass
import hcsr04
import encoder

DATA_UPDATE_FREQ = 20.0 # Hertz

# --- initiliaze compass
I2Ccompass = Adafruit_I2C.Device(0x1e,1)
I2Ccompass.write8(0x00,0x70)
I2Ccompass.write8(0x02,0x01)
# ---
# --- encoders
enc0 = Adafruit_I2C.Device(0x40,1)
enc1 = Adafruit_I2C.Device(0x41,1)
#enc1.write8(0x02,0x3D)
# --- ultrasonic sensor pins
echo_pin = 'P9_23' # GPIO1_17 actual name on BB Black
trig_pin = 'GPIO3_20' # name on board diagram
GPIO.setup(echo_pin, GPIO.IN) 
GPIO.setup(trig_pin, GPIO.OUT)
# --- Initialize UDP
IPADDR = '192.168.8.1' #BBB ip address
PORTNUM = 3553 # port number, has to match the one in MATLAB
# initialize a socket, think of it as a cable
# SOCK_DGRAM specifies that this is UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
s.settimeout(0.0001) # 1ms
# connect the socket, think of it as connecting the cable to the address location
s.bind((IPADDR, PORTNUM))
# ---
# --- initialize on board imu
imu = mpu9250.IMU(enable_dmp = True, dmp_sample_rate = 20, enable_magentometer = False)
# ---

address = []
data = []
data_snt = 13*[0]
speedL, speedR = 127, 127

t0 = time.time()

while 1:
    t1 = time.time()
    try:
        data, address = s.recvfrom(65536)
    except:
        pass
    while data:
        speedR = data[0]
        speedL = data[1]
        try:
            data, address = s.recvfrom(65536)
        except:
            break
    if ((t1-t0) >= (1.0/DATA_UPDATE_FREQ)): # send data every 50 millisecond
        #print(t1-t0)
        t0 = t1
        if address: # at least on package has to be received before we know where to send!
            PACKETDATA = struct.pack('%sf' %len(data_snt),*data_snt)
            s.sendto(PACKETDATA, address)
            data = []
## --- write speed to H-bridge
    print(speedL, speedR)
    motor_control.set_speed(speedL, speedR)
   # [vDC0, vDC1] = motor_control.read_voltage()
   # [temp0, temp1] = motor_control.read_temperature()

## --- reading the compass angle
    heading = compass.get_angle(I2Ccompass)

## --- read pitch and roll
#    data_imu = imu.read()#read_accel_data()#

## --- ultrasonic distance measurement
    distance = hcsr04.distanceMeasurement(trig_pin, echo_pin, GPIO)

## --- encoders
    encoder0, encoder1 = encoder.read_encoders_angle(enc0,enc1)

## --- put data in array to send over udp
    data_snt[0] = heading
    data_snt[1] = 100#vDC0
    data_snt[2] = 100#vDC1
    data_snt[3] = 90#temp0
    data_snt[4] = 90#temp1
    data_snt[6] = encoder0
    data_snt[7] = encoder1
    #data_snt[8] = speed0
    #data_snt[9] = speed1
    data_snt[10] = distance
    #data_snt[11] = data_imu['tb'][0] # pitch
    #data_snt[12] = data_imu['tb'][1] # roll
## ---
# close the socket (UDP connection)
s.close()

