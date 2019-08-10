
import random

#
# def select_movies(m, d):
#     n = len(m)
#     max_d = d - 30
#     m.sort()    # this is n log n
#     ans = [0, 0]
#     for i in range(n - 1, -1, -1):
#         if m[i] <= d:
#             for j in range(0, i, 1):
#                 this_d = m[i] + m[j]
#                 if this_d > max_d:
#                     break
#                 elif this_d > sum(ans):
#                     ans = [m[j], m[i]]
#     return ans

def select_movies(m, d):
    max_d = d - 30
    m = list(filter(lambda x: x <= max_d, m))
    m.sort(reverse=True)    # this is n log n
    ans = [0, 0]
    for m1_idx, m1 in enumerate(m[:-1]):
        for m2 in m[m1_idx + 1:]:
            s = m1 + m2
            if sum(ans) < s <= max_d:
                ans = [m1, m2]
    return ans


movie_times = [90, 85, 75, 60, 120, 150, 125]
duration = 250

movie_times = random.sample(range(60, 200), 140)


print(select_movies(movie_times, duration))
