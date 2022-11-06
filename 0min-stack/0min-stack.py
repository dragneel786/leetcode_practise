class MinStack:

    def __init__(self):
        self.st = deque()
        self.minv = inf

    def push(self, val: int) -> None:
        self.st.append(val)
        self.minv = min(self.minv, val)
        
    def pop(self) -> None:
        if(self.minv == self.st.pop()):
            if(self.st):
                self.minv = min(self.st)
            else:
                self.minv = inf

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minv


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()