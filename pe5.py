"""code for project euler, problem 5: smallest multiple"""
import numpy as np

n = np.arange(1,21)
number = 2521

for i in n:
	if number % i != 0:
		number = number +1
	else:
		print(number)
	
