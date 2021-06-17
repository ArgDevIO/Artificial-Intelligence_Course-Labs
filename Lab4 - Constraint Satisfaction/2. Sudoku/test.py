from constraint import *

if __name__ == '__main__':

    ROWS = 'abcdefghi'
    COLS = '123456789'
    DIGITS = range(1, 10)
    VARS = [row + col for row in ROWS for col in COLS]
    ROWGROUPS = [[row + col for col in COLS] for row in ROWS]
    COLGROUPS = [[row + col for row in ROWS] for col in COLS]
    SQUAREGROUPS = [
        [ROWS[3 * rowgroup + k] + COLS[3 * colgroup + j]
         for j in range(3) for k in range(3)]
        for colgroup in range(3) for rowgroup in range(3)
    ]

    problem = Problem()
    for var in VARS:
        problem.addVariables([var], DIGITS)
    for vargroups in [ROWGROUPS, COLGROUPS, SQUAREGROUPS]:
        for vargroup in vargroups:
            problem.addConstraint(AllDifferentConstraint(), vargroup)
    print(problem.getSolution())
