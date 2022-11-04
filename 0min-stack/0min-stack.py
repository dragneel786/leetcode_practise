class MinStack:

    def __init__(self):
        self.s = deque()
        self.m = float('inf')

    def push(self, val: int) -> None:
        self.m = min(self.m, val)
        self.s.append([val, self.m])

    def pop(self) -> None:
        node = self.s.pop()
        if(len(self.s)):
            self.m = self.s[-1][1]
        else:
            self.m = float('inf')
        return node[0]

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.s[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()