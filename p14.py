"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
from time import time
start = time()
stored_collatz = {}

def CollatzChainCount(number):
    if number == 1:
        return 1
    if stored_collatz.get(number,0):
        return stored_collatz[number]
    if number % 2 == 0:
        stored_collatz[number] = 1 + CollatzChainCount(number/2)
    else:
        stored_collatz[number] = 1 + CollatzChainCount(3*number+1)
    return stored_collatz[number]

longest_chain = 0
for number in range(1,1000000):
    if CollatzChainCount(number) > longest_chain:
        longest_chain = CollatzChainCount(number)
        answer = number

print(answer)

elapsed = time() - start

print(elapsed,"seconds")
