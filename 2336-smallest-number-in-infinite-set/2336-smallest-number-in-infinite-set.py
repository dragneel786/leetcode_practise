class SmallestInfiniteSet:

    def __init__(self):
        self.curr = 1
        self.iset = set()

    def popSmallest(self) -> int:
        val = self.curr
        self.iset.add(val)
        while(self.curr in self.iset):
            self.curr += 1
            
        return val

    def addBack(self, num: int) -> None:
        self.iset.discard(num)
        if(num >= self.curr):
            return
        
        self.curr = num
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)