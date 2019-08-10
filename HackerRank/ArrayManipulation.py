import sys


def arrayManipulation(n, queries):
    arr = [0] * (n + 2)

    for q in queries:
        a = q[0]
        b = q[1]
        k = q[2]

        arr[a] += k
        arr[b + 1] -= k

    maxi = -sys.maxsize - 1
    curr = 0
    for i in arr:
        curr += i
        if curr > maxi:
            maxi = curr

    return maxi


# def arrayManipulation(n, queries):
#     arr = [0] * n
#
#     for q in queries:
#         for i in range(q[0] - 1, q[1]):
#             arr[i] += q[2]
#
#     return max(arr)


a1 = 5
a2 = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
print(arrayManipulation(a1, a2) == 200)

a1 = 10
a2 = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
print(arrayManipulation(a1, a2) == 10)

a1 = 10
a2 = [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]]
print(arrayManipulation(a1, a2) == 31)
