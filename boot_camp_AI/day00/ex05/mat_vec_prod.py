import sys
sys.path.append("/Users/floblanc/Projet/bootcamp_Python_and_AI/boot_camp_AI/day00/ex04/")
from dot import dot
import numpy as np

def mat_vec_prod(x, y):
	if len(x) == 0 or x.shape[1] != len(y) or len(y) == 0:
		return (None)
	tab = []
	for i in range(len(x)):
		tab.append(dot(x[i], y.reshape(1,len(y))[0]))
	return np.array(tab).reshape(len(x), 1)

# W = np.array([
# 	[ -8, 8, -6, 14, 14, -9, -4],
# 	[ 2, -11, -2, -11, 14, -2, 14],
# 	[-13, -2, -5, 3, -8, -4, 13],
# 	[ 2, 13, -14, -15, -14, -15, 13],
# 	[ 2, -1, 12, 3, -7, -3, -6]])
# X = np.array([0, 15, -9, 7, 12, 3, -21]).reshape((7,1))
# Y = np.array([2, 14, -13, 5, 12, 4, -19]).reshape((7,1))
# # print(mat_vec_prod(W, X))
# # # print(W.shape)
# # # array([[ 497],
# # # 	[-356],
# # # 	[-345],
# # # 	[-270],
# # # 	[ -69]])

# print(W.dot(X))

# # array([[ 497],
# # 	[-356],
# # 	[-345],
# # 	[-270],
# # 	[ -69]])

# print(mat_vec_prod(W, Y))

# # array([[ 452],
# # 	[-285],
# # 	[-333],
# # 	[-182],
# # 	[-133]])

# print(W.dot(Y))

# # array([[ 452],
# # 	[-285],
# # 	[-333],
# 	[-182],
# 	[-133]])