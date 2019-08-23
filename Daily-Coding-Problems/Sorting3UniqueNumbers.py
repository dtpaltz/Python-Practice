# Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.
#
# Challenge: Try sorting the list using constant space.
#
# Example 1:
# Input:
# [3, 3, 2, 1, 3, 2, 1]
# Output: [1, 1, 2, 2, 3, 3, 3]

def sortNums(nums):
    size = len(nums)
    lo = min(nums)
    hi = max(nums)

    # Iterate through list backwards and sort
    print("Sorting backwards...")
    for i in range(size - 1, -1, -1):
        print(nums)

        if nums[i] == hi:
            nums.pop(i)
            nums.append(hi)
            print(f"----> HI pop {i} and append")

        if nums[i] == lo:
            nums.pop(i)
            nums.insert(0, lo)
            print(f"----> LO pop {i} and insert 0")

    # Iterate through list forwards and sort
    # print("Sorting forwards...")
    # for i in range(size - 1, -1, -1):
    #     print(nums)
    #
    #     if nums[i] == hi:
    #         nums.pop(i)
    #         nums.append(hi)
    #         print(f"----> HI pop {i} and append")
    #         i -= 1  # need to reconsider the index that was just popped in the next loop iteration
    #
    #     if nums[i] == lo:
    #         nums.pop(i)
    #         nums.insert(0, lo)
    #         print(f"----> LO pop {i} and insert 0")
    #         i -= 1  # need to reconsider the index that was just popped in the next loop iteration

    return nums


if __name__ == '__main__':
    t_list = [3, 3, 2, 1, 3, 2, 1]
    print(sortNums(t_list))
    # [1, 1, 2, 2, 3, 3, 3]
