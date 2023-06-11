#run this as root, sudo su
import time
import serial
import struct
import numpy as np

countme = np.array(0)
xvals = np.array(0)
yvals = np.array(0)
zvals = np.array(0)


#"dev/ttyUSB0"
ser=serial.Serial("/dev/ttyUSB0", baudrate=9600, parity=serial.PARITY_NONE, \
stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS,timeout=1)

counter = 0

while(1):
	counter = counter + 1
	time.sleep(1)
	ztemp = ser.read(1)
	print(ztemp)
	print(counter)
time.sleep(3)
counter = 0
