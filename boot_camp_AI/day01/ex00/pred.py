import sys
sys.path.append("/Users/floblanc/Projet/bootcamp_Python_and_AI/boot_camp_AI/day00/ex05/")
from mat_vec_prod import mat_vec_prod
import numpy as np

def predict_(theta, X):
	# print(theta)
	if (len(theta) != X.shape[1] + 1):
		return None
	return (mat_vec_prod(X, theta[1:]) + theta[0])

# X1 = np.array([[0.], [1.], [2.], [3.], [4.]])
# theta1 = np.array([[2.], [4.]])
# print(predict_(theta1, X1))
# print("=============================")
# # array([[2], [6], [10], [14.], [18.]])
# X2 = np.array([[1], [2], [3], [5], [8]])
# theta2 = np.array([[2.]])
# print(predict_(theta2, X2))
# print("=============================")
# # Incompatible dimension match between X and theta.
# # None
# X3 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8.,
# 80.]])
# theta3 = np.array([[0.05], [1.], [1.], [1.]])
# print(predict_(theta3, X3))
# # array([[22.25], [44.45], [66.65], [88.85]])