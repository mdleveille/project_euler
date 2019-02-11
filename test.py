import sys
sys.setrecursionlimit(2000)

print(sys.getrecursionlimit())

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial((n-1))

print(len(str(factorial((1000)))))
