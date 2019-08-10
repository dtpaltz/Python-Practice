

def find_min(arr):
    min1 = arr[0]
    for n in arr[1:]:
        if n < min1:
            min1 = n
    return min1

def find_min_2(arr):
    min1 = min(arr[:2])
    min2 = max(arr[:2])
    for n in arr[2:]:
        if n < min1:
            min2 = min1
            min1 = n
        elif n < min2:
            min2 = n
    return min2


def find_nth_order(arr, m):
    n = len(arr)
    pivot_range = [0, 0]

    print(arr)

    for i in range(n - 1):
        start_idx = pivot_range[0]
        next_idx = pivot_range[1] + 1
        if arr[start_idx] > arr[next_idx]:
            arr.insert(start_idx, arr.pop(next_idx))
            pivot_range = list(map(lambda p: p + 1, pivot_range))
        else:
            pivot_range[1] += 1

    pivot = pivot_range[0] + 1
    if m > pivot:
        arr = arr[pivot_range[0]:]
        m -= pivot
        return find_nth_order(arr, m)
    elif m < pivot:
        arr = arr[:pivot_range[0]]
        return find_nth_order(arr, m)
    else:
        return arr[pivot]






test_arr = [10, 2, 5, 6, 4, 11, 3, 15, 1]
print(find_nth_order(test_arr, 1))
