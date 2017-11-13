# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6
# routes to the bottom right corner.
#
# How many such routes are there through a 20x20 grid?
#
# Result: 137846528820

# Formula: Binomial Coefficient
# From (0,0) to (a,b):
# ( a + b )
#   ( a )
#
# a+b! / (a! * (a+b - a)!) = a+b! / a! * b!

from math import factorial


def problem(n, k):
    result = factorial(n + k) / (factorial(n) * factorial(k))
    return result

print(problem(20, 20))

