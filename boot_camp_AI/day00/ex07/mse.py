import numpy as np

def mse(y, y_hat):
	if (len(y) == 0 or len(y) != len(y_hat)):
		return (None)
	return sum((y - y_hat)**2) / len(y)

# X = np.array([0, 15, -9, 7, 12, 3, -21])
# Y = np.array([2, 14, -13, 5, 12, 4, -19])
# print(mse(X, Y))

# print(mse(X, X))