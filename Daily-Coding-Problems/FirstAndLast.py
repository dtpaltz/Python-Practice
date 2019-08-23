# Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last
# occurrences of a target element, x. Return -1 if the target is not found.
import bisect
from typing import List
import time


def FirstAndLastBrute(arr: List[int], target: int):
    ans = [-1, -1]


    for i in range(len(arr)):
        if arr[i] == target:
            ans = [i, i]
            break

    while ans[1] + 1 < len(arr) and arr[ans[1] + 1] == target:
        ans[1] += 1

    return ans



if __name__ == '__main__':
    t_target = 7654321
    t_arr = [n for n in range(1, t_target)]
    t_arr.extend([t_target] * 5)
    t_arr.extend(list(range(t_target, t_target*3)))

    start = time.time()

    result = FirstAndLastBrute(t_arr, t_target)
    print(result)

    end = time.time()
    print(end - start)


