#import Adafruit_BBIO.UART as UART
import serial
import time

#UART.setup("UART5")
 
#ser = serial.Serial(port = "/dev/ttyO5", baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
ser = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
ser.close()
ser.open()
while True:
    if ser.isOpen():
        data = ser.read(221)
        print(data)
        time.sleep(1)
