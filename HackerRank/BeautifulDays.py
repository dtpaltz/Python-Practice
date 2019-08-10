




def beautifulDays(i, j, k):
    result = 0
    for n in range(i, (j + 1)):
        diff = abs(n - get_reverse_number(n))
        if diff % k == 0:
            result += 1
    return result


def get_reverse_number(num):
    return int(str(num)[::-1])



print(beautifulDays(20, 23, 6))

