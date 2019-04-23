# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n
# exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand
# multiplier and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written
# as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once
# in your sum.
#
# Answer: 45228

def problem(limit=2000):
    pandigital = '123456789'
    formula = []
    prods = []
    sum_of_products = 0
    for i in list(range(limit+1)):
        for j in list(range(limit+1)):
            prod = i * j
            formula.append(list(map(str, [i, j, prod])))
    for i in list(range(len(formula))):
        if ''.join(sorted(''.join(formula[i]))) == pandigital:
            prods.append(formula[i][2])

    for number in set(prods):
        sum_of_products += int(number)

    return sum_of_products

if __name__ == '__main__':
    print(problem())
