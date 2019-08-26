# This problem was recently asked by Apple:
#
# Given an integer k and a binary search tree, find the floor (less than or equal to) of k, and the
# ceiling (larger than or equal to) of k. If either does not exist, then print them as None.
#
# Here is the definition of a node for the tree.


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def findCeilingFloor(rn, k, floor=None, ceil=None):
    if not rn or not rn.value:
        return

    if rn.value <= k:
        if not floor or rn.value > floor:
            floor = rn.value

    if rn.value >= k:
        if not ceil or rn.value < ceil:
            ceil = rn.value

    if rn.left:
        floor, ceil = findCeilingFloor(rn.left, k, floor, ceil)
    if rn.right:
        floor, ceil = findCeilingFloor(rn.right, k, floor, ceil)

    return [floor, ceil]



if __name__ == "__main__":
    root = Node(8)
    root.left = Node(4)
    root.right = Node(12)

    root.left.left = Node(2)
    root.left.right = Node(6)

    root.right.left = Node(10)
    root.right.right = Node(14)

    print(findCeilingFloor(root, 5))
    # (4, 6)
