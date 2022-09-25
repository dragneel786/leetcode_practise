class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * (k + 1)
        self.front = 0
        self.rear = 0
        
    def enQueue(self, value: int) -> bool:
        if(self.isFull()):
            return False
        
        self.q[self.front] = value
        self.front = self.inc(self.front)
        return True

    def deQueue(self) -> bool:
        if(self.isEmpty()):
            return False
        
        self.rear = self.inc(self.rear)
        return True

    def Front(self) -> int:
        if(self.isEmpty()):
            return -1
        
        return self.q[self.rear]
        

    def Rear(self) -> int:
        if(self.isEmpty()):
            return -1
        
        return self.q[self.front - 1]

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        return self.inc(self.front) == self.rear
    
    def inc(self, i):
        return (i + 1) % len(self.q)
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()