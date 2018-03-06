# The number 3797 has an interesting property. Being prime itself, it is possible to continuously
# remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7.
# Similarly we can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right
# and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
#
# Answer: 748317

import math

def problem(truncatables=[], limit=1000000):
    for number in list(range(11, limit+1)):
        temp_list = []
        r_to_l = [str(number)[i:] for i in list(range(len(str(number))))]
        l_to_r = [str(number)[:i+1] for i in list(range(len(str(number))))]
        temp_list = r_to_l + l_to_r
        for truncatable in temp_list:
            if not is_prime(int(truncatable)):
                break
        else:
            truncatables.append(number)
            if len(truncatables) == 11:
                return sum(truncatables)


def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    max_divs = math.floor(math.sqrt(number))
    for i in list(range(3, max_divs+1, 2)):
        if number % i == 0:
            return False
    return True

if __name__ == '__main__':
    problem()
