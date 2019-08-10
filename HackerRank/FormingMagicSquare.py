import sys
from itertools import permutations


def formingMagicSquare(s):
    #possible_magic_squares = getMagicSquares(len(s))
    possible_magic_squares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ]
    smallest_diff = sys.maxsize
    for ms in possible_magic_squares:
        this_diff = magicSquareDiff(s, ms)
        print(this_diff)
        if this_diff < smallest_diff:
            smallest_diff = this_diff
    print("-------------------")
    return smallest_diff


def getMagicSquares(n):
    a = range(1, (n * n) + 1)
    perm = permutations(a)
    result = []
    for p in list(perm):
        perm_as_sqr = []
        for i in range(0, len(a), n):
            perm_as_sqr.append(p[i:(i + n)])
        if isMagicSquare(perm_as_sqr):
            result.append(perm_as_sqr)
    return result


def isMagicSquare(s):
    n = len(s)
    target_sum = sum(s[0])

    # check rows
    for r in range(n):
        if sum(s[r]) != target_sum:
            return False

    # check cols
    col_sums = [0] * n
    for r in range(n):
        for c in range(len(s[r])):
            col_sums[c] += s[r][c]

    for c_sum in col_sums:
        if c_sum != target_sum:
            return False

    # check diagonals
    diag_sums = [0, 0]
    for r in range(n):
        diag_sums[0] += s[r][r]
        diag_sums[1] += s[r][n - (c + 1)]

    for d_sum in diag_sums:
        if d_sum != target_sum:
            return False

    return True


def magicSquareDiff(s1, s2):
    diff = 0
    for i in range(len(s1)):
        for j in range(len(s1[i])):
            diff += abs(s1[i][j] - s2[i][j])
    return diff


t1 = [[4, 9, 2], [3, 5, 7], [8, 1, 5]] # == 1
t2 = [[7, 6, 5], [7, 2, 8], [5, 3, 4]] # == 18
print(formingMagicSquare(t2))



