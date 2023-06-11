#run this as root, sudo su
import time
import serial
import struct
import numpy as np


#"dev/ttyUSB0"
ser=serial.Serial("/dev/ttyS0", baudrate=9600, parity=serial.PARITY_NONE, \
stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS,timeout=1)



counter = 0
while(1):
	time.sleep(1)
	ztemp = ser.read(1)
	print(ztemp)
	print(counter)
	#ser.write(chz +'\r\n')



