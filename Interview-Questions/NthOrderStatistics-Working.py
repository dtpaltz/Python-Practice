# I think this is the working version, but I need to verify


def find_nth_order(arr, m):
    return find_nth_order_rec(arr, m, 0)

def find_nth_order_rec(arr, m, start):
    pivot_range = [start, start]
    print(m, arr, sep='   ')
    for i in range(len(arr) - 1 - pivot_range[1]):
        start_idx = pivot_range[0]
        next_idx = pivot_range[1] + 1
        if arr[start_idx] > arr[next_idx]:
            arr.insert(start_idx, arr.pop(next_idx))
            pivot_range = list(map(lambda p: p + 1, pivot_range))
        else:
            pivot_range[1] += 1

    if m - 1 < pivot_range[0]:
        arr = arr[:pivot_range[0]]
        return find_nth_order_rec(arr, m, 0)
    elif m - 1 > pivot_range[0]:
        arr = arr[pivot_range[0]:]
        m -= pivot_range[0]
        return find_nth_order_rec(arr, m, start + 1)
    else:
        return arr[pivot_range[0]]


test_arr = [6, 5, 8, 4, 2, 7, 1, 3, 9, 10]
print(find_nth_order(test_arr, 3))

