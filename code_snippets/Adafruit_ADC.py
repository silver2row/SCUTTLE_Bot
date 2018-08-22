import Adafruit_BBIO.ADC as ADC
import time

while True:
    
    ADC.setup()
    value = ADC.read_raw("AIN0")
    
    print(value)
    time.sleep(0.01)
