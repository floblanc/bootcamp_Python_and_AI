import sys
sys.path.append("/Users/floblanc/Projet/bootcamp_Python_and_AI/boot_camp_AI/day00/ex04/")
from dot import dot
import numpy as np

def vec_mse(y, y_hat):
	if (len(y) == 0 or len(y) != len(y_hat)):
		return (None)
	return dot((y - y_hat) / len(y), (y - y_hat))

# X = np.array([0, 15, -9, 7, 12, 3, -21])
# Y = np.array([2, 14, -13, 5, 12, 4, -19])
# print(vec_mse(X, Y))
# print(vec_mse(X, X))