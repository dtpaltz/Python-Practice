# https://www.hackerrank.com/challenges/s10-quartiles/problem?h_r=email&unlock_token=9486acd777be7738967e4702ae9b124e6ab857f2&utm_campaign=10_days_of_statistics_continuous&utm_medium=email&utm_source=daily_reminder


def calc_quartiles(nums):
    nums.sort()
    nums_med = extend_median(nums)
    left_med = extend_median(nums_med[0][:nums_med[1]])
    right_med = extend_median(nums_med[0][(nums_med[1] + 1):])
    return left_med[0][left_med[1]], nums_med[0][nums_med[1]], right_med[0][right_med[1]]


def extend_median(nums):
    n = len(nums)
    if n % 2 == 0:
        a = nums[n // 2 - 1]
        b = nums[n // 2]
        med = (a + b) / 2
        nums.insert(n // 2, med)

    return nums, len(nums) // 2


def print_truncated_float(num):
    print('{0:.2f}'.format(num).rstrip('0').rstrip('.'))


#
# t_lst = [3, 7, 8, 5, 12, 14, 21, 13, 18]
# print(calc_quartiles(t_lst))
