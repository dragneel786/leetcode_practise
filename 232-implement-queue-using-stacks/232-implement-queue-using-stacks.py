class MyQueue:
    st1 = None
    st2 = None

    def __init__(self):
        self.st1 = deque()
        self.st2 = deque()

    def push(self, x: int) -> None:
        self.st1.append(x)

    def pop(self) -> int:
        while(len(self.st1)):
            self.st2.append(self.st1.pop())
        
        val = self.st2.pop()
        
        while(len(self.st2)):
            self.st1.append(self.st2.pop())
        
        return val

    def peek(self) -> int:
        while(len(self.st1)):
            self.st2.append(self.st1.pop())
        
        val = self.st2[-1]
        
        while(len(self.st2)):
            self.st1.append(self.st2.pop())
        
        return val

    def empty(self) -> bool:
        if(len(self.st1)):
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()