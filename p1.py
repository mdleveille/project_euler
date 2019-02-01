limit = 1000

number = 1
num_sum = 0
while number < int(limit):
    if number % 3 == 0 or number % 5 == 0:
        num_sum += number
    number += 1

print(num_sum)
