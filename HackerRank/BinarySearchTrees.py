# Task 1
# The height of a binary search tree is the number of edges between the tree's root and its furthest leaf.
# You are given a pointer, root, pointing to the root of a binary search tree. Complete the getHeight function
# provided in your editor so that it returns the height of the binary search tree.
#
# Task 2
# A level-order traversal, also known as a breadth-first search, visits each level of a tree's nodes from left to
# right, top to bottom. You are given a pointer, root , pointing to the root of a binary search tree. Complete the
# levelOrder function provided in your editor so that it prints the level-order traversal of the binary search tree.
#
# Hint: You'll find a queue helpful in completing this challenge.


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class BinarySearchTree:
    def insert(self, root, data):
        if not root:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def get_height(self, root):
        if root:
            return max(self.get_height(root.left) + 1, self.get_height(root.right) + 1)
        else:
            return -1

    @staticmethod
    def level_order(root):
        nodes = [root]
        while nodes:
            cur = nodes.pop(0)
            print(cur.data, end=' ')
            if cur.left:
                nodes.append(cur.left)
            if cur.right:
                nodes.append(cur.right)
        print()


input_data = [3, 5, 2, 1, 4, 6, 7]
myTree = BinarySearchTree()
root = None  # why are they keeping track of root manually/externally to the BST class????
for data in input_data:
    root = myTree.insert(root, data)
height = myTree.get_height(root)
print(height == 3)
myTree.level_order(root)
