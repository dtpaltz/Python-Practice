# Given five positive integers, find the minimum and maximum values that can be
# calculated by summing exactly four of the five integers. Then print the respective
# minimum and maximum values as a single line of two space-separated long integers.


def miniMaxSum(arr):
    s = sum(arr)
    mins = s - max(arr)
    maxs = s - min(arr)
    print("{0}  {1}".format(mins, maxs))


miniMaxSum([1, 2, 3, 4, 5])
