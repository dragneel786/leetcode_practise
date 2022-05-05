class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.appendleft(x)

    def pop(self) -> int:
        for _ in range(len(self.q) - 1):
            val = self.q.pop()
            self.q.appendleft(val)
        return self.q.pop()
            
    def top(self) -> int:
        for _ in range(len(self.q) - 1):
            val = self.q.pop()
            self.q.appendleft(val)
        
        val = self.q.pop()
        self.q.appendleft(val)
        return val

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()