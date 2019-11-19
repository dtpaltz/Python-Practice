# https://leetcode.com/problems/reverse-integer/


def reverse(x: int) -> int:
    temp = abs(x)
    rev = 0
    print(x)

    while temp != 0:
        rev = (rev * 10) + (temp % 10)
        temp = temp // 10

    if x < 0:
        rev = -1 * rev

    # return 0 if there is overflow with 32 bits
    if rev < -2147483648 or rev > 2147483647:
        rev = 0

    print(rev)


reverse(1534236469)
