import math


def catAndMouse(x, y, z):
    deltas = (abs(z - x), abs(z - y))

    if deltas[0] < deltas[1]:
        print("CAT A")
    elif deltas[1] < deltas[0]:
        print("CAT B")
    else:
        print("MOUSE C")


catAndMouse(1, 2, 3)
catAndMouse(1, 3, 2)