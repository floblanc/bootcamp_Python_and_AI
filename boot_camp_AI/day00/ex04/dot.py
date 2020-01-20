import numpy as np

def dot(x, y):
	if len(x) != len(y) or len(x) == 0 :
		return None
	return sum(x * y)

# X = np.array([0, 15, -9, 7, 12, 3, -21])
# Y = np.array([2, 14, -13, 5, 12, 4, -19])
# print(dot(X, Y))
# print(np.dot(X, Y))

# print(dot(X, X))
# print(np.dot(X, X))

# print(dot(Y, Y))
# print(np.dot(Y, Y))