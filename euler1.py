# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of
# these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.
#
# Answer: 233168


def problem(number):
    multiples = list()
    for i in range(number):
        if not (i % 3) or not (i % 5):
            multiples.append(i)

    return sum(multiples)


print(problem(1000))
