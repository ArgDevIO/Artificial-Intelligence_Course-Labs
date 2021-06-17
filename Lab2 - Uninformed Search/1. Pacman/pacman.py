from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


def prodolzhi_pravo(x, y, direction, obstacles):
    if direction == 'istok':
        if x < 9 and [x + 1, y] not in obstacles:
            x += 1
    elif direction == 'zapad':
        if x > 0 and [x - 1, y] not in obstacles:
            x -= 1
    elif direction == 'sever':
        if y < 9 and [x, y + 1] not in obstacles:
            y += 1
    elif direction == 'jug':
        if y > 0 and [x, y - 1] not in obstacles:
            y -= 1
    return x, y


def prodolzhi_nazad(x, y, direction, obstacles):
    if direction == 'istok':
        if x > 0 and [x - 1, y] not in obstacles:
            x -= 1
            direction = 'zapad'
    elif direction == 'zapad':
        if x < 9 and [x + 1, y] not in obstacles:
            x += 1
            direction = 'istok'
    elif direction == 'sever':
        if y > 0 and [x, y - 1] not in obstacles:
            y -= 1
            direction = 'jug'
    elif direction == 'jug':
        if y < 9 and [x, y + 1] not in obstacles:
            y += 1
            direction = 'sever'
    return x, y, direction


def svrti_levo(x, y, direction, obstacles):
    if direction == 'istok':
        if y < 9 and [x, y + 1] not in obstacles:
            y += 1
            direction = 'sever'
    elif direction == 'zapad':
        if y > 0 and [x, y - 1] not in obstacles:
            y -= 1
            direction = 'jug'
    elif direction == 'sever':
        if x > 0 and [x - 1, y] not in obstacles:
            x -= 1
            direction = 'zapad'
    elif direction == 'jug':
        if x < 9 and [x + 1, y] not in obstacles:
            x += 1
            direction = 'istok'
    return x, y, direction


def svrti_desno(x, y, direction, obstacles):
    if direction == 'istok':
        if y > 0 and [x, y - 1] not in obstacles:
            y -= 1
            direction = 'jug'
    elif direction == 'zapad':
        if y < 9 and [x, y + 1] not in obstacles:
            y += 1
            direction = 'sever'
    elif direction == 'sever':
        if x < 9 and [x + 1, y] not in obstacles:
            x += 1
            direction = 'istok'
    elif direction == 'jug':
        if x > 0 and [x - 1, y] not in obstacles:
            x -= 1
            direction = 'zapad'
    return x, y, direction


class Pacman(Problem):
    def value(self):
        pass

    def __init__(self, obstacles, initial, goal=None):
        super().__init__(initial, goal=goal)
        self.obstacles = obstacles

    def successor(self, state):
        """За дадена состојба, врати речник од парови {акција : состојба}
        достапни од оваа состојба. Ако има многу следбеници, употребете
        итератор кој би ги генерирал следбениците еден по еден, наместо да
        ги генерирате сите одеднаш.

        :param state: дадена состојба
        :return:  речник од парови {акција : состојба} достапни од оваа
                  состојба
        :rtype: dict
        """
        successors = dict()

        man_x, man_y = state[0], state[1]
        man_direction = state[2]

        points_positions = state[3]

        # ProdolzhiPravo
        new_x, new_y = prodolzhi_pravo(man_x, man_y, man_direction, self.obstacles)
        if [man_x, man_y] != [new_x, new_y]:
            successors['ProdolzhiPravo'] = (new_x, new_y, man_direction,
                                            tuple([p for p in points_positions if p[0] != new_x or p[1] != new_y]))

        # ProdolzhiNazad
        new_x, new_y, new_direction = prodolzhi_nazad(man_x, man_y, man_direction, self.obstacles)
        if [man_x, man_y] != [new_x, new_y]:
            successors['ProdolzhiNazad'] = (new_x, new_y, new_direction,
                                            tuple([p for p in points_positions if p[0] != new_x or p[1] != new_y]))

        # SvrtiLevo
        new_x, new_y, new_direction = svrti_levo(man_x, man_y, man_direction, self.obstacles)
        if [man_x, man_y] != [new_x, new_y]:
            successors['SvrtiLevo'] = (new_x, new_y, new_direction,
                                       tuple([p for p in points_positions if p[0] != new_x or p[1] != new_y]))

        # SvrtiDesno
        new_x, new_y, new_direction = svrti_desno(man_x, man_y, man_direction, self.obstacles)
        if [man_x, man_y] != [new_x, new_y]:
            successors['SvrtiDesno'] = (new_x, new_y, new_direction,
                                        tuple([p for p in points_positions if p[0] != new_x or p[1] != new_y]))

        return successors

    def actions(self, state):
        """За дадена состојба state, врати листа од сите акции што може да
        се применат над таа состојба

        :param state: дадена состојба
        :return: листа на акции
        :rtype: list
        """
        return self.successor(state).keys()

    def result(self, state, action):
        """За дадена состојба state и акција action, врати ја состојбата
        што се добива со примена на акцијата над состојбата

        :param state: дадена состојба
        :param action: дадена акција
        :return: резултантна состојба
        """
        return self.successor(state)[action]

    def goal_test(self, state):
        """Врати True ако state е целна состојба. Даденава имплементација
        на методот директно ја споредува state со self.goal, како што е
        специфицирана во конструкторот. Имплементирајте го овој метод ако
        проверката со една целна состојба self.goal не е доволна.

        :param state: дадена состојба
        :return: дали дадената состојба е целна состојба
        :rtype: bool
        """

        return len(state[-1]) == 0


if __name__ == '__main__':
    obstacles_list = [
        [0, 9], [1, 9], [2, 9], [3, 9], [6, 9],
        [0, 8], [8, 8], [9, 8],
        [4, 7], [8, 7], [9, 7],
        [0, 6], [3, 6], [4, 6], [5, 6],
        [4, 5],
        [1, 4], [8, 4], [9, 4],
        [1, 3],
        [1, 2], [6, 2],
        [4, 1], [5, 1], [6, 1], [8, 1],
        [6, 0]
    ]

    inp_x = int(input())
    inp_y = int(input())
    inp_direction = input()  # istok, zapad, sever, jug
    N = int(input())

    points_pos = tuple()
    for i in range(N):
        inp = input()
        points_pos += (tuple(int(p) for p in inp.split(",")),)

    pacman = Pacman(obstacles_list, (inp_x, inp_y, inp_direction, points_pos))

    result = breadth_first_graph_search(pacman)
    print(result.solution())
