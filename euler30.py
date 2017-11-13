# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
#
# Result: 443839


def problem():
    nums = list()
    result = list()
    for i in range(2, 240000):
        nums = [int(num)**5 for num in list(str(i))]
        if sum(nums) == i:
            result.append(i)

    return sum(result)

print(problem())



