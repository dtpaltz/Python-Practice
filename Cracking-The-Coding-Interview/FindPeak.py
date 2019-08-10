
def find_peak(arr):
    return find_peak_rec(arr, 0, len(arr) - 1)


def find_peak_rec(arr, left, right):
    print(arr[left:right + 1])

    if left == right:
        return left

    if right > left:
        mid = (right + left) // 2
        delta = arr[mid] - arr[mid + 1]
        if delta < 0:
            return find_peak_rec(arr, mid+1, right)
        else:
            return find_peak_rec(arr, left, mid)
    else:
        return -1


m = list(range(59, 10001))
m.extend(list(range(9999, 657, -1)))
idx = find_peak(m)
print("Peak is @ [{}] = {}".format(idx, m[idx]))





