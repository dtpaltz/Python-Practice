# This problem was recently asked by Uber:
#
# Given a list of numbers, find if there exists a pythagorean triplet in that list.
# A pythagorean triplet is 3 variables a, b, c where a^2 + b^2 = c^2
#
# Example:
# Input: [3, 5, 12, 5, 13]
# Output: True
# Here, 5^2 + 12^2 = 13^2.


def findPythagoreanTriplets(ar):
    n = len(ar)
    ar = [x ** 2 for x in ar]
    ar.sort()

    # fix one element and find the other two
    # i goes from n - 1 to 2
    for i in range(n - 1, 1, -1):
        # start two index variables from two corners of the array and move them toward each other
        j = 0
        k = i - 1
        while j < k:
            if ar[j] + ar[k] == ar[i]:
                return True
            else:
                if ar[j] + ar[k] < ar[i]:
                    j = j + 1
                else:
                    k = k - 1

    # no triplet found
    return False


print(findPythagoreanTriplets([3, 12, 5, 13]))
# True
