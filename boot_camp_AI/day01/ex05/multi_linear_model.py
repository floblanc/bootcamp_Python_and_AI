import sys
sys.path.append("/Users/floblanc/Projet/bootcamp_Python_and_AI/boot_camp_AI/day01/ex04/")
from linear_model import MyLinearRegression as MyLR
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd

data = pd.read_csv("/Users/floblanc/Projet/bootcamp_Python_and_AI/boot_camp_AI/day01/resources/spacecraft_data.csv")
# X = np.array(data["Age"]).reshape(-1,1)
X = np.array(data["Thrust_power"]).reshape(-1,1)
Y = np.array(data["Sell_price"])
plt.scatter(X,Y)

myLR_age = MyLR([[50], [1.0]])
myLR_age.fit_(X, Y, alpha = 2.5e-4, n_cycle = 10000)
plt.scatter(X, myLR_age.predict_(X))
print(myLR_age.theta)


RMSE_age = myLR_age.mse_(X, Y)
print(RMSE_age)
plt.show()
# 57636.77729...