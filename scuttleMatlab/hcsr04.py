import time


def distanceMeasurement(TRIG,ECHO, GPIO):
    timeout = 0.01 # 10milliseconds
    pulseEnd = time.time()
    pulseStart = time.time()
    GPIO.output(TRIG, True)
    time.sleep(0.0001)
    GPIO.output(TRIG, False)

    while (GPIO.input(ECHO) == 0):
        pulseStart = time.time()
        if (pulseStart - pulseEnd) > timeout:
            break
    while GPIO.input(ECHO) == 1:
        pulseEnd = time.time()
 
    pulseDuration = pulseEnd - pulseStart
    distance = pulseDuration * 17150
    distance = round(distance, 2)
    return distance
