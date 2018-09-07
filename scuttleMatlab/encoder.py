
def read_encoders_angle(enc0,enc1):
    try:
        x = enc0.readU16(0xFE)
        x = ((x << 8) | (x >> 8)) & 0xFFFF 
        meas = ((x & 0xFF00) >> 2) | ( x & 0x3F)
        angle0 = meas*0.0219
    except:
        print('Warning (I2C): Could not read encoder0')
        angle0 = 0
    try:
        x = enc1.readU16(0xFE)
        x = ((x << 8) | (x >> 8)) & 0xFFFF 
        meas = ((x & 0xFF00) >> 2) | ( x & 0x3F)
        angle1 = meas*0.0219
    except:
        print('Warning (I2C): Could not read encoder1')
        angle1 = 0
    return [angle0, angle1]

