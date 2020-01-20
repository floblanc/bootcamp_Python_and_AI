import sys
sys.path.append("/Users/floblanc/Projet/bootcamp_Python_and_AI/boot_camp_AI/day00/ex01/")
from mean import mean
import numpy as np

def variance(x):
	m = mean(x)
	f = lambda x : pow(x - m, 2)
	res = 0
	np.seterr(all='raise')
	try :
		if (len(x) == 0):
			return None
		for elem in x:
			res += f(elem)
	except:
		return None
	return (res / len(x))

#X = np.array([0, 15, -9, 7, 12, 3, -21])
#print(variance(X))

#print(np.var(X))

#print(variance(X/2))

#print(np.var(X/2))