import numpy as np


def get_angle(i2c):
    x, y, z = read_xyz(i2c)
    try:
        heading = np.arctan(abs(y)/abs(x))
        heading = heading*180.0/np.pi
    except:
        heading = 0 
    if y < 0:
        if x < 0:
            heading = 270 - heading 
        else:
            heading = heading + 90
    else:
        if x < 0:
            heading = 270 + heading 
        else:
            heading = 90 - heading
    return heading

def read_xyz(i2c):
    try:
        i2c.write8(0x02,0x01)
        a = i2c.readList(0x03,6)
        x = np.int16((a[0] << 8) | a[1])*0.92
        z = np.int16((a[2] << 8) | a[3])*0.92
        y = np.int16((a[4] << 8) | a[5])*0.92
    except:
        print('Warning (I2C): Could not read compass')
        x,y,z = 0,0,0
    return [x,y,z]
