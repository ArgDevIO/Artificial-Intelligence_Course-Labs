from constraint import *
from operator import itemgetter


def check_max(p1, p2, p3, p4, p5, l1):
    calc_sum = p1[0] + p2[0] + p3[0] + p4[0] + p5[0] + l1[0]
    return True if calc_sum < 100 else False


if __name__ == '__main__':

    participants_n = int(input())
    participants = []
    for i in range(participants_n):
        participant = input()
        participant_parts = participant.split(' ')
        participant_score = float(participant_parts[0])
        participant_name = participant_parts[1]
        participants.append((participant_score, participant_name))

    leaders_n = int(input())
    leaders = []
    for i in range(leaders_n):
        leader = input()
        leader_parts = leader.split(' ')
        leader_score = float(leader_parts[0])
        leader_name = leader_parts[1]
        leaders.append((leader_score, leader_name))

    problem = Problem()

    participants_vars = ["Participant 1", "Participant 2", "Participant 3", "Participant 4", "Participant 5"]
    leader_vars = ["Team leader"]

    problem.addVariables(leader_vars, leaders)
    problem.addVariables(participants_vars, participants)

    problem.addConstraint(AllDifferentConstraint(), participants_vars)
    problem.addConstraint(check_max, leader_vars + participants_vars)

    solutions = problem.getSolutions()

    results = []
    for solution in solutions:
        result = dict()

        to_list = list(solution.values())
        total_score = 0
        for val in to_list:
            total_score += val[0]
        result['Total score'] = total_score
        result['Team leader'] = solution[list(solution.keys())[-1]][1]
        result['Participant 1'] = solution['Participant 5'][1]
        result['Participant 2'] = solution['Participant 4'][1]
        result['Participant 3'] = solution['Participant 3'][1]
        result['Participant 4'] = solution['Participant 2'][1]
        result['Participant 5'] = solution['Participant 1'][1]
        results.append(result)

    sorted_result = sorted(results, key=itemgetter('Total score'), reverse=True)
    for key in sorted_result[0]:
        value = sorted_result[0][key]
        if isinstance(value, float):
            format_float = "{:.1f}".format(value)
            print(f"{key}: {format_float}")
        else:
            print(f"{key}: {sorted_result[0][key]}")
