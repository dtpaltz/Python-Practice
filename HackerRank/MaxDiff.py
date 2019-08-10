# Given an array,find the maximum j – i such that arr[j] > arr[i]

def find_max_diff(arr):
    n = len(arr)
    if n < 2:
        return None
    



t_arr = [8, 17, 3, 10, 5, 7, 1, 4, 15, 2]
print(find_max_diff(t_arr))

