class MinStack:
    s = None
    q = None
    def __init__(self):
        self.s = deque()
        self.q = deque()

    def push(self, val: int) -> None:
        self.s.append(val)
        if(len(self.q) == 0 or self.q[-1] > val):
            self.q.append(val)
        else:
            self.q.append(self.q[-1])

    def pop(self) -> None:
        self.q.pop()
        self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.q[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()