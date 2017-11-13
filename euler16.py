# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?
#
# Answer: 1366


def problem(number):
    result  = list(str(2**number))
    return sum([int(i) for i in result])

print(problem(1000))
