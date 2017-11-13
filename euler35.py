# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves
# prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?
#
# Answer: 55


from collections import deque


def problem(limit):
    res = list()
    for number in range(2, limit):
        if is_circular(number):
            res.append(number)

    return len(res)


def is_prime(number):
    for i in range(2, int(round(number**0.5)) + 1):
        if not number % i:
            return False

    return True


def rotations(number):
    rots = list()
    d = deque(list(str(number)))
    for i in range(len(str(number))):
        d.rotate(len(str(number))-1)
        rots.append(int(''.join(d)))

    return rots


def is_circular(number):
    digits = rotations(number)
    for digit in digits:
        if not is_prime(digit):
            return False
    else:
        return True


print(problem(1000000))
