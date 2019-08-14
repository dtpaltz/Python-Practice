# This gets all valid substrings of a given string

from itertools import combinations


s = "super"
for i, j in combinations(range(len(s) + 1), 2):
    print(s[i:j])





