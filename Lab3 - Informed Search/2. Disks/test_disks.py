from unittest import TestCase
from searching_framework.informed_search import *
from disks import Disks


def get_disks_result(N, L):
    # noinspection DuplicatedCode
    tape = list()
    for i in range(L):
        if i < N:
            tape.append(i + 1)
        else:
            tape.append(0)

    disks = Disks(tuple(tape), tape[::-1])
    return astar_search(disks)


class TestDisks(TestCase):

    def test_1(self):
        output = ['D1: Disk 3', 'D2: Disk 1', 'D2: Disk 1', 'D2: Disk 3', 'D2: Disk 1', 'L1: Disk 3', 'D1: Disk 2', 'D1: Disk 2', 'D2: Disk 2']

        result = get_disks_result(3, 7)
        self.assertEqual(result.solution(), output)

    def test_2(self):
        output = ['D1: Disk 2', 'D1: Disk 1', 'D2: Disk 1']

        result = get_disks_result(2, 4)
        self.assertEqual(result.solution(), output)

    def test_3(self):
        output = ['D1: Disk 3', 'D2: Disk 1', 'L1: Disk 2', 'L2: Disk 3', 'D1: Disk 1', 'D2: Disk 2']

        result = get_disks_result(3, 4)
        self.assertEqual(result.solution(), output)

    def test_4(self):
        output = ['D2: Disk 1', 'D2: Disk 2', 'D2: Disk 1']

        result = get_disks_result(2, 5)
        self.assertEqual(result.solution(), output)

    def test_5(self):
        output = ['D1: Disk 3', 'D2: Disk 1', 'D2: Disk 1', 'L1: Disk 3', 'D2: Disk 2']

        result = get_disks_result(3, 5)
        self.assertEqual(result.solution(), output)

    def test_6(self):
        output = ['D1: Disk 4', 'D2: Disk 2', 'L1: Disk 3', 'D2: Disk 1', 'L1: Disk 3', 'L2: Disk 2', 'L1: Disk 4', 'D2: Disk 1', 'L1: Disk 4', 'D2: Disk 2', 'L1: Disk 4', 'D2: Disk 3']

        result = get_disks_result(4, 5)
        self.assertEqual(result.solution(), output)

    def test_7(self):
        output = ['D1: Disk 3', 'D2: Disk 1', 'D2: Disk 1', 'D1: Disk 1', 'D1: Disk 2', 'D2: Disk 2']

        result = get_disks_result(3, 6)
        self.assertEqual(result.solution(), output)

    def test_8(self):
        output = ['D1: Disk 4', 'D2: Disk 2', 'D1: Disk 1', 'L2: Disk 3', 'L2: Disk 4', 'D1: Disk 2', 'D2: Disk 1', 'D2: Disk 1', 'D1: Disk 3', 'D2: Disk 3']

        result = get_disks_result(4, 6)
        self.assertEqual(result.solution(), output)

    def test_9(self):
        output = ['D1: Disk 5', 'D2: Disk 3', 'D2: Disk 1', 'L1: Disk 2', 'L2: Disk 4', 'L2: Disk 5', 'D1: Disk 3', 'D2: Disk 1', 'D2: Disk 2', 'L1: Disk 4', 'L2: Disk 5', 'L2: Disk 3', 'D1: Disk 1', 'D2: Disk 2', 'D2: Disk 4']

        result = get_disks_result(5, 6)
        self.assertEqual(result.solution(), output)

    def test_10(self):
        output = ['D1: Disk 4', 'D2: Disk 2', 'D2: Disk 2', 'L1: Disk 4', 'L1: Disk 3', 'D2: Disk 1', 'D2: Disk 1', 'D2: Disk 1', 'D1: Disk 3', 'D2: Disk 3']

        result = get_disks_result(4, 7)
        self.assertEqual(result.solution(), output)
