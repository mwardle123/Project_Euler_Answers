"""
Project Euler Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6, and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sumMultiplesOf(multiples,max):
    sum = 0
    for x in range(max):
        if isMultipleOf(x, multiples):
            sum += x
    return sum

def isMultipleOf(i, multiples):
    for j in multiples:
        if i%j == 0:
            return True
    return False

print(sumMultiplesOf([3,5],1000))
