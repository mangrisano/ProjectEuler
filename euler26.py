# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to
# 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring
# cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
#
# Result: 983


def problem():
    r_max = 0
    number = 2
    for i in range(2, 1000):
        if reminders(1, i) > r_max:
            r_max = reminders(1, i)
            number = i

    return number


def reminders(num, den):
    r_list = list()
    reminder = (num % den) * 10
    while reminder not in r_list:
        r_list.append(reminder)
        reminder = (reminder % den) * 10

    return len(r_list)


print(problem())
