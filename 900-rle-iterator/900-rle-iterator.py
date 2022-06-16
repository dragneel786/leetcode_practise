class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.e = encoding

    def next(self, n: int) -> int:
        if(not self.e):
            return -1
        
        for i in range(0, len(self.e), 2):
            if(n <= self.e[i]):
                self.e = self.e[i:]
                self.e[0] -= n
                return self.e[1]
            
            n -= self.e[i]
        
        if(n > 0):
            self.e = []
        return -1
        
        
        

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)