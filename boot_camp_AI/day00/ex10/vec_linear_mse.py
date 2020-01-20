import sys
sys.path.append("/Users/floblanc/Projet/bootcamp_Python_and_AI/boot_camp_AI/day00/ex04/")
from dot import dot
sys.path.append("/Users/floblanc/Projet/bootcamp_Python_and_AI/boot_camp_AI/day00/ex05/")
from mat_vec_prod import mat_vec_prod
import numpy as np

def vec_linear_mse(x, y, theta):
	if (len(x) == 0 or len(x) != len(y) or len(theta) == 0 or len(theta) != x.shape[1]):
		return (None)
	y = y.reshape(len(y), 1)
	return dot((mat_vec_prod(x, theta) - y) / len(y), mat_vec_prod(x, theta) - y)[0]

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
# print(vec_linear_mse(X, Y, Z))
# W = np.array([0,0,0])
# print(vec_linear_mse(X, Y, W))