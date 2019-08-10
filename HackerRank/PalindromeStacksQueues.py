
class Solution:
    def __init__(self):
        self.charStack = []
        self.charQueue = []

    def pushCharacter(self, ch):
        self.charStack.append(ch)

    def enqueueCharacter(self, ch):
        self.charQueue.append(ch)

    def popCharacter(self):
        return self.charStack.pop()

    def dequeueCharacter(self):
        return self.charQueue.pop(0)


