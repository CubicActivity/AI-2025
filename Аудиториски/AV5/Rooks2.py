from constraint import *

# (i1,j1) (i2,j2)
def not_attacking(rook1, rook2):
    return rook1[0] != rook2[0] and rook1[1] != rook1[1]


if __name__ == "__main__":
    problem = Problem()
    domain = range(0, 8)

    # columns
    rooks = range(0, 8)

    problem.addVariables(rooks, domain)

    # not in the same row
    problem.addConstraint(AllDifferentConstraint(), rooks)
    # for rook1 in rooks:
    #     for rook2 in rooks:
    #         if rook1 != rook2:
    #             problem.addConstraint(lambda r1, r2: r1 != r2, (rook1, rook2))

    solution = problem.getSolution()
    print(solution)



