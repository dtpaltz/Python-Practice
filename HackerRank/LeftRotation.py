

def left_rotate(d, a):
    return a[d:] + a[:d]




arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(left_rotate(5, arr))

