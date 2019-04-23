# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145
#
# Find the sum of all numbers which are equal to the sum of
# the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
#
# Answer: 40730

from math import factorial

def problem():
    res = 0
    facts = {str(number): factorial(number) for number in list(range(10))}
    for number in list(range(3, 1000000)):
        sum_facts = sum([facts[num] for num in str(number)])
        if sum_facts == number:
            res += number
    return res

if __name__ == '__main__':
    print(problem())
