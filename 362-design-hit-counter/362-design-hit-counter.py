class HitCounter:

    def __init__(self):
        self.q = deque()

    def hit(self, timestamp: int) -> None:
        if(self.q and self.q[-1][0] == timestamp):
            self.q[-1][1] += 1
        else:
            self.q.append([timestamp, 1])

    def getHits(self, timestamp: int) -> int:
        while(self.q and self.q[0][0] <= (timestamp - 300)):
            self.q.popleft()
        return sum(q[1] for q in self.q)
            


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)