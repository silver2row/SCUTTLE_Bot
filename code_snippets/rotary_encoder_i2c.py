import Adafruit_GPIO.I2C as Adafruit_I2C
import time

i2c = Adafruit_I2C.Device(0x40,1)

while True:
#    i2c.write8(0x02,0x3D)
    a = i2c.readList(0xfd,3)
    print(a[0],a[1],a[2])
    time.sleep(1)