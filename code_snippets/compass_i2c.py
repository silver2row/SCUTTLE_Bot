import time
import Adafruit_GPIO.I2C as Adafruit_I2C
import numpy as np

i2c = Adafruit_I2C.Device(0x1e,1)
i2c.write8(0x00,0x70)
i2c.write8(0x02,0x01)
while 1:
    a = i2c.readList(0x03,6)
    i2c.write8(0x02,0x01)
    x = np.int16((a[0] << 8) | a[1])*0.92
    z = np.int16((a[2] << 8) | a[3])*0.92
    y = np.int16((a[4] << 8) | a[5])*0.92
    print('x:',x,'y:',y,'z:',z)
    time.sleep(0.1)
