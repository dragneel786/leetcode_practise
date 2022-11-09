class StockSpanner:

    def __init__(self):
        self.stocks = deque()
        
    def next(self, price: int) -> int:
        count = 1
        while(self.stocks and self.stocks[-1][0] <= price):
            count += self.stocks.pop()[1]
        
        self.stocks.append((price, count))
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)