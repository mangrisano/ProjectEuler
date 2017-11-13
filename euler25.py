# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
#
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
#
# Result: 4782


def problem():
    it = 1
    digits = 0
    while True:
        digits = len(str(fibonacci(it)))
        if digits == 1000:
            return it
        else:
            digits = 0
        it += 1

    return digits


def fibonacci(number):
    if number < 3:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

print(problem())
