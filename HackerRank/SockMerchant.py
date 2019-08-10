import math


def sockMerchant(n, ar):
    sock_ar = [0] * 100
    for s in ar:
        sock_ar[s - 1] += 1

    count = 0
    for n in sock_ar:
        count += math.floor(n / 2)

    return count
