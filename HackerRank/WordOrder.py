# https://www.hackerrank.com/challenges/word-order/problem


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

n = int(input())
seen = OrderedDict()
for i in range(n):
    line = str(input())
    if line not in seen:
        seen[line] = 0
    seen[line] += 1

print(len(seen))

print(*seen.values())

