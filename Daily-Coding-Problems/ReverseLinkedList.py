# This problem was recently asked by Google:
#
# Given a singly-linked list, reverse the list. This can be done iteratively or recursively. Can you get both solutions?
#
# Example:
# Input: 4 -> 3 -> 2 -> 1 -> 0 -> NULL
# Output: 0 -> 1 -> 2 -> 3 -> 4 -> NULL


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # Function to print the list
    def printList(self):
        node = self
        output = ''
        while node:
            output += str(node.val)
            output += " "
            node = node.next
        print(output)

    # Iterative Solution
    @staticmethod
    def reverseIteratively(head):
        prev = head
        curr = head.next
        prev.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

    # Recursive Solution
    @staticmethod
    def reverseRecursively(head):
        if not head or not head.next:
            return head

        rest = ListNode.reverseRecursively(head.next)
        head.next.next = head
        head.next = None

        return rest


if __name__ == '__main__':
    # Initialize the test list:
    testHead = ListNode(4)
    node1 = ListNode(3)
    testHead.next = node1
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(1)
    node2.next = node3
    testTail = ListNode(0)
    node3.next = testTail

    print("Initial list: ")
    testHead.printList()
    # 4 3 2 1 0
    # testHead.reverseIteratively(testHead)
    testHead.reverseRecursively(testHead)
    print("List after reversal: ")
    testTail.printList()
    # 0 1 2 3 4
