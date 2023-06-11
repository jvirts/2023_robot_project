#run this as root, sudo su
import time
import serial
import struct
import numpy as np


#"dev/ttyUSB0"
ser=serial.Serial("/dev/ttyS0", baudrate=9600, parity=serial.PARITY_NONE, \
stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS,timeout=1)



chz = 'z\r\n'
while(1):
	ser.write(chz.encode())
	#ser.write(chz +'\r\n')



