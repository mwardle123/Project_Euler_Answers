from math import sqrt

def FindPrimeFactors(x):
    if not x <=1:
        n = 2
        while (x%n != 0):
            n = FindNextPrime(n)
        factors = FindPrimeFactors(x/n)
        factors.add(n)
        return factors
    else:
        return set()


def FindNextPrime(x):
    x += 1
    while (not CheckIfPrime(x)):
        x += 1
    return x

def CheckIfPrime(x):
    if (x <= 1):
        return False

    for i in range(2, int(sqrt(x))+1):
        if (x%i==0):
            return False
    return True

primeFactors = FindPrimeFactors(600851475143)
print(sorted(primeFactors)[len(primeFactors)-1])