"""code for project euler, problem 1: Multiples of 3 and 5"""
import numpy as np
k = 3
p = 5
sum = 0
list = np.arange(0,1000)
for i in np.arange(0,len(list)):
	n = list[i]
	if n % k == 0:
		sum = sum+n
	elif n % p == 0:
		sum = sum+n
print("Total sum is %i" % (sum))