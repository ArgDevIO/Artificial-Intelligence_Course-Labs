from constraint import *

if __name__ == '__main__':

    participants_n = int(input())
    participants = dict()

    i = 0
    while i < participants_n:
        i += 1
        participant = input()
        participant_parts = participant.split(' ')
        participant_score = participant_parts[0]
        participant_name = participant_parts[1]
        participants[participant_name] = participant_score

    leaders_n = int(input())
    leaders = dict()

    i = 0
    while i < leaders_n:
        i += 1
        leader = input()
        leader_parts = leader.split(' ')
        leader_score = leader_parts[0]
        leader_name = leader_parts[1]
        leaders[leader_name] = leader_score

    problem = Problem(MinConflictsSolver())

    participants_vars = ["P1", "P2", "P3", "P4", "P5"]
    leader_vars = ["0"]

    problem.addVariables(leader_vars, leaders)
    problem.addVariables(participants_vars, participants)

    problem.addConstraint(AllDifferentConstraint(), participants_vars)

    solution = problem.getSolutions()

    print(solution)
