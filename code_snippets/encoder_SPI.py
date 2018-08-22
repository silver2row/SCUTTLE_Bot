#import the library
from Adafruit_BBIO.SPI import SPI

#Only need to execute one of the following lines:

#spi = SPI(bus, device) #/dev/spidev<bus>.<device>
#spi1 = SPI(0,0)	#/dev/spidev1.0
#spi2 = SPI(0,1)	#/dev/spidev1.1
#spi3 = SPI(1,0)	#/dev/spidev2.0
spi4 = SPI(1,1)	#/dev/spidev2.1
readspi = read.spidev1(14, spi2)

print readspi