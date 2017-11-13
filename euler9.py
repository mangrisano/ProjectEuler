# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
#
# Answer: 31875000


def problem(number):
    c = 0
    for a in range(1, number):
        for b in range(a + 1, number):
            c = (a**2 + b**2) ** 0.5
            if c > b:
                if (a + b + c == 1000):
                    return int(a * b * c)

print(problem(1000))

