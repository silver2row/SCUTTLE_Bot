import serial
import time

ser = serial.Serial(port = "/dev/ttyS1", baudrate=9600, timeout=1) 

def set_speed(speedL, speedR):
    ser.write([0xFF, 0x0D, speedL])
    ser.write([0xFF, 0x00, speedR])


def read_voltage():
    ser.write([0xAA, 0x0D, 0x21, 0x17])
    response = ser.read(2)
    v_dc0 = int.from_bytes(response,'little')
    ser.write([0xAA, 0, 0x21, 0x17])
#    response = ser.read(2)
    v_dc1 = int.from_bytes(response,'little')
    return [v_dc0/1e3, v_dc1/1e3]

def read_temperature():
    ser.write([0xAA, 0x0D, 0x21, 0x18])
    response = ser.read(2)
    temp0 = int.from_bytes(response,'little')
    ser.write([0xAA, 1, 0x21, 0x18])
#    response = ser.read(2)
    temp1 = int.from_bytes(response,'little')
    return [temp0/10, temp1/10]

