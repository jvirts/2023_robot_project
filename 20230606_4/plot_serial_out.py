import numpy as np
import matplotlib.pyplot as plt

def moving_average(a,n = 3) :
	ret = np.cumsum(a,dtype=float)
	ret[n:] = ret[n:] - ret[:-n]
	return ret[n-1:]/n






with open('python_read_serial.out') as f:
	array = []
	for line in f:
		array.append([float(x) for x in line.split()])
plot_array = np.asarray(array)		

x_mov_avg = moving_average(plot_array[:,1],n=8)

plt.plot(plot_array[7:,0],x_mov_avg,label="x mov avg")
#plt.plot(plot_array[:,0],plot_array[:,1],label="x")
#plt.plot(plot_array[:,0],plot_array[:,2],label="y")
#plt.plot(plot_array[:,0],plot_array[:,3],label="z")
plt.legend()
plt.show()
