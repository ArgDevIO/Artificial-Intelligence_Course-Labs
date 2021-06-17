import random


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, position):
        print(position)
        self.x = position[0]
        self.y = position[1]


class Game:
    def __init__(self, game_matrix):
        self.game_matrix = game_matrix

    def get_game_matrix(self):
        return self.game_matrix


class Pacman:

    _MOVES = {
        1: 'UP',
        2: 'DOWN',
        3: 'LEFT',
        4: 'RIGHT'
    }

    def __init__(self, matrix, food_counter, height, width):
        self.game = Game(matrix)
        self.player = Player(0, 0)
        self.food_counter = food_counter
        self.width = width
        self.height = height

    def play_game(self):
        # print("playing...")
        # print("Food Left: ", self.food_counter)
        temp_matrix = self.game.get_game_matrix()

        while (self.food_counter != 0):
            food_positions = self.check_for_food(
                self.player.x, self.player.y, temp_matrix)

            if len(food_positions) == 1:
                # print("Move to that position")
                self.player.move([food_positions[0][0], food_positions[0][1]])
                self.food_counter -= 1
                temp_matrix[self.player.x][self.player.y] = '#'
            elif len(food_positions) > 1:
                # print("Move to random food position")
                random_position = random.randint(0, 1)
                self.player.move(
                    [food_positions[random_position][0], food_positions[random_position][1]])
                self.food_counter -= 1
                temp_matrix[self.player.x][self.player.y] = '#'
            else:
                # print("Move to random position")
                random_position = self.get_random_position()
                self.player.move(random_position)
                if (temp_matrix[random_position[0]][random_position[1]] == "."):
                    self.food_counter -= 1
                    temp_matrix[self.player.x][self.player.y] = '#'
        else:
            print("===== GAME FINISHED =====")

    def get_random_position(self):
        random_num = random.randint(1, 4)

        if self._MOVES[random_num] == 'UP':
            x = self.player.x - 1
            y = self.player.y
            return [x if x > 0 else 0, y]
        elif self._MOVES[random_num] == 'DOWN':
            x = self.player.x + 1
            y = self.player.y
            return [x if x < self.height else self.player.x - 1, y]
        elif self._MOVES[random_num] == 'LEFT':
            x = self.player.x
            y = self.player.y - 1
            return [x, y if y > 0 else 0]
        elif self._MOVES[random_num] == 'RIGHT':
            x = self.player.x
            y = self.player.y + 1
            return [x, y if y < self.width else self.player.y - 1]

    def check_for_food(self, row, column, matrix):
        food_positions = []

        row_range = range(row - 1 if (row - 1 > 0) else 0, row +
                          2 if (row + 2 < self.height) else self.height - 1)
        column_range = range(column - 1 if (column - 1 > 0) else 0,
                             column + 2 if (column + 2 < self.width) else self.width - 1)

        for d_row in row_range:
            for d_column in column_range:
                if ((d_row == row and d_column == column) or
                    ((d_row == row + 1) and (d_column == column + 1)) or
                    ((d_row == row - 1) and (d_column == column - 1)) or
                    (d_row == (row + 1) and d_column == (column - 1)) or
                        (d_row == (row - 1) and d_column == (column + 1))):
                    continue
                if (matrix[d_row][d_column] == '.'):
                    food_positions.append([d_row, d_column])

        return food_positions


def main():

    height = int(input())
    width = int(input())

    matrix = []
    food_counter = 0

    for i in range(height):
        elements = list(input())
        food_counter += elements.count('.')
        matrix.append(elements)

    if (food_counter != 0):
        pacman = Pacman(matrix, food_counter, height, width)
        pacman.play_game()
    else:
        print("Nothing to do here")

    # print('\n'.join([' '.join([item for item in row])
    #                  for row in matrix]))


if __name__ == '__main__':
    main()
