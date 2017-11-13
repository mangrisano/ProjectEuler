# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#
# Answer: 232792560


def problem():
    number = 0
    found = False
    while not found:
        number += 1
        l = list()
        for i in range(1, 21):
            if number % i == 0:
                l.append(i)
                if len(l) == 20:
                    found = True
            else:
                break

    return number


print problem()



