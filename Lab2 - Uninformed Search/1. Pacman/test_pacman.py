from unittest import TestCase
from pacman import Pacman
from pacman_new import *


def get_pacman_result(x, y, direction, points_positions):
    # noinspection DuplicatedCode
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

    pacman_obj = Pacman(obstacles_list, (x, y, direction, points_positions))
    return breadth_first_graph_search(pacman_obj)


class TestPacman(TestCase):

    def test_1(self):
        output = ['ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiNazad',
                  'ProdolzhiPravo', 'SvrtiDesno', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo',
                  'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiNazad', 'ProdolzhiPravo', 'SvrtiLevo', 'ProdolzhiPravo',
                  'ProdolzhiPravo', 'ProdolzhiPravo', 'SvrtiLevo', 'ProdolzhiNazad', 'ProdolzhiPravo', 'SvrtiLevo',
                  'ProdolzhiPravo', 'SvrtiDesno']

        result = get_pacman_result(0, 0, 'istok', ((2, 6), (4, 0), (6, 5), (8, 2), (8, 3)))
        self.assertEqual(result.solution(), output)

    def test_2(self):
        output = ['ProdolzhiPravo', 'SvrtiLevo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'SvrtiDesno', 'ProdolzhiPravo',
                  'SvrtiLevo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'SvrtiLevo',
                  'SvrtiDesno', 'ProdolzhiNazad', 'ProdolzhiPravo', 'SvrtiDesno', 'ProdolzhiPravo', 'ProdolzhiPravo',
                  'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'SvrtiLevo', 'ProdolzhiPravo',
                  'ProdolzhiPravo']

        result = get_pacman_result(9, 5, 'sever', ((5, 0), (0, 7)))
        self.assertEqual(result.solution(), output)

    def test_3(self):
        output = ['SvrtiDesno', 'ProdolzhiPravo', 'SvrtiLevo', 'ProdolzhiPravo', 'SvrtiDesno', 'ProdolzhiPravo',
                  'ProdolzhiNazad', 'SvrtiDesno', 'ProdolzhiPravo', 'SvrtiDesno', 'SvrtiLevo', 'SvrtiDesno',
                  'ProdolzhiPravo', 'SvrtiDesno', 'SvrtiLevo', 'SvrtiDesno', 'ProdolzhiPravo', 'SvrtiDesno']

        result = get_pacman_result(9, 9, 'jug', ((3, 5), (3, 7), (5, 5), (5, 7)))
        self.assertEqual(result.solution(), output)

    def test_4(self):
        output = ['ProdolzhiPravo', 'SvrtiDesno', 'ProdolzhiPravo', 'SvrtiDesno', 'SvrtiLevo', 'ProdolzhiPravo',
                  'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiNazad', 'ProdolzhiPravo',
                  'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'SvrtiDesno', 'ProdolzhiPravo', 'SvrtiLevo',
                  'ProdolzhiPravo', 'ProdolzhiPravo', 'SvrtiDesno', 'ProdolzhiPravo', 'ProdolzhiPravo',
                  'ProdolzhiPravo', 'ProdolzhiPravo', 'SvrtiLevo', 'SvrtiDesno', 'ProdolzhiPravo']

        result = get_pacman_result(0, 7, 'istok', ((0, 0), (9, 9)))
        self.assertEqual(result.solution(), output)

    def test_5(self):
        output = ['SvrtiLevo', 'ProdolzhiPravo', 'ProdolzhiNazad', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo',
                  'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'SvrtiDesno', 'SvrtiDesno', 'ProdolzhiPravo']

        result = get_pacman_result(4, 3, 'sever', ((2, 3), (3, 3), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (9, 2), (8, 2), (7, 2)))
        self.assertEqual(result.solution(), output)

    def test_6(self):
        output = ['ProdolzhiPravo', 'SvrtiLevo', 'SvrtiLevo', 'ProdolzhiPravo', 'SvrtiLevo', 'ProdolzhiPravo', 'SvrtiLevo', 'ProdolzhiPravo']

        result = get_pacman_result(4, 3, 'jug', ((3, 2), (3, 3), (3, 4), (4, 2), (4, 4), (5, 2), (5, 3), (5, 4)))
        self.assertEqual(result.solution(), output)

    def test_7(self):
        output = ['SvrtiLevo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'SvrtiDesno', 'SvrtiLevo', 'ProdolzhiPravo', 'SvrtiLevo']

        result = get_pacman_result(0, 0, 'istok', ((0, 7),))
        self.assertEqual(result.solution(), output)

    def test_8(self):
        output = []

        result = get_pacman_result(0, 0, 'istok', ())
        self.assertEqual(result.solution(), output)

    def test_9(self):
        output = ['SvrtiLevo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'SvrtiLevo', 'ProdolzhiPravo', 'ProdolzhiNazad',
                  'ProdolzhiPravo', 'SvrtiDesno', 'ProdolzhiPravo', 'ProdolzhiPravo', 'SvrtiDesno', 'ProdolzhiPravo',
                  'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'SvrtiDesno', 'SvrtiDesno',
                  'ProdolzhiPravo', 'SvrtiDesno', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo',
                  'SvrtiLevo', 'ProdolzhiPravo']

        result = get_pacman_result(3, 3, 'zapad', ((4, 0), (5, 0), (5, 7), (7, 2), (8, 2), (9, 2)))
        self.assertEqual(result.solution(), output)

    def test_10(self):
        output = ['ProdolzhiNazad', 'SvrtiDesno', 'ProdolzhiPravo', 'SvrtiLevo', 'SvrtiDesno', 'ProdolzhiPravo',
                  'ProdolzhiNazad', 'ProdolzhiPravo', 'SvrtiLevo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo',
                  'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'SvrtiLevo',
                  'ProdolzhiPravo', 'ProdolzhiNazad', 'ProdolzhiPravo', 'SvrtiDesno', 'ProdolzhiPravo', 'ProdolzhiPravo',
                  'SvrtiLevo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'SvrtiLevo',
                  'ProdolzhiPravo', 'ProdolzhiPravo', 'SvrtiDesno', 'ProdolzhiPravo']

        result = get_pacman_result(5, 7, 'jug', ((0, 0), (9, 0), (9, 9)))
        self.assertEqual(result.solution(), output)
