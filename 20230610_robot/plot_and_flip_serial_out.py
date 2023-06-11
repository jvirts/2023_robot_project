import numpy as np
import matplotlib.pyplot as plt
with open('python_read_serial.out') as f:
	array = []
	for line in f:
		array.append([float(x) for x in line.split()])
plot_array = np.asarray(array)		

plt.plot(plot_array[0:2501,0],plot_array[0:2501,1],label="x")
plt.plot(plot_array[0:2501,0],plot_array[5001:2499:-1,1],label="xflip")



plt.legend()
plt.show()
print(plot_array.shape)