# Take the number 192 and multiply it by each of 1, 2, and 3:
#
# 192 x 1 = 192
# 192 x 2 = 384
# 192 x 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576.
# We will call 192384576 the concatenated product of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving
# the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated
# product of an integer with (1,2, … , n) where n > 1?
#
# Answer: 932718654

def problem(limit=10000, range_numbers=9):
    max_number = 0
    pandigital = 0
    for number in list(range(1, limit+1)):
        ispandigital, pandigital = is_pandigital(number, range_numbers)
        if ispandigital:
            if pandigital > max_number:
                max_number = pandigital
    return max_number

def is_pandigital(number, limit):
    st_pandigit = ''
    pandigital = '123456789'
    for i in list(range(1, limit+1)):
        st_pandigit += str(number * i)
        if len(st_pandigit) >= 9:
            break
    if ''.join(sorted(st_pandigit)) == pandigital:
        return True, int(st_pandigit)
    return False, int(st_pandigit)

if __name__ == '__main__':
    print(problem())
