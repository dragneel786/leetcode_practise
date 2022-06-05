class StockPrice:

    def __init__(self):
        self.time = defaultdict(lambda:0)
        self.min = []
        self.max = []
        self.curr = 0
        
    def update(self, timestamp: int, price: int) -> None:
        self.time[timestamp] = price
        if(timestamp >= self.curr):
            self.curr = timestamp
        heappush(self.min, (price, timestamp))
        heappush(self.max, (-price, timestamp))
        
    def current(self) -> int:
        return self.time[self.curr]

    def maximum(self) -> int:
        while(-self.max[0][0] != self.time[self.max[0][1]]):
            heappop(self.max)
        return -self.max[0][0]

    def minimum(self) -> int:
        while(self.min[0][0] != self.time[self.min[0][1]]):
            heappop(self.min)
        return self.min[0][0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()