from constraint import *
from operator import itemgetter


def check_meeting(a, b, c, d):
    simona_free_time = [13, 14, 16, 19]
    marija_free_time = [14, 15, 18]
    petar_free_time = [12, 13, 16, 17, 18, 19]

    marija = a
    simona = b
    petar = c
    sostanok = d

    if simona == 1 and sostanok in simona_free_time:
        if marija == 1 and sostanok in marija_free_time and petar == 1 and sostanok in petar_free_time:
            return True
        if marija == 1 and sostanok in marija_free_time and petar == 0:
            return True
        if marija == 0 and petar == 1 and sostanok in petar_free_time:
            return True
    return False


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    domain = [1, 0]
    domain_sostanok = []
    for i in range (12, 21):
        domain_sostanok.append(i)

    problem.addVariable("Marija_prisustvo", domain)
    problem.addVariable("Simona_prisustvo", domain)
    problem.addVariable("Petar_prisustvo", domain)
    problem.addVariable("vreme_sostanok", domain_sostanok)
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(lambda a, b, c, d: check_meeting(a, b, c, d), ("Marija_prisustvo", "Simona_prisustvo", "Petar_prisustvo", "vreme_sostanok"))
    # ----------------------------------------------------

    new_solution = []
    for solution in problem.getSolutions():
        new_dict = dict()

        new_dict["Simona_prisustvo"] = solution["Simona_prisustvo"]
        new_dict["Marija_prisustvo"] = solution["Marija_prisustvo"]
        new_dict["Petar_prisustvo"] = solution["Petar_prisustvo"]
        new_dict["vreme_sostanok"] = solution["vreme_sostanok"]

        new_solution.append(new_dict)

    for x in sorted(new_solution, key=itemgetter("Marija_prisustvo", "Simona_prisustvo", "Petar_prisustvo"), reverse=True):
        print(x)
