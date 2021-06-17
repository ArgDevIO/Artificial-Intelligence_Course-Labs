from constraint import *


def get_boxes(board):
    boxes = []
    for i in range(9):
        if i == 0 or i % 3 == 0:
            box_set_1 = board[i][:3] + board[i + 1][:3] + board[i + 2][:3]
            boxes.append(box_set_1)
            box_set_2 = board[i][3:6] + board[i + 1][3:6] + board[i + 2][3:6]
            boxes.append(box_set_2)
            box_set_3 = board[i][6:] + board[i + 1][6:] + board[i + 2][6:]
            boxes.append(box_set_3)
    return boxes


if __name__ == '__main__':

    solver = input()
    problem = Problem(eval(solver + '()'))

    variables = range(1, 10)
    domain = range(0, 81)

    rows = []
    for row in range(9):
        rows.append([row * 9 + i for i in range(9)])

    columns = []
    for col in range(9):
        columns.append([col + 9 * i for i in range(9)])

    boxes = get_boxes(rows)

    for var in domain:
        problem.addVariables([var], variables)

    for var_groups in [rows, columns, boxes]:
        for var_group in var_groups:
            problem.addConstraint(AllDifferentConstraint(), var_group)

    solution = problem.getSolution()
    print(solution)

# if __name__ == '__main__':
#     problem = Problem(BacktrackingSolver())
#     variables = []
#     for variable in variables:
#         problem.addVariable(variable, Domain(set(range(100))))
#
#     # ---Tuka dodadete gi ogranichuvanjata----------------
#
#     # ----------------------------------------------------
#
#     print(problem.getSolution())
