

def is_in_range(a, b, n):
    return a <= n <= b


def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_collision = 0
    for f in apples:
        if is_in_range(s, t, f + a):
            apple_collision += 1

    print(apple_collision)

    orange_collision = 0
    for f in oranges:
        if is_in_range(s, t, f + b):
            orange_collision += 1

    print(orange_collision)










