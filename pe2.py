"""code for project euler, problem 2: Even Fibonacci numbers"""
import numpy as np
sum = 0

fib = [0,1]
for i in np.arange(2, 100):
	x = fib[i-1]+fib[i-2]
	if x > 4000000:
		break
	fib.append(x)

for i in fib:
	n = i
	if n % 2 ==0:
		sum = sum +n

print('The sum of the even Fibonacci number under 4 million is %i' % (sum))