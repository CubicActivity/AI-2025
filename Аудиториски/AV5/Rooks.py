#8x8 chess table
# must have 8 rooks not attacking eachother

"""
(row, column)
"""

#(i1,j1) (i2,j2)
def not_attacking(rook1, rook2):
    return rook1[0] != rook2[0] and rook1[1] != rook2[1]

from constraint import *

if __name__ == "__main__":
    problem = Problem()

    domain = [(i,j) for i in range(0,8) for j in range(0,8)]

    rooks = range(1, 9)

    problem.addVariables(rooks, domain)

     #all rooks diff row & diff col


    for rook1 in rooks:
        for rook2 in rooks:
            if rook1 != rook2: #moze i so rook1 < rook2
                problem.addConstraint(not_attacking, (rook1, rook2))


    solution = problem.getSolutions()
    print(solution)