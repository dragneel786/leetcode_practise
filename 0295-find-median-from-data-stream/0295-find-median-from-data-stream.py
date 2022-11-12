class MedianFinder:

    def __init__(self):
        self.heap1 = []
        self.heap2 = []

    def addNum(self, num: int) -> None:
        if(not self.heap1 or num <= -self.heap1[0]):
            heappush(self.heap1, -num)
        else:
            heappush(self.heap2, num)
        
        diff = len(self.heap1) - len(self.heap2)
        if(diff >= 2):
            heappush(self.heap2, -heappop(self.heap1))
        
        elif(diff <= -2):
            heappush(self.heap1, -heappop(self.heap2))

    def findMedian(self) -> float:
        min_len, max_len = len(self.heap1), len(self.heap2)
        if(min_len == max_len):
            return (self.heap2[0] - self.heap1[0]) / 2
        
        elif(min_len > max_len):
            return -self.heap1[0]
        
        else:
            return self.heap2[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()