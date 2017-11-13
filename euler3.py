# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143?
#
# Answer: 6857


def problem(number):
    factor = 2
    factors = list()
    while number > 1:
        if not (number % factor):
            factors.append(factor)
            number /= factor
        else:
            factor += 1

    return max(factors)


print(problem(600851475143))
