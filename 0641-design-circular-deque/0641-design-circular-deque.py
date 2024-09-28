class Node:
    def __init__(self, val = -1, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next
        
class MyCircularDeque:

    def __init__(self, k: int):
        self.head = self.tail = None
        self.k = k
        self.size = 0
        

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.size += 1
        new_node = Node(value, None, self.head)
        if self.head:
            self.head.prev = new_node
            
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        
        return True
            
        
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.size += 1
        if self.tail is None:
            self.head = self.tail = Node(value)
        
        else:
            self.tail.next = Node(value, self.tail, None)
            self.tail = self.tail.next
            
        return True

    
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        self.size -= 1
        nxt = self.head.next
        self.head.next = None
        self.head = nxt
        if nxt is None:
            self.tail = None
        else:
            self.head.prev = None
            
        return True
            

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        self.size -= 1
        prev = self.tail.prev
        self.tail.prev = None
        
        self.tail = prev
        if prev is None:
            self.head = None
        
        else:
            self.tail.next = None
        
        return True

    
    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.head.val

    
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.tail.val

    
    def isEmpty(self) -> bool:
        return self.size <= 0

    def isFull(self) -> bool:
        return self.size == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()