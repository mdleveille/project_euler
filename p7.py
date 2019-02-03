"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
"""
from math import sqrt

def DivisibleBy(this,that):
    if this % that == 0:
        return True
    else:
        return False

def GetDivisors(number):
    d = 2
    divisors = []
    while d <= sqrt(number):
        if DivisibleBy(number,d):
            divisors.append(d)
            d += 1
        else:
            d += 1
    return divisors

number = 2
primes = []
while len(primes) < 10001:
    if not GetDivisors(number):
        primes.append(number)
        number += 1
    else:
        number += 1

print("The 10,001st prime is ",max(primes))
