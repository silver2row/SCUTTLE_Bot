import serial
import time

ser = serial.Serial(port = "/dev/ttyO0", baudrate=9600) # UT0

#data = [0xAA, 0x00, 0x21, 0x17] # Pololu
data = [0xAA,0xA1, 0x17] # compact
#print 'sending'
ser.write(data)
#print 'data sent'
#print 'requesting'
time.sleep(0.1)
response = ser.read(2)
#print [response]
# convert to str to hex and re-arrange bytes
x = int(response.encode('hex'),16)
v_dc = ((x << 8) | (x >> 8)) & 0xFFFF 
print(v_dc/1e3)

