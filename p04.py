"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
a = 100
b = 100
products = []
palindromes = []

while a < 1000:
    b = 100
    while b < 1000:
        product = a * b
        products.append(product)
        b += 1
    a += 1

for number in products:
    if str(number) == str(number)[::-1]:
        palindromes.append(number)

print("The largest palindromic product of two 3-digit numbers is {}.".format(max(palindromes)))
