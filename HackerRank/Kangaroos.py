# You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line
# ready to jump in the positive direction (i.e, toward positive infinity).
#
# The first kangaroo starts at location  and moves at a rate of  meters per jump.
# The second kangaroo starts at location  and moves at a rate of  meters per jump.
# You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it
# is possible, return YES, otherwise return NO.
#
# kangaroo has the following parameter(s):
#
# x1, v1: integers, starting position and jump distance for kangaroo 1
# x2, v2: integers, starting position and jump distance for kangaroo 2


def kangaroo(x1, v1, x2, v2):
    x1r = x1
    x2r = x2
    for j in range(100):  # I'm sure there's a smarter way of doing this...
        if x1r == x2r:
            print("YES")
            break
        x1r += v1
        x2r += v2
    else:
        print("NO")


kangaroo(0, 3, 4, 2)  # == YES
kangaroo(0, 2, 5, 3)  # == NO
