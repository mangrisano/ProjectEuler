# Euler published the remarkable quadratic formula:
# 
# n² + n + 41
# 
# It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. 
# However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly 
# when n = 41, 41² + 41 + 41 is clearly divisible by 41.
# 
# Using computers, the incredible formula  n² – 79n + 1601 was discovered, which produces 80 primes 
# for the consecutive values n = 0 to 79. The product of the coefficients, -79 and 1601, is -126479.
# 
# Considering quadratics of the form:
# 
# n² + an + b, where |a| < 1000 and |b| < 1000 where |n| is the modulus/absolute
# value of n.
# e.g. |11| = 11 and |-4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression
# that produces the maximum number of  primes for consecutive values of n, starting with n = 0.
#
# result: -59231

import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divs = math.floor(math.sqrt(n))
    for i in range(3, max_divs + 1, 2):
        if n % i == 0:
            return False
    return True

def problem():
    res = []
    max_count = 0
    for a in list(range(-999, 1000, 2)):
        for b in list(range(-999, 1001)):
            count = 0
            n = 0
            while is_prime(n**2 + a*n + b):
                n += 1
                count += 1
            if count > max_count:
                max_count = count
                res.append([max_count, a * b])
    return max(res)


print(problem())
