class RecentCounter:

    def __init__(self):
        self.rcounter = deque()
        

    def ping(self, t: int) -> int:
        while(self.rcounter and\
              t - self.rcounter[0] > 3000):
            self.rcounter.popleft()
        
        self.rcounter.append(t)
        return len(self.rcounter)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)