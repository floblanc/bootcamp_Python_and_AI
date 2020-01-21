import sys
sys.path.append("/Users/floblanc/Projet/bootcamp_Python_and_AI/boot_camp_AI/day01/ex00/")
from pred import predict_
import numpy as np

def cost_elem_(theta, X, Y):
	if (len(theta) != X.shape[1] + 1 or len(X) != len(Y) or len(X) == 0):
		return None
	return ((predict_(theta, X) - Y)**2) / (len(X) * 2)

def cost_(theta, X, Y):
	return sum(cost_elem_(theta, X, Y))[0]

# X1 = np.array([[0.], [1.], [2.], [3.], [4.]])
# theta1 = np.array([[2.], [4.]])
# Y1 = np.array([[2.], [7.], [12.], [17.], [22.]])
# print(cost_elem_(theta1, X1, Y1))
# # array([[0.], [0.1], [0.4], [0.9], [1.6]])
# print(cost_(theta1, X1, Y1))
# # 3.0
# X2 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8.,80.]])
# theta2 = np.array([[0.05], [1.], [1.], [1.]])
# Y2 = np.array([[19.], [42.], [67.], [93.]])
# print(cost_elem_(theta2, X2, Y2))
# # array([[1.3203125], [0.7503125], [0.0153125], [2.1528125]])
# print(cost_(theta2, X2, Y2))
# # 4.238750000000004