



def solve(arr, queries):
    R = []
    for i in queries:
        L = []
        for j in range(len(arr) - i + 1):
            maximum = arr[j]
            for k in range(1, i):
                if arr[j+k] > maximum:
                    maximum = arr[j + k]
            L.append(maximum)
        R.append(min(L))
    return R












a1 = [33, 11, 44, 11, 55]
a2 = [1, 2, 3, 4, 5]
print(solve(a1, a2) == [11, 33, 44, 44, 55])


a1 = [1, 2, 3, 4, 5]
a2 = [1, 2, 3, 4, 5]
print(solve(a1, a2) == [1, 2, 3, 4, 5])


