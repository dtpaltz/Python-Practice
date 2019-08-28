# This problem was recently asked by LinkedIn:
#
# You are given a positive integer N which represents the number of steps in a staircase.
# You can either climb 1 or 2 steps at a time.
# Write a function that returns the number of unique ways to climb the stairs.
#
# Can you find a solution in O(n) time?

def staircase(n):
    if n == 0 or n == 1:
        return 1
    else:
        return staircase(n - 1) + staircase(n - 2)


# using an alternate set of allowed steps that can be taken
def num_ways_X(n):
    if n == 0:
        return 1

    total = 0
    for i in [1, 3, 5]:
        if n - 1 >= 0:
            total += num_ways_X(n - i)
    return total



def num_ways_X_bottom_up(n, steps):
    if n == 0:
        return 1

    nums = [0] * (n + 1)
    nums[0] = 1
    for i in range(1, n + 1):
        total = 0
        for s in steps:
            if i - s >= 0:
                total += nums[i - s]
        nums[i] = total
    return nums[n]





print(staircase(4))
# 5

print(staircase(5))
# 8

