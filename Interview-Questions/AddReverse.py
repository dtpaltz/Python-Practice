from typing import *

# Hi, here's your problem today. This problem was recently asked by Microsoft:
#
# You are given two linked-lists representing two non-negative integers. The digits are stored in reverse order and
# each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

def AddReversedLists(a: List[int], b: List[int]):
    for i in range(len(a) - len(b)):
        b.append(0)
    for i in range(len(b) - len(a)):
        a.append(0)

    for i in range(len(a)):
        if a[i] >= 10 or b[i] >= 10:
            raise Exception("Invalid input: list elements must be single digits")

    ans = []
    carry = 0
    for i in range(len(a)):
        thisSum = [int(x) for x in str(a[i] + b[i] + carry)]

        if i == len(a) - 1:
            ans.extend(thisSum[::-1])
        else:
            ans.append(thisSum.pop())
            carry = thisSum.pop() if len(thisSum) > 0 else 0

    return ans


# 745 + 678 = 1423
# 547 + 876 = 3241
a = [5, 4, 7]
b = [8, 7, 6]
s = AddReversedLists(a, b)
n = int(''.join(map(str, s)))
print(n)
