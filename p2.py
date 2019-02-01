limit = 4000000

fib = [1,2]
even_fib_sum = 0
while max(fib) < limit:
    new_fib = fib[-1] + fib[-2]
    fib.append(new_fib)
    continue

for number in fib:
    if number % 2 ==0:
        even_fib_sum += number

print(even_fib_sum)

