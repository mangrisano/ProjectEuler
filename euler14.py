# The following iterative sequence is defined for the set of positive integers:
#
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has
# not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.
#
# Answer: 837799


def problem(max_value):
    lenght = 0
    result = 0
    for value in range(1, max_value):
        orig_value = value
        chain = [value]
        while value > 1:
            if is_even(value):
                value /= 2

            else:
                value = (3 * value) + 1
            chain.append(value)
        if len(chain) > lenght:
            lenght = len(chain)
            result = orig_value

    return result


def is_even(number):
    if not (number % 2):
        return True

    return False

print(problem(1000000))
