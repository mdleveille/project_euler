"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


limit = 1000

number = 1
num_sum = 0
while number < int(limit):
    if number % 3 == 0 or number % 5 == 0:
        num_sum += number
    number += 1

print("The sum of all the multiples of 3 and 5 under 1000 is ", num_sum)
