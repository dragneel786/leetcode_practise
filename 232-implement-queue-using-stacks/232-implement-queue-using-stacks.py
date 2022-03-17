class MyQueue:
    

    def __init__(self):
        self.enque = deque()
        self.deque = deque()

    def push(self, x: int) -> None:
        if(not len(self.enque)):
            self.deque.reverse()
            self.enque = self.deque.copy()
            self.deque.clear()
        self.enque.append(x)

    def pop(self) -> int:
        if(not len(self.deque)):
            self.enque.reverse()
            self.deque = self.enque.copy()
            self.enque.clear()
        return self.deque.pop()

    def peek(self) -> int:
        if(not len(self.deque)):
            self.enque.reverse()
            self.deque = self.enque.copy()
            self.enque.clear()
        return self.deque[-1]
    
    def empty(self) -> bool:
        if(len(self.enque) or len(self.deque)):
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()