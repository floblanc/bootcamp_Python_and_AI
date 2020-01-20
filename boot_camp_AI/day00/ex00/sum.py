import numpy as np

def sum_(x, f):
	res = 0
	np.seterr(all='raise')
	try :
		if (len(x) == 0):
			return None
		for elem in x:
			res += f(elem)
	except:
		return None
	return res

#X = np.array([0, 15, -9, 7, 12, 3, -21])
#print(sum_(X, lambda x: x/0))

# = np.array([0, 15, -9, 7, 12, 3, -21])
#print(sum_(X, lambda x: x**2))
