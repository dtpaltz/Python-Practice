class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def in_order(self):
        if self:
            if self.left:
                self.left.in_order()
            print(self.data)
            if self.right:
                self.right.in_order()

    def lvl_order(self):
        nodes = [self]
        while nodes:
            curr_node = nodes.pop(0)
            print(curr_node.data)
            if curr_node.left:
                nodes.append(curr_node.left)
            if curr_node.right:
                nodes.append(curr_node.right)

    def exists(self, n):
        if self.data == n:
            return True
        elif n < self.data and self.left:
            return self.left.exists(n)
        elif n > self.data and self.right:
            return self.right.exists(n)
        else:
            return False



tree = Node(8)
tree.insert(3)
tree.insert(10)
tree.insert(7)
tree.insert(11)
tree.insert(2)
tree.insert(9)
tree.insert(1)
tree.insert(6)

print(tree.exists(110))