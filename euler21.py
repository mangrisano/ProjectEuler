# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called
# amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.
#
# Result: 31626


def problem(number):
    result = 0
    for i in range(1, number):
        if is_amicable(i):
            result += i

    return result


def d(number):
    result = list()
    for i in range(1, number):
        if not (number % i):
            result.append(i)

    return sum(result)


def is_amicable(number):
    if number == d(number):
        return False
    d_number = d(number)
    if number == d(d_number):
        return True

    return False

print(problem(10000))
