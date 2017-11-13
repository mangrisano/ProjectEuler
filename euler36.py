# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)
#
# Answer: 872187


def problem(limit):
    palindromes = list()
    for number in range(1, limit):
        b_number = bin(number)[2:]
        if is_palindrome(number) and is_palindrome(b_number):
            palindromes.append(number)

    return sum(palindromes)


def is_palindrome(s):
    if not isinstance(s, str):
        s = str(s)
    if s == s[::-1]:
        return True
    return False


print(problem(1000000))
