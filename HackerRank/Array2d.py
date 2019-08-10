import sys



def hourglassSum(arr):
    max_sum = -sys.maxsize - 1
    for i in range(len(arr) - 2):
        for j in range(len(arr[i]) - 2):
            s = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            if s > max_sum:
                max_sum = s

    return max_sum



a1 = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
#print(hourglassSum(a1))


print(3 > None)


