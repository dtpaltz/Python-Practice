from Statistics import Quartiles as q


n = 20
X = [10, 40, 30, 50, 20, 10, 40, 30, 50, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
F = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 40, 30, 50, 20, 10, 40, 30, 50, 20]
S = []
for i in range(n):
    t = [X[i]] * F[i]
    S.extend(t)
S.sort()
print(len(S))
print(S)
qs = q.calc_quartiles(S)
print(qs)
iqr = round(float(qs[2] - qs[0]), 1)
print(iqr)



