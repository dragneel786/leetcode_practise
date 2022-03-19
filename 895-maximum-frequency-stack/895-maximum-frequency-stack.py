class FreqStack:
    
    def __init__(self):
        self.mc = 0
        self.count = defaultdict(lambda:0)
        self.st = defaultdict(lambda:deque())

    def push(self, val: int) -> None:
        self.count[val] += 1
        self.st[self.count[val]].append(val)
        if(self.count[val] > self.mc):
            self.mc = self.count[val]

    def pop(self) -> int:
        ret = self.st[self.mc].pop()
        if(not len(self.st[self.mc])):
            self.mc -= 1
        self.count[ret] -= 1
        return ret
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()