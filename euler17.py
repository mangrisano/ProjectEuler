# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
# letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
# Result: 21124


def problem():
    result = 0
    all_numbers = list()
    one_digit_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    two_digits_numbers = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
                          "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty",
                          "ninety"]
    three_digits_numbers = ["hundred"]

    for number in one_digit_numbers:
        all_numbers.append(number)
    for number in two_digits_numbers:
        all_numbers.append(number)
        if number.endswith("ty"):
            for digit in one_digit_numbers:
                all_numbers.append(number + digit)
    for digit in one_digit_numbers:
        for number in three_digits_numbers:
            all_numbers.append(digit + number)
            for n in one_digit_numbers:
                all_numbers.append(digit + number + 'and' + n)
            for n in two_digits_numbers:
                all_numbers.append(digit + number + 'and' + n)
                if n.endswith("ty"):
                    for y in one_digit_numbers:
                        all_numbers.append(digit + number + 'and' + n + y)

    all_numbers.append("onethousand")
    for number in all_numbers:
        result += len(number)

    return result

print problem()
