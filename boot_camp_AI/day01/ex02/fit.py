import sys
sys.path.append("/Users/floblanc/Projet/bootcamp_Python_and_AI/boot_camp_AI/day01/ex00/")
from pred import predict_
sys.path.append("/Users/floblanc/Projet/bootcamp_Python_and_AI/boot_camp_AI/day01/ex01/")
from cost_function import cost_
sys.path.append("/Users/floblanc/Projet/bootcamp_Python_and_AI/boot_camp_AI/day00/ex12/")
from vec_gradient import vec_gradient
import numpy as np

def fit_(theta, X, Y, alpha, n_cycle):
	for i in range(n_cycle):
		tmp = theta
		for j in range(len(theta)):
			
		theta = tmp
	return theta

X1 = np.array([[0.], [1.], [2.], [3.], [4.]])
Y1 = np.array([[2.], [6.], [10.], [14.], [18.]])
theta1 = np.array([[1.], [1.]])
theta1 = fit_(theta1, X1, Y1, alpha = 0.01, n_cycle=2000)
print(theta1)
# array([[2.0023..],[3.9991..]])
print(predict_(theta1, X1))
# array([2.0023..], [6.002..], [10.0007..], [13.99988..], [17.9990..])

X2 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8.,
80.]])
Y2 = np.array([[19.6], [-2.8], [-25.2], [-47.6]])
theta2 = np.array([[42.], [1.], [1.], [1.]])
theta2 = fit_(theta2, X2, Y2, alpha = 0.0005, n_cycle=42000)
print(theta2)
# array([[41.99..],[0.97..], [0.77..], [-1.20..]])
print(predict_(theta2, X2))
# array([[19.5937..], [-2.8021..], [-25.1999..], [-47.5978..]])