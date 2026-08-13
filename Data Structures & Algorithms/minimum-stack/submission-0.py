class MinStack:

    def __init__(self):
        self.auxStack = list()
        self.stack = list()

    def push(self, val: int) -> None:
        # Add to normal stack
        self.stack.append(val)

        # Add to aux stack
        minVal = val if (len(self.auxStack) == 0 or val < self.getMin()) else self.getMin()
        self.auxStack.append(val)
        self.auxStack.append(minVal)
        

    def pop(self) -> None:
        # Pop from normal stack
        self.stack.pop()

        # Pop from aux stack
        self.auxStack.pop()
        self.auxStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.auxStack[-1]

        
