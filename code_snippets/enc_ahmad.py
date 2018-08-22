import Adafruit_GPIO.I2C as Adafruit_I2C
import time
#import matplotlib

#i2c = Adafruit_I2C.Device(0x0c,1)
i2c = Adafruit_I2C.Device(0x40,1)
#i2c.write8(0x02,0x3D)
#a = i2c.readList(0x03,6)
#for i in a:
#    print(i)
#print(i2c.readU8(0x15))
#time.sleep(0.5)
#i2c.write8(0x15,0xF3)
#time.sleep(0.5)
#print(i2c.readU8(0x16))
n = 50
#meas_a = [0]*n
#diag = [0]*n
#i = 0
while 1:
    x = i2c.readU16(0xFE)
    #x2 = i2c.readU16(0xFE)
    #x1 = i2c.readU16(0xFF)
    #meas1 = (x2 >> 2) | (x1 & 0x3F)
    #print('16 bit: ', format(x,'016b'))
    #print('16 bit: ', format(0x00C0,'016b'))
    #x = int(response.encode('hex'),16)
    x = ((x << 8) | (x >> 8)) & 0xFFFF 
    meas = ((x & 0xFF00) >> 2) | ( x & 0x3F)
    #if i > n-1:
    #    #print(meas_a)
    #    if (sum(diag)) == 0:
    #print(sum(meas_a)/n)
    #    i = -1
    #print(format(i2c.readU16(250),'016b'))
    #print(format(i2c.readU8(22),'08b'))
    #print(format(i2c.readU8(23),'08b'))
    diag = (i2c.readU8(0xFB) & 0x08) == 8
    meas_a = meas*0.0219
    #i = i + 1
    #print('14 bit: ',format(meas,'014b'), ' Decimal: ',meas*0.0219)
    #print('14 bit: ',format(meas1,'014b'), ' Decimal: ',meas1*0.0219)
    print(meas_a)