import sys
sys.path.append("/Users/floblanc/Projet/bootcamp_Python_and_AI/boot_camp_AI/day00/ex04/")
from dot import dot
sys.path.append("/Users/floblanc/Projet/bootcamp_Python_and_AI/boot_camp_AI/day01/ex03/")
from mylinearregression import MyLinearRegression as MyLR
sys.path.append("/Users/floblanc/Projet/bootcamp_Python_and_AI/boot_camp_AI/day00/ex05/")
from mat_vec_prod import mat_vec_prod
sys.path.append("/Users/floblanc/Projet/bootcamp_Python_and_AI/boot_camp_AI/day00/ex12/")
from vec_gradient import vec_gradient
import numpy as np
import matplotlib.pyplot as plt

class MyLinearRegression():
	def __init__(self, theta):
		self.theta = np.array(theta)

	def predict_(self, X):
		# print(X.shape)
		# print(self.theta.shape)
		if (self.theta.shape[0] != X.shape[1] + 1):
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
		# print("=================")
		# print(self.mse_(X[:,1:], Y))
		for n in range(n_cycle):
			self.theta -= alpha * (vec_gradient(X, Y, self.theta)).reshape(self.theta.shape)
		return self.theta

	def mse_(self, X, Y):
		Y = Y.reshape(Y.shape[0], 1)
		return (sum((self.predict_(X) - Y)**2) / len(X))[0]

 
# import pandas as pd
# from sklearn.metrics import mean_squared_error

# data = pd.read_csv("/Users/floblanc/Projet/bootcamp_Python_and_AI/boot_camp_AI/day01/resources/are_blue_pills_magics.csv")
# Xpill = np.array(data["Micrograms"]).reshape(-1,1)
# Yscore = np.array(data["Score"]).reshape(-1,1)

# linear_model1 = MyLinearRegression(np.array([[89.0], [-8]]))
# linear_model2 = MyLinearRegression(np.array([[89.0], [-6]]))
# Y_model1 = linear_model1.predict_(Xpill)
# Y_model2 = linear_model2.predict_(Xpill)

# plt.axis
# plt.scatter(Xpill, Yscore)
# plt.plot(Xpill, Y_model1)
# plt.plot(Xpill, Y_model2, 'r')
# plt.show()

# print(linear_model1.mse_(Xpill, Yscore))
# # 57.60304285714282
# print(mean_squared_error(Yscore, Y_model1))
# # 57.603042857142825
# print(linear_model2.mse_(Xpill, Yscore))
# # 232.16344285714285
# print(mean_squared_error(Yscore, Y_model2))
# # 232.16344285714285