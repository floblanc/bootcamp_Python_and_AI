import sys
sys.path.append("/Users/floblanc/Projet/bootcamp_Python_and_AI/boot_camp_AI/day00/ex02/")
from variance import variance
import numpy as np

def std(x):
	var = variance(x)
	if (var):
		return var**0.5
	return None

# X = np.array([0, 15, -9, 7, 12, 3, -21])
# print(std(X))
# print(np.std(X))
# Y = np.array([2, 14, -13, 5, 12, 4, -19])
# print(std(Y))
# print(np.std(Y))