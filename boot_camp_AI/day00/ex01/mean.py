import sys
sys.path.append("/Users/floblanc/Projet/bootcamp_Python_and_AI/boot_camp_AI/day00/ex00/")
from sum import sum_
import numpy as np
def mean(x):
	s = sum_(x)
	if (s):
		return s / len(x)
	return None

#X = np.array([])
#print(mean(X))

#X = np.array([0, 15, -9, 7, 12, 3, -21])
#print(mean(X ** 2))