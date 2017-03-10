"""code for project euler, problem 3: Largest prime factor"""
import numpy as np

x = 600851475143
#x = 13195                # prime factors are 5,7,13,29

myint = x
num_str = str(x)

digit_sum = 0
for i in np.arange(0,len(num_str)):
	digit_sum = digit_sum + int(num_str[i])
	print(digit_sum)

