class Node:
    def __init__(self, key = "", val = 0, prev = None, nxt = None,):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt

class AllOne:

    def __init__(self):
        self.keys = dict()
        self.head = self.tail = None

    def inc(self, key: str) -> None:
        self.keys.setdefault(key, Node(key))
        node = self.keys[key]
        node.val += 1
        
        if node.val > 1 and node.nxt and node.nxt.val < node.val:
            nxt = node.nxt
            prev = node.prev
            nxt.prev = prev
            
            if self.head == node:
                self.head = nxt
            else:
                prev.nxt = nxt
                
            
            while(nxt is not None and nxt.val < node.val):
                prev = nxt
                nxt = nxt.nxt
            
            node.prev = prev
            node.nxt = nxt
            prev.nxt = node
            if nxt: 
                nxt.prev = node
            else:
                self.tail = node
        
        elif node.val == 1:
            node.nxt = self.head
            if self.head:
                self.head.prev = node
            else:
                self.tail = node
                
            self.head = node
        
        # self.printItems()
        
    
    def dec(self, key: str) -> None:
        self.keys.setdefault(key, Node())
        node = self.keys[key]
        node.val -= 1
        
        nxt, prev = node.nxt, node.prev
        
        if node.val >= 1 and node.prev and node.prev.val > node.val:
            prev.nxt = nxt
            if self.tail == node:
                self.tail = prev
            else:
                nxt.prev = prev
                
            while(prev is not None and prev.val > node.val):
                nxt = prev
                prev = prev.prev
            
            node.prev = prev
            node.nxt = nxt
            nxt.prev = node
            if prev: prev.nxt = node
        
        elif node.val == 0:
            del self.keys[key]
            if self.head == node:
                self.head = nxt
            else:
                prev.nxt = nxt
            
            if self.tail == node:
                self.tail = prev
            else:
                nxt.prev = prev
    
        # self.printItems()

    def getMaxKey(self) -> str:
        if self.tail:
            return self.tail.key
        
        return ""

    
    def getMinKey(self) -> str:
        if self.head:
            return self.head.key
        
        return ""
    
    
    def printItems(self):
        curr = self.head
        print("------")
        while curr is not None:
            print(curr.key, curr.val)
            curr = curr.nxt
        print("Tail", self.tail.key, self.tail.val)