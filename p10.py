"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import time
limit = 2000000

sieve = [True] * limit
sieve[0] = sieve[1] = False
prime_sum = 0
for number,isPrime in enumerate(sieve):
    if isPrime:
        prime_sum += number
        for multiple in range(number*number, limit, number):
            sieve[multiple] = False
print("Sum of primes under 2,000,000 is", prime_sum)
