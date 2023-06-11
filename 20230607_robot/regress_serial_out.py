#see https://towardsdatascience.com/simple-linear-regression-from-scratch-in-numpy-871335e14b7a
# y = b0 + b1*x

import numpy as np
import matplotlib.pyplot as plt

def get_rmse(y_true,y_pred):
	return np.sqrt((np.sum((y_pred - y_true)**2))/len(y_true))

with open('python_read_serial.out') as f:
	array = []
	for line in f:
		array.append([float(x) for x in line.split()])
plot_array = np.asarray(array)	


x = plot_array[0:3000,0]
y = plot_array[0:3000,1]

numerator = np.sum((x - np.mean(x))*(y - np.mean(y)))
denominator = np.sum((x - np.mean(x))**2)
b1 = numerator / denominator
b0 = np.mean(y) - b1*np.mean(x)
xhat = b0 + b1*x

zz = get_rmse(x,xhat)
print(zz)

plt.plot(plot_array[0:3000,0],plot_array[0:3000,1],label="x")
#plt.plot(plot_array[:,0],plot_array[:,2],label="y")
plt.plot(plot_array[0:3000,0],xhat,label="xhat")
plt.legend()
plt.show()