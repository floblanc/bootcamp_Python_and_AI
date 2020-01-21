import sys
sys.path.append("/Users/floblanc/Projet/bootcamp_Python_and_AI/boot_camp_AI/day00/ex04/")
from dot import dot
sys.path.append("/Users/floblanc/Projet/bootcamp_Python_and_AI/boot_camp_AI/day00/ex05/")
from mat_vec_prod import mat_vec_prod
import numpy as np

def predict_(theta, X):
	return (sum(dot(theta, X)))