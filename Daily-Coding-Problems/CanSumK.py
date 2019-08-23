# This problem was recently asked by Google.
#
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.


def can_sum_k(arr, k):
    compliments = set()
    for num in arr:
        if num in compliments:
            return True
        compliments.add(k - num)
    return False


t_arr = [10, 15, 3, 7]
t_k = 171
print(can_sum_k(t_arr, t_k))


# This problem was recently asked by Facebook:
#
# Given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that add to k.
#
# Try to do it in a single pass of the list.

# Example:
# Given [4, 7, 1 , -3, 2] and k = 5,
# return true since 4 + 1 = 5.

print(can_sum_k([4, 7, 1, -3, 2], 5))
# True
