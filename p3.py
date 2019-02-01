from math import sqrt

def DivisibleBy(this,that):
    if this % that == 0:
        return True
    else:
        return False

def GetDivisors(number):
    d = 2
    divisors = []
    while d <= int(number/2):
        if DivisibleBy(number,d):
            divisors.append(d)
            d += 1
        else:
            d += 1
    print(divisors)



# def isPrime(Number):


GetDivisors(6983247)



