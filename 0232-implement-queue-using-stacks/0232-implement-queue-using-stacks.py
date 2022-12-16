class MyQueue:

    def __init__(self):
        self.pu = deque()
        self.po = deque()

    def push(self, x: int) -> None:
        while(self.pu):
            self.po.append(self.pu.pop())
        
        self.pu.append(x)
        
        while(self.po):
            self.pu.append(self.po.pop())

    def pop(self) -> int:
        return self.pu.pop()

    def peek(self) -> int:
        return self.pu[-1]

    def empty(self) -> bool:
        return len(self.pu) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()