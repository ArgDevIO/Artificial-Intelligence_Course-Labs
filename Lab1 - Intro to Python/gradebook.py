line = input()
students = {}


def getGrade(points):
    if points > 90:
        return 10
    elif points > 80:
        return 9
    elif points > 70:
        return 8
    elif points > 60:
        return 7
    elif points > 50:
        return 6
    else:
        return 5


while line.strip() != "end":
    student_info = line.split(',')

    full_name = f'{student_info[0]} {student_info[1]}'
    indexID = student_info[2]
    subject = student_info[3]
    total_points = (int(student_info[4]) +
                    int(student_info[5]) +
                    int(student_info[6]))
    grade = getGrade(total_points)

    if indexID not in students:
        students[indexID] = {'full_name': full_name,
                             'subjects': {subject: grade}}
    else:
        students[indexID]['subjects'][subject] = grade

    line = input()

for student in students.values():
    print(f'Student: {student["full_name"]}')
    for subject, grade in student["subjects"].items():
        print(f'\t{subject}: {grade}')
    print()
