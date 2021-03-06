# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#
# Result:

from datetime import date


def problem():
    result = 0
    year = 1901
    month = 1
    end_period = date(2000, 12, 31)
    while year <= end_period.year and month <= end_period.month:
        d = date(year, month, 1)
        if d.weekday() == 6:
            result += 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1

    return result

print(problem())




