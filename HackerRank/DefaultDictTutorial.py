# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

from collections import defaultdict

n, m = [int(x) for x in input().split()]

seen = defaultdict(lambda: [])

for i in range(1, n + 1):
    w = str(input())
    seen[w].append(i)

for j in range(m):
    w = str(input())
    if w in seen:
        print(*seen[w])
    else:
        print(-1)

