class Node:
    def __init__(self, key = 0, val = 0, prev = None, next = None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next
        
class LRUCache:
    def __init__(self, capacity: int):
        self.data = defaultdict(lambda:None)
        self.cap = capacity
        self.root = self.tail = None

    def get(self, key: int) -> int:
        data = self.data
        if(not data[key]):
            return -1
        
        ret = data[key]
        self.moveToEnd(ret)
        return ret.val

    def put(self, key: int, value: int) -> None:
        def appendToEnd(node):
            if(not self.root):
                self.root = node
            
            if(self.tail):
                self.tail.next = node
            self.tail = node
        
        def deleteFromTop() -> Node:
            d = self.root
            self.root = d.next
            if(self.root):
                self.root.prev = None
            d.next = None
            if(d == self.tail):
                self.tail = None
            return d
                
        data = self.data
        if(not data[key]):
            newNode = Node(key, value, self.tail)
            if(not self.cap):
                deleted = deleteFromTop()
                data[deleted.key] = None
                self.cap += 1
                
            appendToEnd(newNode)
            data[key] = newNode
            self.cap -= 1
        else:
            data[key].val = value
            self.moveToEnd(data[key])
            
    def moveToEnd(self, node) -> None:
        if(self.tail == node):
            return

        if(self.root == node):
            self.root = node.next

        if(node.prev):
            node.prev.next = node.next

        node.next.prev = node.prev
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)