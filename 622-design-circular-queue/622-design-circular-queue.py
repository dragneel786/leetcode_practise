class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class MyCircularQueue:

    def __init__(self, k: int):
        self.s = 0
        self.ms = k
        self.front = None
        self.rear = None

    def enQueue(self, value: int) -> bool:
        if(self.isFull()): return False
        if(not self.rear):
            self.rear = Node(value)
            self.front = self.rear
        else:
            self.rear.next = Node(value, self.front)
            self.rear = self.rear.next
        self.s += 1
        return True

    def deQueue(self) -> bool:
        if(self.isEmpty()): return False
        if(self.front == self.rear):
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front
        self.s -= 1
        return True
    
    def Front(self) -> int:
        if(not self.front):
            return -1
        return self.front.val
        

    def Rear(self) -> int:
        if(not self.rear):
            return -1
        return self.rear.val

    def isEmpty(self) -> bool:
        return self.s == 0

    def isFull(self) -> bool:
        return self.s == self.ms


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()