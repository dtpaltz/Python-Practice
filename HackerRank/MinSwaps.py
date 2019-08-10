




def minimumSwapsX(arr):
    temp = [-1] * (len(arr) + 1)
    for pos, val in enumerate(arr):
        temp[val] = pos
        pos += 1
    swaps = 0
    for i in range(len(arr)):
        if arr[i] != i+1:
            swaps += 1
            t = arr[i]
            arr[i] = i+1
            arr[temp[i+1]] = t
            temp[t] = temp[i+1]
    return swaps







def minimumSwaps(arr):
    temp = [None] * (len(arr) + 1)
    for idx, val in enumerate(arr):
        temp[val] = idx
    swaps = 0
    for idx, val in enumerate(arr):
        if arr[idx] != idx + 1:
            swaps += 1
            t = arr[idx]
            arr[idx] = idx + 1
            arr[temp[idx + 1]] = t
            temp[t] = temp[idx + 1]
    return swaps














ta = [1, 3, 5, 2, 4, 6, 7]
print("Min swaps = " + str(minimumSwaps(ta)))








