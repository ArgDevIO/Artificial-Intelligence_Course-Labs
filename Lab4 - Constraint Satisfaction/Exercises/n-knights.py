from constraint import *


def check_constraint(k1, k2):
    flag = k1 != k2

    for (x, y) in [(a, b) for a in list(range(-2, 3)) for b in list(range(-2, 3)) if abs(a) != abs(b) and a != 0 and b != 0]:
        flag = flag and (k1[0] + x, k1[1] + y) != k2

    # flag = flag and (k1_x - 1, k1_y + 2) != k2
    #
    # flag = flag and (k1_x + 1, k1_y + 2) != k2
    #
    # flag = flag and (k1_x + 2, k1_y + 1) != k2
    #
    # flag = flag and (k1_x + 2, k1_y - 1) != k2
    #
    # flag = flag and (k1_x + 1, k1_y - 2) != k2
    #
    # flag = flag and (k1_x - 1, k1_y - 2) != k2
    #
    # flag = flag and (k1_x - 2, k1_y - 1) != k2
    #
    # flag = flag and (k1_x - 2, k1_y + 1) != k2

    return flag


if __name__ == '__main__':
    N = int(input())

    problem = Problem()

    domain = []
    for i in range(N):
        for j in range(N):
            domain.append((i, j))

    knights = range(N)

    problem.addVariables(knights, domain)

    for knight1 in knights:
        for knight2 in knights:
            if knight1 < knight2:
                problem.addConstraint(lambda k1, k2: check_constraint(k1, k2), (knight1, knight2))

    if N <= 4:
        print(len(problem.getSolutions()))
    else:
        print(problem.getSolution())
