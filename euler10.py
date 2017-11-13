# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
#
# Answer: 142913828922


def problem(number):
    result = 0
    for i in range(2, number):
        if is_prime(i):
            result += i

    return result


def is_prime(number):
    for i in range(2, int(round(number**0.5)) + 1):
        if not (number % i):
            return False

    return True

print(problem(2000000))
