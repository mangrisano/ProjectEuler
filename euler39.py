# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}
# there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?
#
# Answer: 840

from math import sqrt

def problem(limit=1000):
    solutions = {}
    for perimeter in list(range(1, 1001)):
        counter = 0
        for max_cat in list(range(1, limit + 1)):
            for min_cat in list(range(1, limit + 1)):
                ipotenusa = sqrt(max_cat**2 + min_cat**2)
                solution = max_cat + min_cat + ipotenusa
                if solution == perimeter:
                    counter += 1
                else:
                    continue

        solutions[counter] = perimeter

    return solutions[max(solutions.keys())]

if __name__ == '__main__':
    print(problem())
