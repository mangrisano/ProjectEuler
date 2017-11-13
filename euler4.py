# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
# is 9009 = 91 x 99
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#
# Answer: 906609


def problem():
    prod = 1
    palindrome = list()
    for i in range(100, 1000):
        for j in range(i, 1000):
            prod = i * j
            if is_palindrome(prod):
                palindrome.append(prod)

    return max(palindrome)


def is_palindrome(number):
    if str(number) == str(number)[::-1]:
        return True

    return False


print(problem())
