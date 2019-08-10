# given a list of points find the k points closest to the origin (0,0)

import math
import heapq

d1 = [(-2, 4), (0, -2), (-1, 0), (3, 5), (-2, -3), (3, 2)]


def calc_point_distance(p1, p2):
    return math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))


def closest_k_points(points, k):
    # pointWithDist = []
    mh = []

    for p in points:
        pDist = calc_point_distance((0,0), p)
        dp = (pDist, p)
        # print(dp)
        # pointWithDist.append(dp)
        heapq.heappush(mh, dp)

    # print('-------------------')
    closest_points = []

    for i in range(k):
        closest_points.append(heapq.heappop(mh)[1])

    # print(pointWithDist)
    # print(mh)
    return closest_points


print(closest_k_points(d1, 2))


