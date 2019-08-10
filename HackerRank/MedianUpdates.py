import bisect


def binary_search(arr, x):
    return binary_search_recursive(arr, 0, len(arr) - 1, x)


def binary_search_recursive(arr, l, r, x):
    if r >= l:
        mid = l + (r - l ) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search_recursive(arr, l, mid - 1, x)
        else:
            return binary_search_recursive(arr, mid + 1, r, x)
    else:
        return -1


def calc_median(arr):
    mid = (len(arr) - 1) // 2
    if len(arr) % 2 == 0:
        return (arr[mid] + arr[mid + 1]) / 2
    else:
        return arr[mid]


def median(a, x):
    n = len(a)
    arr = []

    for i in range(n):
        o = a[i]
        n = x[i]
        eidx = binary_search(arr, n) # exists index
        if o == 'r':
            if eidx >= 0:
                del arr[eidx]
            if len(arr) == 0:
                print('Wrong!')
        else:
            idx = bisect.bisect_left(arr, n)
            arr.insert(idx, n)

        if len(arr) > 0:
            med = calc_median(arr)
            print(('%f' % med).rstrip('0').rstrip('.'))


a1 = ['r', 'a', 'a', 'a', 'r', 'r', 'r']
a2 = [ 1,   1,   2,   1,   1,   2,   1]
median(a1, a2)

