from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


def D1(index, tap):
    if (index + 1) < len(tap) and tap[index + 1] is None:
        temp_elem = tap[index]
        tap[index] = None
        tap[index + 1] = temp_elem
        return True, tap
    return False, tap


def D2(index, tap):
    if (index + 2) < len(tap) and tap[index + 2] is None and tap[index + 1] is not None:
        temp_elem = tap[index]
        tap[index] = None
        tap[index + 2] = temp_elem
        return True, tap
    return False, tap


def L1(index, tap):
    if (index - 1) >= 0 and tap[index - 1] is None:
        temp_elem = tap[index]
        tap[index] = None
        tap[index - 1] = temp_elem
        return True, tap
    return False, tap


def L2(index, tap):
    if (index - 2) >= 0 and tap[index - 2] is None and tap[index - 1] is not None:
        temp_elem = tap[index]
        tap[index] = None
        tap[index - 2] = temp_elem
        return True, tap
    return False, tap


class Disks(Problem):
    def value(self):
        pass

    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()

        temp_disks = list(state)

        for disk in temp_disks:
            if disk is None:
                continue

            index = temp_disks.index(disk)
            # D1
            flag, new_tape = D1(index, list(state))
            if flag:
                successors[f'D1: {disk}'] = tuple(new_tape)

            # D2
            flag, new_tape = D2(index, list(state))
            if flag:
                successors[f'D2: {disk}'] = tuple(new_tape)

            # L1
            flag, new_tape = L1(index, list(state))
            if flag:
                successors[f'L1: {disk}'] = tuple(new_tape)

            # L2
            flag, new_tape = L2(index, list(state))
            if flag:
                successors[f'L2: {disk}'] = tuple(new_tape)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        # return check_goal(list(state)[::-1])
        return list(state) == self.goal


def check_goal(tap):
    for disk in tap:
        if disk is not None:
            num = int(disk.split(' ')[1])
            if tap.index(disk) != num - 1:
                return False
        else:
            first_none = tap.index(disk)
            for disk_none in range(first_none, len(tap)):
                if tap[disk_none] is not None:
                    return False
    return True


if __name__ == '__main__':
    N = int(input())
    L = int(input())

    tape = list()
    j = 1
    for i in range(L):
        if j <= N:
            tape.append(f"Disk {j}")
            j += 1
        else:
            tape.append(None)

    disks = Disks(tuple(tape), tape[::-1])

    result = breadth_first_graph_search(disks)
    print(result.solution())
