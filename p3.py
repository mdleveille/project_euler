from math import sqrt

class Number():
    def __init__(self,value):
        self.number = value

    def DivisibleBy(self,this):
        if self.number % this == 0:
            return True
            break
        else:
            return False
            break

def isPrime(Number):
    divisor = 2
    divisors = []
    while divisor <= sqrt(Number.number):
        if Number.DivisibleBy(divisor):
            print(divisor)
            divisor += 1
            continue
        #     print("{} is divisible by {}".format(Number.number,divisor))
        #     divisors.append(divisor)
        #     divisor += 1
        #     continue





n = Number(687)
print(sqrt(n.number))
isPrime(n)


