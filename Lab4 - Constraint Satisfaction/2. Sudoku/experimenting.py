var1 = 'C'
var2 = 'C'


def get_character_distance(char1, char2):
    return abs(ord(char1.upper()) - ord(char2.upper()))


def check_adjacent(a, b):
    if get_character_distance(a, b) > 1:
        return True
    return False


print(check_adjacent(var1, var2))
