# https://www.hackerrank.com/challenges/itertools-permutations/problem
# https://www.hackerrank.com/challenges/itertools-combinations/problem
import itertools as it
from itertools import permutations

s = "HACK"
k = 2

perm = list(permutations(s, k))
perm.sort()

for i in perm:
    print(*i, sep='')


print('=' * 40)


s = "HACK"
k = 2

combs = []
for i in range(1, k + 1):
    t = [''.join(x) for x in it.combinations(sorted(s), i)]
    t.sort()
    combs.extend(t)

for i, c in enumerate(combs):
    if i < len(combs) - 1:
        print(c)
    else:
        print(c, end='')


print('=' * 40)


for key, grp in it.groupby([1, 1, 2, 2, 2, 3]):
    print('{}: {}'.format(key, list(grp)))










