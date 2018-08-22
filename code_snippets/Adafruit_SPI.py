#import the library
from Adafruit_BBIO.SPI import SPI
 
#Only need to execute one of the following lines:
#spi = SPI(bus, device) #/dev/spidev<bus>.<device>

spi = SPI(2,1)	#/dev/spidev1.1
