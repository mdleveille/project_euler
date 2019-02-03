"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
# LOOKED UP

def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
        # print(a,b)
    return a

def find_lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return int(a * b / gcd(a, b))

numbers = range(2,21)
num1 = numbers[0]
num2 = numbers[1]

lcm = find_lcm(num1, num2)

for number in numbers:
    # print("=={}==".format(number))
    lcm = find_lcm(lcm, number)

print(lcm)
