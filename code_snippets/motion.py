#Written By: Daniyal Ansari

import Adafruit_GPIO.I2C as Adafruit_I2C, Adafruit_BBIO.GPIO as GPIO, time, getopt, sys, math, serial, types, socket, signal, rcpy, rcpy.mpu9250 as mpu9250

ser_motor = serial.Serial(port = "/dev/ttyO0", baudrate=9600) # UT0

def turn(angle=None,mode=None,speed=30,direction=None):

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
                
                    data_l = [255, 0, 128 - speed]  #   Rotate Left
                    data_r = [255, 1, 128 + speed]
            
                elif 180 < angle and 360 > angle:   # If converted angle is between 180 and 360, point turn clockwise
                                
                    data_l = [255, 0, 128 + speed]  #   Rotate Left
                    data_r = [255, 1, 128 - speed]

                ser_motor.write(data_l)
                ser_motor.write(data_r)

            if (compass_deg-2) <= angle and angle <= (compass_deg+2):

                data_l = [146, 32]  # Does not need bytearray()
                data_r = [146, 32]

                ser_motor.write(data_l)
                ser_motor.write(data_r)
                
    
            elif mode == "swing":
            
                continue        
            
            else:
                
                continue

        data_l = [146, 32]  # Brake
        data_r = [146, 32]

        ser_motor.write(data_l)
        ser_motor.write(data_r)
            
        turn = False
            
        print("Done!")
        
        pass

'''
def forward(value-None,unit=None,direction=None,speed=None):	# Value = Number of Wheel Rotations or Distance to Travel, Unit = Swing or Point


def backward(value-None,unit=None,direction=None,speed=None):

def gyro(axis=None,unit=None):	# Unit: Raw, x, y, z

'''

def compass(unit=None):
    
    i2c = Adafruit_I2C.Device(0x1e,1)
    
    i2c.write8(0x01,0x71)
    i2c.write8(0x02,0x01)
    i2c.write8(0x03,0x02)
    
#    i2c.write8(0x02,0x3D)

#    i2c.write8(0x02,0x3D)
    a = i2c.readList(0x03,6)
    return(a[0],a[1],a[2],a[3],a[4],a[5])


'''
def irProximity(unit=None):	# Unit: Raw, cm, inches


'''

def rotaryEncoder(motor=None,unit=None):
    
    i2c = Adafruit_I2C.Device(0x40,1)
    i2c.write8(0x02,0x3D)
    a = i2c.readList(0xfd,3)
    return(a[0],a[1],a[2])
    

'''

def hbridgeTemp(unit=None):

	ser_motor.write() # ENTER TEMP DATA REQUEST

def barrelVoltage(unit=None):	# Unit: Raw, Volts

def lipoVoltage(unit=None):	# Unit: Raw, Volts

def motorMessage(message):

	if len(message) == 0 && if isinstance(m, list) == True:		# Check if Custom Message is an Array and has at Least 1 Argument

		message = ser_motor.write(message)

	else:

		print("motorMessage(): Requires at least 1 argument!")

		exit()
'''

    
    

def stop(delay=None):

    if time == None:

        data_l = [146, 32]  # Does not need bytearray()
        data_r = [146, 32]

        ser_motor.write(data_l)
        ser_motor.write(data_r)
        
    elif delay >= int(0):
    
        time.sleep(delay-3) # Time delay -3 for motor response time... Sloppy...
        
    pass

def end():

    exit()
  
def remote_keyboard():  
  
    UDP_IP = "192.168.8.1"
    UDP_PORT = 6969
    
    data = 0
    
    exit = False
    
    ser_motor = serial.Serial(port = "/dev/ttyO0", baudrate=9600) # UT0
    
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
    
    sock.bind((UDP_IP, UDP_PORT))
    
    data_l = [146, 32]  # Brake
    data_r = [146, 32]
    
    while exit == False:
        	
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        
        if data == b"0":
        	data_l = [255, 1, 254]  #   Rotate Left
        	data_r = [255, 0,   0]
        
        elif data == b"1":
        	data_l = [255, 0, 254]  #   Rotate Right
        	data_r = [255, 1,   0]
        
        elif data == b"2":
        	data_l = [255, 0, 254]  # Go Forward
        	data_r = [255, 1, 254]
        
        elif data == b"3":
        	data_l = [255, 0, 0]   # Go Backwards
        	data_r = [255, 1, 0]
        
        elif data == b"4":
        	data_l = [146, 32]  # Brake
        	data_r = [146, 32]
        
        elif data == b"5":
            exit = True
        
        else:
        
        	continue
        print('done with command')
        sock.sendto('test',addr)
        print('responded')

        ser_motor.write(data_l)
        ser_motor.write(data_r)
        