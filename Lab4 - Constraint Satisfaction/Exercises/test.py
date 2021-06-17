list3 = [(a, b) for a in list(range(-2, 3)) for b in list(range(-2, 3)) if abs(a) != abs(b) and a != 0 and b != 0]
print(list3)
