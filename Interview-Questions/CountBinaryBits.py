from typing import List

# This problem was recently asked by Amazon.
#
# Given a list of numbers, return the total number of active bits used to represent all the numbers.
#
# For example, given base 10 numbers [1, 2, 3], return 4 since...
# (1 => 0001 = 1 active bits) +
# (2 => 0010 = 1 active bits) +
# (3 => 0011 = 2 active bits)
# === 4 total active bits

def countActiveBits(nums: List[int]):
    total = 0

    for n in nums:
        bStr = bin(n)
        count = bStr.count('1')
        total += count
        print(f"{n} has {count} active bits  =>   {bStr}")

    print("-" * 60)
    print(f"Total active bits = {total}")
    return total


countActiveBits([1, 2, 3, 5, 7, 9, 13, 15, 63, 127, 2047])

