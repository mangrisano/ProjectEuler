# n! means n x (n - 1) x 3 x 2 x 1
# For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!
#
# Answer: 648


def problem(number):
    result = list(str(factorial(number)))
    return sum([int(i) for i in result])


def factorial(number):
    if number == 1:
        return 1
    else:
        return factorial(number - 1) * number

print(problem(100))