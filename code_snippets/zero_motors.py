import serial
import Adafruit_GPIO.I2C as Adafruit_I2C

i2c = Adafruit_I2C.Device(0x40,1)
ser = serial.Serial(port = "/dev/ttyO0", baudrate=9600) # UT0

n = 50
meas_a = [0]*n
diag = [0]*n
i = 0

speed = 25

wheel_r = 0

data_r = [255, 1, 128]

while 1:

    x = i2c.readU16(0xFE)
    x = ((x << 8) | (x >> 8)) & 0xFFFF 
    meas = ((x & 0xFF00) >> 2) | ( x & 0x3F)

    if i > n-1:
        if (sum(diag)) == 0:
            wheel_r = sum(meas_a)/n
            print(wheel_r)
        i = -1

    diag[i] = (i2c.readU8(0xFB) & 0x08) == 8
    meas_a[i] = meas*0.0219
    i = i + 1
