class Node:
    def __init__(self, val = 0, nxt = None):
        self.val = val
        self.nxt = nxt
        
class CustomStack:

    def __init__(self, maxSize: int):
        self.head = None
        self.max_size = maxSize
        self.curr_size = 0

    def push(self, x: int) -> None:
        if self.curr_size >= self.max_size:
            return
        
        self.curr_size += 1
        new_node = Node(x, self.head)
        self.head = new_node

    def pop(self) -> int:
        if self.curr_size <= 0:
            return -1
        
        self.curr_size -= 1
        pop_val = self.head.val
        nxt = self.head.nxt
        self.head.nxt = None
        self.head = nxt
        return pop_val

    def increment(self, k: int, val: int) -> None:
        temp = self.head
        index = 0
        while(index < (self.curr_size - k) and temp is not None):
            temp = temp.nxt
            index += 1
        
        while(temp is not None):
            temp.val += val
            temp = temp.nxt


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)