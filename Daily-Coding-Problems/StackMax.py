# This problem was recently asked by Twitter:
#
# Implement a class for a stack that supports all the regular functions (push, pop) and an additional
# function of max() which returns the maximum element in the stack (return None if the stack is empty).
# Each method should run in constant time.

class MaxStack:
    def __init__(self):
        # main stack
        self.mainStack = []

        # stack to keep track of max element
        self.trackStack = []

    def push(self, x):
        self.mainStack.append(x)
        if len(self.mainStack) == 1:
            self.trackStack.append(x)
            return

        # If current element is greater than
        # the top element of track stack,
        # append the current element to track
        # stack otherwise append the element
        # at top of track stack again into it.
        if x > self.trackStack[-1]:
            self.trackStack.append(x)
        else:
            self.trackStack.append(self.trackStack[-1])

    def max(self):
        return self.trackStack[-1]

    def pop(self):
        self.mainStack.pop()
        self.trackStack.pop()


if __name__ == "__main__":
    s = MaxStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(2)
    print(s.max())
    # 3
    s.pop()
    s.pop()
    print(s.max())
    # 2
