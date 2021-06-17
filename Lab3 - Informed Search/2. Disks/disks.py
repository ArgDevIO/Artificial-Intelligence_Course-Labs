from searching_framework.informed_search import *
from searching_framework.utils import Problem


class Disks(Problem):

    def value(self):
        pass

    def __init__(self, initial, goal):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()
        disks = list(state)

        for disk in disks:
            if disk == 0:
                continue

            # D1
            temp_disks = list(state)
            index = temp_disks.index(disk)
            if (index + 1) < len(temp_disks) and temp_disks[index + 1] == 0:
                temp_disks[index], temp_disks[index + 1] = temp_disks[index + 1], temp_disks[index]
                successors[f'D1: Disk {disk}'] = tuple(temp_disks)

            # D2
            temp_disks = list(state)
            index = temp_disks.index(disk)
            if (index + 2) < len(temp_disks) and temp_disks[index + 2] == 0 and temp_disks[index + 1] != 0:
                temp_disks[index], temp_disks[index + 2] = temp_disks[index + 2], temp_disks[index]
                successors[f'D2: Disk {disk}'] = tuple(temp_disks)

            # L1
            temp_disks = list(state)
            index = temp_disks.index(disk)
            if (index - 1) >= 0 and temp_disks[index - 1] == 0:
                temp_disks[index], temp_disks[index - 1] = temp_disks[index - 1], temp_disks[index]
                successors[f'L1: Disk {disk}'] = tuple(temp_disks)

            # L2
            temp_disks = list(state)
            index = temp_disks.index(disk)
            if (index - 2) >= 0 and temp_disks[index - 2] == 0 and temp_disks[index - 1] != 0:
                temp_disks[index], temp_disks[index - 2] = temp_disks[index - 2], temp_disks[index]
                successors[f'L2: Disk {disk}'] = tuple(temp_disks)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return list(state) == self.goal

    def h(self, node):
        state = list(node.state)
        counter = 0

        x = len(node.state) - 1
        while self.goal[x] != 0:
            if self.goal[x] != state[x]:
                counter += 1
            x -= 1

        return counter


if __name__ == '__main__':
    N = int(input())
    L = int(input())

    tape = list()
    for i in range(L):
        if i < N:
            tape.append(i + 1)
        else:
            tape.append(0)

    disks_obj = Disks(tuple(tape), tape[::-1])

    result = astar_search(disks_obj)
    print(result.solution())
