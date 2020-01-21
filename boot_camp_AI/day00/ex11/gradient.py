import sys
sys.path.append("/Users/floblanc/Projet/bootcamp_Python_and_AI/boot_camp_AI/day00/ex04/")
from dot import dot
import numpy as np

def gradient(x, y, theta):
	if (len(x) == 0 or len(x) != len(y) or len(theta) == 0 or len(theta) != x.shape[1]):
		return (None)
	res = 0
	for i in range(len(x)):
		tmp = np.zeros(x.shape[1])
		for j in range(x.shape[1]):
			tmp[j] = (dot(theta, x[i]) - y[i]) * x[i][j]
		res += tmp
	return res / len(x)

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
# print(gradient(X, Y, Z))
# # array([ -37.35714286, 183.14285714, -393.        ])
# W = np.array([0,0,0])
# print(gradient(X, Y, W))
# # array([ 0.85714286, 23.28571429, -26.42857143])
# print(gradient(X, X.dot(Z), Z))
# # print(grad(X, X.dot(Z), Z))
# # array([0., 0., 0.])