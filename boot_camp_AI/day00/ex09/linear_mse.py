import sys
sys.path.append("/Users/floblanc/Projet/bootcamp_Python_and_AI/boot_camp_AI/day00/ex04/")
from dot import dot
import numpy as np

def linear_mse(x, y, theta):
	if (len(x) == 0 or len(x) != len(y) or len(theta) == 0 or len(theta) != x.shape[1]):
		return (None)
	res = 0.0
	for i in range(len(y)):
		res += pow(dot(theta,x[i]) - y[i], 2)
	return res / len(y)

# X = np.array([
#     [ -6, -7, -9],
#         [ 13, -2, 14],
#         [ -7, 14, -1],
#         [ -8, -4, 6],
#         [ -5, -9, 6],
#         [ 1, -5, 11],
#         [ 9, -11, 8]])
# Y = np.array([2, 14, -13, 5, 12, 4, -19])
# Z = np.array([3,0.5,-6])
# print(linear_mse(X, Y, Z))
# W = np.array([0,0,0])
# print(linear_mse(X, Y, W))