n = int(input())
list = []


# def minesweeper(list):  # Using For Loops
#     for row in range(len(list)):
#         for column in range(len(list)):
#             if (list[row][column] != '#'):
#                 list[row][column] = str(count_bombs(row, column, list))

def minesweeper(list):  # Using List Comprehension
    return [[count_bombs(row, column, list) for (column, c_value) in enumerate(r_value)] for (row, r_value) in enumerate(list)]


def count_bombs(row, column, list):
    if list[row][column] == '#':
        return '#'

    counter = 0
    row_range = range(row - 1 if (row - 1 > 0) else 0, row +
                      2 if (row + 2 < len(list)) else len(list))
    column_range = range(column - 1 if (column - 1 > 0) else 0,
                         column + 2 if (column + 2 < len(list)) else len(list))

    for d_row in row_range:
        for d_column in column_range:
            if (list[d_row][d_column] == '#'):
                counter += 1

    return str(counter)


for i in range(n):
    elements = input().split('   ')
    list.append(elements)

print('\n'.join(['   '.join([item for item in row])
                 for row in minesweeper(list)]))
