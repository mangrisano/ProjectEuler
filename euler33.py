# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting
# to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained
# by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value
# and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value
# of the denominator.
#
# Answer: 100

from fractions import Fraction

def problem(limit=100):
    prod = 1
    for num in list(range(11, limit)):
        if num % 10 == 0:
            continue
        for den in list(range(num+1, limit)):
            if den % 10 == 0:
                continue
            fractions = num / den
            is_common, new_num, new_den = deldigit(num, den)
            if new_den == 0:
                break
            if is_common:
                if fractions == (new_num/new_den):
                    prod *= Fraction(new_num, new_den)

    return prod.denominator

def deldigit(num, den):
    is_common = False
    snum = [digit for digit in str(num)]
    sden = [digit for digit in str(den)]
    for digit in snum:
        if digit in sden:
            snum.remove(digit)
            sden.remove(digit)
            is_common = True
    if is_common:
        return is_common, int(snum[0]), int(sden[0])
    return is_common, num, den

if __name__ == '__main__':
    print(problem())
