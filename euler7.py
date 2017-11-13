# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
#
# Answer: 104743


def problem(number):
    count = 1
    value = 3
    if number == 1:
        return 2
    else:
        while True:
            if is_prime(value):
                count += 1
                if count == number:
                    return value
            value += 2


def is_prime(number):
    for i in range(2, int(round(number**0.5)) + 1):
        if not (number % i):
            return False
    return True

print(problem(6))



