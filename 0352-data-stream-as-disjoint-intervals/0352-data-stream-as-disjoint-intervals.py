class SummaryRanges:

    def __init__(self):
        self.stream = []
        self.seen = set()

    def addNum(self, value: int) -> None:
        if(value not in self.seen):
            insort(self.stream, value)
            self.seen.add(value)

    def getIntervals(self) -> List[List[int]]:
        ans = []
        curr = self.stream[0]
        for i in range(1, len(self.stream)):
            if(self.stream[i - 1] + 1 != self.stream[i]):
                ans.append([curr, self.stream[i - 1]])
                curr = self.stream[i]
        
        ans.append([curr, self.stream[-1]])
        return ans


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()