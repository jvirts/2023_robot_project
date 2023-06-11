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
ser=serial.Serial("/dev/ttyS0", baudrate=57600, parity=serial.PARITY_NONE, \
stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS,timeout=1)

f = open('python_read_serial.out','w')

packet = bytearray()
packet.append(0x1)
ser.write(packet)
time.sleep(3)
counter = 0
while counter < 5000:
	bytesToRead = ser.inWaiting()
	if (bytesToRead > 0):
#		ztemp = ser.read(4)
#		testme = struct.unpack('l',ztemp)
		countme = np.append(countme,(struct.unpack('l',ser.read(4))))
		xvals = np.append(xvals,(struct.unpack('f',ser.read(4))))
		yvals = np.append(yvals,(struct.unpack('f',ser.read(4))))
		zvals = np.append(zvals,(struct.unpack('f',ser.read(4))))
#		print(counter)
		counter = counter + 1
np.savetxt(f,np.column_stack((countme,xvals,yvals,zvals)),fmt = '%d %f %f %f ')
f.close()
