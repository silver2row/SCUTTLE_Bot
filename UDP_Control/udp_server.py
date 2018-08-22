import socket
import serial

UDP_IP = "192.168.8.1"
UDP_PORT = 6969

data = 0

exit = False

ser = serial.Serial(port = "/dev/ttyO0", baudrate=9600) # UT0

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
    	
    ser.write(data_l)
    ser.write(data_r)
