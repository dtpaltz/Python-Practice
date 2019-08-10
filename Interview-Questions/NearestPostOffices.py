

import math


def calc_distance(p1, p2):
    m, n = p1
    p, q = p2
    return math.sqrt((m - p) * (m - p) + (n - q) * (n - q))


def nearest_post_offices(me, post_offices, k):
    distances = list(map(lambda p: (p, calc_distance(me, p)), post_offices))
    distances.sort(key=lambda tup: tup[1])
    return list(map(lambda p: p[0], distances[:k]))









_pos = [[-16, 5], [-1, 2], [4, 3], [10, -2], [0, 3], [-5, -9]]
_me = (0, 0)
print(nearest_post_offices(_me, _pos, 3))





