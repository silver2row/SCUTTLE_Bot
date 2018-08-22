import Adafruit_BBIO.GPIO as GPIO
import time
import signal
import serial

ultrasonic = True

speed = 125

if speed > 125:

    speed = 125

ultra_avg = [10]

n = 0
recoveredDistance = 0

echo_pin = 'P9_23' # GPIO1_17 actual name on BB Black
trig_pin = 'GPIO3_20' # name on board diagram
GPIO.setup(echo_pin, GPIO.IN)
GPIO.setup(trig_pin, GPIO.OUT)

UDP_IP = "localhost"	# IP to Listen on
UDP_PORT = 1221			# Port to Listen on

bufferSize = 1024 # Yes, lots of space.

ser = serial.Serial(port = "/dev/ttyO0", baudrate=9600) # UT0












data_l = [146, 32]  # Does not need bytearray()
data_r = [146, 32]

def distanceMeasurement(TRIG,ECHO):
    timeout = 0.01 # 10milliseconds
    pulseEnd = time.time()
    pulseStart = time.time()
    GPIO.output(TRIG, True)
    time.sleep(0.0001)
    GPIO.output(TRIG, False)

    while (GPIO.input(ECHO) == 0):# and (time.time()-pulseStart < 1):
        pulseStart = time.time()
        if (pulseStart - pulseEnd) > timeout:
            break
    while GPIO.input(ECHO) == 1:
        pulseEnd = time.time()

    pulseDuration = pulseEnd - pulseStart
    print(pulseEnd - pulseStart)
    distance = pulseDuration * 17150
    distance = round(distance, 2)
    return distance

while 1:

    data, addr = sock.recvfrom(bufferSize)

    data = str(data)

    data = int(data[2:len(str(data))-1])

#    data = int(data)

#    print(data)


    if data > 0 and data < 40:

      #  print(data, "Turn Left!")

        #   turn left
        data_l = [255, 0, 128 - speed]  # Does not need bytearray()
        data_r = [255, 1, 128 + speed]

    elif data > 40 and data < 120:

     #   print(data, "Good!")

#        data_l = [146, 32]  # Does not need bytearray()
#        data_r = [146, 32]

#        data_l = [255, 0, speed]  # Does not need bytearray()
#        data_r = [255, 1, speed]

        if recoveredDistance < 80 and recoveredDistance > 30:

            data_l = [146, 32]  # Does not need bytearray()
            data_r = [146, 32]

        elif recoveredDistance > 30 or recoveredDistance > 80:

            data_l = [255, 0, 128 + speed]  # Does not need bytearray()
            data_r = [255, 1, 128 + speed]  # Does not need bytearray()
#            print("foraward")

        elif recoveredDistance < 30:

            data_l = [255, 0, 128 - speed]  # Does not need bytearray()
            data_r = [255, 1, 128 - speed]  # Does not need bytearray()
#            print("BACK")

    elif data > 120:

    #    print(data, "Turn Right!")
    #   turn right
        data_l = [255, 0, 128 + speed]  # Does not need bytearray()
        data_r = [255, 1, 128 - speed]

    elif data > 160:

        print(data, "lol wut")

    ser.write(data_l)
    ser.write(data_r)

    if ultrasonic == True:

        n = n + 1

        if n > 10:

            recoveredDistance = distanceMeasurement(trig_pin, echo_pin)

            if abs(recoveredDistance) > 10000:

                recoveredDistance = 30

            #print ("Distance: ", recoveredDistance, "cm")

            time.sleep(0.1)

            print(n)

            n = 0


    else:

        continue

ser.close()
