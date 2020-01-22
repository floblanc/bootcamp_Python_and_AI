import sys
sys.path.append("/Users/floblanc/Projet/bootcamp_Python_and_AI/boot_camp_AI/day00/ex05/")
from mat_vec_prod import mat_vec_prod
sys.path.append("/Users/floblanc/Projet/bootcamp_Python_and_AI/boot_camp_AI/day00/ex12/")
from vec_gradient import vec_gradient
import numpy as np

class MyLinearRegression():
	def __init__(self, theta):
		self.theta = np.array(theta)

	def predict_(self, X):
		if (len(self.theta) != X.shape[1] + 1):
			return None
		return (mat_vec_prod(X, self.theta[1:]) + self.theta[0])

	def cost_elem_(self, X, Y):
		if (len(self.theta) != X.shape[1] + 1 or len(X) != len(Y) or len(X) == 0):
			return None
		return ((self.predict_(X) - Y)**2) / (len(X) * 2)

	def cost_(self, X, Y):
		return sum(self.cost_elem_(X, Y))[0]

	def fit_(self, X, Y, alpha, n_cycle):
		if (len(self.theta) != X.shape[1] + 1 or len(X) != len(Y) or len(X) == 0):
			return None
		X = np.c_[np.ones(len(X)), X]
		for n in range(n_cycle):
			self.theta -= alpha * (vec_gradient(X, Y, self.theta)).reshape(self.theta.shape)
		return self.theta

# from mylinearregression import MyLinearRegression as MyLR

# X = np.array([[1., 1., 2., 3.], [5., 8., 13., 21.], [34., 55., 89.,
# 144.]])
# Y = np.array([[23.], [48.], [218.]])
# mylr = MyLR([[1.], [1.], [1.], [1.], [1]])
# print(mylr.predict_(X))
# print("=====================")
# # array([[8.], [48.], [323.]])
# print(mylr.cost_elem_(X,Y))
# print("=====================")
# # array([[37.5], [0.], [1837.5]])
# print(mylr.cost_(X,Y))
# print("=====================")
# # 1875.0
# mylr.fit_(X, Y, alpha = 1.6e-4, n_cycle=200000)
# print(mylr.theta)
# print("=====================")
# # array([[18.023..], [3.323..], [-0.711..], [1.605..], [-0.1113..]])
# print(mylr.predict_(X))
# print("=====================")
# # array([[23.499..], [47.385..], [218.079...]])
# print(mylr.cost_elem_(X,Y))
# print("=====================")
# # array([[0.041..], [0.062..], [0.001..]])
# print(mylr.cost_(X,Y))
# print("=====================")
# # 0.1056..